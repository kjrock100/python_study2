# `lowest_common_ancestor.py` 코드 설명

이 문서는 `lowest_common_ancestor.py` 스크립트에 구현된 최소 공통 조상(Lowest Common Ancestor, LCA) 찾기 알고리즘에 대해 설명합니다.

## 1. 최소 공통 조상(LCA)이란?

트리 자료 구조에서 두 노드 `u`와 `v`의 최소 공통 조상은, `u`와 `v`를 모두 자손으로 가지는 노드들 중에서 가장 깊이가 깊은(즉, 두 노드에 가장 가까운) 노드를 의미합니다.

이 스크립트는 **BFS(너비 우선 탐색)**와 **이진 리프팅(Binary Lifting)** 기법을 결합하여 LCA 쿼리를 효율적으로 처리합니다.

-   **전처리(Preprocessing)**: O(N log N)
-   **쿼리(Query)**: O(log N)

## 2. 알고리즘 동작 원리

알고리즘은 크게 두 단계로 나뉩니다.

1.  **전처리 단계**:
    -   **BFS 실행 (`breadth_first_search`)**: 루트 노드부터 BFS를 수행하여 각 노드의 깊이(`level`)와 직계 부모(`parent[0]`)를 계산합니다.
    -   **희소 배열 생성 (`create_sparse`)**: 각 노드에 대해 2^i 번째 조상을 미리 계산하여 `parent` 배열(희소 배열)에 저장합니다. 이를 통해 특정 노드에서 2^i 만큼 위로 한 번에 점프할 수 있게 됩니다.

2.  **쿼리 단계 (`lowest_common_ancestor`)**:
    -   두 노드 `u`, `v`의 깊이를 맞춥니다. 더 깊은 노드를 다른 노드와 같은 깊이가 될 때까지 위로 올립니다. (이진 리프팅을 사용하여 O(log N)만에 이동)
    -   깊이가 같아진 두 노드가 동일하다면, 그 노드가 바로 LCA입니다.
    -   만약 다르다면, 두 노드가 같은 부모를 가질 때까지 동시에 한 칸씩 위로 올립니다. 이 과정 역시 이진 리프팅을 통해 효율적으로 수행됩니다. 두 노드의 공통 부모가 바로 LCA가 됩니다.

## 3. 함수 설명

### `breadth_first_search(...)`
-   **역할**: BFS를 통해 각 노드의 `level`(깊이)과 `parent[0]`(직계 부모)를 계산합니다.
-   **동작**:
    1.  루트 노드를 큐에 넣고 `level[root]`를 0으로 설정합니다.
    2.  큐에서 노드를 하나씩 꺼내면서, 방문하지 않은 인접 노드들의 `level`과 `parent[0]`을 설정하고 큐에 추가합니다.

### `create_sparse(...)`
-   **역할**: 이진 리프팅을 위한 희소 배열 `parent`를 채웁니다.
-   **동작**: 동적 프로그래밍을 이용합니다. `parent[j][i]` (노드 `i`의 2^j 번째 조상)는 `parent[j-1][parent[j-1][i]]` (노드 `i`의 2^(j-1) 번째 조상의 2^(j-1) 번째 조상)와 같습니다.

### `lowest_common_ancestor(u, v, ...)`
-   **역할**: 두 노드 `u`, `v`의 LCA를 O(log N) 시간에 찾습니다.
-   **동작**:
    1.  `level[u]`와 `level[v]`를 비교하여 항상 `u`가 더 깊은 노드가 되도록 조정합니다.
    2.  두 노드의 깊이 차이만큼 `u`를 위로 올립니다.
    3.  만약 `u`와 `v`가 같다면 `u`를 반환합니다.
    4.  `u`와 `v`가 같아지기 직전까지 두 노드를 동시에 위로 올립니다.
    5.  마지막으로 `u`의 직계 부모(`parent[0][u]`)를 반환합니다.

### `swap(a, b)`
-   **역할**: 두 정수를 XOR 연산을 이용해 교환하는 유틸리티 함수입니다.

## 4. 사용 예제

`main` 함수는 다음과 같은 트리 구조를 예제로 사용합니다.

```
        1
      / | \
     2  3  4
    /  /    \
   5  6      8
  / \ |     / \
 9  10 11  12 13
```

```python
def main() -> None:
    max_node = 13
    # ... (그래프, parent, level 배열 초기화) ...

    # 1. 전처리: BFS로 level과 직계 부모 계산
    level, parent = breadth_first_search(level, parent, max_node, graph, 1)
    # 2. 전처리: 희소 배열 생성
    parent = create_sparse(max_node, parent)

    # 3. 쿼리 실행
    print("LCA of node 1 and 3 is: ", lowest_common_ancestor(1, 3, level, parent))
    # 출력: LCA of node 1 and 3 is:  1

    print("LCA of node 5 and 6 is: ", lowest_common_ancestor(5, 6, level, parent))
    # 출력: LCA of node 5 and 6 is:  1

    print("LCA of node 7 and 11 is: ", lowest_common_ancestor(7, 11, level, parent))
    # 출력: LCA of node 7 and 11 is:  3
```