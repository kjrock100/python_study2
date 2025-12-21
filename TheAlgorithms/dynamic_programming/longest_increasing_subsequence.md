# 최장 증가 부분 수열 (Longest Increasing Subsequence) - O(N^2)

이 문서는 `longest_increasing_subsequence.py` 파일에 구현된 **최장 증가 부분 수열(LIS)** 알고리즘에 대해 설명합니다.

## 개요

최장 증가 부분 수열(LIS) 문제는 주어진 수열에서 오름차순으로 정렬된 가장 긴 부분 수열을 찾는 문제입니다. 이 코드는 **동적 계획법(Dynamic Programming)**을 사용하여 $O(N^2)$의 시간 복잡도로 문제를 해결합니다.

## 주요 함수: `longest_subsequence(array)`

### `longest_subsequence(array: list[int]) -> list[int]`
- **목적**: 입력 리스트 `array`의 최장 증가 부분 수열을 반환합니다.
- **매개변수**:
  - `array`: 정수 리스트.
- **반환값**: 최장 증가 부분 수열 리스트.

### 알고리즘 동작 원리

1. **초기화**:
   - `sequences` 리스트: 각 인덱스 `i`에 대해, `array[i]`를 마지막 원소로 가지는 최장 증가 부분 수열을 저장합니다. 처음에는 각 원소 자신만 포함하는 리스트로 초기화됩니다.
   - `lengths` 리스트: `sequences`에 저장된 각 부분 수열의 길이를 저장합니다.

2. **DP 테이블 채우기**:
   - 이중 반복문을 사용하여 모든 원소 쌍 `(array[i], array[j])`을 비교합니다 (`j < i`).
   - 만약 `array[j] < array[i]`이고, `array[j]`로 끝나는 부분 수열의 길이가 `array[i]`로 끝나는 현재 부분 수열의 길이보다 크거나 같다면:
     - `array[i]`를 `array[j]`의 부분 수열 뒤에 붙여서 더 긴 수열을 만들 수 있습니다.
     - `sequences[i]`와 `lengths[i]`를 갱신합니다.

3. **최장 수열 찾기**:
   - `lengths` 리스트에서 가장 큰 값을 가진 인덱스(`max_length_index`)를 찾습니다.
   - `sequences[max_length_index]`가 최종적인 최장 증가 부분 수열이 됩니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
# 결과: [10, 22, 33, 41, 60, 80]
```

## 참고 사항

- 이 코드는 LIS를 찾는 가장 직관적인 동적 계획법 구현 중 하나입니다.
- 더 빠른 $O(N \log N)$ 시간 복잡도를 가진 알고리즘도 존재하며, 이는 이진 탐색을 활용합니다. (`longest_increasing_subsequence_o(nlogn).py` 참고)
