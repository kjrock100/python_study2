# 인접 리스트 그래프 (Graph Adjacency List)

이 문서는 `graph_list.py` 파일에 구현된 **인접 리스트(Adjacency List)** 방식의 그래프 자료구조에 대해 설명합니다.

## 개요

이 코드는 파이썬의 딕셔너리(`dict`)를 사용하여 그래프를 구현합니다. 유향 그래프(Directed Graph)와 무향 그래프(Undirected Graph)를 모두 지원하며, 제네릭(Generic)을 사용하여 다양한 타입의 데이터를 정점(Vertex)으로 사용할 수 있습니다.

## 주요 클래스: `GraphAdjacencyList`

### `__init__(self, directed: bool = True)`

- **목적**: 그래프 객체를 초기화합니다.
- **매개변수**:
  - `directed`: `True`이면 유향 그래프, `False`이면 무향 그래프로 생성됩니다. (기본값: `True`)
- **속성**:
  - `self.adj_list`: 정점과 그 이웃 정점들의 리스트를 저장하는 딕셔너리입니다.

### `add_edge(self, source_vertex: T, destination_vertex: T)`

- **목적**: 두 정점 사이에 간선을 추가합니다.
- **매개변수**:
  - `source_vertex`: 시작 정점.
  - `destination_vertex`: 도착 정점.
- **동작 원리**:
  - 정점이 그래프에 존재하지 않으면 새로 생성합니다.
  - **무향 그래프 (`directed=False`)**:
    - `source`에서 `destination`으로, `destination`에서 `source`로 양방향 연결을 추가합니다.
  - **유향 그래프 (`directed=True`)**:
    - `source`에서 `destination`으로 가는 단방향 연결만 추가합니다.
    - `destination` 정점이 없다면 키(Key)만 생성하고 빈 리스트를 할당합니다.
- **반환값**: 메서드 체이닝(Method Chaining)을 위해 `self`를 반환합니다.

### `__repr__(self)`

- **목적**: 그래프의 현재 상태(인접 리스트)를 문자열로 반환합니다. `pprint.pformat`을 사용하여 보기 좋게 출력합니다.

## 사용법

클래스 독스트링(Docstring)에 포함된 예제를 통해 사용법을 확인할 수 있습니다.

```python
# 유향 그래프 예시
d_graph = GraphAdjacencyList()
d_graph.add_edge(0, 1)
d_graph.add_edge(1, 2).add_edge(1, 4).add_edge(1, 5)
print(d_graph)

# 무향 그래프 예시
u_graph = GraphAdjacencyList(directed=False)
u_graph.add_edge('a', 'b')
```
