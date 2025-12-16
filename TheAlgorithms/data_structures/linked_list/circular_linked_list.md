# `circular_linked_list.py` 코드 설명

이 문서는 `circular_linked_list.py` 스크립트에 구현된 원형 연결 리스트(Circular Linked List) 자료 구조에 대해 설명합니다.

## 1. 원형 연결 리스트(Circular Linked List)란?

원형 연결 리스트는 일반적인 단일 연결 리스트와 유사하지만, 마지막 노드의 `next` 포인터가 `None`을 가리키는 대신 **리스트의 첫 번째 노드(head)를 가리키는** 특징을 가집니다.

**주요 특징:**
-   **순환 구조**: 리스트의 어느 노드에서 시작하더라도 모든 노드를 방문할 수 있습니다.
-   **시작점과 끝점**: `head`와 `tail` 포인터를 유지하여 리스트의 시작과 끝에 효율적으로 접근할 수 있습니다. `tail.next`는 항상 `head`를 가리킵니다.
-   **빈 리스트**: `head`와 `tail`이 모두 `None`일 때 리스트는 비어있습니다.

## 2. 클래스 구조

### `Node` 클래스

연결 리스트를 구성하는 각 요소를 표현하는 클래스입니다.

-   `__init__(self, data: Any)`: 노드를 초기화합니다.
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드를 가리키는 참조.

### `CircularLinkedList` 클래스

원형 연결 리스트 전체를 관리하고, 삽입, 삭제, 순회 등의 연산을 제공하는 메인 클래스입니다.

## 3. 주요 메서드 설명

### `__init__(self)`
-   **역할**: 빈 원형 연결 리스트를 초기화합니다.
-   **속성**:
    -   `head`: 리스트의 첫 번째 노드를 가리킵니다. (초기값: `None`)
    -   `tail`: 리스트의 마지막 노드를 가리킵니다. (초기값: `None`)

### `__iter__(self) -> Iterator[Any]`
-   **역할**: 리스트의 모든 데이터를 순회하는 이터레이터(iterator)를 반환합니다. `for item in circular_list:`와 같이 사용할 수 있습니다.
-   **동작**: `head`부터 시작하여 `next` 포인터를 따라 이동하며 데이터를 `yield`합니다. 다시 `head`에 도달하면 순회를 멈춥니다.

### `__len__(self) -> int`
-   **역할**: 리스트에 포함된 노드의 개수를 반환합니다. `len(circular_list)` 구문을 지원합니다.
-   **동작**: `__iter__`를 사용하여 모든 노드를 순회하고 그 개수를 셉니다.

### `__repr__(self)`
-   **역할**: 리스트의 내용을 문자열로 표현합니다. `print(circular_list)`와 같이 사용할 수 있습니다.
-   **동작**: `__iter__`를 사용하여 모든 노드의 데이터를 `->`로 연결된 문자열로 만듭니다.

### `insert_tail(self, data: Any) -> None`
-   **역할**: 리스트의 끝에 새로운 데이터를 삽입합니다.
-   **동작**: 내부적으로 `insert_nth(len(self), data)`를 호출합니다.

### `insert_head(self, data: Any) -> None`
-   **역할**: 리스트의 시작 부분에 새로운 데이터를 삽입합니다.
-   **동작**: 내부적으로 `insert_nth(0, data)`를 호출합니다.

### `insert_nth(self, index: int, data: Any) -> None`
-   **역할**: 특정 `index` 위치에 새로운 데이터를 삽입합니다.
-   **예외**: `index`가 유효 범위를 벗어나면 `IndexError`를 발생시킵니다.
-   **동작**:
    1.  새로운 `Node`를 생성합니다.
    2.  **빈 리스트**: `head`가 `None`이면, 새 노드가 `head`이자 `tail`이 되고, 자신을 가리키도록 합니다.
    3.  **헤드 삽입**: `index`가 0이면, 새 노드를 `head`로 만들고 `tail.next`와 기존 `head`가 새 노드를 가리키도록 합니다.
    4.  **중간/꼬리 삽입**: `index - 1` 위치의 노드를 찾은 후, 새 노드를 그 노드의 `next`로 연결합니다. `index`가 리스트의 끝이면 `tail`을 갱신합니다.

### `delete_front(self)`
-   **역할**: 리스트의 첫 번째 노드를 삭제하고 그 데이터를 반환합니다.
-   **동작**: 내부적으로 `delete_nth(0)`를 호출합니다.

### `delete_tail(self) -> Any`
-   **역할**: 리스트의 마지막 노드를 삭제하고 그 데이터를 반환합니다.
-   **동작**: 내부적으로 `delete_nth(len(self) - 1)`를 호출합니다.

### `delete_nth(self, index: int = 0) -> Any`
-   **역할**: 특정 `index` 위치의 노드를 삭제하고 그 데이터를 반환합니다.
-   **예외**: `index`가 유효 범위를 벗어나면 `IndexError`를 발생시킵니다.
-   **동작**:
    1.  **단일 노드**: 리스트에 노드가 하나뿐이면 `head`와 `tail`을 `None`으로 설정합니다.
    2.  **헤드 삭제**: `index`가 0이면, `tail.next`가 `head.next`를 가리키게 하고 `head`를 다음 노드로 이동시킵니다.
    3.  **중간/꼬리 삭제**: `index - 1` 위치의 노드를 찾은 후, 해당 노드의 `next`를 삭제할 노드의 `next`로 연결합니다. `index`가 리스트의 끝이면 `tail`을 갱신합니다.

### `is_empty(self) -> bool`
-   **역할**: 리스트가 비어있는지 여부를 반환합니다.
-   **동작**: `len(self)`가 0인지 확인합니다.

## 4. 사용 예제

스크립트 하단에 포함된 `test_circular_linked_list()` 함수는 이 클래스의 다양한 기능을 검증하는 예제를 보여줍니다.

```python
def test_circular_linked_list() -> None:
    circular_linked_list = CircularLinkedList()
    assert len(circular_linked_list) == 0
    assert circular_linked_list.is_empty() is True
    assert str(circular_linked_list) == ""

    # 빈 리스트에서 삭제 시도 (IndexError 발생 확인)
    try:
        circular_linked_list.delete_front()
        assert False
    except IndexError:
        assert True

    # 여러 원소 삽입
    for i in range(5):
        circular_linked_list.insert_nth(i, i + 1)
    assert str(circular_linked_list) == "1->2->3->4->5"

    # 꼬리 삽입
    circular_linked_list.insert_tail(6)
    assert str(circular_linked_list) == "1->2->3->4->5->6"

    # 머리 삽입
    circular_linked_list.insert_head(0)
    assert str(circular_linked_list) == "0->1->2->3->4->5->6"

    # 머리 삭제
    assert circular_linked_list.delete_front() == 0
    # 꼬리 삭제
    assert circular_linked_list.delete_tail() == 6
    assert str(circular_linked_list) == "1->2->3->4->5"

    # 중간 노드 삭제
    assert circular_linked_list.delete_nth(2) == 3
    assert str(circular_linked_list) == "1->2->4->5"

    # 중간 노드 삽입
    circular_linked_list.insert_nth(2, 3)
    assert str(circular_linked_list) == "1->2->3->4->5"

    assert circular_linked_list.is_empty() is False
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/circular_linked_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.