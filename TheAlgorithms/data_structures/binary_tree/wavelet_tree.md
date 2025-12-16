# `wavelet_tree.py` 코드 설명

이 문서는 `wavelet_tree.py` 스크립트에 구현된 웨이블릿 트리(Wavelet Tree) 자료 구조에 대해 설명합니다.

## 1. 웨이블릿 트리란?

웨이블릿 트리는 배열에 대한 다양한 범위 쿼리(range queries)를 효율적으로 처리하기 위해 설계된 자료 구조입니다. 세그먼트 트리나 펜윅 트리와 같은 다른 이진 트리와는 달리, 웨이블릿 트리는 노드를 인덱스가 아닌 **실제 요소 값**을 기준으로 분할합니다.

주요 특징:
-   **값 기반 분할**: 각 노드는 요소 값의 범위를 절반으로 나누어 자식 노드를 생성합니다.
-   **효율적인 쿼리**: `rank` (특정 값의 출현 횟수), `quantile` (k번째 작은 값), `range_counting` (특정 값 범위 내 요소 개수) 등의 쿼리를 O(log M) 시간에 처리할 수 있습니다. (여기서 M은 값의 범위)
-   **공간 복잡도**: O(N log M) 또는 O(N) (알파벳 크기에 따라 다름).

## 2. `Node` 클래스

웨이블릿 트리를 구성하는 각 노드를 표현하는 클래스입니다.

-   `__init__(self, length: int) -> None`: 노드를 초기화합니다.
    -   `minn`: 이 노드가 담당하는 값 범위의 최솟값.
    -   `maxx`: 이 노드가 담당하는 값 범위의 최댓값.
    -   `map_left`: `list[int]`. 원본 배열의 각 인덱스 `i`에 대해, `arr[0...i]` 구간에서 왼쪽 자식으로 가는 요소의 누적 개수를 저장합니다. 이는 자식 노드로 인덱스를 매핑하는 데 사용됩니다.
    -   `left`: 왼쪽 자식 노드에 대한 참조.
    -   `right`: 오른쪽 자식 노드에 대한 참조.
-   `__repr__(self) -> str`: 노드의 `minn`과 `maxx` 값을 문자열로 표현합니다.

## 3. 핵심 함수 설명

### `build_tree(arr: list[int]) -> Node | None`
-   **역할**: 주어진 배열 `arr`을 기반으로 웨이블릿 트리를 구축하고, 트리의 루트 노드를 반환합니다.
-   **동작 원리 (재귀)**:
    1.  현재 노드의 `minn`과 `maxx`를 설정합니다.
    2.  **기저 사례**: `minn == maxx`인 경우 (노드가 단일 고유 값만 포함), 해당 노드를 리프 노드로 반환합니다.
    3.  `pivot = (minn + maxx) // 2`를 기준으로 `arr`를 두 개의 서브 배열(`left_arr`, `right_arr`)로 분할합니다.
        -   `left_arr`: `pivot`보다 작거나 같은 요소들.
        -   `right_arr`: `pivot`보다 큰 요소들.
        -   이 과정에서 `map_left` 배열을 채워 각 인덱스까지 왼쪽 자식으로 가는 요소의 개수를 기록합니다.
    4.  `left_arr`와 `right_arr`에 대해 재귀적으로 `build_tree`를 호출하여 왼쪽 및 오른쪽 자식 트리를 구축합니다.

### `rank_till_index(node: Node | None, num: int, index: int) -> int`
-   **역할**: 원본 배열의 `[0, index]` 구간에서 `num`이 몇 번 나타나는지 반환합니다.
-   **동작 원리 (재귀)**:
    1.  **기저 사례**: `index < 0` 또는 `node is None`이면 0을 반환합니다.
    2.  **리프 노드**: `node.minn == node.maxx`이면, `node.minn == num`인 경우 `index + 1` (즉, 해당 구간의 모든 요소)을 반환하고, 아니면 0을 반환합니다.
    3.  `pivot = (node.minn + node.maxx) // 2`를 기준으로 `num`이 어느 자식 트리로 가야 할지 결정합니다.
        -   `num <= pivot`: 왼쪽 자식 트리로 이동합니다. `map_left[index]`를 사용하여 왼쪽 자식 트리에 해당하는 새로운 `index`를 계산합니다.
        -   `num > pivot`: 오른쪽 자식 트리로 이동합니다. `index - map_left[index]`를 사용하여 오른쪽 자식 트리에 해당하는 새로운 `index`를 계산합니다.

### `rank(node: Node | None, num: int, start: int, end: int) -> int`
-   **역할**: 원본 배열의 `[start, end]` 구간에서 `num`이 몇 번 나타나는지 반환합니다.
-   **동작**: `rank_till_index(node, num, end) - rank_till_index(node, num, start - 1)` 공식을 사용하여 구간 내 출현 횟수를 계산합니다.

### `quantile(node: Node | None, index: int, start: int, end: int) -> int`
-   **역할**: 원본 배열의 `[start, end]` 구간에서 `index`번째로 작은 요소(0-indexed)를 반환합니다.
-   **동작 원리 (재귀)**:
    1.  **기저 사례**: 유효하지 않은 범위이거나 `node is None`이면 -1을 반환합니다.
    2.  **리프 노드**: `node.minn == node.maxx`이면 `node.minn`을 반환합니다.
    3.  현재 노드의 `[start, end]` 구간에서 왼쪽 자식 트리로 가는 요소의 개수(`num_elements_in_left_tree`)를 계산합니다.
    4.  `index`가 `num_elements_in_left_tree`보다 작으면, 왼쪽 자식 트리로 이동하여 `index`번째 작은 값을 찾습니다.
    5.  그렇지 않으면, 오른쪽 자식 트리로 이동하여 `index - num_elements_in_left_tree`번째 작은 값을 찾습니다.

### `range_counting(node: Node | None, start: int, end: int, start_num: int, end_num: int) -> int`
-   **역할**: 원본 배열의 `[start, end]` 구간에서 값이 `[start_num, end_num]` 범위에 속하는 요소의 개수를 반환합니다.
-   **동작 원리 (재귀)**:
    1.  **기저 사례**: 유효하지 않은 범위이거나 `node is None`, 또는 현재 노드의 값 범위가 쿼리 값 범위와 전혀 겹치지 않으면 0을 반환합니다.
    2.  **완전 포함**: 현재 노드의 값 범위 `[node.minn, node.maxx]`가 쿼리 값 범위 `[start_num, end_num]`에 완전히 포함되면, 현재 구간 `[start, end]`의 모든 요소 개수(`end - start + 1`)를 반환합니다.
    3.  그 외의 경우: 왼쪽 및 오른쪽 자식 트리로 재귀 호출하여 결과를 합산합니다. 이때, 각 자식 트리로 전달되는 `start`와 `end` 인덱스는 `map_left`를 사용하여 적절히 조정됩니다.

## 4. 사용 예제

스크립트의 `if __name__ == "__main__"` 블록은 `doctest`를 실행하여 함수의 동작을 검증합니다. 다음은 `doctest`에 포함된 예제들입니다.

```python
test_array = [2, 1, 4, 5, 6, 0, 8, 9, 1, 2, 0, 6, 4, 2, 0, 6, 5, 3, 2, 7]

# 트리 구축
root = build_tree(test_array)

# rank_till_index 예제
# rank_till_index(root, 6, 6) -> 1 (test_array[0...6]에서 6은 한 번 나옴)
# rank_till_index(root, 2, 0) -> 1 (test_array[0...0]에서 2는 한 번 나옴)
# rank_till_index(root, 1, 10) -> 2 (test_array[0...10]에서 1은 두 번 나옴)

# rank 예제
# rank(root, 6, 3, 13) -> 2 (test_array[3...13]에서 6은 두 번 나옴)
# rank(root, 2, 0, 19) -> 4 (test_array[0...19]에서 2는 네 번 나옴)

# quantile 예제
# quantile(root, 2, 2, 5) -> 5 (test_array[2...5] = [4, 5, 6, 0]에서 2번째로 작은 값은 5)
# quantile(root, 5, 2, 13) -> 4 (test_array[2...13]에서 5번째로 작은 값은 4)

# range_counting 예제
# range_counting(root, 1, 10, 3, 7) -> 3 (test_array[1...10]에서 3~7 사이 값은 4, 5, 6 세 개)
# range_counting(root, 0, 19, 0, 100) -> 20 (전체 배열에서 0~100 사이 값은 20개)
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/wavelet_tree.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.