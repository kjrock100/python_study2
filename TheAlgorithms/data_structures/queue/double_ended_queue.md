# `double_ended_queue.py` 코드 설명

이 문서는 `double_ended_queue.py` 스크립트에 구현된, 이중 연결 리스트(Doubly Linked List)를 이용한 덱(Deque, Double-Ended Queue) 자료 구조에 대해 설명합니다.

## 1. Deque (덱) 이란?

덱(Deque)은 "데크"라고 읽으며, 양쪽 끝(front, back)에서 요소의 삽입과 삭제가 모두 가능한 선형 자료 구조입니다. 큐(Queue)와 스택(Stack)의 기능을 모두 수행할 수 있는 유연한 구조입니다.

**주요 특징:**
-   **양방향 연산**: 리스트의 앞과 뒤 모두에서 O(1) 시간 복잡도로 요소를 추가하거나 제거할 수 있습니다.
-   **구현**: 이 코드는 이중 연결 리스트를 사용하여 덱을 구현합니다. 각 노드는 데이터와 함께 이전 노드(`prev`)와 다음 노드(`next`)에 대한 참조를 가집니다.

## 2. 클래스 구조

### `Deque` 클래스

덱의 모든 기능과 상태를 관리하는 메인 클래스입니다.

#### `_Node` 내부 클래스
-   **역할**: 이중 연결 리스트의 각 노드를 표현합니다. `dataclass`로 정의되어 간결합니다.
-   **속성**:
    -   `val`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드에 대한 참조.
    -   `prev`: 이전 노드에 대한 참조.

#### `_Iterator` 내부 클래스
-   **역할**: `Deque`가 `for` 루프와 같은 반복 구문에서 사용될 수 있도록 이터레이터 프로토콜을 구현합니다.
-   **동작**: `_front`부터 시작하여 `next` 포인터를 따라 이동하며 각 노드의 데이터를 반환합니다.

## 3. 주요 메서드 설명

### 3.1. 초기화 및 기본 메서드

-   `__init__(self, iterable: Iterable[Any] | None = None)`: 덱을 초기화합니다. 선택적으로 초기 데이터를 받아 `append`를 통해 덱을 구성할 수 있습니다.
-   `__len__(self) -> int`: 덱에 포함된 요소의 개수를 반환합니다. (O(1))
-   `__eq__(self, other: object) -> bool`: 두 덱의 내용이 같은지 비교합니다. (O(N))
-   `__iter__(self) -> Deque._Iterator`: 순회를 위한 이터레이터 객체를 반환합니다.
-   `__repr__(self) -> str`: 덱의 내용을 리스트 형태로 출력합니다. (O(N))
-   `is_empty(self) -> bool`: 덱이 비어있는지 확인합니다. (O(1))

### 3.2. 삽입 메서드

#### `append(self, val: Any) -> None`
-   **역할**: 덱의 맨 뒤(오른쪽)에 `val`을 추가합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  새로운 노드를 생성합니다.
    2.  덱이 비어있으면, 새 노드가 `_front`이자 `_back`이 됩니다.
    3.  그렇지 않으면, 기존 `_back` 노드의 `next`를 새 노드로, 새 노드의 `prev`를 기존 `_back`으로 연결한 후, `_back`을 새 노드로 갱신합니다.

#### `appendleft(self, val: Any) -> None`
-   **역할**: 덱의 맨 앞(왼쪽)에 `val`을 추가합니다.
-   **시간 복잡도**: O(1)
-   **동작**: `append`와 유사하게, `_front` 포인터를 기준으로 노드를 연결하고 `_front`를 갱신합니다.

#### `extend(self, iter: Iterable[Any]) -> None`
-   **역할**: 주어진 이터러블(`iter`)의 모든 요소를 덱의 맨 뒤에 추가합니다.
-   **시간 복잡도**: O(k) (k는 `iter`의 길이)
-   **동작**: `iter`의 각 요소에 대해 `append`를 반복 호출합니다.

#### `extendleft(self, iter: Iterable[Any]) -> None`
-   **역할**: 주어진 이터러블(`iter`)의 모든 요소를 덱의 맨 앞에 추가합니다.
-   **시간 복잡도**: O(k) (k는 `iter`의 길이)
-   **동작**: `iter`의 각 요소에 대해 `appendleft`를 반복 호출합니다.

### 3.3. 삭제 메서드

#### `pop(self) -> Any`
-   **역할**: 덱의 맨 뒤(오른쪽) 요소를 제거하고 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  `_back` 노드를 저장합니다.
    2.  `_back`을 `_back.prev`로 이동시키고, 새로운 `_back`의 `next`를 `None`으로 설정하여 연결을 끊습니다.
    3.  저장해 둔 원래 `_back` 노드의 값을 반환합니다.

#### `popleft(self) -> Any`
-   **역할**: 덱의 맨 앞(왼쪽) 요소를 제거하고 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**: `pop`과 유사하게, `_front` 포인터를 기준으로 노드를 제거하고 `_front`를 갱신합니다.

## 4. 사용 예제

`doctest`에 포함된 예제는 이 클래스의 다양한 활용법을 보여줍니다. 이 구현은 파이썬 표준 라이브러리인 `collections.deque`와 동일한 인터페이스와 동작을 목표로 합니다.

```python
from collections import deque

# 우리 Deque와 collections.deque 비교

# 생성
our_deque_1 = Deque([1, 2, 3])
deque_collections_1 = deque([1, 2, 3])
assert list(our_deque_1) == list(deque_collections_1)

# append
our_deque_1.append(4)
deque_collections_1.append(4)
assert list(our_deque_1) == list(deque_collections_1)

# appendleft
our_deque_1.appendleft(0)
deque_collections_1.appendleft(0)
assert list(our_deque_1) == list(deque_collections_1)

# pop
our_popped = our_deque_1.pop()
collections_popped = deque_collections_1.pop()
assert our_popped == collections_popped
assert list(our_deque_1) == list(deque_collections_1)

# popleft
our_popped = our_deque_1.popleft()
collections_popped = deque_collections_1.popleft()
assert our_popped == collections_popped
assert list(our_deque_1) == list(deque_collections_1)

# 길이
assert len(our_deque_1) == len(deque_collections_1)
```

## 5. 다른 구현과의 비교 (`deque_doubly.py`)

이 파일(`double_ended_queue.py`)은 `deque_doubly.py`와 매우 유사한 덱을 구현하지만, 몇 가지 차이점이 있습니다.

-   **헤더/트레일러 노드**: `deque_doubly.py`는 실제 데이터를 저장하지 않는 더미 노드(헤더, 트레일러)를 사용하여 경계 조건 처리를 간소화합니다. 반면, 이 구현은 `_front`와 `_back` 포인터가 직접 데이터 노드를 가리키며, 덱이 비었을 때는 `None`을 가리킵니다.
-   **구조**: 이 구현은 `_Node`와 `_Iterator`를 `Deque` 클래스 내부에 정의하여 캡슐화를 강화했습니다.
-   **테스트**: `doctest`에서 `collections.deque`와의 직접적인 비교를 통해 기능의 정확성을 더욱 철저히 검증합니다.

## 6. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/queue/double_ended_queue.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.