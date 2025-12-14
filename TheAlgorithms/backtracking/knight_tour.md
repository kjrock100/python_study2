
이 파이썬 스크립트는 유명한 퍼즐 중 하나인 나이트 투어(Knight's Tour) 문제를 해결하는 알고리즘을 구현한 것입니다. 나이트 투어는 체스판의 나이트(Knight)가 특정 위치에서 시작하여, 보드의 모든 칸을 정확히 한 번씩만 방문하는 경로를 찾는 문제입니다. 이 코드는 **백트래킹(Backtracking)**이라는 재귀적 탐색 기법을 사용하여 해답을 찾습니다.

## 코드 전체 구조

코드는 크게 4개의 함수로 구성되어 있습니다.

1. get_valid_pos: 현재 위치에서 나이트가 이동할 수 있는 유효한 다음 위치들을 계산합니다.
2. is_complete: 체스판의 모든 칸을 방문했는지 확인합니다.
3. open_knight_tour_helper: 백트래킹을 사용하여 실제 투어 경로를 찾는 핵심 재귀 함수입니다.
4. open_knight_tour: 문제를 설정하고, 모든 시작점에서 투어를 시도하여 최종 결과를 반환하는 메인 함수입니다.

이제 각 함수를 자세히 살펴보겠습니다.

## get_valid_pos 함수

```python
def get_valid_pos(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Find all the valid positions a knight can move to from the current position.

    >>> get_valid_pos((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    """

    y, x = position
    # 나이트가 이동할 수 있는 8가지 방향
    positions = [
        (y + 1, x + 2), (y - 1, x + 2), (y + 1, x - 2), (y - 1, x - 2),
        (y + 2, x + 1), (y + 2, x - 1), (y - 2, x + 1), (y - 2, x - 1),
    ]
    permissible_positions = []

    # 8가지 방향 중 체스판을 벗어나지 않는 위치만 필터링
    for position in positions:
        y_test, x_test = position
        if 0 <= y_test < n and 0 <= x_test < n:
            permissible_positions.append(position)

    return permissible_positions
```

- 역할: 현재 나이트의 위치(position)와 체스판의 크기(n)를 입력받아, 다음으로 이동할 수 있는 모든 유효한 칸의 좌표 리스트를 반환합니다.
- 동작:
    1. 나이트가 L자 형태로 이동할 수 있는 8가지 모든 경우의 수를 positions 리스트에 정의합니다.
    2. for 루프를 돌며 각 후보 위치가 체스판(n x n)의 경계 내에 있는지 확인합니다.
    3. 체스판을 벗어나지 않는 유효한 위치들만 permissible_positions 리스트에 추가하여 반환합니다.

## is_complete 함수

```python
 Show full code block 
def is_complete(board: list[list[int]]) -> bool:
    """
    Check if the board (matrix) has been completely filled with non-zero values.
    """
    # 보드에 0이 하나라도 있으면 False, 모두 0이 아니면 True
    return not any(elem == 0 for row in board for elem in row)
```

- 역할: 체스판(board)의 모든 칸이 방문되었는지(즉, 0이 아닌 값으로 채워졌는지) 확인합니다.
- 동작: any()와 제너레이터 표현식을 사용하여 보드의 모든 요소를 효율적으로 검사합니다. 만약 방문하지 않은 칸(값이 0)이 하나라도 발견되면 any()가 True가 되고, not 연산자에 의해 최종적으로 False를 반환합니다. 모든 칸이 방문되었다면 True를 반환합니다.

## open_knight_tour_helper 함수 (핵심 로직)

```python
def open_knight_tour_helper(
    board: list[list[int]], pos: tuple[int, int], curr: int
) -> bool:
    """
    Helper function to solve knight tour problem.
    """
    # 1. 재귀 종료 조건 (Base Case)
    if is_complete(board):
        return True

    # 2. 재귀 호출 (Recursive Step)
    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:  # 아직 방문하지 않은 칸이라면
            # 선택 (Choose)
            board[y][x] = curr + 1
            # 탐색 (Explore)
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            # 선택 취소 (Unchoose / Backtrack)
            board[y][x] = 0

    return False
```

- 역할: 백트래킹을 통해 나이트 투어의 해답을 재귀적으로 탐색합니다.
- 동작 원리 (Choose - Explore - Unchoose):
    1. 재귀 종료 조건: is_complete(board)를 호출하여 모든 칸을 방문했는지 확인합니다. 만약 그렇다면, 투어가 성공적으로 완료된 것이므로 True를 반환합니다.
    2. 재귀 호출:
        - get_valid_pos를 호출하여 현재 위치(pos)에서 이동할 수 있는 다음 후보 위치들을 가져옵니다.
        - for 루프를 통해 각 후보 위치를 순회합니다.
        - 선택 (Choose): 만약 후보 위치가 아직 방문하지 않은 곳(board[y][x] == 0)이라면, 그 칸에 다음 이동 순서(curr + 1)를 기록합니다.
        - 탐색 (Explore): open_knight_tour_helper 함수를 자기 자신에 대해 다시 호출하여, 방금 선택한 경로를 따라 더 깊이 탐색을 진행합니다. 만약 이 재귀 호출이 True를 반환하면, 해답을 찾은 것이므로 즉시 True를 반환하며 모든 재귀를 종료시킵니다.
        - 선택 취소 (Unchoose / Backtrack): 만약 탐색(Explore) 단계에서 해답을 찾지 못하고 재귀 호출이 False를 반환했다면, 방금 전의 선택이 잘못된 경로였음을 의미합니다. 따라서 board[y][x] = 0으로 값을 되돌려놓고(백트래킹), for 루프의 다음 후보 위치로 넘어가 다른 경로를 탐색합니다.
    3. 모든 후보 위치를 시도했음에도 해답을 찾지 못하면 False를 반환합니다.

## open_knight_tour 함수

```python
def open_knight_tour(n: int) -> list[list[int]]:
    """
    Find the solution for the knight tour problem for a board of size n.
    """
    board = [[0 for i in range(n)] for j in range(n)]

    # 모든 칸을 시작점으로 하여 투어를 시도
    for i in range(n):
        for j in range(n):
            board[i][j] = 1  # (i, j)를 시작점으로 설정
            if open_knight_tour_helper(board, (i, j), 1):
                return board # 해답을 찾으면 즉시 반환
            board[i][j] = 0  # 해답을 못 찾았으면 시작점 리셋

    # 모든 시작점을 시도해도 해답이 없으면 에러 발생
    raise ValueError(f"Open Kight Tour cannot be performed on a board of size {n}")
```

- 역할: 나이트 투어 문제를 초기화하고, 해결 과정을 총괄하는 메인 함수입니다.
- 동작:
    1. n x n 크기의 체스판을 0으로 초기화합니다.
    2. 이중 for 루프를 사용하여 보드의 모든 칸 (i, j)를 한 번씩 시작점으로 설정해 봅니다.
    3. 특정 칸을 시작점으로 설정(board[i][j] = 1)한 뒤, open_knight_tour_helper를 호출하여 투어를 시작합니다.
    4. 만약 헬퍼 함수가 True를 반환하면, 해답을 찾은 것이므로 완성된 board를 즉시 반환합니다.
    5. 헬퍼 함수가 False를 반환하면, 해당 시작점에서는 해답이 없는 것이므로 시작점을 다시 0으로 초기화하고 다음 시작점을 시도합니다.
    6. 모든 칸을 시작점으로 시도했음에도 해답을 찾지 못하면, 해당 n 크기의 보드에서는 나이트 투어가 불가능하다는 ValueError를 발생시킵니다. (예: 2x2, 3x3, 4x4 보드)

## if __name__ == "__main__" 블록

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

- 이 스크립트가 직접 실행될 때, doctest.testmod()를 호출합니다.
- doctest는 함수들의 주석(docstring) 안에 >>> 형태로 작성된 예제 코드를 자동으로 실행하고, 그 결과가 실제 함수의 반환값과 일치하는지 검사해주는 유용한 테스트 도구입니다. 이를 통해 코드의 정확성을 간편하게 확인할 수 있습니다.
