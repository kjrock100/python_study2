# `non_recursive_segment_tree.py` 코드 설명

이 문서는 `non_recursive_segment_tree.py` 스크립트에 구현된 비재귀적(Iterative) 세그먼트 트리에 대해 설명합니다.

## 1. 비재귀적 세그먼트 트리란?

세그먼트 트리는 배열의 특정 구간에 대한 연산(예: 합, 곱, 최댓값, 최솟값)을 효율적으로 수행하는 자료 구조입니다. 일반적으로 재귀(Recursion)를 사용하여 구현하지만, 이 스크립트는 반복문(Iteration)을 사용하여 동일한 기능을 구현합니다.

**주요 특징:**
-   **구간 쿼리 (Range Query)**: O(log N)
-   **단일 원소 업데이트 (Point Update)**: O(log N)
-   **구현**: 재귀 호출 없이 반복문으로만 구성되어 있어 함수 호출 오버헤드가 없고, 경우에 따라 더 빠를 수 있습니다.

이 구현은 **교환 법칙이 성립하는(commutative)** 결합 함수(`fnc`)와 함께 동작하도록 설계되었습니다. (예: 덧셈, 곱셈, min, max)

## 2. 구현 방식

이 세그먼트 트리는 크기가 `2 * N`인 하나의 리스트(`st`)를 사용하여 트리를 표현합니다.

-   **`st[N:]`**: 원본 배열의 원소들이 저장됩니다 (리프 노드).
-   **`st[:N]`**: 트리의 내부 노드들이 저장됩니다. `st[i]`는 `st[2*i]`와 `st[2*i+1]`의 결합 결과입니다.

## 3. 클래스 및 메서드 설명

### `SegmentTree(Generic[T])` 클래스

#### `__init__(self, arr: list[T], fnc: Callable[[T, T], T])`
-   **역할**: 세그먼트 트리를 초기화하고 빌드합니다.
-   **매개변수**:
    -   `arr`: 원본 데이터 리스트.
    -   `fnc`: 두 원소를 결합하는 함수 (예: `lambda a, b: a + b`, `min`, `max`).
-   **동작**:
    1.  크기가 `2 * N`인 `st` 리스트를 생성하고, `N`번 인덱스부터 `arr`의 내용으로 채웁니다.
    2.  `build()` 메서드를 호출하여 트리의 나머지 부분을 구축합니다.

#### `build(self) -> None`
-   **역할**: 세그먼트 트리의 내부 노드를 계산하여 채웁니다.
-   **시간 복잡도**: O(N)
-   **동작**: 리프 노드의 바로 위 부모 노드들부터 시작하여 루트 노드(`st[1]`)까지 거슬러 올라가며 각 부모 노드의 값을 계산합니다.

#### `update(self, p: int, v: T) -> None`
-   **역할**: `p`번 인덱스의 원소 값을 `v`로 업데이트합니다.
-   **시간 복잡도**: O(log N)
-   **동작**:
    1.  리프 노드 `st[p + N]`의 값을 `v`로 변경합니다.
    2.  해당 노드부터 시작하여 루트까지 올라가면서 영향을 받는 모든 부모 노드의 값을 다시 계산합니다.

#### `query(self, l: int, r: int) -> T | None`
-   **역할**: 구간 `[l, r]` (양 끝 포함)에 대한 연산 결과를 반환합니다.
-   **시간 복잡도**: O(log N)
-   **동작**:
    1.  `l`과 `r`을 `st` 리스트 상의 실제 인덱스(`l+N`, `r+N`)로 변환합니다.
    2.  `l`이 `r`을 넘어설 때까지 반복합니다.
    3.  `l`이 오른쪽 자식(홀수 인덱스)이면, `st[l]` 값을 결과에 포함시키고 `l`을 다음 노드로 이동시킵니다.
    4.  `r`이 왼쪽 자식(짝수 인덱스)이면, `st[r]` 값을 결과에 포함시키고 `r`을 이전 노드로 이동시킵니다.
    5.  `l`과 `r`을 각각 부모 노드로 이동시킵니다.

## 4. 사용 예제

```python
if __name__ == "__main__":
    # 테스트용 배열
    test_array = [1, 10, -2, 9, -3, 8, 4, -7, 5, 6, 11, -12]

    # 다양한 결합 함수로 세그먼트 트리 생성
    min_segment_tree = SegmentTree(test_array, min)
    max_segment_tree = SegmentTree(test_array, max)
    sum_segment_tree = SegmentTree(test_array, lambda a, b: a + b)

    # 구간 [0, 11]의 최솟값 쿼리
    print(f"Min in [0, 11]: {min_segment_tree.query(0, 11)}")
    # 출력: Min in [0, 11]: -12

    # 구간 [3, 7]의 최댓값 쿼리
    print(f"Max in [3, 7]: {max_segment_tree.query(3, 7)}")
    # 출력: Max in [3, 7]: 9

    # 구간 [0, 4]의 합 쿼리
    print(f"Sum in [0, 4]: {sum_segment_tree.query(0, 4)}")
    # 출력: Sum in [0, 4]: 15

    # 2번 인덱스의 값을 6으로 업데이트
    sum_segment_tree.update(2, 6)

    # 업데이트 후 구간 [0, 4]의 합 쿼리
    print(f"Sum in [0, 4] after update: {sum_segment_tree.query(0, 4)}")
    # 출력: Sum in [0, 4] after update: 23
```

## 5. 테스트

스크립트에는 `doctest`와 `if __name__ == "__main__"` 블록 내의 종합적인 테스트 코드가 포함되어 있습니다. 터미널에서 다음 명령어를 실행하여 코드의 정확성을 검증할 수 있습니다.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/non_recursive_segment_tree.py
```

모든 `assert` 문을 통과하면 아무런 출력 없이 정상적으로 종료됩니다.