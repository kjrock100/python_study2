# 무작위 그래프 생성기 (Random Graph Generator)

이 문서는 `random_graph_generator.py` 파일에 구현된 **무작위 그래프 생성** 알고리즘에 대해 설명합니다.

## 개요

이 코드는 주어진 정점(Vertex)의 수와 간선(Edge)이 존재할 확률을 기반으로 무작위 그래프를 생성합니다. 이는 **Erdős-Rényi 모델 ($G(n, p)$)**을 따르며, 유향 그래프(Directed Graph)와 무향 그래프(Undirected Graph)를 모두 지원합니다. 그래프는 **인접 리스트(Adjacency List)** 형태인 딕셔너리로 반환됩니다.

## 주요 함수

### `random_graph(vertices_number: int, probability: float, directed: bool = False) -> dict`

- **목적**: 지정된 확률에 따라 간선을 생성하여 무작위 그래프를 만듭니다.
- **매개변수**:
  - `vertices_number`: 정점의 개수 ($n$).
  - `probability`: 임의의 두 정점 사이에 간선이 존재할 확률 ($p$, 0.0 ~ 1.0).
  - `directed`: `True`이면 유향 그래프, `False`이면 무향 그래프를 생성합니다. (기본값: `False`)
- **반환값**: 생성된 그래프의 인접 리스트 (딕셔너리).
- **동작 원리**:
  1. **특수 케이스 처리**:
     - 확률이 1 이상이면 `complete_graph`를 호출하여 완전 그래프를 반환합니다.
     - 확률이 0 이하이면 간선이 없는 그래프를 반환합니다.
  2. **간선 생성**:
     - 모든 정점 쌍 `(i, j)` (단, `i < j`)에 대해 반복합니다.
     - 0과 1 사이의 난수를 생성하여 `probability`보다 작으면 간선을 추가합니다.
     - **무향 그래프**인 경우, `j`에서 `i`로 가는 간선도 함께 추가합니다.

### `complete_graph(vertices_number: int) -> dict`

- **목적**: 모든 정점이 서로 연결된 **완전 그래프(Complete Graph)**를 생성합니다.
- **매개변수**: `vertices_number` (정점의 개수).
- **반환값**: 완전 그래프의 인접 리스트.
- **동작**: 리스트 컴프리헨션을 사용하여 자기 자신을 제외한 모든 정점과 연결된 리스트를 생성합니다.

## 사용법

`if __name__ == "__main__":` 블록의 `doctest` 예제를 통해 동작을 확인할 수 있습니다.

```python
import random
from random_graph_generator import random_graph

# 시드 설정 (재현 가능한 결과를 위해)
random.seed(1)

# 정점 4개, 연결 확률 0.5인 무향 그래프 생성
graph = random_graph(4, 0.5)
print(graph)
# 출력 예시: {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}

# 정점 4개, 연결 확률 0.5인 유향 그래프 생성
random.seed(1)
d_graph = random_graph(4, 0.5, directed=True)
print(d_graph)
# 출력 예시: {0: [1], 1: [2, 3], 2: [3], 3: []}
```
