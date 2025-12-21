# 부분집합의 합 (Sum of Subset)

이 문서는 `sum_of_subset.py` 파일에 구현된 **부분집합의 합(Sum of Subset)** 알고리즘에 대해 설명합니다. 이 문제는 주어진 정수 집합에서 일부 원소를 선택하여 그 합이 특정 목표 값(Required Sum)이 될 수 있는지를 판별하는 문제입니다.

## 개요

이 알고리즘은 **동적 계획법(Dynamic Programming)**을 사용하여 해결합니다. 가능한 모든 부분집합을 확인하는 전수 조사(Brute Force) 방식은 $O(2^n)$의 시간이 걸리지만, 동적 계획법을 사용하면 $O(n \cdot sum)$의 시간 복잡도로 해결할 수 있습니다.

## 주요 함수: `isSumSubset(arr, arrLen, requiredSum)`

### `isSumSubset(arr, arrLen, requiredSum)`
- **목적**: 주어진 리스트 `arr`의 부분집합 합으로 `requiredSum`을 만들 수 있는지 확인하고 결과를 출력합니다.
- **매개변수**:
  - `arr`: 정수 리스트.
  - `arrLen`: 리스트의 길이.
  - `requiredSum`: 만들고자 하는 목표 합.
- **동작**: 결과(`True` 또는 `False`)를 화면에 출력합니다.

### 알고리즘 동작 원리

1. **DP 테이블 초기화**:
   - `subset`이라는 2차원 리스트를 생성합니다. 크기는 `(arrLen + 1) x (requiredSum + 1)`입니다.
   - `subset[i][j]`는 `arr`의 처음 `i`개의 원소를 사용하여 합 `j`를 만들 수 있는지를 나타내는 불리언(Boolean) 값입니다.

2. **기저 사례 (Base Cases)**:
   - **합이 0인 경우**: 원소를 하나도 선택하지 않으면 합이 0이 되므로, 모든 `i`에 대해 `subset[i][0] = True`입니다.
   - **원소가 없는 경우**: 원소가 없는데 합이 0보다 큰 경우는 불가능하므로, `j > 0`인 모든 `j`에 대해 `subset[0][j] = False`입니다.

3. **테이블 채우기 (Bottom-Up)**:
   - 이중 반복문을 사용하여 `i` (고려할 원소의 수)를 1부터 `arrLen`까지, `j` (현재 목표 합)를 1부터 `requiredSum`까지 순회합니다.
   - **점화식**:
     - 현재 원소 `arr[i-1]`이 현재 목표 합 `j`보다 큰 경우:
       - 이 원소는 포함할 수 없으므로, 이전 단계(`i-1`)의 결과를 그대로 가져옵니다.
       - `subset[i][j] = subset[i-1][j]`
     - 현재 원소 `arr[i-1]`이 현재 목표 합 `j`보다 작거나 같은 경우:
       - 이 원소를 **포함하지 않는 경우**(`subset[i-1][j]`)와 **포함하는 경우**(`subset[i-1][j - arr[i-1]]`) 중 하나라도 가능하면 `True`가 됩니다.
       - `subset[i][j] = subset[i-1][j] or subset[i-1][j - arr[i-1]]`

4. **결과 출력**:
   - 모든 계산이 끝나면 `subset[arrLen][requiredSum]`의 값을 출력합니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
isSumSubset([2, 4, 6, 8], 4, 5)
# 출력: False (어떤 조합으로도 5를 만들 수 없음)

isSumSubset([2, 4, 6, 8], 4, 14)
# 출력: True (2 + 4 + 8 = 14, 6 + 8 = 14 등 가능)
```