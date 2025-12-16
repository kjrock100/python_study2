# `segment_tree_other.py` 코드 설명

이 문서는 `segment_tree_other.py` 스크립트에 구현된 재귀적, 노드 기반의 세그먼트 트리에 대해 설명합니다.

## 1. 세그먼트 트리란?

세그먼트 트리는 배열의 특정 구간에 대한 연산(예: 합, 곱, 최댓값, 최솟값)을 효율적으로 수행하는 자료 구조입니다. 이 구현은 각 노드를 객체로 표현하며, 재귀(Recursion)를 통해 트리를 구축하고 쿼리합니다.

**주요 특징:**
-   **구간 쿼리 (Range Query)**: O(log N)
-   **단일 원소 업데이트 (Point Update)**: O(log N)
-   **구축 (Build)**: O(N)

이 구현은 `non_recursive_segment_tree.py`와 달리, 실제 트리처럼 각 노드를 `SegmentTreeNode` 객체로 만들고 이들을 연결하는 방식입니다.

## 2. 클래스 구조

### `SegmentTreeNode` 클래스

트리를 구성하는 각 노드를 표현하는 클래스입니다.

-   `__init__(self, start, end, val, left=None, right=None)`: 노드를 초기화합니다.
    -   `start`, `end`: 이 노드가 담당하는 구간의 시작과 끝 인덱스.
    -   `val`: 해당 구간의 연산 결과 값.
    -   `mid`: 구간의 중간 인덱스.
    -   `left`, `right`: 왼쪽, 오른쪽 자식 노드에 대한 참조.

### `SegmentTree` 클래스

세그먼트 트리 전체를 관리하고, 사용자에게 인터페이스를 제공하는 메인 클래스입니다.

## 3. 메서드 설명

### `__init__(self, collection: Sequence, function)`
-   **역할**: 세그먼트 트리를 초기화하고, `_build_tree`를 호출하여 트리를 구축합니다.
-   **매개변수**:
    -   `collection`: 원본 데이터 시퀀스(리스트 등).
    -   `function`: 두 원소를 결합하는 함수 (예: `operator.add`, `max`, `min`).

### `update(self, i, val)`
-   **역할**: `i`번 인덱스의 원소 값을 `val`로 업데이트합니다. 공개용 인터페이스이며, 내부적으로 `_update_tree`를 호출합니다.
-   **시간 복잡도**: O(log N)

### `query_range(self, i, j)`
-   **역할**: 구간 `[i, j]` (양 끝 포함)에 대한 연산 결과를 반환합니다. 공개용 인터페이스이며, 내부적으로 `_query_range`를 호출합니다.
-   **시간 복잡도**: O(log N)

### `traverse(self)`
-   **역할**: 트리의 모든 노드를 레벨 순서(너비 우선 탐색)로 순회하는 제너레이터(generator)를 반환합니다. 디버깅이나 시각화에 유용합니다.

### 내부 헬퍼 메서드 (Underscore `_`로 시작)

#### `_build_tree(self, start, end)`
-   **역할**: 재귀적으로 세그먼트 트리를 구축합니다.
-   **동작**: 주어진 `[start, end]` 구간을 반으로 나누어 왼쪽과 오른쪽 자식 트리를 재귀적으로 만든 후, 두 자식의 결과 값을 `function`으로 결합하여 현재 노드의 값을 설정합니다.

#### `_update_tree(self, node, i, val)`
-   **역할**: 재귀적으로 `i`번 인덱스를 포함하는 리프 노드를 찾아 값을 갱신하고, 상위 노드들의 값을 다시 계산합니다.
-   **동작**: `i`가 현재 노드의 `mid`보다 작거나 같으면 왼쪽으로, 크면 오른쪽으로 재귀 호출을 보냅니다. 재귀가 끝난 후, 현재 노드의 값을 자식 노드들의 값을 이용해 갱신합니다.

#### `_query_range(self, node, i, j)`
-   **역할**: 재귀적으로 `[i, j]` 구간에 대한 쿼리를 수행합니다.
-   **동작**:
    1.  **완전 일치**: 현재 노드의 구간이 쿼리 구간 `[i, j]`와 정확히 일치하면 현재 노드의 값을 반환합니다.
    2.  **부분 포함 (왼쪽)**: 쿼리 구간이 현재 노드의 왼쪽 자식에만 포함되면 왼쪽으로 재귀 호출합니다.
    3.  **부분 포함 (오른쪽)**: 쿼리 구간이 현재 노드의 오른쪽 자식에만 포함되면 오른쪽으로 재귀 호출합니다.
    4.  **양쪽 걸침**: 쿼리 구간이 양쪽 자식에 모두 걸쳐 있으면, 양쪽으로 각각 재귀 호출하여 얻은 두 결과를 `function`으로 결합하여 반환합니다.

## 4. 사용 예제

`doctest`와 `if __name__ == "__main__"` 블록에 다양한 사용 예제가 포함되어 있습니다.

```python
import operator

# 덧셈을 위한 세그먼트 트리 생성
num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)

# 구간 [1, 3]의 합 쿼리
print(num_arr.query_range(1, 3))
# 출력: 9 (1 + 5 + 3)

# 1번 인덱스의 값을 5로 업데이트
num_arr.update(1, 5)

# 업데이트 후 구간 [1, 3]의 합 쿼리
print(num_arr.query_range(1, 3))
# 출력: 13 (5 + 5 + 3)

# 최댓값을 위한 세그먼트 트리 생성
max_arr = SegmentTree([2, 1, 5, 3, 4], max)

# 구간 [1, 3]의 최댓값 쿼리
print(max_arr.query_range(1, 3))
# 출력: 5
```

## 5. 테스트

스크립트에는 `doctest`가 포함되어 있어 코드의 정확성을 쉽게 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/segment_tree_other.py
```

테스트가 성공하면 아무런 출력도 나타나지 않습니다.