# 최대 부분 배열 합 (Maximum Subarray Sum)

이 문서는 `max_subarray_sum.py` 파일에 구현된 **최대 부분 배열 합(Maximum Subarray Sum)** 알고리즘에 대해 설명합니다. 이 알고리즘은 주어진 정수 배열에서 연속된 부분 배열의 합 중 가장 큰 값을 찾는 문제를 해결합니다.

## 개요

이 코드는 **분할 정복(Divide and Conquer)** 방식을 사용하여 문제를 해결합니다. 배열을 절반으로 나누어 각 부분에서의 최대 합을 구하고, 두 부분을 걸치는 경우까지 고려하여 전체의 최댓값을 찾습니다. 이 방식의 시간 복잡도는 $O(n \log n)$입니다.

## 주요 함수 설명

### `max_sum_from_start(array)`
- **목적**: 배열의 첫 번째 요소(인덱스 0)부터 시작하는 연속된 부분 배열의 합 중 최댓값을 구합니다.
- **동작**: 배열을 순회하며 누적 합을 계산하고, 그중 가장 컸던 값을 반환합니다.

### `max_cross_array_sum(array, left, mid, right)`
- **목적**: 중간 지점(`mid`)을 포함하여 왼쪽과 오른쪽으로 걸쳐 있는 부분 배열의 최대 합을 구합니다.
- **동작**:
  1. **왼쪽 부분**: `mid`에서 `left` 방향으로(역순으로) 뻗어나가며 최대 합을 구합니다. 이를 위해 배열을 슬라이싱하고 뒤집은 후(`[::-1]`) `max_sum_from_start`를 호출합니다.
  2. **오른쪽 부분**: `mid + 1`에서 `right` 방향으로 뻗어나가며 최대 합을 구합니다.
  3. 두 부분의 최대 합을 더하여 반환합니다.

### `max_subarray_sum(array, left, right)`
- **목적**: 분할 정복을 수행하는 메인 재귀 함수입니다.
- **매개변수**:
  - `array`: 전체 배열.
  - `left`, `right`: 현재 탐색 중인 범위의 시작과 끝 인덱스.
- **알고리즘 단계**:
  1. **기저 사례 (Base Case)**: `left == right`이면 원소가 하나뿐이므로 해당 값을 반환합니다.
  2. **분할 (Divide)**: 중간 인덱스 `mid`를 계산합니다.
  3. **정복 (Conquer)**:
     - `left_half_sum`: 왼쪽 절반(`left` ~ `mid`)에서의 최대 합을 재귀적으로 구합니다.
     - `right_half_sum`: 오른쪽 절반(`mid + 1` ~ `right`)에서의 최대 합을 재귀적으로 구합니다.
  4. **결합 (Combine)**:
     - `cross_sum`: 중간 지점을 걸치는 최대 합을 `max_cross_array_sum`으로 구합니다.
     - 세 가지 값(`left_half_sum`, `right_half_sum`, `cross_sum`) 중 최댓값을 반환합니다.

## 사용법

코드 하단에서 사용 예시를 확인할 수 있습니다:

```python
array = [-2, -5, 6, -2, -3, 1, 5, -6]
array_length = len(array)
print("Maximum sum of contiguous subarray:", max_subarray_sum(array, 0, array_length - 1))
```

위 예제의 경우 `[6, -2, -3, 1, 5]` 부분 배열의 합인 **7**이 출력됩니다.
