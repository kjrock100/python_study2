# `deque_doubly.py` 코드 설명

이 문서는 `deque_doubly.py` 스크립트에 구현된 이중 연결 리스트(Doubly Linked List)를 이용한 덱(Deque) 자료 구조에 대해 설명합니다.

## 1. Deque (덱) 이란?

덱(Deque, Double-Ended Queue)은 양쪽 끝에서 요소의 삽입과 삭제가 모두 가능한 선형 자료 구조입니다. 큐(Queue)와 스택(Stack)의 기능을 모두 수행할 수 있습니다.

**주요 특징:**
-   **양방향 접근**: 리스트의 앞과 뒤 모두에서 요소를 추가하거나 제거할 수 있습니다.
-   **효율적인 연산**: 이 구현에서는 모든 삽입, 삭제, 접근 연산이 O(1)의 시간 복잡도를 가집니다.

## 2. 이중 연결 리스트(Doubly Linked List) 기반 구현

이 코드는 덱을 이중 연결 리스트를 사용하여 구현합니다. 각 노드는 데이터와 함께 이전 노드(`_prev`)와 다음 노드(`_next`)에 대한 참조를 가집니다.

**헤더(Header)와 트레일러(Trailer) 노드**:
실제 데이터를 저장하지 않는 `_header`와 `_trailer`라는 두 개의 특수 노드를 사용하여 리스트의 시작과 끝을 표시합니다. 이 더미 노드들은 경계 조건 처리(예: 빈 리스트, 첫 번째/마지막 요소 삽입/삭제)를 크게 간소화하여 코드의 일관성을 높여줍니다.

```
  _header <-> Node1 <-> Node2 <-> ... <-> NodeN <-> _trailer
```

## 3. 클래스 및 메서드 설명

### 3.1. `_DoublyLinkedBase` 클래스

이 클래스는 이중 연결 리스트의 기본 구조와 공통 연산을 정의하는 **비공개(private) 추상 기본 클래스**입니다. `LinkedDeque`는 이 클래스를 상속받아 덱의 기능을 구현합니다.

#### `_Node` 내부 클래스
-   **역할**: 이중 연결 리스트의 각 노드를 표현합니다.
-   **속성**:
    -   `_prev`: 이전 노드에 대한 참조.
    -   `_data`: 노드가 저장하는 실제 데이터.
    -   `_next`: 다음 노드에 대한 참조.
-   `has_next_and_prev()`: 디버깅용 헬퍼 메서드.

#### `__init__(self)`
-   **역할**: 이중 연결 리스트의 헤더와 트레일러 노드를 초기화하고 서로 연결합니다.

#### `__len__(self)`
-   **역할**: 리스트에 포함된 실제 데이터 노드의 개수를 반환합니다.

#### `is_empty(self)`
-   **역할**: 리스트가 비어있는지 여부를 반환합니다.

#### `_insert(self, predecessor, e, successor)`
-   **역할**: `predecessor`와 `successor` 노드 사이에 새로운 노드 `e`를 삽입하는 헬퍼 메서드입니다.
-   **시간 복잡도**: O(1)

#### `_delete(self, node)`
-   **역할**: 주어진 `node`를 리스트에서 삭제하는 헬퍼 메서드입니다.
-   **시간 복잡도**: O(1)

### 3.2. `LinkedDeque` 클래스

`_DoublyLinkedBase`를 상속받아 덱의 구체적인 연산들을 구현합니다.

#### `first(self)`
-   **역할**: 덱의 첫 번째 요소를 반환합니다.
-   **예외**: 덱이 비어있으면 `Exception`을 발생시킵니다.
-   **시간 복잡도**: O(1)

#### `last(self)`
-   **역할**: 덱의 마지막 요소를 반환합니다.
-   **예외**: 덱이 비어있으면 `Exception`을 발생시킵니다.
-   **시간 복잡도**: O(1)

#### `add_first(self, element)`
-   **역할**: 덱의 맨 앞에 `element`를 삽입합니다.
-   **동작**: `_header`와 `_header._next` 사이에 새 노드를 삽입합니다.
-   **시간 복잡도**: O(1)

#### `add_last(self, element)`
-   **역할**: 덱의 맨 뒤에 `element`를 삽입합니다.
-   **동작**: `_trailer._prev`와 `_trailer` 사이에 새 노드를 삽입합니다.
-   **시간 복잡도**: O(1)

#### `remove_first(self)`
-   **역할**: 덱의 맨 앞에 있는 요소를 제거하고 반환합니다.
-   **예외**: 덱이 비어있으면 `IndexError`를 발생시킵니다.
-   **동작**: `_header._next` 노드를 삭제합니다.
-   **시간 복잡도**: O(1)

#### `remove_last(self)`
-   **역할**: 덱의 맨 뒤에 있는 요소를 제거하고 반환합니다.
-   **예외**: 덱이 비어있으면 `IndexError`를 발생시킵니다.
-   **동작**: `_trailer._prev` 노드를 삭제합니다.
-   **시간 복잡도**: O(1)

## 4. 사용 예제

스크립트의 각 메서드에 포함된 `doctest`는 해당 메서드의 사용법을 보여줍니다.

```python
d = LinkedDeque()

# 덱이 비어있는지 확인
print(d.is_empty())
# 출력: True

# 맨 앞에 'A' 삽입
d.add_first('A')
print(d.first())
# 출력: 'A'

# 맨 뒤에 'B' 삽입
d.add_last('B')
print(d.last())
# 출력: 'B'

# 현재 덱: A <-> B
# 맨 앞에 'C' 삽입
d.add_first('C')
# 현재 덱: C <-> A <-> B
print(d.first())
# 출력: 'C'

# 맨 앞에서 제거
print(d.remove_first())
# 출력: 'C'
# 현재 덱: A <-> B

# 맨 뒤에서 제거
print(d.remove_last())
# 출력: 'B'
# 현재 덱: A

# 덱의 길이 확인
print(len(d))
# 출력: 1
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/deque_doubly.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.