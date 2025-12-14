이 코드는 유명한 N-Queens 문제를 백트래킹(Backtracking) 알고리즘을 사용하여 해결하는 파이썬 스크립트입니다.

## N-Queens 문제란?

N x N 크기의 체스판에 N개의 퀸을 서로 공격할 수 없도록 배치하는 문제입니다. 퀸은 가로, 세로, 대각선 방향으로 제약 없이 움직일 수 있으므로, 어떤 퀸도 다른 퀸과 같은 행, 열, 대각선에 위치해서는 안 됩니다.

## 코드 분석

코드는 크게 3개의 함수(isSafe, solve, printboard)와 메인 실행 부분으로 구성되어 있습니다.

### 1. isSafe(board, row, column) 함수

```python
def isSafe(board: list[list[int]], row: int, column: int) -> bool:
    """
    현재 보드 상태에서 (row, column) 위치에 퀸을 놓아도 안전한지 확인합니다.
    """
    # 같은 행에 다른 퀸이 있는지 확인
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    # 같은 열에 다른 퀸이 있는지 확인
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    # 왼쪽 위 대각선에 퀸이 있는지 확인
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    # 오른쪽 위 대각선에 퀸이 있는지 확인
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True
```

- 역할: 특정 위치 (row, column)에 퀸을 놓을 수 있는지(안전한지) 검사합니다.
- 동작 원리:
    1. 가로 (행) 검사: 현재 row의 모든 칸을 확인하여 다른 퀸이 있는지 검사합니다.
    2. 세로 (열) 검사: 현재 column의 모든 칸을 확인하여 다른 퀸이 있는지 검사합니다.
    3. 대각선 검사: 현재 위치에서 왼쪽 위, 오른쪽 위 대각선 방향으로 다른 퀸이 있는지 검사합니다. 아래쪽 대각선은 아직 퀸이 배치되지 않았으므로 검사할 필요가 없습니다.
- 반환값: 퀸을 놓을 수 있으면 True, 없으면 False를 반환합니다.

### 2. solve(board, row) 함수 (핵심 로직)

```python
def solve(board: list[list[int]], row: int) -> bool:
    """
    백트래킹을 사용하여 재귀적으로 해를 찾습니다.
    """
    # 1. 재귀 종료 조건 (Base Case)
    if row >= len(board):
        solution.append(board)
        printboard(board)
        print()
        return True

    # 2. 재귀 호출 (Recursive Step)
    for i in range(len(board)):
        if isSafe(board, row, i):
            # 선택 (Choose): 퀸을 놓는다.
            board[row][i] = 1
            # 탐색 (Explore): 다음 행으로 이동하여 계속 진행한다.
            solve(board, row + 1)
            # 선택 취소 (Unchoose / Backtrack): 놓았던 퀸을 다시 회수한다.
            board[row][i] = 0
    return False
```

- 역할: 백트래킹 알고리즘의 핵심으로, 가능한 모든 해를 재귀적으로 탐색합니다.
- 동작 원리:
    1. 재귀 종료 조건: 만약 row가 체스판의 크기(n)와 같거나 커지면, 모든 행에 퀸을 성공적으로 배치했다는 의미입니다. 이 때의 보드 상태를 solution 리스트에 추가하고, 화면에 출력한 뒤 True를 반환합니다.
    2. 재귀 탐색:
        - 현재 row의 모든 열(i)을 순회합니다.
        - isSafe(board, row, i)를 호출하여 (row, i) 위치에 퀸을 놓을 수 있는지 확인합니다.
        - 만약 안전하다면:
            1. 선택(Choose): 해당 위치에 퀸을 놓습니다 (board[row][i] = 1).
            2. 탐색(Explore): solve(board, row + 1)를 재귀 호출하여 다음 행에 퀸을 놓으러 갑니다.
            3. 선택 취소(Unchoose/Backtrack): 다음 행의 탐색이 모두 끝나고 돌아오면, 방금 놓았던 퀸을 다시 회수합니다 (board[row][i] = 0). 이 과정이 백트래킹의 핵심입니다. 현재 위치에 퀸을 놓는 모든 경우를 탐색했으므로, 퀸을 치우고 현재 행의 다른 열에 퀸을 놓는 경우를 시도하기 위함입니다.

### 3. printboard(board) 함수 및 메인 실행 블록

```python
def printboard(board: list[list[int]]) -> None:
    """
    해결된 보드를 'Q'와 '.'으로 예쁘게 출력합니다.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# 메인 실행 부분
n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
```

- printboard: solve 함수가 찾은 해(성공한 보드)를 사람이 보기 좋게 Q와 .으로 변환하여 출력합니다.
- 메인 실행:
    - n = 8로 8x8 체스판을 설정합니다.
    - board를 0으로 채워진 2차원 리스트로 초기화합니다.
    - solve(board, 0)을 호출하여 0번째 행부터 문제 풀이를 시작합니다.
    - 모든 탐색이 끝나면 solution 리스트에 저장된 해의 총개수를 출력합니다.

## 코드 개선 제안

현재 코드는 N-Queens 문제를 잘 해결하지만, 몇 가지 개선을 통해 더 효율적이고 파이썬다운 코드로 만들 수 있습니다.

1. 전역 변수 solution 제거: 전역 변수는 코드의 흐름을 파악하기 어렵게 만들 수 있습니다. solve 함수가 찾은 해들을 리스트로 반환하고, 메인 함수에서 이를 받아 처리하는 것이 더 좋은 구조입니다.
2. isSafe 함수 최적화: 현재 isSafe 함수는 퀸을 놓을 때마다 전체 행, 열, 대각선을 다시 검사하여 비효율적입니다. n_queens_math.py 파일에서처럼, 각 열과 대각선이 사용 중인지를 별도의 리스트나 집합(set)으로 관리하면 O(1) 시간 복잡도로 안전 여부를 확인할 수 있어 성능이 크게 향상됩니다.
3. solve 함수의 반환 값: 현재 solve 함수는 모든 해를 찾도록 설계되었지만, True 또는 False를 반환하는 로직이 혼재되어 있습니다. 모든 해를 찾는 것이 목적이므로 반환 값이 굳이 필요 없습니다.

아래는 위 제안들을 반영하여 수정한 코드입니다.

```
n_queens.py
-53
+52
 Show full code block 
"""
from __future__ import annotations

solution = []


def isSafe(board: list[list[int]], row: int, column: int) -> bool:
    """
    This function returns a boolean value True if it is safe to place a queen there
    considering the current state of the board.

    Parameters :
    board(2D matrix) : board
    row ,column : coordinates of the cell on a board

    Returns :
    Boolean Value

    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
    n = len(board)
    # Check this column on upper side
    for i in range(row):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(column, n)):
        if board[i][j] == 1:
            return False
    return True


def solve(board: list[list[int]], row: int) -> bool:
def solve_n_queens(n: int) -> list[list[list[int]]]:
    """
    It creates a state space tree and calls the safe function until it receives a
    False Boolean and terminates that branch and backtracks to the next
    possible solution branch.
    Solves the N-Queens problem and returns all possible solutions.
    """
    if row >= len(board):
        """
        If the row number exceeds N we have board with a successful combination
        and that combination is appended to the solution list and the board is printed.
    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_util(board, 0, solutions)
    return solutions

        """
        solution.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        """
        For every row it iterates through each column to check if it is feasible to
        place a queen there.
        If all the combinations for that particular branch are successful the board is
        reinitialized for the next possible combination.
        """
        if isSafe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False

def solve_util(
    board: list[list[int]], row: int, solutions: list[list[list[int]]]
) -> None:
    """
    A recursive utility function to solve N-Queens problem.
    """
    n = len(board)
    if row >= n:
        # All queens are placed, so add a copy of the board to solutions
        solution_copy = [row_data[:] for row_data in board]
        solutions.append(solution_copy)
        return

    for col in range(n):
        if isSafe(board, row, col):
            # Place the queen
            board[row][col] = 1
            # Recur to place rest of the queens
            solve_util(board, row + 1, solutions)
            # Backtrack and remove the queen from the current cell
            board[row][col] = 0


def printboard(board: list[list[int]]) -> None:
    """
    Prints the boards that have a successful combination.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    for row_data in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row_data))


# n=int(input("The no. of queens"))
n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))
if __name__ == "__main__":
    try:
        # n = int(input("Enter the number of queens: "))
        n = 4  # Example for n=4
        if n <= 0:
            print("Number of queens must be a positive integer.")
        else:
            all_solutions = solve_n_queens(n)
            print(f"Found {len(all_solutions)} solutions for {n}-Queens problem:\n")
            for i, sol in enumerate(all_solutions):
                print(f"Solution {i+1}:")
                printboard(sol)
                print()
    except ValueError:
        print("Invalid input. Please enter an integer.")
```

