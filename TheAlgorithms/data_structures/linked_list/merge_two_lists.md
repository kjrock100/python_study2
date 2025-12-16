# `merge_two_lists.py` 코드 설명

이 문서는 `merge_two_lists.py` 스크립트에 구현된, 두 개의 정렬된 연결 리스트를 병합하는 기능에 대해 설명합니다.

## 1. 개요

이 스크립트는 항상 정렬된 상태를 유지하는 단일 연결 리스트(`SortedLinkedList`) 클래스를 정의하고, 이 클래스의 두 인스턴스를 병합하여 하나의 새로운 정렬된 연결 리스트를 만드는 함수(`merge_lists`)를 제공합니다.

## 2. 클래스 및 함수 설명

### `Node` 데이터클래스

-   **역할**: 연결 리스트를 구성하는 각 요소를 표현하는 간단한 데이터 클래스입니다.
-   **속성**:
    -   `data`: 노드가 저장하는 정수 값.
    -   `next`: 다음 노드를 가리키는 참조.

### `SortedLinkedList` 클래스

-   **역할**: 항상 오름차순으로 정렬된 상태를 유지하는 단일 연결 리스트를 나타냅니다.

#### `__init__(self, ints: Iterable[int])`
-   **역할**: 정수들의 시퀀스(`ints`)를 받아 정렬된 연결 리스트를 생성합니다.
-   **동작**:
    1.  입력받은 `ints`를 `sorted()` 함수를 사용하여 오름차순으로 정렬합니다.
    2.  정렬된 리스트를 **역순으로** 순회하면서 각 요소를 새로운 노드로 만들어 리스트의 맨 앞에 계속 추가합니다. 이 과정을 통해 최종적으로 오름차순의 연결 리스트가 완성됩니다.

#### `__iter__(self) -> Iterator[int]`
-   **역할**: 리스트의 모든 데이터를 순회하는 이터레이터(iterator)를 반환합니다. `for item in sorted_list:`와 같이 사용할 수 있습니다.

#### `__len__(self) -> int`
-   **역할**: 리스트에 포함된 노드의 개수를 반환합니다.
-   **시간 복잡도**: O(N), 리스트의 모든 노드를 순회하여 길이를 계산합니다.

#### `__str__(self) -> str`
-   **역할**: 리스트의 내용을 `->`로 연결된 문자열로 표현합니다.

### `merge_lists(sll_one: SortedLinkedList, sll_two: SortedLinkedList) -> SortedLinkedList`

-   **역할**: 두 개의 `SortedLinkedList` 객체를 병합하여 새로운 `SortedLinkedList`를 반환합니다.
-   **동작 방식의 특징**:
    -   이 함수는 전통적인 연결 리스트 병합 방식(두 리스트의 노드를 하나씩 비교하며 포인터를 재연결하는 방식)을 사용하지 않습니다.
    -   대신, 더 간단한 접근 방식을 사용합니다:
        1.  `list(sll_one)`과 `list(sll_two)`를 통해 두 연결 리스트를 파이썬의 일반 리스트로 변환합니다.
        2.  두 리스트를 `+` 연산자로 합칩니다.
        3.  합쳐진 리스트를 `SortedLinkedList`의 생성자에 전달하여 완전히 새로운 정렬된 연결 리스트를 만듭니다.
    -   이 방식은 구현이 매우 간단하지만, 중간에 두 개의 전체 리스트를 메모리에 생성하므로, 매우 큰 리스트를 병합할 때는 메모리 효율성이 떨어질 수 있습니다.

## 3. 사용 예제

스크립트의 `doctest`와 `if __name__ == "__main__"` 블록은 이 코드의 사용법을 보여줍니다.

```python
# 테스트 데이터
test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 0, 8, 10, 3, -2)

# 두 개의 정렬된 연결 리스트 생성
sll_odd = SortedLinkedList(test_data_odd)
sll_even = SortedLinkedList(test_data_even)

print(f"List 1: {sll_odd}")
# 출력: List 1: -11 -> -1 -> 0 -> 1 -> 3 -> 5 -> 7 -> 9

print(f"List 2: {sll_even}")
# 출력: List 2: -2 -> 0 -> 2 -> 3 -> 4 -> 6 -> 8 -> 10

# 두 리스트 병합
merged = merge_lists(sll_odd, sll_even)

print(f"Merged List: {merged}")
# 출력: Merged List: -11 -> -2 -> -1 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

# 병합된 리스트의 길이 확인
print(f"Length of merged list: {len(merged)}")
# 출력: Length of merged list: 16
```

## 4. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/merge_two_lists.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.