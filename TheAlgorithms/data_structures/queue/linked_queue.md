# `linked_queue.py` 코드 설명

이 문서는 `linked_queue.py` 스크립트에 구현된, 단일 연결 리스트(Singly Linked List)를 이용한 큐(Queue) 자료 구조에 대해 설명합니다.

## 1. 큐(Queue)란?

큐는 선입선출(First-In, First-Out, FIFO) 원칙을 따르는 선형 자료 구조입니다. 즉, 가장 먼저 추가된 요소가 가장 먼저 제거됩니다.

**주요 연산:**
-   **Enqueue**: 큐의 끝(rear)에 요소를 추가합니다. (이 코드에서는 `put` 메서드)
-   **Dequeue**: 큐의 앞(front)에서 요소를 제거하고 반환합니다. (이 코드에서는 `get` 메서드)

## 2. 연결 리스트 기반 구현

이 코드는 큐를 단일 연결 리스트를 사용하여 구현합니다.

-   **`front` 포인터**: 큐의 첫 번째 노드를 가리킵니다. `get` 연산은 이 노드에서 발생합니다.
-   **`rear` 포인터**: 큐의 마지막 노드를 가리킵니다. `put` 연산은 이 노드 뒤에 새로운 노드를 추가하고 `rear`를 갱신합니다.

이 방식을 사용하면 `put`과 `get` 연산 모두 O(1)의 시간 복잡도를 가집니다.

## 3. 클래스 및 메서드 설명

### `Node` 클래스
-   **역할**: 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드를 가리키는 참조.

### `LinkedQueue` 클래스

#### `__init__(self)`
-   **역할**: 빈 큐를 초기화합니다.
-   **속성**:
    -   `front`: 큐의 첫 번째 노드를 가리킵니다. (초기값: `None`)
    -   `rear`: 큐의 마지막 노드를 가리킵니다. (초기값: `None`)

#### `__iter__(self) -> Iterator[Any]`
-   **역할**: 큐의 모든 데이터를 순회하는 이터레이터(iterator)를 반환합니다.

#### `__len__(self) -> int`
-   **역할**: 큐에 포함된 요소의 개수를 반환합니다.
-   **시간 복잡도**: O(N), 큐의 모든 노드를 순회하여 길이를 계산합니다.
    > **개선 제안**: 클래스에 `size` 속성을 추가하고 `put`/`get` 시마다 값을 증감시키면 O(1)으로 개선할 수 있습니다.

#### `__str__(self) -> str`
-   **역할**: 큐의 내용을 `<-`로 연결된 문자열로 표현합니다.

#### `is_empty(self) -> bool`
-   **역할**: 큐가 비어있는지 확인합니다.
-   **동작**: `len(self)`가 0인지 확인합니다. (시간 복잡도: O(N))
    > **개선 제안**: `self.front is None`으로 확인하면 O(1)으로 개선할 수 있습니다.

#### `put(self, item: Any) -> None`
-   **역할**: 큐의 끝(rear)에 새로운 `item`을 추가합니다.
-   **시간 복잡도**: O(N), 내부적으로 `is_empty()`를 호출하기 때문입니다. `is_empty()`가 개선되면 O(1)이 됩니다.
-   **동작**:
    1.  새로운 `Node`를 생성합니다.
    2.  큐가 비어있으면, `front`와 `rear`가 모두 새 노드를 가리키게 합니다.
    3.  그렇지 않으면, 기존 `rear` 노드의 `next`를 새 노드로 연결하고, `rear`를 새 노드로 갱신합니다.

#### `get(self) -> Any`
-   **역할**: 큐의 앞(front)에서 요소를 제거하고 반환합니다.
-   **시간 복잡도**: O(N), 내부적으로 `is_empty()`를 호출하기 때문입니다. `is_empty()`가 개선되면 O(1)이 됩니다.
-   **동작**:
    1.  큐가 비어있으면 `IndexError`를 발생시킵니다.
    2.  `front` 노드의 데이터를 저장합니다.
    3.  `front` 포인터를 다음 노드로 이동시킵니다.
    4.  만약 `front`가 `None`이 되면(큐가 비게 되면), `rear`도 `None`으로 설정합니다.
    5.  저장해 둔 데이터를 반환합니다.

#### `clear(self) -> None`
-   **역할**: 큐의 모든 요소를 제거합니다.
-   **시간 복잡도**: O(1)
-   **동작**: `front`와 `rear`를 모두 `None`으로 설정합니다.

## 4. 사용 예제

`doctest`에 포함된 예제는 이 클래스의 사용법을 보여줍니다.

```python
queue = LinkedQueue()

# 큐가 비어있는지 확인
print(queue.is_empty())
# 출력: True

# 데이터 삽입 (put)
queue.put(5)
queue.put(9)
queue.put('python')

print(queue)
# 출력: 5 <- 9 <- python

# 데이터 추출 (get)
print(queue.get())
# 출력: 5

print(queue.get())
# 출력: 9

print(len(queue))
# 출력: 1

# 큐 비우기
queue.clear()
print(queue.is_empty())
# 출력: True
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/queue/linked_queue.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.