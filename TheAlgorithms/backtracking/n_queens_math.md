이 코드는 유명한 N-Queens 문제를 푸는 파이썬 스크립트입니다. N-Queens 문제는 N x N 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치하는 모든 경우의 수를 찾는 문제입니다.

이 코드의 가장 큰 특징은 백트래킹(Backtracking) 알고리즘에 간단한 수학적 원리를 접목하여 대각선 충돌을 매우 효율적으로 확인한다는 점입니다.

## 코드의 핵심 아이디어

1. 보드 표현: 퀸의 위치를 1차원 리스트로 표현합니다. 예를 들어 [1, 3, 0, 2]는 4x4 체스판에서 첫 번째 행(인덱스 0)의 1번 열, 두 번째 행(인덱스 1)의 3번 열, ... 에 퀸이 놓여있음을 의미합니다.
    - 이 방식은 각 행에 퀸이 하나씩만 존재함을 보장하므로, 가로(수평) 충돌은 자연스럽게 방지됩니다.
    - 세로(수직) 충돌은 리스트에 같은 값이 있는지 확인하는 것으로 간단히 해결됩니다 (예: col in possible_board).

2. 대각선 충돌 확인 (수학적 접근): 체스판을 좌표 평면으로 생각하고, 각 칸을 (row, col) 좌표로 봅니다.

    - 오른쪽 아래로 향하는 대각선 (\): 이 대각선 위에 있는 모든 칸들은 행 - 열 값이 항상 같습니다.
    - 왼쪽 아래로 향하는 대각선 (/): 이 대각선 위에 있는 모든 칸들은 행 + 열 값이 항상 같습니다.

코드는 이 원리를 이용하여, 퀸을 놓을 때마다 row - col 값과 row + col 값을 각각 별도의 리스트(diagonal_right_collisions, diagonal_left_collisions)에 저장합니다. 그리고 새로운 퀸을 놓기 전에, 계산된 row - col 또는 row + col 값이 이미 해당 리스트에 존재하는지 확인하여 대각선 충돌을 즉시 감지합니다.

## 함수별 분석

### depth_first_search 함수 (핵심 로직)

이 함수는 깊이 우선 탐색(DFS)을 이용한 백트래킹으로, 가능한 모든 해답을 재귀적으로 찾아냅니다.

```python
def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:
    # 현재 퀸을 놓을 행 번호
    row = len(possible_board)

    # 1. 재귀 종료 조건 (Base Case)
    # 모든 행에 퀸을 성공적으로 배치한 경우
    if row == n:
        # [1, 3, 0, 2] 같은 숫자 리스트를 체스판 모양으로 변환하여 결과에 추가
        boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
        return

    # 2. 재귀 호출 (Recursive Step)
    # 현재 행(row)의 모든 열(col)을 순회하며 퀸을 놓을 위치를 탐색
    for col in range(n):

        # 충돌 확인
        if (
            col in possible_board  # 세로 충돌
            or row - col in diagonal_right_collisions  # 오른쪽 대각선 충돌
            or row + col in diagonal_left_collisions  # 왼쪽 대각선 충돌
        ):
            continue # 충돌이 발생하면 다음 열로 넘어감

        # 충돌이 없으면, 현재 위치에 퀸을 놓고 다음 행으로 재귀 호출
        # (새로운 리스트를 만들어 전달함으로써 상태를 업데이트)
        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
        )
```

- 동작 원리:
    1. 재귀 종료 조건: row가 n과 같아지면, N개의 퀸을 모두 성공적으로 배치했다는 의미입니다. 현재 퀸의 위치가 담긴 possible_board를 예쁜 체스판 모양으로 변환하여 최종 결과 리스트 boards에 추가하고 재귀를 종료합니다.
    2. 재귀 호출: for 루프를 통해 현재 행에 퀸을 놓을 수 있는 모든 열을 시도합니다.
        - 충돌 검사: if 문에서 세로, 오른쪽 대각선, 왼쪽 대각선 충돌을 한 번에 확인합니다. 하나라도 충돌하면 해당 위치는 건너뜁니다.
        - 탐색 진행: 충돌이 없는 안전한 위치라면, 현재 퀸의 위치 정보(col, row-col, row+col)를 각 리스트에 추가하여 다음 행(row+1)을 탐색하기 위해 depth_first_search 함수를 다시 호출합니다.
        - 백트래킹: 이 구현에서는 pop()을 사용한 명시적인 백트래킹 대신, 재귀 호출 시 possible_board + [col]처럼 새로운 리스트를 생성하여 전달합니다. 재귀 호출이 끝나고 돌아오면, 현재 함수의 possible_board는 변경되지 않은 상태이므로 자연스럽게 이전 상태로 돌아와 for 루프의 다음 열을 탐색하게 됩니다.

## n_queens_solution 함수

이 함수는 전체 프로세스를 시작하고 최종 결과를 출력하는 역할을 합니다.

```python
def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = [] # 모든 해답을 저장할 리스트
    # 빈 보드에서 탐색 시작
    depth_first_search([], [], [], boards, n)

    # 찾은 모든 해답 보드를 출력
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")
```

## 코드 개선 제안

현재 코드는 수학적 원리를 잘 활용하여 명료하게 작성되었지만, 메모리 효율성 측면에서 개선할 여지가 있습니다. 재귀 호출마다 + 연산으로 새로운 리스트를 계속 생성하는 것은 n이 커질수록 메모리 사용량을 늘릴 수 있습니다.

set을 사용하고, 재귀 호출 전후에 원소를 추가/제거하는 방식으로 수정하면 메모리 효율성을 높일 수 있습니다.

```
n_queens_math.py
-13
+27
 Show full code block 

def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    col_placements: set[int],
    diag_right_placements: set[int],
    diag_left_placements: set[int],
    boards: list[list[str]],
    n: int,
) -> None:
    """
    >>> boards = []
    >>> depth_first_search([], [], [], boards, 4)
    >>> depth_first_search([], set(), set(), set(), boards, 4)
    >>> for board in boards:
    ...     print(board)
    ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
        # If any or these are True it means there is a collision so we continue to the
        # next value in the for loop.
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
            col in col_placements
            or row - col in diag_right_placements
            or row + col in diag_left_placements
        ):
            continue

        # If it is False we call dfs function again and we update the inputs
        # Choose
        possible_board.append(col)
        col_placements.add(col)
        diag_right_placements.add(row - col)
        diag_left_placements.add(row + col)

        # Explore
        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
            possible_board,
            col_placements,
            diag_right_placements,
            diag_left_placements,
            boards,
            n,
        )

        # Unchoose (Backtrack)
        diag_left_placements.remove(row + col)
        diag_right_placements.remove(row - col)
        col_placements.remove(col)
        possible_board.pop()


def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)
    depth_first_search([], set(), set(), set(), boards, n)

    # Print all the boards
    for board in boards:
```

### 변경점 요약

1. set 자료구조 사용: 충돌 여부를 확인하는 col_placements, diag_right_placements, diag_left_placements를 리스트 대신 set으로 변경했습니다. set에서의 in 연산은 평균적으로 O(1)의 시간 복잡도를 가져 리스트의 O(n)보다 훨씬 빠릅니다.
2. 명시적 백트래킹: 재귀 호출 전에 add()와 append()로 상태를 변경(Choose)하고, 재귀 호출이 끝난 후에 remove()와 pop()으로 상태를 원래대로 되돌립니다(Unchoose/Backtrack). 이 방식은 재귀 호출 시마다 새로운 객체를 생성하지 않아 메모리 사용에 더 효율적입니다.
