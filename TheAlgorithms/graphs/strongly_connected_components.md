# 강한 연결 요소 (Strongly Connected Components)

이 문서는 `strongly_connected_components.py` 파일에 구현된 **강한 연결 요소(SCC)** 찾기 알고리즘에 대해 설명합니다. 이 구현은 **코사라주 알고리즘(Kosaraju's Algorithm)**을 기반으로 합니다.

## 개요

유향 그래프(Directed Graph)에서 강한 연결 요소(SCC)란, 해당 부분 그래프 내의 모든 정점 쌍 $(u, v)$에 대해 $u$에서 $v$로 가는 경로와 $v$에서 $u$로 가는 경로가 모두 존재하는 최대 부분 그래프를 의미합니다.

코사라주 알고리즘은 두 번의 깊이 우선 탐색(DFS)을 사용하여 $O(V + E)$ 시간 복잡도로 SCC를 찾아냅니다.

## 주요 함수

### `topology_sort(graph, vert, visited) -> list[int]`

- **목적**: 첫 번째 DFS를 수행하여 정점들의 탐색 종료 순서를 기록합니다.
- **매개변수**:
  - `graph`: 원본 그래프의 인접 리스트.
  - `vert`: 현재 탐색 중인 정점.
  - `visited`: 방문 여부 리스트.
- **반환값**: 탐색이 완료된 순서대로 정점이 담긴 리스트 (`order`).
- **동작**:
  - 정점을 방문하고, 이웃 정점들을 재귀적으로 방문합니다.
  - 모든 이웃 방문이 끝난 후 현재 정점을 `order` 리스트에 추가합니다. (스택과 유사한 역할)

### `find_components(reversed_graph, vert, visited) -> list[int]`

- **목적**: 전치 그래프(Reversed Graph)에서 DFS를 수행하여 하나의 강한 연결 요소를 찾습니다.
- **매개변수**:
  - `reversed_graph`: 간선 방향이 뒤집힌 그래프.
  - `vert`: 탐색 시작 정점.
  - `visited`: 방문 여부 리스트.
- **반환값**: 하나의 SCC를 구성하는 정점 리스트 (`component`).

### `strongly_connected_components(graph) -> list[list[int]]`

- **목적**: 전체 알고리즘을 조율하여 모든 SCC를 반환합니다.
- **알고리즘 단계**:
  1. **전치 그래프 생성**: 원본 그래프의 간선 방향을 반대로 한 `reversed_graph`를 생성합니다.
  2. **1차 DFS (`topology_sort`)**: 원본 그래프에서 DFS를 수행하여 정점들의 종료 순서(`order`)를 구합니다.
  3. **2차 DFS (`find_components`)**: `order`의 역순(종료 시간이 늦은 순서)으로 정점을 선택하여, 아직 방문하지 않았다면 `reversed_graph`에서 DFS를 수행합니다. 이때 방문되는 정점들이 하나의 SCC를 형성합니다.
  4. **결과 반환**: 발견된 모든 SCC 리스트를 반환합니다.

## 사용법

독스트링(Docstring)에 포함된 예제를 통해 동작을 확인할 수 있습니다.

```python
test_graph = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}
# 0, 1, 2는 서로 순환하고, 3, 4, 5는 서로 순환함

print(strongly_connected_components(test_graph))
# 결과: [[0, 2, 1], [3, 5, 4]] (순서는 구현에 따라 다를 수 있음)
```
