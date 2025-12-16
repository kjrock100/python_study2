# `circular_queue_linked_list.py` 코드 설명

이 문서는 `circular_queue_linked_list.py` 스크립트에 구현된, 이중 연결 리스트를 이용한 원형 큐(Circular Queue) 자료 구조에 대해 설명합니다.

## 1. 원형 큐(Circular Queue)란?

원형 큐는 한정된 크기의 배열이나 리스트를 사용하여, 큐의 시작과 끝이 원형으로 연결된 것처럼 동작하는 큐입니다. 일반 큐와 달리, 큐의 끝에 도달하면 다시 처음으로 돌아와 비어있는 공간을 재사용할 수 있어 공간 효율성이 높습니다.

## 2. 구현 방식: 고정 크기 이중 연결 리스트

이 코드는 원형 큐를 구현하기 위해 독특한 방식을 사용합니다.

-   **고정 크기 노드 할당**: 큐가 생성될 때, 주어진 용량(`initial_capacity`)만큼의 `Node` 객체를 미리 생성하여 이중 연결 리스트로 원형으로 연결해 둡니다.
-   **데이터 필드 사용**: 각 노드는 `data` 필드를 가지며, 이 필드가 `None`이면 해당 슬롯은 비어있음을, 값이 있으면 채워져 있음을 의미합니다.
-   **`front`와 `rear` 포인터**:
    -   `front`: 큐의 첫 번째 요소가 있는 노드를 가리킵니다. `dequeue` 연산은 이 노드에서 발생합니다.
    -   `rear`: 큐의 마지막 요소가 있는 노드를 가리킵니다. `enqueue` 연산은 이 노드 다음의 빈 노드에서 발생합니다.

이 방식은 동적으로 노드를 생성/삭제하는 일반적인 연결 리스트와 달리, 고정된 크기의 버퍼를 노드로 구현한 것과 유사합니다.

## 3. 클래스 및 메서드 설명

### `Node` 클래스
-   **역할**: 이중 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터. 비어있을 경우 `None`.
    -   `next`: 다음 노드를 가리키는 참조.
    -   `prev`: 이전 노드를 가리키는 참조.

### `CircularQueueLinkedList` 클래스

#### `__init__(self, initial_capacity: int = 6)`
-   **역할**: 주어진 용량으로 원형 큐를 초기화합니다.
-   **동작**: `create_linked_list`를 호출하여 고정된 수의 노드를 생성하고 원형으로 연결합니다.

#### `create_linked_list(self, initial_capacity: int)`
-   **역할**: `initial_capacity` 개수만큼의 `Node`를 미리 생성하고, 이들을 이중 연결 리스트로 만들어 원형 구조를 완성합니다.

#### `is_empty(self) -> bool`
-   **역할**: 큐가 비어있는지 확인합니다.
-   **동작**: `front`와 `rear` 포인터가 같은 노드를 가리키고, 그 노드의 `data`가 `None`일 때 비어있는 것으로 간주합니다.

#### `check_is_full(self) -> None`
-   **역할**: 큐가 가득 찼는지 확인하고, 가득 찼으면 `Exception`을 발생시킵니다.
-   **동작**: `rear`의 다음 노드가 `front`이고, `rear`의 데이터가 `None`이 아닐 때(즉, `rear`가 유효한 데이터를 가리킬 때) 가득 찬 것으로 간주합니다.

#### `first(self) -> Any | None`
-   **역할**: 큐의 첫 번째 요소를 삭제하지 않고 반환합니다.
-   **시간 복잡도**: O(1)

#### `enqueue(self, data: Any) -> None`
-   **역할**: 큐의 끝에 새로운 데이터를 추가합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  큐가 가득 찼는지 확인합니다.
    2.  큐가 비어있지 않으면, `rear` 포인터를 다음 노드로 이동시킵니다. (큐가 비어있을 때는 `front`와 `rear`가 같은 위치에 있으므로 이동하지 않습니다.)
    3.  새로운 `rear` 노드의 `data` 필드에 값을 저장합니다.

#### `dequeue(self) -> Any`
-   **역할**: 큐의 첫 번째 요소를 제거하고 그 값을 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  큐가 비어있는지 확인합니다.
    2.  `front` 노드의 데이터를 임시 변수에 저장합니다.
    3.  `front` 노드의 `data`를 `None`으로 만들어 슬롯을 비웁니다.
    4.  큐에 요소가 하나만 있었던 경우가 아니라면, `front` 포인터를 다음 노드로 이동시킵니다.
    5.  저장해 둔 데이터를 반환합니다.

## 4. 사용 예제

`doctest`에 포함된 예제는 이 클래스의 사용법을 보여줍니다.

```python
# 용량이 2인 원형 큐 생성
cq = CircularQueueLinkedList(2)

# 데이터 삽입
cq.enqueue('a')
cq.enqueue('b')

# 큐가 가득 찬 상태에서 삽입 시도 (예외 발생)
try:
    cq.enqueue('c')
except Exception as e:
    print(e)
# 출력: Full Queue

# 첫 번째 요소 확인
print(cq.first())
# 출력: 'a'

# 데이터 추출
print(cq.dequeue())
# 출력: 'a'

print(cq.dequeue())
# 출력: 'b'

# 큐가 비어있는지 확인
print(cq.is_empty())
# 출력: True

# 빈 큐에서 추출 시도 (예외 발생)
try:
    cq.dequeue()
except Exception as e:
    print(e)
# 출력: Empty Queue
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/queue/circular_queue_linked_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.