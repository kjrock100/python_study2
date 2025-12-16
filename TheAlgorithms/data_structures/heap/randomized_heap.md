# `randomized_heap.py` 코드 설명

이 문서는 `randomized_heap.py` 스크립트에 구현된 무작위 힙(Randomized Heap) 또는 무작위 멜딩 가능 힙(Randomized Meldable Heap)에 대해 설명합니다.

## 1. 무작위 힙(Randomized Heap)이란?

무작위 힙은 **최소 힙(Min-Heap)** 속성을 만족하는 이진 트리 기반의 자료 구조입니다. 이 힙의 가장 큰 특징은 **병합(merge)** 연산을 매우 간단하고 효율적으로 수행한다는 점입니다.

**핵심 아이디어**:
-   두 힙을 병합할 때, 두 루트 중 더 작은 값을 가진 노드를 새로운 루트로 삼습니다.
-   그 후, 새로운 루트의 두 자식 중 하나를 **무작위로 선택**하여 다른 힙의 루트와 재귀적으로 병합합니다.

이 무작위성 덕분에 트리가 한쪽으로 치우치는 것을 방지하고, 평균적으로 O(log N)의 연산 시간을 보장합니다. 모든 연산(삽입, 삭제, 병합)이 `merge` 연산을 기반으로 이루어집니다.

## 2. 클래스 구조

### `RandomizedHeapNode` 클래스
-   **역할**: 힙을 구성하는 각 노드를 표현합니다.
-   **속성**:
    -   `_value`: 노드가 저장하는 값.
    -   `left`, `right`: 왼쪽, 오른쪽 자식 노드에 대한 참조.
-   **핵심 메서드**:
    -   `merge(root1, root2)`: 두 개의 노드(를 루트로 하는 힙)를 병합하는 정적 메서드입니다. 이 함수가 무작위 힙의 모든 연산의 핵심입니다.

### `RandomizedHeap` 클래스
-   **역할**: 무작위 힙 전체를 관리하고 사용자에게 인터페이스를 제공합니다.
-   **속성**:
    -   `_root`: 힙의 루트 노드를 가리킵니다.

## 3. 주요 메서드 설명

### `__init__(self, data: Iterable[T] | None = ())`
-   **역할**: 힙을 초기화합니다. 선택적으로 초기 데이터를 받아 힙을 구성할 수 있습니다.
-   **동작**: `data`의 각 항목에 대해 `insert` 메서드를 호출합니다.

### `insert(self, value: T)`
-   **역할**: 힙에 새로운 값을 삽입합니다.
-   **시간 복잡도**: O(log N)
-   **동작**: 현재 힙의 루트(`self._root`)와 삽입할 값을 가진 새로운 단일 노드 힙을 `RandomizedHeapNode.merge`를 통해 병합합니다.

### `pop(self) -> T | None`
-   **역할**: 힙에서 가장 작은 값(루트)을 제거하고 반환합니다.
-   **시간 복잡도**: O(log N)
-   **동작**:
    1.  현재 루트의 값을 저장합니다.
    2.  루트의 왼쪽 자식과 오른쪽 자식을 `RandomizedHeapNode.merge`를 통해 병합하여 새로운 루트로 만듭니다.
    3.  저장해 둔 원래 루트의 값을 반환합니다.

### `top(self) -> T`
-   **역할**: 힙에서 가장 작은 값을 삭제하지 않고 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**: `self._root.value`를 즉시 반환합니다.

### `clear(self)`
-   **역할**: 힙의 모든 요소를 제거합니다.
-   **동작**: `self._root`를 `None`으로 설정합니다.

### `to_sorted_list(self) -> list[Any]`
-   **역할**: 힙의 모든 요소를 오름차순으로 정렬된 리스트로 반환합니다. 이 과정에서 힙은 비워집니다.
-   **동작**: 힙이 빌 때까지 `pop`을 반복하여 결과를 리스트에 추가합니다.

### `__bool__(self)`
-   **역할**: 힙이 비어있는지 여부를 확인합니다. `if heap:` 과 같은 구문에서 사용됩니다.

## 4. 사용 예제

`doctest`에 포함된 예제는 무작위 힙의 다양한 활용법을 보여줍니다.

```python
# 리스트로부터 힙 생성
rh = RandomizedHeap([2, 3, 1, 5, 1, 7])

# 정렬된 리스트로 변환 (힙은 비워짐)
print(rh.to_sorted_list())
# 출력: [1, 1, 2, 3, 5, 7]

# 빈 힙 생성 및 원소 삽입
rh = RandomizedHeap()
rh.insert(1)
rh.insert(-1)
rh.insert(0)

# 최솟값 확인
print(rh.top())
# 출력: -1

# 최솟값 추출
print(rh.pop())
# 출력: -1

# 다음 최솟값 확인
print(rh.top())
# 출력: 0

# 힙이 비어있는지 확인
print(bool(rh))
# 출력: True

rh.clear()
print(bool(rh))
# 출력: False
```

## 5. 테스트

스크립트에는 `doctest`가 포함되어 있어 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/heap/randomized_heap.py
```

테스트가 성공하면 아무런 출력도 나타나지 않습니다.