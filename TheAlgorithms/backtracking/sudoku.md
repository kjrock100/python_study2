이 코드는 유명한 스도쿠(Sudoku) 퍼즐을 백트래킹(Backtracking) 알고리즘을 사용해 해결하는 파이썬 스크립트입니다.

## 코드 분석

코드는 크게 4개의 함수(is_safe, find_empty_location, sudoku, print_solution)와 실행을 위한 예제 데이터 및 메인 블록으로 구성되어 있습니다.

### 1. is_safe(grid, row, column, n) 함수

```python
def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    """
    이 함수는 각 행, 열, 3x3 하위 그리드에 'n'이라는 숫자가 포함되어 있는지 확인합니다.
    '안전하지 않은' 경우(중복된 숫자가 발견된 경우) False를 반환하고,
    '안전한' 경우 True를 반환합니다.
    """
    # 같은 행 또는 열에 n이 있는지 확인
    for i in range(9):
        if grid[row][i] == n or grid[i][column] == n:
            return False

    # 3x3 박스 안에 n이 있는지 확인
    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False

    return True
```

- 역할: 특정 위치 (row, column)에 숫자 n을 놓는 것이 스도쿠 규칙에 맞는지(안전한지) 검사합니다.
- 동작 원리:
    1. 가로/세로 검사: 현재 row의 모든 칸과 column의 모든 칸을 확인하여 숫자 n이 이미 존재하는지 검사합니다.
    2. 3x3 박스 검사: 현재 칸이 속한 3x3 박스 내에 숫자 n이 이미 있는지 검사합니다. (row - row % 3)와 (column - column % 3)는 현재 칸이 속한 3x3 박스의 시작점(좌측 상단) 좌표를 찾는 계산입니다.
    3. 위의 검사에서 중복된 숫자를 찾으면 False를, 모든 검사를 통과하면 True를 반환합니다.

### 2. find_empty_location(grid) 함수

```python
def find_empty_location(grid: Matrix) -> tuple[int, int] | None:
    """
    이 함수는 빈 위치를 찾아 해당 행과 열에 숫자를 할당할 수 있도록 합니다.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None
```

- 역할: 스도쿠 그리드에서 아직 숫자가 채워지지 않은 칸(값이 0인 칸)을 찾습니다.
- 동작 원리: 그리드의 처음부터 순서대로 탐색하다가 값이 0인 칸을 발견하면 즉시 해당 칸의 좌표 (i, j)를 반환합니다. 모든 칸이 채워져 있다면 None을 반환합니다.

### 3. sudoku(grid) 함수 (핵심 로직)

```python
def sudoku(grid: Matrix) -> Matrix | None:
    """
    부분적으로 채워진 그리드를 받아 스도쿠 해결 요구 사항
    (행, 열, 박스에 중복 없음)을 충족하는 방식으로 모든 미할당 위치에
    값을 할당하려고 시도합니다.
    """
    # 1. 빈 칸 찾기
    if location := find_empty_location(grid):
        row, column = location
    else:
        # 2. 재귀 종료 조건 (Base Case)
        # 빈 칸이 없으면 퍼즐이 완성된 것이므로 그리드를 반환
        return grid

    # 3. 재귀 호출 (Recursive Step)
    for digit in range(1, 10):
        # (row, column)에 digit을 놓는 것이 안전한지 확인
        if is_safe(grid, row, column, digit):
            # 선택 (Choose): 숫자를 놓는다
            grid[row][column] = digit

            # 탐색 (Explore): 다음 빈 칸을 채우기 위해 재귀 호출
            if sudoku(grid) is not None:
                return grid # 해결책을 찾았으면 그대로 반환

            # 선택 취소 (Unchoose / Backtrack): 해결책을 못 찾았으면 원래대로 되돌림
            grid[row][column] = 0

    return None # 1~9까지 모든 숫자를 시도해도 해결 못하면 None 반환
```

- 역할: 백트래킹 알고리즘의 핵심으로, 가능한 모든 해를 재귀적으로 탐색하여 스도쿠를 풉니다.
- 동작 원리:
    1. 빈 칸 찾기: find_empty_location을 호출하여 다음에 채울 빈 칸을 찾습니다.
    2. 재귀 종료 조건 (Base Case): 만약 빈 칸이 없다면(None이 반환되면), 모든 칸이 성공적으로 채워졌다는 의미이므로, 완성된 grid를 반환하며 재귀를 종료합니다.
    3. 재귀 탐색:
        - 빈 칸 (row, column)에 1부터 9까지의 숫자를 하나씩 시도해봅니다.
        - is_safe 함수를 통해 해당 숫자를 놓아도 되는지 확인합니다.
        - 선택(Choose): 만약 안전하다면, 해당 위치에 숫자를 놓습니다 (grid[row][column] = digit).
        - 탐색(Explore): sudoku(grid)를 다시 호출하여 다음 빈 칸을 채우러 갑니다. 만약 이 재귀 호출이 None이 아닌 grid를 반환했다면, 이는 해결책을 찾았다는 의미이므로, 그 결과를 계속 위로 전달합니다.
        - 선택 취소(Unchoose/Backtrack): 만약 재귀 호출이 None을 반환했다면, 현재 놓았던 숫자가 잘못된 선택이었음을 의미합니다. 따라서, 방금 놓았던 숫자를 다시 회수하고 칸을 0으로 되돌립니다 (grid[row][column] = 0). 이 과정이 바로 백트래킹입니다. 그리고 루프의 다음 숫자로 시도를 계속합니다.
    4. 만약 1부터 9까지 모든 숫자를 시도했지만 해결책을 찾지 못하면, None을 반환하여 이전 재귀 단계에 실패를 알립니다.

### 4. print_solution(grid) 및 메인 실행 블록

```python
def print_solution(grid: Matrix) -> None:
    # ... (생략) ...

if __name__ == "__main__":
    # 그리드 복사본을 만들어 원본과 비교할 수 있도록 함
    for example_grid in (initial_grid, no_solution):
        # ... (생략) ...
        solution = sudoku(example_grid)
        if solution is not None:
            print_solution(solution)
        else:
            print("Cannot find a solution.")
```

- print_solution: sudoku 함수가 찾은 해(성공한 그리드)를 사람이 보기 좋게 9x9 형태로 출력합니다.
- if __name__ == "__main__": 스크립트가 직접 실행될 때, initial_grid(해결 가능한 예제)와 no_solution(해결 불가능한 예제)에 대해 각각 sudoku 함수를 실행하고 그 결과를 출력합니다.

이 코드는 백트래킹의 전형적인 "선택, 탐색, 선택 취소" 패턴을 잘 보여주는 훌륭한 예제입니다.


