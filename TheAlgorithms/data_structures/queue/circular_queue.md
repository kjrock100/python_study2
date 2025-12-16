# `circular_queue.py` 코드 설명

이 문서는 `circular_queue.py` 스크립트에 구현된, 배열(리스트)을 이용한 원형 큐(Circular Queue) 자료 구조에 대해 설명합니다.

## 1. 원형 큐(Circular Queue)란?

원형 큐는 한정된 크기의 배열(이 코드에서는 파이썬 리스트)을 사용하여, 큐의 시작과 끝이 원형으로 연결된 것처럼 동작하는 큐입니다. 일반 큐와 달리, 큐의 끝에 도달하면 다시 처음으로 돌아와 비어있는 공간을 재사용할 수 있어 공간 효율성이 높습니다.

이 구현은 `front`와 `rear` 두 개의 인덱스와 `size` 변수를 사용하여 큐의 상태를 관리합니다.

## 2. 클래스 및 메서드 설명

### `CircularQueue` 클래스

#### `__init__(self, n: int)`
-   **역할**: 주어진 용량(`n`)으로 원형 큐를 초기화합니다.
-   **속성**:
    -   `n`: 큐의 최대 용량.
    -   `array`: 실제 데이터가 저장되는 리스트. `None`으로 초기화됩니다.
    -   `front`: 큐의 첫 번째 요소가 있는 인덱스.
    -   `rear`: 큐의 마지막 요소 바로 다음, 즉 새로운 요소가 삽입될 인덱스.
    -   `size`: 현재 큐에 저장된 요소의 개수.

#### `__len__(self) -> int`
-   **역할**: 큐의 현재 크기(`size`)를 반환합니다. `len(queue)` 구문을 지원합니다.
-   **시간 복잡도**: O(1)

#### `is_empty(self) -> bool`
-   **역할**: 큐가 비어있는지 확인합니다.
-   **동작**: `self.size`가 0인지 확인합니다.
-   **시간 복잡도**: O(1)

#### `first(self)`
-   **역할**: 큐의 첫 번째 요소를 삭제하지 않고 반환합니다.
-   **동작**: 큐가 비어있으면 `False`를, 아니면 `self.array[self.front]`를 반환합니다.
-   **시간 복잡도**: O(1)

#### `enqueue(self, data)`
-   **역할**: 큐의 끝에 새로운 데이터를 추가합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  큐가 가득 찼는지(`self.size >= self.n`) 확인하고, 가득 찼으면 `Exception`을 발생시킵니다.
    2.  `self.rear` 인덱스에 데이터를 저장합니다.
    3.  `self.rear`를 `(self.rear + 1) % self.n` 공식을 사용하여 다음 위치로 이동시킵니다. (배열의 끝에 도달하면 0으로 돌아감)
    4.  `self.size`를 1 증가시킵니다.

#### `dequeue(self)`
-   **역할**: 큐의 첫 번째 요소를 제거하고 그 값을 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  큐가 비어있는지(`self.size == 0`) 확인하고, 비어있으면 `Exception`을 발생시킵니다.
    2.  `self.front` 인덱스의 데이터를 임시 변수에 저장합니다.
    3.  해당 슬롯을 `None`으로 만들어 비웁니다.
    4.  `self.front`를 `(self.front + 1) % self.n` 공식을 사용하여 다음 위치로 이동시킵니다.
    5.  `self.size`를 1 감소시킵니다.
    6.  저장해 둔 데이터를 반환합니다.

## 3. 사용 예제

`doctest`에 포함된 예제는 이 클래스의 사용법을 보여줍니다.

```python
# 용량이 5인 원형 큐 생성
cq = CircularQueue(5)

# 큐가 비어있는지 확인
print(cq.is_empty())
# 출력: True

# 데이터 삽입
cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")

print(len(cq))      # 출력: 3
print(cq.first())   # 출력: 'A'

# 데이터 추출
print(cq.dequeue()) # 출력: 'A'
print(cq.first())   # 출력: 'B'

# 추가 데이터 삽입 (rear가 배열의 끝을 넘어 순환)
cq.enqueue("D")
cq.enqueue("E")
cq.enqueue("F")

# 큐가 가득 찬 상태에서 삽입 시도 (예외 발생)
try:
    cq.enqueue("G")
except Exception as e:
    print(e)
# 출력: QUEUE IS FULL
```

## 4. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/queue/circular_queue.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.