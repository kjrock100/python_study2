# 양방향 너비 우선 탐색 (Bidirectional Breadth-First Search)

이 문서는 `bidirectional_breadth_first_search.py` 파일에 구현된 **양방향 너비 우선 탐색(Bidirectional BFS)** 알고리즘에 대해 설명합니다.

## 개요

양방향 BFS는 시작 노드와 목표 노드 양쪽에서 동시에 너비 우선 탐색을 진행하여 중간에서 만나는 지점을 찾는 알고리즘입니다. 단방향 BFS에 비해 탐색해야 하는 노드의 수가 기하급수적으로 줄어들 수 있어, 최단 경로를 더 빠르게 찾을 수 있습니다.

## 주요 설정

- `grid`: 0(이동 가능)과 1(장애물)로 구성된 2차원 리스트입니다.
- `delta`: 상, 좌, 하, 우 4방향 이동을 정의합니다. `[[-1, 0], [0, -1], [1, 0], [0, 1]]`

## 주요 클래스

### `Node`

- **목적**: 그리드 상의 위치와 경로 정보를 저장합니다.
- **속성**:
  - `pos_x`, `pos_y`: 현재 좌표.
  - `goal_x`, `goal_y`: 목표 좌표.
  - `parent`: 경로 역추적을 위한 부모 노드.

### `BreadthFirstSearch` (단방향 BFS)

- **목적**: 일반적인 단방향 너비 우선 탐색을 수행합니다.
- **주요 메서드**:
  - `search()`: 큐(Queue)를 사용하여 너비 우선 탐색을 진행합니다. 목표에 도달하면 경로를 반환합니다.
  - `get_successors(parent)`: 현재 위치에서 이동 가능한(장애물이 없고 그리드 내부인) 이웃 노드들을 반환합니다.
  - `retrace_path(node)`: 부모 노드를 따라가며 시작점부터 현재 노드까지의 경로를 복원합니다.

### `BidirectionalBreadthFirstSearch` (양방향 BFS)

- **목적**: 시작점과 목표점에서 동시에 탐색을 진행하여 경로를 찾습니다.
- **속성**:
  - `fwd_bfs`: 시작점에서 목표점으로 향하는 정방향 BFS 인스턴스.
  - `bwd_bfs`: 목표점에서 시작점으로 향하는 역방향 BFS 인스턴스.
- **주요 메서드**:
  - `search()`:
    - 두 방향의 BFS 큐에서 노드를 하나씩 꺼내며 탐색합니다.
    - 두 탐색의 현재 노드가 같은 위치(`pos`)를 가리키면, 두 경로가 만난 것으로 간주하고 경로를 합칩니다.
  - `retrace_bidirectional_path(fwd_node, bwd_node)`: 정방향 경로와 역방향 경로를 결합하여 전체 최단 경로를 생성합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 단방향 BFS와 양방향 BFS의 실행 시간을 비교하는 예제를 확인할 수 있습니다.

```python
# 실행 예시
# 그리드 출력
# Unidirectional BFS computation time : ...
# Bidirectional BFS computation time : ...
```

## 참고 자료
- Wikipedia: Bidirectional search
