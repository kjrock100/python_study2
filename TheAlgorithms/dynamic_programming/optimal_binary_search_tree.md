# 최적 이진 탐색 트리 (Optimal Binary Search Tree)

이 문서는 `optimal_binary_search_tree.py` 파일에 구현된 **최적 이진 탐색 트리(Optimal BST)** 알고리즘에 대해 설명합니다. 이 알고리즘은 주어진 키(Key)와 빈도수(Frequency)를 바탕으로 검색 비용을 최소화하는 이진 탐색 트리를 구축합니다.

## 개요

각 노드마다 검색될 확률(빈도)이 다를 때, 자주 검색되는 노드를 루트에 가깝게 배치하여 전체적인 검색 비용을 줄이는 것이 목표입니다. 이 코드는 **동적 계획법(Dynamic Programming)**을 사용하여 $O(n^2)$의 시간 복잡도로 최적의 트리를 찾습니다.

## 주요 클래스 및 함수

### `Node` 클래스
- **목적**: 이진 탐색 트리의 노드 정보를 저장합니다.
- **속성**:
  - `key`: 노드의 키 값.
  - `freq`: 노드가 검색되는 빈도수.

### `print_binary_search_tree(root, key, i, j, parent, is_left)`
- **목적**: 계산된 `root` 테이블을 바탕으로 최적 이진 탐색 트리의 구조를 재귀적으로 출력합니다.
- **매개변수**:
  - `root`: 최적의 루트 노드 인덱스를 저장한 2차원 배열.
  - `key`: 키 값 리스트.
  - `i`, `j`: 현재 서브트리의 범위.
  - `parent`: 부모 노드의 키 값 (루트인 경우 -1).
  - `is_left`: 현재 노드가 부모의 왼쪽 자식인지 여부.

### `find_optimal_binary_search_tree(nodes)`
- **목적**: 최적 이진 탐색 트리를 계산하고 결과를 출력합니다.
- **매개변수**: `nodes` (Node 객체들의 리스트).
- **알고리즘 동작 원리**:
  1. **정렬**: 입력된 노드들을 키(`key`) 기준으로 오름차순 정렬합니다.
  2. **초기화**:
     - `dp[i][j]`: $i$부터 $j$까지의 노드로 만들 수 있는 최적 트리의 최소 비용.
     - `sum[i][j]`: $i$부터 $j$까지의 노드 빈도수의 합.
     - `root[i][j]`: $i$부터 $j$까지의 노드로 구성된 최적 트리의 루트 노드 인덱스.
  3. **DP 테이블 채우기**:
     - 부분 트리의 길이(`interval_length`)를 2부터 $n$까지 늘려가며 반복합니다.
     - 각 구간 $(i, j)$에 대해 가능한 모든 루트 $r$을 시도합니다.
     - **크누스 최적화 (Knuth's Optimization)**: 루트 $r$의 탐색 범위를 `root[i][j-1]`에서 `root[i+1][j]` 사이로 제한하여 성능을 개선합니다.
     - 점화식: `cost = left_cost + sum[i][j] + right_cost`
     - 최소 비용을 `dp[i][j]`에 저장하고, 해당 루트를 `root[i][j]`에 기록합니다.
  4. **결과 출력**: 최소 비용과 트리 구조를 출력합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

1. 1부터 10까지의 키와 무작위 빈도수를 가진 `Node` 객체들을 생성합니다.
2. `find_optimal_binary_search_tree` 함수를 호출하여 최적 트리를 찾고 구조를 출력합니다.

```python
# 예시 출력
Binary search tree nodes:
...
The cost of optimal BST for given tree nodes is 324.
20 is the root of the binary search tree.
...
```
