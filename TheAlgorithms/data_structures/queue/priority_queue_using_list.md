# `priority_queue_using_list.py` 코드 설명

이 문서는 `priority_queue_using_list.py` 스크립트에 구현된, 파이썬 리스트를 이용한 두 가지 종류의 우선순위 큐(Priority Queue)에 대해 설명합니다.

## 1. 우선순위 큐(Priority Queue)란?

우선순위 큐는 각 요소가 '우선순위'를 가지는 큐입니다. 요소를 제거할 때, 일반 큐처럼 먼저 들어온 순서가 아니라 우선순위가 가장 높은 요소가 먼저 제거되는 특징을 가집니다.

이 스크립트는 두 가지 방식의 우선순위 큐를 구현합니다.

1.  **`FixedPriorityQueue`**: 우선순위가 0, 1, 2와 같이 몇 개의 고정된 레벨로 나뉜 큐.
2.  **`ElementPriorityQueue`**: 요소의 값 자체가 우선순위가 되는 큐.

## 2. 사용자 정의 예외

-   `OverFlowError`: 큐가 정해진 용량(100)을 초과하여 요소를 추가하려고 할 때 발생합니다.
-   `UnderFlowError`: 큐가 비어있는데 요소를 제거하려고 할 때 발생합니다.

## 3. `FixedPriorityQueue` 클래스

이 클래스는 여러 개의 고정된 우선순위 레벨을 가집니다. 각 우선순위마다 별도의 큐(파이썬 리스트)를 유지합니다.

### 메서드 설명

-   `__init__(self)`: 3개의 빈 리스트를 가지는 `queues` 속성을 초기화합니다. `queues[0]`이 가장 높은 우선순위를 가집니다.
-   `enqueue(self, priority: int, data: int)`: 주어진 `priority`에 해당하는 큐에 `data`를 추가합니다. (시간 복잡도: O(1) amortized)
-   `dequeue(self) -> int`: 가장 높은 우선순위(0번) 큐부터 순서대로 확인하여, 비어있지 않은 첫 번째 큐에서 요소를 제거하고 반환합니다. 각 큐 내에서는 선입선출(FIFO) 원칙을 따릅니다.
    -   **성능 참고**: 이 메서드는 `queue.pop(0)`을 사용하는데, 이는 리스트의 모든 요소를 한 칸씩 앞으로 이동시켜야 하므로 O(N)의 시간 복잡도를 가집니다. (N은 해당 우선순위 큐의 길이). 이로 인해 큐가 길어질수록 성능이 저하됩니다. `collections.deque`를 사용하면 O(1)로 개선할 수 있습니다.
-   `__str__(self)`: 각 우선순위 큐의 내용을 문자열로 반환합니다.

### 사용 예제

```python
fpq = FixedPriorityQueue()
fpq.enqueue(0, 10)  # 우선순위 0
fpq.enqueue(1, 70)  # 우선순위 1
fpq.enqueue(0, 100) # 우선순위 0

print(fpq.dequeue()) # 출력: 10 (우선순위 0에서 먼저 들어온 값)
print(fpq.dequeue()) # 출력: 100
print(fpq.dequeue()) # 출력: 70 (우선순위 0이 비었으므로 우선순위 1에서 추출)
```

## 4. `ElementPriorityQueue` 클래스

이 클래스는 요소의 값 자체가 우선순위가 됩니다. 값이 작을수록 우선순위가 높습니다.

### 메서드 설명

-   `__init__(self)`: 빈 리스트 `queue`를 초기화합니다.
-   `enqueue(self, data: int)`: 큐에 데이터를 추가합니다. (시간 복잡도: O(1) amortized)
-   `dequeue(self) -> int`: 큐에서 가장 작은 값(가장 높은 우선순위)을 찾아 제거하고 반환합니다.
    -   **성능 참고**: 이 메서드는 `min(self.queue)` (O(N))와 `self.queue.remove(data)` (O(N))를 사용하여 구현되어, 전체 시간 복잡도가 O(N)입니다. 이는 매우 비효율적이며, 큐의 크기가 커질수록 성능이 급격히 저하됩니다. 이와 같은 우선순위 큐는 일반적으로 **힙(Heap)** 자료 구조를 사용하여 구현하는 것이 훨씬 효율적입니다 (삽입/삭제 모두 O(log N)).
-   `__str__(self)`: 큐의 현재 내용을 문자열로 반환합니다.

### 사용 예제

```python
epq = ElementPriorityQueue()
epq.enqueue(70)
epq.enqueue(10)
epq.enqueue(100)

print(epq.dequeue()) # 출력: 10 (가장 작은 값)
print(epq.dequeue()) # 출력: 70
print(epq.dequeue()) # 출력: 100
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/queue/priority_queue_using_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.