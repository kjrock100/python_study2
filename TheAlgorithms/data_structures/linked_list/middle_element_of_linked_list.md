# `middle_element_of_linked_list.py` 코드 설명

이 문서는 `middle_element_of_linked_list.py` 스크립트에 구현된, 단일 연결 리스트(Singly Linked List)의 중간 요소를 찾는 알고리즘에 대해 설명합니다.

## 1. 문제 설명: 연결 리스트의 중간 요소 찾기

이 문제의 목표는 주어진 단일 연결 리스트에서 중간에 위치한 요소를 찾는 것입니다.

-   리스트의 요소 개수가 홀수이면, 정확히 가운데 있는 요소를 찾습니다. (예: `1->2->3->4->5` 에서 `3`)
-   리스트의 요소 개수가 짝수이면, 두 개의 중간 요소 중 두 번째 요소를 찾습니다. (예: `1->2->3->4` 에서 `3`)

## 2. 핵심 알고리즘: 토끼와 거북이 (Fast & Slow Pointer)

이 코드는 중간 요소를 찾기 위해 **'토끼와 거북이'** 또는 **'빠른 포인터와 느린 포인터'** 라고 불리는 효율적인 알고리즘을 사용합니다.

-   **시간 복잡도**: O(N) - 리스트를 한 번만 순회합니다.
-   **공간 복잡도**: O(1) - 추가적인 데이터 구조를 사용하지 않습니다.

**동작 원리:**
1.  두 개의 포인터, `slow_pointer`와 `fast_pointer`를 모두 리스트의 시작(`head`)에서 출발시킵니다.
2.  `fast_pointer`는 한 번에 두 칸씩 이동하고, `slow_pointer`는 한 번에 한 칸씩 이동합니다.
3.  `fast_pointer`가 리스트의 끝에 도달하면(즉, `fast_pointer` 또는 `fast_pointer.next`가 `None`이 되면), `slow_pointer`는 정확히 리스트의 중간 지점에 위치하게 됩니다.

## 3. 클래스 및 메서드 설명

### `Node` 클래스
-   **역할**: 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드를 가리키는 참조.

### `LinkedList` 클래스

#### `__init__(self)`
-   **역할**: 빈 연결 리스트를 생성하며, `head`를 `None`으로 초기화합니다.

#### `push(self, new_data: int) -> int`
-   **역할**: 리스트의 맨 앞에 새로운 데이터를 삽입합니다. (스택의 `push`와 유사)
-   **동작**:
    1.  `new_data`로 새로운 `Node`를 생성합니다.
    2.  새 노드의 `next`가 현재 `head`를 가리키게 합니다.
    3.  `head`를 새 노드로 갱신합니다.

#### `middle_element(self) -> int | None`
-   **역할**: '토끼와 거북이' 알고리즘을 사용하여 리스트의 중간 요소를 찾아 그 데이터를 반환합니다.
-   **동작**:
    1.  `slow_pointer`와 `fast_pointer`를 `self.head`로 초기화합니다.
    2.  **빈 리스트 처리**: 리스트가 비어있으면 메시지를 출력하고 `None`을 반환합니다.
    3.  `while` 루프를 통해 `fast_pointer`가 리스트 끝에 도달할 때까지 두 포인터를 이동시킵니다.
    4.  루프가 종료되면 `slow_pointer`가 가리키는 노드의 데이터를 반환합니다.

## 4. 사용 예제

`doctest`에 포함된 예제는 이 클래스의 사용법을 보여줍니다.

```python
link = LinkedList()

# 빈 리스트의 경우
print(link.middle_element())
# 출력: No element found.

# 여러 데이터 삽입
link.push(5)
link.push(6)
link.push(8)
link.push(8)
link.push(10)
link.push(12)
link.push(17)
link.push(7)
link.push(3)
link.push(20)
link.push(-20)

# 현재 리스트: -20 -> 20 -> 3 -> 7 -> 17 -> 12 -> 10 -> 8 -> 8 -> 6 -> 5 (총 11개)

# 중간 요소 찾기
print(link.middle_element())
# 출력: 12
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/middle_element_of_linked_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.