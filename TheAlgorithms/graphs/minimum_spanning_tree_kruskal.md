# 크루스칼 알고리즘 (Kruskal's Algorithm)

이 문서는 `minimum_spanning_tree_kruskal.py` 파일에 구현된 **크루스칼 알고리즘**에 대해 설명합니다.

## 개요

크루스칼 알고리즘은 가중치가 있는 무향 그래프에서 **최소 신장 트리(MST, Minimum Spanning Tree)**를 찾는 그리디 알고리즘입니다. 간선들을 가중치 오름차순으로 정렬한 뒤, 사이클을 형성하지 않는 간선을 순서대로 선택하여 트리를 구성합니다.

## 주요 함수: `kruskal`

### `kruskal(num_nodes: int, edges: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]`

- **목적**: 주어진 그래프의 최소 신장 트리를 구성하는 간선들의 리스트를 반환합니다.
- **매개변수**:
  - `num_nodes`: 그래프의 노드 개수.
  - `edges`: 간선 정보가 담긴 리스트. 각 요소는 `(node1, node2, cost)` 형태의 튜플입니다.
- **반환값**: MST에 포함된 간선들의 리스트.

### 알고리즘 동작 원리

1. **간선 정렬**:
   - 입력받은 `edges`를 가중치(`cost`) 기준으로 오름차순 정렬합니다.

2. **Union-Find 초기화**:
   - `parent` 리스트를 생성하여 각 노드가 자기 자신을 부모로 가리키도록 초기화합니다. 이는 서로소 집합(Disjoint Set)을 관리하기 위함입니다.

3. **간선 선택 루프**:
   - 정렬된 간선을 하나씩 순회합니다.
   - **Find**: `find_parent` 함수를 사용하여 두 노드(`node1`, `node2`)가 속한 집합의 루트(대표)를 찾습니다. 경로 압축(Path Compression) 기법이 적용되어 있습니다.
   - **Union**: 두 노드의 루트가 다르다면(즉, 아직 연결되지 않았다면):
     - 해당 간선을 MST 리스트(`minimum_spanning_tree`)에 추가합니다.
     - 총 비용(`minimum_spanning_tree_cost`)을 갱신합니다.
     - 두 집합을 하나로 합칩니다 (`parent[parent_a] = parent_b`).

4. **결과 반환**:
   - 최종적으로 구성된 MST 간선 리스트를 반환합니다.

## 사용법

`if __name__ == "__main__":` 블록을 통해 사용자 입력을 받아 실행할 수 있으며, `doctest`를 통해 예제 케이스를 검증할 수 있습니다.

```python
# 예시 실행
# 노드 수: 4, 간선: (0, 1, 3), (1, 2, 5), (2, 3, 1)
edges = [(0, 1, 3), (1, 2, 5), (2, 3, 1)]
mst = kruskal(4, edges)
print(mst)
# 결과: [(2, 3, 1), (0, 1, 3), (1, 2, 5)]
```

## 시간 복잡도
- 간선 정렬: $O(E \log E)$
- Union-Find 연산: 거의 상수 시간 (역 아커만 함수)
- 전체 복잡도: $O(E \log E)$ 또는 $O(E \log V)$