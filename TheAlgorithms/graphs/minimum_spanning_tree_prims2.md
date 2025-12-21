# 프림 알고리즘 2 (Prim's Algorithm 2)

이 문서는 `minimum_spanning_tree_prims2.py` 파일에 구현된 **프림 알고리즘(Prim's Algorithm)**에 대해 설명합니다. 이 코드는 최소 신장 트리(MST)를 구하기 위해 작성되었으며, 효율적인 연산을 위해 **최소 우선순위 큐(Min Priority Queue)**를 직접 구현하여 사용합니다.

## 개요

프림 알고리즘은 가중치가 있는 무향 그래프에서 모든 정점을 포함하면서 간선의 가중치 합이 최소가 되는 트리(MST)를 찾는 알고리즘입니다.

이 구현의 특징은 Python의 내장 `heapq`를 사용하는 대신, 힙 내의 원소 값을 효율적으로 갱신(`decrease-key`)할 수 있는 기능을 갖춘 우선순위 큐 클래스를 정의하여 사용한다는 점입니다.

## 주요 클래스

### `MinPriorityQueue`

- **목적**: 최소 힙(Min-Heap) 자료구조를 관리합니다.
- **특징**: `position_map`을 사용하여 힙 내부의 각 원소가 배열의 어느 인덱스에 위치하는지 추적합니다. 이를 통해 특정 원소의 우선순위(가중치)가 변경되었을 때 $O(\log N)$ 시간 복잡도로 힙을 재정렬할 수 있습니다.
- **주요 메서드**:
  - `push(elem, weight)`: 원소를 큐에 추가합니다.
  - `extract_min()`: 최솟값을 가진 원소를 제거하고 반환합니다.
  - `update_key(elem, weight)`: 큐에 있는 원소의 가중치를 변경하고 힙 속성을 유지하도록 위치를 조정합니다.
  - `is_empty()`: 큐가 비어있는지 확인합니다.

### `GraphUndirectedWeighted`

- **목적**: 가중치가 있는 무향 그래프를 인접 딕셔너리 형태로 표현합니다.
- **메서드**:
  - `add_node(node)`: 그래프에 노드를 추가합니다.
  - `add_edge(node1, node2, weight)`: 두 노드 사이의 간선과 가중치를 추가합니다.

## 주요 함수: `prims_algo`

### `prims_algo(graph)`

- **목적**: 주어진 그래프에 대해 알고리즘을 실행하여 거리 정보와 부모 노드 정보를 반환합니다.
- **매개변수**: `GraphUndirectedWeighted` 객체.
- **반환값**: `(dist, parent)` 튜플.
  - `dist`: 각 노드까지의 계산된 거리(가중치).
  - `parent`: 각 노드의 부모 노드 (트리 구조).
- **알고리즘 동작**:
  1. 모든 노드의 거리를 무한대로 초기화하고 우선순위 큐에 넣습니다.
  2. 시작 노드를 선택하여 거리를 0으로 설정합니다.
  3. 큐가 빌 때까지 최솟값을 가진 노드를 추출하고, 해당 노드의 이웃 노드들을 확인합니다.
  4. 이웃 노드로 가는 경로가 더 짧다면 거리를 갱신하고 우선순위 큐를 업데이트(`update_key`)합니다.
  
  *(참고: 이 구현의 거리 갱신 로직 `dist[neighbour] > dist[node] + weight`는 다익스트라 알고리즘의 최단 경로 갱신 방식과 유사하게 작성되어 있습니다.)*

## 사용법

`prims_algo` 함수의 독스트링 예제를 통해 실행 방법을 확인할 수 있습니다.

```python
graph = GraphUndirectedWeighted()
graph.add_edge("a", "b", 3)
graph.add_edge("b", "c", 10)
# ... 간선 추가 ...

dist, parent = prims_algo(graph)
```
