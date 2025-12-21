# 0-1 너비 우선 탐색 최단 경로 (0-1 BFS Shortest Path)

이 문서는 `bfs_zero_one_shortest_path.py` 파일에 구현된 **0-1 BFS 알고리즘**에 대해 설명합니다.

## 개요

일반적인 다익스트라 알고리즘은 $O(E \log V)$의 시간 복잡도를 가지지만, 간선의 가중치가 0 또는 1로만 구성된 그래프에서는 **0-1 BFS**를 사용하여 $O(E + V)$의 시간 복잡도로 최단 경로를 구할 수 있습니다.

이 알고리즘은 덱(Deque, Double-ended queue)을 사용하여 가중치가 0인 간선은 덱의 앞쪽(Front)에, 가중치가 1인 간선은 덱의 뒤쪽(Back)에 추가함으로써 정렬 상태를 유지합니다.

## 주요 클래스

### `Edge`
- **목적**: 가중치가 있는 유향 그래프의 간선 정보를 저장하는 데이터 클래스입니다.
- **속성**:
  - `destination_vertex`: 도착 정점 인덱스.
  - `weight`: 간선의 가중치 (0 또는 1).

### `AdjacencyList`
- **목적**: 인접 리스트 방식으로 그래프를 표현하고 경로 탐색 기능을 제공합니다.

#### `__init__(self, size: int)`
- 그래프의 크기(정점 개수)를 받아 초기화합니다.

#### `add_edge(self, from_vertex: int, to_vertex: int, weight: int)`
- **목적**: 그래프에 유향 간선을 추가합니다.
- **제약 사항**: 가중치(`weight`)는 반드시 0 또는 1이어야 하며, 정점 인덱스는 유효한 범위 내에 있어야 합니다. 그렇지 않으면 `ValueError`가 발생합니다.

#### `get_shortest_path(self, start_vertex: int, finish_vertex: int) -> int | None`
- **목적**: 시작 정점에서 도착 정점까지의 최단 거리를 계산합니다.
- **알고리즘 동작 원리**:
  1. `deque`를 생성하고 시작 정점을 넣습니다.
  2. `distances` 리스트를 초기화하여 시작점은 0, 나머지는 `None`으로 설정합니다.
  3. 덱이 빌 때까지 다음 과정을 반복합니다:
     - 덱의 앞에서 정점(`current_vertex`)을 꺼냅니다.
     - 인접한 모든 간선에 대해:
       - 새로운 거리(`new_distance`)가 기존 거리보다 짧으면 거리를 갱신합니다.
       - **가중치가 0인 경우**: 덱의 **맨 앞(`appendleft`)**에 추가합니다. (거리가 늘어나지 않았으므로 우선 처리)
       - **가중치가 1인 경우**: 덱의 **맨 뒤(`append`)**에 추가합니다. (거리가 1 늘어났으므로 나중에 처리)
  4. 도착 정점까지의 거리를 반환합니다. 경로가 없으면 `ValueError`를 발생시킵니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 코드를 검증합니다.

사용 예시:
```python
g = AdjacencyList(3)
g.add_edge(0, 1, 0)  # 0 -> 1 (가중치 0)
g.add_edge(1, 2, 1)  # 1 -> 2 (가중치 1)

shortest_dist = g.get_shortest_path(0, 2)
# 결과: 1
```

## 참고 자료
- Codeforces Blog Entry
