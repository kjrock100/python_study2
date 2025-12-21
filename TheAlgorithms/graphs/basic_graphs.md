# 기본 그래프 알고리즘 (Basic Graph Algorithms)

이 문서는 `basic_graphs.py` 파일에 구현된 **기본적인 그래프 알고리즘**들에 대해 설명합니다. 그래프 초기화부터 탐색, 최단 경로, 최소 신장 트리(MST) 등 다양한 알고리즘을 포함하고 있습니다.

## 그래프 초기화 함수

사용자 입력을 받아 그래프를 생성하는 함수들입니다.
- `initialize_unweighted_directed_graph(node_count, edge_count)`: 가중치 없는 유향 그래프 초기화.
- `initialize_unweighted_undirected_graph(node_count, edge_count)`: 가중치 없는 무향 그래프 초기화.
- `initialize_weighted_undirected_graph(node_count, edge_count)`: 가중치 있는 무향 그래프 초기화.

## 그래프 탐색 (Graph Traversal)

### `dfs(G, s)`
- **깊이 우선 탐색 (Depth First Search)**
- 스택(Stack)을 사용하여 구현되었습니다.
- 시작 노드 `s`에서 출발하여 가능한 깊게 그래프를 탐색합니다.

### `bfs(G, s)`
- **너비 우선 탐색 (Breadth First Search)**
- 큐(Queue, `collections.deque`)를 사용하여 구현되었습니다.
- 시작 노드 `s`에서 가까운 노드부터 차례대로 탐색합니다.

## 최단 경로 알고리즘 (Shortest Path Algorithms)

### `dijk(G, s)`
- **다익스트라 알고리즘 (Dijkstra's Algorithm)**
- 시작 노드 `s`로부터 다른 모든 노드까지의 최단 거리를 계산합니다.
- 그리디(Greedy) 방식을 사용하며, 음수 가중치가 없을 때 사용 가능합니다.
- *참고*: 이 구현에서는 우선순위 큐 대신 선형 탐색을 사용하여 최소 거리를 찾습니다.

### `floy(A_and_n)`
- **플로이드-워셜 알고리즘 (Floyd Warshall's Algorithm)**
- 모든 노드 쌍 간의 최단 거리를 구합니다.
- **매개변수**: `(A, n)` 형태의 튜플 (인접 행렬, 노드 수).
- 3중 반복문을 사용하여 거리를 갱신합니다.

## 최소 신장 트리 (Minimum Spanning Tree)

### `prim(G, s)`
- **프림 알고리즘 (Prim's Algorithm)**
- 시작 노드 `s`에서 시작하여 트리를 확장해 나가는 방식입니다.
- 현재 트리와 연결된 간선 중 가장 가중치가 작은 간선을 선택합니다.

### `krusk(E_and_n)`
- **크루스칼 알고리즘 (Kruskal's Algorithm)**
- **매개변수**: `(E, n)` 형태의 튜플 (간선 리스트, 노드 수).
- 간선 리스트(`E`)를 가중치 기준으로 정렬한 뒤, 사이클을 형성하지 않는 간선을 선택하여 트리를 만듭니다.
- 서로소 집합(Disjoint Set) 개념을 사용하여 사이클 여부를 확인합니다.

## 기타 알고리즘

### `topo(G, ind=None, Q=None)`
- **위상 정렬 (Topological Sort)**
- 유향 그래프의 노드들을 선형으로 정렬합니다. (선후 관계 유지)
- 진입 차수(`ind`)가 0인 노드부터 큐(`Q`)에 넣어 처리합니다.

### `find_isolated_nodes(graph)`
- 그래프 내에서 연결된 간선이 없는 고립된 노드들을 찾아 반환합니다.

## 입력 헬퍼 함수

- `adjm()`: 인접 행렬 입력을 받습니다.
- `edglist()`: 간선 리스트 입력을 받습니다.

## 실행 방법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다.
1. 노드 수와 간선 수를 입력합니다.
2. 그래프 종류(1, 2, 3)를 선택합니다.
3. 간선 정보를 입력하면 해당 그래프 객체가 생성됩니다.

```python
# 예시 입력
# Number of nodes and edges: 5 6
# Press 1 or 2 or 3 ... : 2
# Edge 1: <node1> <node2> 1 2
# ...
```
