# `doubly_linked_list.py` 코드 설명

이 문서는 `doubly_linked_list.py` 스크립트에 구현된 이중 연결 리스트(Doubly Linked List) 자료 구조에 대해 설명합니다.

## 1. 이중 연결 리스트(Doubly Linked List)란?

이중 연결 리스트는 각 노드가 데이터와 함께 **이전 노드(previous)**와 **다음 노드(next)**에 대한 참조를 모두 가지고 있는 연결 리스트입니다.

**주요 특징:**
-   **양방향 탐색**: 단일 연결 리스트와 달리, 앞뒤 양방향으로 리스트를 탐색할 수 있습니다.
-   **효율적인 삭제**: 특정 노드를 삭제할 때, 이전 노드를 찾기 위해 리스트를 처음부터 탐색할 필요가 없어 O(1) 시간에 삭제가 가능합니다 (노드 참조가 주어졌을 경우).
-   **양 끝 접근**: 이 구현은 `head`와 `tail` 포인터를 모두 유지하여 리스트의 양 끝에 O(1) 시간 복잡도로 접근하고 요소를 추가/삭제할 수 있습니다.

## 2. 클래스 구조

### `Node` 클래스
-   **역할**: 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `previous`: 이전 노드를 가리키는 참조.
    -   `next`: 다음 노드를 가리키는 참조.

### `DoublyLinkedList` 클래스
-   **역할**: 이중 연결 리스트 전체를 관리하고, 삽입, 삭제, 순회 등의 연산을 제공하는 메인 클래스입니다.

## 3. 주요 메서드 설명

### 3.1. 기본 및 조회 메서드

-   `__init__(self)`: 빈 리스트를 생성하며 `head`와 `tail`을 `None`으로 초기화합니다.
-   `__iter__(self)`: 리스트를 순회할 수 있는 이터레이터(iterator)를 반환합니다.
-   `__str__(self)`: 리스트의 모든 데이터를 `->`로 연결된 문자열로 반환합니다.
-   `__len__(self)`: 리스트에 포함된 노드의 개수를 반환합니다. (시간 복잡도: O(N))
-   `is_empty(self)`: 리스트가 비어있는지 확인합니다. (O(N))

### 3.2. 삽입 메서드

-   `insert_at_head(self, data)`: 리스트의 맨 앞에 새로운 데이터를 삽입합니다. (O(1))
-   `insert_at_tail(self, data)`: 리스트의 맨 뒤에 새로운 데이터를 삽입합니다. (O(1))
-   `insert_at_nth(self, index, data)`: 0-기반 `index` 위치에 새로운 데이터를 삽입합니다.
    -   **동작**: `index`가 0이면 머리에, `index`가 `len(self)`이면 꼬리에 삽입합니다. 그 외의 경우, 해당 위치까지 순회(O(N))한 후 노드를 삽입합니다.

### 3.3. 삭제 메서드

-   `delete_head(self)`: 리스트의 첫 번째 노드를 삭제하고 그 데이터를 반환합니다. (O(1))
-   `delete_tail(self)`: 리스트의 마지막 노드를 삭제하고 그 데이터를 반환합니다. (O(1))
-   `delete_at_nth(self, index)`: 0-기반 `index` 위치의 노드를 삭제하고 그 데이터를 반환합니다.
    -   **동작**: `index`가 0이면 머리를, `index`가 `len(self) - 1`이면 꼬리를 삭제합니다. 그 외의 경우, 해당 위치까지 순회(O(N))한 후 노드를 삭제합니다.
-   `delete(self, data)`: 특정 `data` 값을 가진 첫 번째 노드를 찾아 삭제합니다.
    -   **동작**: 값을 찾기 위해 리스트를 순회(O(N))한 후, 해당 노드를 삭제합니다.

## 4. 사용 예제

스크립트의 `test_doubly_linked_list()` 함수 내 `doctest`는 이 클래스의 다양한 기능을 검증하는 예제를 보여줍니다.

```python
linked_list = DoublyLinkedList()

# 리스트가 비었는지 확인
assert linked_list.is_empty() is True

# 머리에 삽입
linked_list.insert_at_head('b')
linked_list.insert_at_head('a')

# 꼬리에 삽입
linked_list.insert_at_tail('c')

print(linked_list)
# 출력: a->b->c

# 순회
print(tuple(linked_list))
# 출력: ('a', 'b', 'c')

# 길이 확인
print(len(linked_list))
# 출력: 3

# 특정 위치에 삽입 (0-based index)
linked_list.insert_at_nth(2, 'z')
print(linked_list)
# 출력: a->b->z->c

# 머리 삭제
deleted_data = linked_list.delete_head()
print(f"Deleted: {deleted_data}, List: {linked_list}")
# 출력: Deleted: a, List: b->z->c

# 꼬리 삭제
deleted_data = linked_list.delete_tail()
print(f"Deleted: {deleted_data}, List: {linked_list}")
# 출력: Deleted: c, List: b->z

# 값으로 삭제
deleted_data = linked_list.delete('z')
print(f"Deleted: {deleted_data}, List: {linked_list}")
# 출력: Deleted: z, List: b
```

## 5. 다른 구현과의 비교 (`doubly_linked_list_two.py`)

이 파일(`doubly_linked_list.py`)은 `doubly_linked_list_two.py`와 매우 유사한 기능을 제공하지만, 몇 가지 차이점이 있습니다.

-   **메서드 구조**: 이 구현은 `insert_at_nth`와 `delete_at_nth`를 핵심 로직으로 삼고, `insert_at_head/tail` 및 `delete_head/tail`이 이들을 호출하는 구조입니다. 반면, `doubly_linked_list_two.py`는 각 삽입/삭제 메서드가 독립적인 로직을 가지는 경향이 있습니다.
-   **이터레이터**: 이 구현은 `__iter__` 메서드 내에서 직접 `yield`를 사용하여 이터레이터를 구현하는 반면, `doubly_linked_list_two.py`는 별도의 `LinkedListIterator` 클래스를 사용합니다.

## 6. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/doubly_linked_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.