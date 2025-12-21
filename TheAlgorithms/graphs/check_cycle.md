# 사이클 확인 (Check Cycle)

이 문서는 `check_cycle.py` 파일에 구현된 **유향 그래프(Directed Graph)에서의 사이클 탐지** 알고리즘에 대해 설명합니다.

## 개요

그래프 내에 순환(Cycle)이 존재하는지 여부를 확인하는 알고리즘입니다. 깊이 우선 탐색(DFS)을 사용하여 구현되었으며, 현재 탐색 중인 경로(Recursion Stack)에 이미 방문한 노드가 다시 등장하는지를 확인하여 사이클을 감지합니다.

## 주요 함수

### `check_cycle(graph: dict) -> bool`

- **목적**: 주어진 그래프에 사이클이 존재하는지 확인합니다.
- **매개변수**:
  - `graph`: 인접 리스트 형태의 딕셔너리 (예: `{0: [1], 1: [2], ...}`).
- **반환값**: 사이클이 있으면 `True`, 없으면 `False`.
- **동작 원리**:
  - 모든 노드에 대해 방문 여부를 확인합니다.
  - 방문하지 않은 노드에 대해 `depth_first_search`를 호출합니다.
  - 하나라도 사이클이 발견되면 즉시 `True`를 반환합니다.

### `depth_first_search(graph: dict, vertex: int, visited: set, rec_stk: set) -> bool`

- **목적**: DFS를 수행하며 역방향 간선(Back Edge)이 존재하는지 확인합니다.
- **매개변수**:
  - `vertex`: 현재 탐색 중인 정점.
  - `visited`: 전체 탐색 과정에서 방문한 정점들의 집합.
  - `rec_stk`: 현재 재귀 호출 스택에 있는 정점들의 집합 (현재 경로).
- **알고리즘**:
  1. 현재 정점(`vertex`)을 `visited`와 `rec_stk`에 추가합니다.
  2. 이웃 정점들을 순회합니다:
     - 방문하지 않은 이웃이라면 재귀적으로 `depth_first_search`를 호출합니다.
     - **중요**: 만약 이웃이 이미 `rec_stk`에 존재한다면, 이는 현재 경로 상의 조상 노드로 돌아가는 것이므로 **사이클**입니다 (`True` 반환).
  3. 탐색이 끝나면 현재 정점을 `rec_stk`에서 제거합니다 (백트래킹).
  4. 사이클을 발견하지 못했다면 `False`를 반환합니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 코드를 검증합니다.

사용 예시:
```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
has_cycle = check_cycle(graph)
print(has_cycle)  # 출력: True
```