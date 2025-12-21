# 벨만-포드 알고리즘 (Bellman-Ford Algorithm)

이 문서는 `bellman_ford.py` 파일에 구현된 **벨만-포드 알고리즘**에 대해 설명합니다.

## 개요

벨만-포드 알고리즘은 가중치가 있는 유향 그래프에서 시작 정점(Source Vertex)으로부터 다른 모든 정점까지의 최단 경로를 찾는 알고리즘입니다. 다익스트라(Dijkstra) 알고리즘과 달리 **음수 가중치**를 가진 간선이 있어도 사용할 수 있으며, **음수 사이클(Negative Cycle)**의 존재 여부를 감지할 수 있습니다.

## 주요 함수

### `bellman_ford(graph, vertex_count, edge_count, src)`

- **목적**: 시작 정점 `src`에서 모든 다른 정점까지의 최단 거리를 계산합니다.
- **매개변수**:
  - `graph`: 간선 정보가 담긴 리스트. 각 요소는 `{"src": u, "dst": v, "weight": w}` 형태의 딕셔너리입니다.
  - `vertex_count`: 정점의 개수 ($V$).
  - `edge_count`: 간선의 개수 ($E$).
  - `src`: 시작 정점의 인덱스.
- **반환값**: 각 정점까지의 최단 거리를 담은 리스트 (`distance`).
- **예외 처리**: 그래프에 음수 사이클이 존재하면 `Exception("Negative cycle found")`를 발생시킵니다.

### `check_negative_cycle(graph, distance, edge_count)`

- **목적**: 벨만-포드 알고리즘의 수행 후 음수 사이클이 존재하는지 확인합니다.
- **동작 원리**: 모든 간선에 대해 한 번 더 완화(Relaxation) 과정을 시도합니다. 만약 거리가 더 줄어드는 간선이 있다면, 음수 사이클이 존재하는 것입니다.

### `print_distance(distance, src)`

- **목적**: 계산된 최단 거리를 보기 좋게 출력합니다.

## 알고리즘 동작 과정

1. **초기화**:
   - `distance` 리스트를 생성하고 모든 값을 무한대(`float("inf")`)로 설정합니다.
   - 시작 정점 `src`의 거리는 `0`으로 설정합니다.

2. **간선 완화 (Relaxation)**:
   - 정점의 개수보다 하나 적은 횟수(`vertex_count - 1`)만큼 반복합니다.
   - 각 반복마다 모든 간선을 확인하며, `distance[u] + weight < distance[v]`인 경우 `distance[v]`를 갱신합니다.

3. **음수 사이클 확인**:
   - `check_negative_cycle` 함수를 호출하여 음수 사이클 여부를 확인합니다.

## 사용법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다.
1. `doctest`를 실행하여 예제 케이스를 검증합니다.
2. 사용자로부터 정점 수, 간선 수, 그리고 각 간선의 정보(출발, 도착, 가중치)를 입력받아 알고리즘을 실행합니다.

```python
# 실행 예시
# Enter number of vertices: 5
# Enter number of edges: 8
# Edge 1
# Enter source, destination, weight: 0 1 -1
# ...
```
