# 막대 자르기 (Rod Cutting)

이 문서는 `rod_cutting.py` 파일에 구현된 **막대 자르기(Rod Cutting)** 문제 해결 알고리즘에 대해 설명합니다. 이 문제는 주어진 길이 `n`의 막대와 각 길이별 가격표가 있을 때, 막대를 여러 조각으로 잘라 팔아 얻을 수 있는 최대 수익을 찾는 고전적인 동적 계획법(Dynamic Programming) 문제입니다.

## 개요

이 파일은 막대 자르기 문제를 해결하기 위한 세 가지 다른 접근 방식을 제공합니다:
1. **단순 재귀 (Naive Recursion)**: 지수 시간 복잡도를 가집니다.
2. **하향식 동적 계획법 (Top-Down DP)**: 메모이제이션(Memoization)을 사용합니다.
3. **상향식 동적 계획법 (Bottom-Up DP)**: 타뷸레이션(Tabulation)을 사용합니다.

## 주요 함수 설명

### `naive_cut_rod_recursive(n, prices)`
- **방식**: 단순 재귀.
- **동작**: 길이 `n`의 막대를 1부터 `n`까지 모든 가능한 첫 번째 조각 `i`로 잘라보고, 나머지 부분(`n-i`)에 대해 재귀적으로 최대 수익을 구한 뒤, `prices[i-1]`을 더한 값들 중 최댓값을 찾습니다.
- **문제점**: 동일한 하위 문제(subproblem)를 여러 번 반복해서 계산하므로 시간 복잡도가 $O(2^n)$으로 매우 비효율적입니다.

### `top_down_cut_rod(n, prices)`
- **방식**: 하향식 동적 계획법 (재귀 + 메모이제이션).
- **동작**:
  - `_top_down_cut_rod_recursive` 헬퍼 함수를 사용합니다.
  - `max_rev` 배열(메모)을 만들어 이미 계산된 하위 문제의 결과를 저장합니다.
  - 재귀 호출 시, `max_rev`에 값이 이미 존재하면 계산 없이 바로 반환합니다.
  - 값이 없으면 계산 후 `max_rev`에 저장합니다.
- **성능**: 각 하위 문제는 한 번만 계산되므로 시간 복잡도는 $O(n^2)$입니다.

### `bottom_up_cut_rod(n, prices)`
- **방식**: 상향식 동적 계획법 (반복문, Tabulation).
- **동작**:
  - `max_rev` 배열(DP 테이블)을 생성하고 `max_rev[0]`을 0으로 초기화합니다.
  - 길이가 1인 막대부터 `n`인 막대까지 순서대로 최대 수익을 계산하여 테이블에 채워나갑니다.
  - 길이 `i`의 최대 수익을 구하기 위해, 이전에 계산된 더 작은 길이들의 최대 수익 값을 활용합니다.
  - **점화식**: `max_rev[i] = max(prices[j-1] + max_rev[i-j])` for `j` in `1..i`
- **성능**: 이중 반복문을 사용하므로 시간 복잡도는 $O(n^2)$입니다.

### `_enforce_args(n, prices)`
- **목적**: 입력 인자의 유효성을 검사합니다.
- **검사 항목**:
  - `n`이 음수인지 여부.
  - `n`이 `prices` 리스트의 길이보다 큰지 여부.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

1. 가격표 `prices`와 막대 길이 `n`을 정의합니다.
2. 세 가지 함수(`naive_cut_rod_recursive`, `top_down_cut_rod`, `bottom_up_cut_rod`)를 모두 호출합니다.
3. 각 함수의 결과가 예상된 최대 수익과 일치하는지, 그리고 세 함수의 결과가 서로 동일한지 `assert`를 통해 검증합니다.

```python
prices = [6, 10, 12, 15, 20, 23]
n = len(prices)
# 예상 최대 수익: 36 (길이 1짜리 6개로 자를 때)

max_rev_top_down = top_down_cut_rod(n, prices)
max_rev_bottom_up = bottom_up_cut_rod(n, prices)
max_rev_naive = naive_cut_rod_recursive(n, prices)
```
