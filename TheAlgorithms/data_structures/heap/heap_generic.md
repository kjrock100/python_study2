# `heap_generic.py` 코드 설명

이 문서는 `heap_generic.py` 스크립트에 구현된 제네릭 힙(Generic Heap) 자료 구조에 대해 설명합니다.

## 1. 제네릭 힙(Generic Heap)이란?

이 코드는 일반적인 이진 힙(Binary Heap)을 구현한 클래스입니다. "제네릭(Generic)"이라는 이름처럼, 생성 시 `key` 함수를 어떻게 전달하느냐에 따라 **최소 힙(Min-Heap)** 또는 **최대 힙(Max-Heap)**으로 모두 동작할 수 있는 유연한 구조를 가집니다.

**주요 특징:**
-   **유연성**: `key` 함수를 통해 최소 힙과 최대 힙을 모두 지원합니다. (기본값은 최대 힙)
-   **효율적인 업데이트 및 삭제**: 내부적으로 딕셔너리(`pos_map`)를 사용하여 각 항목의 위치를 추적합니다. 이 덕분에 파이썬의 표준 `heapq` 모듈에서는 지원하지 않는, 임의의 항목을 O(log N) 시간에 **업데이트**하거나 **삭제**하는 강력한 기능을 제공합니다.

## 2. 클래스 및 메서드 설명

### `Heap` 클래스

#### `__init__(self, key=None)`
-   **역할**: 힙을 초기화합니다.
-   **매개변수**:
    -   `key`: 항목의 우선순위(점수)를 계산하는 함수.
        -   `None` (기본값): `lambda x: x`와 동일하게 동작하여 **최대 힙**이 됩니다.
        -   `lambda x: -x`: 값의 부호를 반전시켜 **최소 힙**으로 동작하게 합니다.
-   **속성**:
    -   `arr`: 실제 힙 항목 `[item, score]`을 저장하는 리스트.
    -   `pos_map`: `item`을 키로, `arr`에서의 인덱스를 값으로 갖는 딕셔너리. 항목의 위치를 빠르게 찾는 데 사용됩니다.

### 핵심 연산 (Core Operations)

#### `insert_item(self, item, item_value)`
-   **역할**: 힙에 새로운 항목을 삽입합니다.
-   **동작**: 항목을 배열의 끝에 추가한 후, `_heapify_up`을 호출하여 힙 속성을 만족하도록 위치를 조정합니다.

#### `get_top(self)`
-   **역할**: 힙에서 우선순위가 가장 높은 항목(최대 힙에서는 최댓값, 최소 힙에서는 최솟값)을 삭제하지 않고 반환합니다.

#### `extract_top(self)`
-   **역할**: 힙에서 우선순위가 가장 높은 항목을 제거하고 반환합니다.
-   **동작**: 내부적으로 `delete_item`을 호출하여 루트 노드를 삭제합니다.

### 고급 연산 (Advanced Operations)

#### `update_item(self, item, item_value)`
-   **역할**: 이미 힙에 있는 항목의 우선순위 값을 갱신합니다.
-   **시간 복잡도**: O(log N)
-   **동작**: `pos_map`을 이용해 항목의 위치를 O(1)에 찾은 후, 값을 갱신하고 `_heapify_up`과 `_heapify_down`을 호출하여 힙 속성을 복원합니다.

#### `delete_item(self, item)`
-   **역할**: 힙에서 특정 항목을 삭제합니다.
-   **시간 복잡도**: O(log N)
-   **동작**:
    1.  `pos_map`을 이용해 삭제할 항목의 위치를 찾습니다.
    2.  해당 항목을 힙의 마지막 항목과 교체합니다.
    3.  힙의 크기를 1 줄입니다.
    4.  교체된 위치에서 `_heapify_up`과 `_heapify_down`을 호출하여 힙 속성을 복원합니다.

### 내부 헬퍼 메서드

-   `_parent(i)`, `_left(i)`, `_right(i)`: 특정 인덱스의 부모 및 자식 인덱스를 계산합니다.
-   `_swap(i, j)`: `arr` 리스트의 두 항목을 교환하고, `pos_map`의 인덱스 정보도 함께 갱신합니다.
-   `_heapify_up(index)`, `_heapify_down(index)`: 특정 위치에서부터 위 또는 아래 방향으로 힙 속성을 만족시키도록 재정렬합니다.

## 3. 사용 예제

`doctest`에 포함된 예제는 이 제네릭 힙의 다양한 활용법을 보여줍니다.

```python
# 최대 힙으로 사용 (기본값)
h_max = Heap()
h_max.insert_item(5, 34)
h_max.insert_item(7, 37)
print(h_max.get_top())  # 출력: [7, 37]

# 최소 힙으로 사용 (key 함수 지정)
h_min = Heap(key=lambda x: -x)
h_min.insert_item(5, 34)
h_min.insert_item(6, 31)
h_min.insert_item(7, 37)
print(h_min.get_top())  # 출력: [6, -31]

# 항목 값 업데이트
h_min.update_item(7, 20) # 7번 항목의 값을 37에서 20으로 변경
print(h_min.get_top())  # 출력: [7, -20]

# 항목 삭제
h_min.delete_item(7)
print(h_min.get_top())  # 출력: [6, -31]
```

## 4. 테스트

스크립트에는 `doctest`가 포함되어 있어 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/heap/heap_generic.py
```

테스트가 성공하면 아무런 출력도 나타나지 않습니다.