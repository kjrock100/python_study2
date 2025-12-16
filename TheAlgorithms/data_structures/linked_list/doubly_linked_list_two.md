# `doubly_linked_list_two.py` 코드 설명

이 문서는 `doubly_linked_list_two.py` 스크립트에 구현된 이중 연결 리스트(Doubly Linked List) 자료 구조에 대해 설명합니다.

## 1. 이중 연결 리스트(Doubly Linked List)란?

이중 연결 리스트는 각 노드가 데이터와 함께 **이전 노드(previous)**와 **다음 노드(next)**에 대한 참조를 모두 가지고 있는 연결 리스트입니다.

**주요 특징:**
-   **양방향 탐색**: 단일 연결 리스트와 달리, 앞뒤 양방향으로 리스트를 탐색할 수 있습니다.
-   **효율적인 삭제**: 특정 노드를 삭제할 때, 이전 노드를 찾기 위해 리스트를 처음부터 탐색할 필요가 없어 O(1) 시간에 삭제가 가능합니다 (노드 참조가 주어졌을 경우).
-   **양 끝 접근**: 이 구현은 `head`와 `tail` 포인터를 모두 유지하여 리스트의 양 끝에 O(1) 시간 복잡도로 접근하고 요소를 추가할 수 있습니다.

## 2. 클래스 구조

### `Node` 클래스
-   **역할**: 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `previous`: 이전 노드를 가리키는 참조.
    -   `next`: 다음 노드를 가리키는 참조.

### `LinkedListIterator` 클래스
-   **역할**: `LinkedList`가 `for` 루프와 같은 반복 구문에서 사용될 수 있도록 이터레이터 프로토콜을 구현합니다.
-   **동작**: `head`부터 시작하여 `next` 포인터를 따라 이동하며 각 노드의 데이터를 반환합니다.

### `LinkedList` 클래스
-   **역할**: 이중 연결 리스트 전체를 관리하고, 삽입, 삭제, 순회 등의 연산을 제공하는 메인 클래스입니다.

## 3. 주요 메서드 설명

### 3.1. 기본 및 조회 메서드

-   `__init__(self)`: 빈 리스트를 생성하며 `head`와 `tail`을 `None`으로 초기화합니다.
-   `__str__(self)`: 리스트의 모든 데이터를 공백으로 구분된 문자열로 반환합니다.
-   `__contains__(self, value)`: 리스트에 특정 `value`가 포함되어 있는지 확인합니다. (시간 복잡도: O(N))
-   `__iter__(self)`: `LinkedListIterator` 객체를 반환하여 리스트를 순회할 수 있게 합니다.
-   `get_head_data()`, `get_tail_data()`: 리스트의 첫 번째 또는 마지막 데이터를 반환합니다. (O(1))
-   `is_empty(self)`: 리스트가 비어있는지 확인합니다. (O(1))
-   `get_node(self, item)`: 특정 `item` 값을 가진 첫 번째 노드를 찾아 반환합니다. (O(N))

### 3.2. 삽입 메서드

-   `insert(self, value)`: 리스트의 맨 끝에 새로운 노드를 추가합니다. 내부적으로 `set_tail`을 호출합니다. (O(1))
-   `set_head(self, node)`: 주어진 `node`를 리스트의 맨 앞에 삽입합니다. (O(1))
-   `set_tail(self, node)`: 주어진 `node`를 리스트의 맨 뒤에 삽입합니다. (O(1))
-   `insert_before_node(self, node, node_to_insert)`: 특정 `node` 바로 앞에 `node_to_insert`를 삽입합니다. (O(1))
-   `insert_after_node(self, node, node_to_insert)`: 특정 `node` 바로 뒤에 `node_to_insert`를 삽입합니다. (O(1))
-   `insert_at_position(self, position, value)`: 1-기반 `position`에 새로운 `value`를 삽입합니다. 해당 위치를 찾기 위해 O(N)의 시간이 소요됩니다.

### 3.3. 삭제 메서드

-   `delete_value(self, value)`: 특정 `value`를 가진 첫 번째 노드를 삭제합니다.
    -   **동작**: `get_node`로 노드를 찾고(O(N)), `remove_node_pointers`로 연결을 끊습니다(O(1)).
-   `remove_node_pointers(node)`: (정적 메서드) 주어진 `node`의 이전 노드와 다음 노드를 직접 연결하여 `node`를 리스트에서 완전히 분리합니다.

## 4. 사용 예제

스크립트의 `create_linked_list()` 함수 내 `doctest`는 이 클래스의 다양한 기능을 검증하는 예제를 보여줍니다.

```python
new_linked_list = LinkedList()

# 리스트가 비었는지 확인
assert new_linked_list.is_empty() is True

# 원소 삽입 (꼬리에 추가됨)
new_linked_list.insert(10)
new_linked_list.insert(20)
print(new_linked_list)
# 출력: 10 20

# 머리에 삽입
new_linked_list.set_head(Node(1000))
print(new_linked_list)
# 출력: 1000 10 20

# 꼬리에 삽입
new_linked_list.set_tail(Node(2000))
print(new_linked_list)
# 출력: 1000 10 20 2000

# 특정 위치에 삽입 (1-based index)
new_linked_list.insert_at_position(position=3, value=15)
print(new_linked_list)
# 출력: 1000 10 15 20 2000

# 순회
for value in new_linked_list:
    print(value, end=" ")
# 출력: 1000 10 15 20 2000

# 값 포함 여부 확인
assert (15 in new_linked_list) is True

# 값으로 삭제
new_linked_list.delete_value(value=15)
assert (15 in new_linked_list) is False
print(new_linked_list)
# 출력: 1000 10 20 2000

# 머리/꼬리 삭제
new_linked_list.delete_value(1000)
new_linked_list.delete_value(2000)
print(new_linked_list)
# 출력: 10 20
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/doubly_linked_list_two.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.