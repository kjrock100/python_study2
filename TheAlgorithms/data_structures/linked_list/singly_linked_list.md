# `singly_linked_list.py` 코드 설명

이 문서는 `singly_linked_list.py` 스크립트에 구현된 단일 연결 리스트(Singly Linked List) 자료 구조에 대해 설명합니다.

## 1. 단일 연결 리스트(Singly Linked List)란?

단일 연결 리스트는 데이터를 담고 있는 노드(Node)들이 한 줄로 연결된 선형 자료 구조입니다. 각 노드는 데이터와 함께 다음 노드를 가리키는 참조(포인터)를 가지고 있습니다.

**주요 특징:**
-   **동적 크기**: 배열과 달리 크기가 고정되어 있지 않아 동적으로 요소를 추가하거나 제거할 수 있습니다.
-   **순차적 접근**: 특정 요소에 접근하려면 리스트의 처음(head)부터 순서대로 탐색해야 합니다.
-   **단방향**: 각 노드는 다음 노드만 알 수 있고, 이전 노드에 대한 정보는 없습니다.

## 2. 클래스 구조

### `Node` 클래스
-   **역할**: 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드를 가리키는 참조.

### `LinkedList` 클래스
-   **역할**: 단일 연결 리스트 전체를 관리하고, 삽입, 삭제, 순회 등의 연산을 제공하는 메인 클래스입니다.

## 3. 주요 메서드 설명

### 3.1. Dunder (Special) 메서드

-   `__init__(self)`: 빈 리스트를 생성하며 `head`를 `None`으로 초기화합니다.
-   `__iter__(self)`: 리스트의 모든 데이터를 순회하는 이터레이터(iterator)를 반환합니다. `for item in linked_list:`와 같이 사용할 수 있습니다.
-   `__len__(self)`: 리스트에 포함된 노드의 개수를 반환합니다.
    -   **시간 복잡도**: O(N), 리스트 전체를 순회하여 길이를 계산합니다.
-   `__repr__(self)`: 리스트의 내용을 `->`로 연결된 문자열로 표현합니다. `print(linked_list)`와 같이 사용할 수 있습니다.
-   `__getitem__(self, index)`: 리스트의 `index` 위치에 있는 노드의 **데이터**를 반환합니다. `linked_list[i]` 구문을 지원합니다.
-   `__setitem__(self, index, data)`: 리스트의 `index` 위치에 있는 노드의 데이터를 새로운 `data`로 변경합니다. `linked_list[i] = value` 구문을 지원합니다.

### 3.2. 삽입 메서드

-   `insert_tail(self, data)`: 리스트의 맨 끝에 새로운 데이터를 삽입합니다.
    -   **시간 복잡도**: O(N), 꼬리를 찾기 위해 전체 리스트를 순회합니다.
-   `insert_head(self, data)`: 리스트의 맨 앞에 새로운 데이터를 삽입합니다.
    -   **시간 복잡도**: O(1)
-   `insert_nth(self, index, data)`: 0-기반 `index` 위치에 새로운 데이터를 삽입합니다.
    -   **시간 복잡도**: O(N), 해당 위치를 찾기 위해 순회해야 합니다.

### 3.3. 삭제 메서드

-   `delete_head(self)`: 리스트의 첫 번째 노드를 삭제하고 그 데이터를 반환합니다.
    -   **시간 복잡도**: O(1)
-   `delete_tail(self)`: 리스트의 마지막 노드를 삭제하고 그 데이터를 반환합니다.
    -   **시간 복잡도**: O(N), 꼬리의 이전 노드를 찾기 위해 전체 리스트를 순회합니다.
-   `delete_nth(self, index)`: 0-기반 `index` 위치의 노드를 삭제하고 그 데이터를 반환합니다.
    -   **시간 복잡도**: O(N), 해당 위치를 찾기 위해 순회해야 합니다.

### 3.4. 유틸리티 메서드

-   `print_list(self)`: 리스트의 모든 노드 데이터를 출력합니다. (`__repr__`과 기능적으로 동일)
-   `is_empty(self)`: 리스트가 비어있는지 확인합니다.
    -   **시간 복잡도**: O(1)
-   `reverse(self)`: 연결 리스트의 순서를 뒤집습니다. (in-place 연산)
    -   **시간 복잡도**: O(N)
    -   **동작**: 세 개의 포인터(`prev`, `current`, `next_node`)를 사용하여 리스트를 순회하면서 각 노드의 `next` 방향을 반대로 바꿉니다.

## 4. 사용 예제

`test_singly_linked_list()` 함수 내 `doctest`는 이 클래스의 다양한 기능을 검증하는 예제를 보여줍니다.

```python
linked_list = LinkedList()

# 리스트가 비었는지 확인
assert linked_list.is_empty() is True

# 머리에 삽입
linked_list.insert_head("b")
linked_list.insert_head("a")

# 꼬리에 삽입
linked_list.insert_tail("c")

print(linked_list)
# 출력: a->b->c

# 순회
for item in linked_list:
    print(item, end=" ")
# 출력: a b c

# 길이 확인
print(len(linked_list))
# 출력: 3

# 인덱싱으로 접근 및 수정
print(linked_list[1])  # 출력: b
linked_list[1] = "z"
print(linked_list)     # 출력: a->z->c

# 리스트 뒤집기
linked_list.reverse()
print(linked_list)
# 출력: c->z->a

# 삭제
deleted_data = linked_list.delete_head()
print(f"Deleted: {deleted_data}, List: {linked_list}")
# 출력: Deleted: c, List: z->a
```

## 5. 개선 제안

-   **O(1) `__len__`**: `__len__` 메서드는 현재 O(N)의 시간 복잡도를 가집니다. 클래스에 `size` 속성을 추가하고 삽입/삭제 시마다 값을 증감시키면 O(1)으로 개선할 수 있습니다.
-   **O(1) `insert_tail`**: `tail` 포인터를 추가로 유지하면, 꼬리 삽입/삭제 연산을 O(1) 시간 복잡도로 개선할 수 있습니다. (이 경우 이중 연결 리스트가 더 적합할 수 있습니다.)

## 6. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/singly_linked_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.