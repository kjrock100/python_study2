# 매칭을 이용한 최소 정점 덮개 (Matching Min Vertex Cover)

이 문서는 `matching_min_vertex_cover.py` 파일에 구현된 **매칭(Matching) 접근법**을 사용한 **최소 정점 덮개(Minimum Vertex Cover)** 근사 알고리즘에 대해 설명합니다.

## 개요

**최소 정점 덮개 문제**는 그래프의 모든 간선을 커버하기 위해 선택해야 하는 최소한의 정점 집합을 찾는 문제입니다. 이 문제는 NP-Hard이므로, 다항 시간 내에 최적해를 구하는 것이 어렵습니다.

이 알고리즘은 **극대 매칭(Maximal Matching)**을 이용하여 근사해를 구합니다. 그래프에서 서로 공유하는 정점이 없는 간선들의 집합(매칭)을 찾고, 그 간선들의 양쪽 끝점을 모두 정점 덮개에 포함시키는 방식입니다. 이 방법은 최적해의 크기보다 최대 2배 더 많은 정점을 선택할 수 있는 **2-근사 알고리즘(2-Approximation Algorithm)**입니다.

## 주요 함수

### `matching_min_vertex_cover(graph: dict) -> set`

- **목적**: 매칭 접근법을 사용하여 최소 정점 덮개의 근사해를 구합니다.
- **매개변수**:
  - `graph`: 인접 리스트 형태의 딕셔너리. (Key: 정점, Value: 이웃 정점 리스트)
- **반환값**: 선택된 정점들의 집합(`set`).
- **알고리즘 동작 원리**:
  1. `get_edges` 함수를 통해 그래프의 모든 간선 집합을 가져옵니다.
  2. 간선 집합이 비어있지 않은 동안 반복합니다:
     - 임의의 간선 `(u, v)`를 하나 선택(pop)합니다.
     - 두 정점 `u`와 `v`를 모두 결과 집합(`chosen_vertices`)에 추가합니다.
     - 선택된 정점 `u` 또는 `v`와 연결된 모든 간선을 간선 집합에서 제거합니다. (이 간선들은 이미 커버되었으므로)
  3. 결과 집합을 반환합니다.

### `get_edges(graph: dict) -> set`

- **목적**: 인접 리스트로 표현된 그래프에서 모든 간선을 추출하여 집합으로 반환합니다.
- **동작**:
  - 그래프의 모든 정점과 이웃을 순회하며 `(from_node, to_node)` 형태의 튜플을 집합에 추가합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 `doctest`를 실행하여 코드를 검증합니다.

```python
graph = {
    0: [1, 3],
    1: [0, 3],
    2: [0, 3, 4],
    3: [0, 1, 2],
    4: [2, 3]
}
print(matching_min_vertex_cover(graph))
# 출력 예시: {0, 1, 2, 4} (실행 순서에 따라 선택되는 간선이 달라질 수 있음)
```

## 참고 자료
- Wolfram MathWorld: Minimum Vertex Cover
- Princeton University Lecture Notes: Approximation Algorithms