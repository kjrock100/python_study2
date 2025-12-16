# `binomial_heap.py` 코드 설명

이 문서는 `binomial_heap.py` 스크립트에 구현된 이항 힙(Binomial Heap) 자료 구조에 대해 설명합니다.

## 1. 이항 힙(Binomial Heap)이란?

이항 힙은 **이항 트리(Binomial Tree)**들의 집합으로 구성된 최소 힙(Min-Heap)입니다. 일반적인 이진 힙과 달리, 두 개의 힙을 효율적으로 병합(Merge)하는 데 강점이 있습니다.

**주요 특징:**
-   각 이항 트리는 최소 힙 속성을 만족합니다 (부모 노드 <= 자식 노드).
-   같은 차수(order)의 이항 트리는 힙 내에 최대 하나만 존재합니다.
-   n개의 노드를 가진 이항 힙은 이진법 표현과 유사하게, 서로 다른 차수의 이항 트리들로 구성됩니다.

**시간 복잡도:**
-   **삽입 (Insert)**: O(log N) (분할 상환 분석으로는 O(1))
-   **최소값 찾기 (Peek)**: O(1)
-   **최소값 삭제 (Delete Min)**: O(log N)
-   **힙 병합 (Merge)**: O(log N)

## 2. 클래스 구조

### `Node` 클래스
이항 트리를 구성하는 각 노드를 표현합니다.

-   `__init__(self, val)`: 노드를 초기화합니다.
    -   `val`: 노드가 저장하는 값.
    -   `left_tree_size`: 왼쪽 서브트리의 크기. 이항 트리에서는 이 값이 차수(order)와 관련이 있습니다. (Order k 트리의 크기는 2^k)
    -   `left`, `right`, `parent`: 이중 연결 리스트(Doubly-linked list)처럼 노드를 연결하는 포인터.
        -   `parent`: 루트 노드들 사이에서는 다음 차수의 트리 루트를, 일반 노드에서는 부모 노드를 가리킵니다.
        -   `left`: 루트 노드들 사이에서는 이전 차수의 트리 루트를, 일반 노드에서는 왼쪽 자식을 가리킵니다.
        -   `right`: 오른쪽 자식을 가리킵니다.
-   `mergeTrees(self, other)`: 동일한 차수의 두 이항 트리를 병합하여 한 단계 더 높은 차수의 트리로 만듭니다.

### `BinomialHeap` 클래스
이항 힙 전체를 관리하는 메인 클래스입니다.

-   `__init__(...)`: 힙을 초기화합니다.
    -   `size`: 힙에 있는 총 노드의 개수.
    -   `bottom_root`: 가장 낮은 차수(order 0)의 이항 트리 루트를 가리킵니다. 루트 리스트의 시작점 역할을 합니다.
    -   `min_node`: 힙 전체에서 최소값을 가진 노드를 가리킵니다.

## 3. 주요 메서드 설명

### `insert(self, val)`
-   **역할**: 힙에 새로운 값을 삽입합니다.
-   **동작**:
    1.  삽입할 값을 가진 새로운 노드(차수 0인 이항 트리)를 생성합니다.
    2.  이 새로운 트리를 기존 힙의 루트 리스트에 추가합니다. 이는 사실상 단일 노드 힙과의 병합 연산과 같습니다.
    3.  루트 리스트를 순회하며 같은 차수의 트리가 있으면 `mergeTrees`를 통해 하나로 합칩니다. 이 과정을 더 이상 합칠 트리가 없을 때까지 반복합니다.

### `mergeHeaps(self, other)`
-   **역할**: 현재 힙과 다른 힙(`other`)을 병합합니다.
-   **동작**:
    1.  두 힙의 루트 리스트를 차수(order) 순으로 정렬하여 하나의 리스트로 만듭니다.
    2.  `insert`와 유사하게, 합쳐진 루트 리스트를 순회하며 같은 차수의 트리가 있으면 계속해서 병합합니다.
    3.  전체 크기와 `min_node`를 갱신합니다.

### `deleteMin(self)`
-   **역할**: 힙에서 최소값 노드를 삭제하고 그 값을 반환합니다.
-   **동작**:
    1.  `min_node`를 힙의 루트 리스트에서 제거합니다.
    2.  `min_node`의 자식들은 그 자체로 또 다른 이항 힙을 구성합니다. 이 자식들로 새로운 힙을 만듭니다.
    3.  원래 힙(최소값 노드가 제거된)과 방금 만들어진 새로운 힙을 `mergeHeaps`를 통해 병합합니다.
    4.  병합된 힙에서 새로운 `min_node`를 찾습니다.

### `peek(self)`
-   **역할**: 힙에서 최소값을 삭제하지 않고 반환합니다.
-   **동작**: `self.min_node.val`을 즉시 반환합니다. (O(1))

### `preOrder()`, `__str__()`
-   **역할**: 힙의 구조를 전위 순회 방식으로 시각화하여 출력합니다. 디버깅 및 구조 확인에 유용합니다.

## 4. 사용 예제

`doctest`에 포함된 예제는 이항 힙의 생성, 삽입, 삭제, 병합 과정을 보여줍니다.

```python
import numpy as np

# 힙 생성 및 30개 원소 삽입
first_heap = BinomialHeap()
permutation = np.random.permutation(list(range(30)))
for number in permutation:
    first_heap.insert(number)

# 힙 크기 확인
print(first_heap.size)
# 출력: 30

# 25개 원소 삭제 및 출력
for i in range(25):
    print(first_heap.deleteMin(), end=" ")
# 출력: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

# 두 번째 힙 생성
second_heap = BinomialHeap()
vals = [17, 20, 31, 34]
for value in vals:
    second_heap.insert(value)

# 두 힙 병합
merged = second_heap.mergeHeaps(first_heap)

# 병합된 힙의 최소값 확인
print(merged.peek())
# 출력: 17

# 병합된 힙의 모든 원소 삭제 및 출력
while not first_heap.isEmpty():
    print(first_heap.deleteMin(), end=" ")
# 출력: 17 20 25 26 27 28 29 31 34
```

## 5. 테스트

스크립트에는 `doctest`가 포함되어 있어 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/heap/binomial_heap.py
```