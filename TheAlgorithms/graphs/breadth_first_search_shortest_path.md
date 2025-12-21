# 너비 우선 탐색 최단 경로 (BFS Shortest Path)

이 문서는 `breadth_first_search_shortest_path.py` 파일에 구현된 **너비 우선 탐색(BFS)**을 이용한 최단 경로 탐색 알고리즘에 대해 설명합니다.

## 개요

가중치가 없는 그래프(Unweighted Graph)에서 특정 시작 노드(Source Node)로부터 목표 노드(Target Node)까지의 최단 경로를 찾는 데 BFS가 사용됩니다. 이 코드는 경로를 추적하기 위해 부모 노드 정보를 저장하는 방식을 사용합니다.

## 주요 클래스: `Graph`

### `__init__(self, graph: dict[str, list[str]], source_vertex: str)`

- **목적**: 그래프 객체를 초기화합니다.
- **매개변수**:
  - `graph`: 인접 리스트 형태의 딕셔너리.
  - `source_vertex`: 탐색을 시작할 출발 정점.
- **속성**:
  - `self.parent`: BFS 탐색 과정에서 각 노드의 부모 노드를 저장하는 딕셔너리입니다. 이를 통해 나중에 경로를 역추적할 수 있습니다.

### `breath_first_search(self)`

- **목적**: 시작 정점으로부터 BFS를 수행하여 연결된 모든 노드를 방문하고 부모 관계를 기록합니다.
- **동작 원리**:
  - 큐(Queue)를 사용하여 너비 우선 탐색을 진행합니다.
  - 방문하지 않은 이웃 노드를 발견하면, `visited` 집합에 추가하고 `self.parent`에 현재 노드를 부모로 기록한 뒤 큐에 넣습니다.
  - *참고*: 코드 내 함수명이 `breath_first_search`로 되어 있습니다 (Breadth의 오타로 보임).

### `shortest_path(self, target_vertex: str) -> str`

- **목적**: `breath_first_search` 실행 후, 저장된 부모 정보를 바탕으로 시작점에서 목표점까지의 최단 경로 문자열을 반환합니다.
- **매개변수**: `target_vertex` (목표 정점).
- **반환값**:
  - 경로가 존재하는 경우: `"v1->v2->...->vn"` 형태의 문자열.
  - 경로가 존재하지 않는 경우: `"No path from vertex:..."` 메시지.
- **동작 원리**:
  - 재귀적으로 부모 노드를 찾아 올라가며 경로 문자열을 구성합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 실행 예시를 확인할 수 있습니다.

```python
graph_data = {
    "A": ["B", "C", "E"],
    ...
}
g = Graph(graph_data, "G")
g.breath_first_search()  # 먼저 탐색을 수행해야 함

print(g.shortest_path("D"))
# 출력: G->C->A->B->D
```
