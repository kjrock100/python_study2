# 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)

이 문서는 `graphs_floyd_warshall.py` 파일에 구현된 **플로이드-워셜 알고리즘**에 대해 설명합니다.

## 개요

플로이드-워셜 알고리즘은 가중치가 있는 유향 그래프(Weighted Directed Graph)에서 **모든 정점 쌍(All Pairs)** 간의 최단 거리를 구하는 알고리즘입니다. 음수 가중치를 가진 간선이 있어도 동작하지만, 음수 사이클이 존재하면 사용할 수 없습니다.

시간 복잡도는 정점의 개수가 $V$일 때 $O(V^3)$입니다.

## 주요 함수

### `floyd_warshall(graph, v)`

- **목적**: 모든 정점 쌍 사이의 최단 거리를 계산합니다.
- **매개변수**:
  - `graph`: 인접 행렬(Adjacency Matrix) 형태로 표현된 그래프. `graph[i][j]`는 정점 `i`에서 `j`로 가는 간선의 가중치입니다. 연결되지 않은 경우 무한대(`float("inf")`)로 설정됩니다.
  - `v`: 정점의 개수.
- **반환값**: 최단 거리 행렬(`dist`)과 정점 개수(`v`)를 튜플로 반환합니다.
- **알고리즘 동작**:
  1. `dist` 행렬을 초기화하고 입력받은 `graph`의 가중치를 복사합니다.
  2. 3중 반복문을 수행합니다:
     - `k`: 거쳐가는 중간 정점
     - `i`: 출발 정점
     - `j`: 도착 정점
  3. 점화식 `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`을 사용하여, `k`를 거쳐가는 경로가 더 짧다면 거리를 갱신합니다.

### `_print_dist(dist, v)`

- **목적**: 계산된 최단 거리 행렬을 보기 좋게 출력합니다.
- **동작**:
  - 거리가 무한대(`float("inf")`)인 경우 "INF"로 출력하고, 그렇지 않으면 정수형으로 변환하여 출력합니다.

## 사용법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다. 사용자로부터 정점 수, 간선 수, 그리고 각 간선의 정보(출발, 도착, 가중치)를 입력받습니다.

**입력 예시:**
```text
Enter number of vertices: 3
Enter number of edges: 2
Edge 1
Enter source: 1
Enter destination: 2
Enter weight: 2
Edge 2
Enter source: 2
Enter destination: 1
Enter weight: 1
```

**주의 사항**:
- 입력받는 정점 인덱스는 0부터 시작하는 것으로 가정합니다. (코드 상에서는 입력받은 값을 그대로 인덱스로 사용)
- 자기 자신으로의 거리(`graph[i][i]`)는 0으로 초기화됩니다.
