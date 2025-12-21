# 깊이 우선 탐색 2 (Depth First Search 2)

이 문서는 `depth_first_search_2.py` 파일에 구현된 **재귀적 깊이 우선 탐색(Recursive DFS)** 알고리즘에 대해 설명합니다.

## 개요

깊이 우선 탐색(DFS)은 그래프의 시작 정점에서 출발하여 한 분기를 끝까지 탐색한 후, 다음 분기로 넘어가는 방식의 탐색 알고리즘입니다. 이 구현은 `Graph` 클래스와 재귀 함수를 사용하여 DFS를 수행합니다.

## 주요 클래스: `Graph`

### `__init__(self)`
- **목적**: 그래프 객체를 초기화합니다.
- **속성**:
  - `self.vertex`: 정점과 간선 정보를 저장하는 딕셔너리입니다. (인접 리스트 방식)

### `add_edge(self, from_vertex: int, to_vertex: int)`
- **목적**: 그래프에 유향 간선(Directed Edge)을 추가합니다.
- **매개변수**:
  - `from_vertex`: 시작 정점.
  - `to_vertex`: 도착 정점.
- **동작**: `from_vertex`가 딕셔너리에 없으면 새로 생성하고, 있으면 리스트에 `to_vertex`를 추가합니다.

### `print_graph(self)`
- **목적**: 그래프의 인접 리스트 상태를 출력합니다.

### `dfs(self)`
- **목적**: 깊이 우선 탐색을 시작하는 진입점 함수입니다.
- **동작**:
  - `visited` 리스트를 생성하여 방문 여부를 추적합니다. (정점의 개수만큼 `False`로 초기화)
  - 모든 정점에 대해 반복하며, 아직 방문하지 않은 정점이 있다면 `dfs_recursive`를 호출합니다. 이는 그래프가 분리되어 있어도 모든 정점을 방문하기 위함입니다.

### `dfs_recursive(self, start_vertex: int, visited: list)`
- **목적**: 실제로 재귀적으로 탐색을 수행하는 헬퍼 함수입니다.
- **동작**:
  - 현재 정점(`start_vertex`)을 방문 처리(`True`)하고 출력합니다.
  - 그래프의 정점들을 순회하며 방문하지 않은 정점에 대해 재귀 호출을 수행합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 실행 예시를 확인할 수 있습니다.

```python
g = Graph()
g.add_edge(0, 1)
# ... 간선 추가 ...
g.print_graph()
print("DFS:")
g.dfs()
# 출력 예시: 0 1 2 3
```
