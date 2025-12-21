# 원리금 균등 상환액 계산 (Equated Monthly Installments)

이 문서는 `equated_monthly_installments.py` 파일에 구현된 **원리금 균등 상환액(EMI)** 계산 알고리즘에 대해 설명합니다.

## 개요

원리금 균등 상환 방식은 대출 기간 동안 매월 원금과 이자를 합하여 동일한 금액을 상환하는 방식입니다. 이 코드는 대출 원금, 연이율, 상환 기간(년)을 입력받아 매월 납부해야 할 금액을 계산합니다.

## 공식

매월 상환액 $A$는 다음 공식을 사용하여 계산합니다:

$$A = P \cdot \frac{r(1+r)^n}{(1+r)^n - 1}$$

- $P$: 대출 원금 (Principal)
- $r$: 월 이자율 (연이율 / 12)
- $n$: 총 상환 횟수 (상환 기간(년) $\times$ 12)

## 주요 함수: `equated_monthly_installments`

### `equated_monthly_installments(principal, rate_per_annum, years_to_repay)`

- **목적**: 매월 상환해야 할 원리금 균등 상환액을 계산합니다.
- **매개변수**:
  - `principal` (float): 대출 원금. (0보다 커야 함)
  - `rate_per_annum` (float): 연이율. (예: 12%는 0.12로 입력, 0 이상이어야 함)
  - `years_to_repay` (int): 상환 기간(년). (0보다 큰 정수여야 함)
- **반환값**: 매월 상환액 (float).

### 예외 처리 (Input Validation)

다음과 같은 경우 `Exception`을 발생시킵니다:
1. `principal <= 0`: 원금은 0보다 커야 합니다.
2. `rate_per_annum < 0`: 이자율은 0보다 작을 수 없습니다.
3. `years_to_repay <= 0` 또는 정수가 아닌 경우: 상환 기간은 1 이상의 정수여야 합니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
# 원금 25,000, 연이율 12%, 3년 상환
equated_monthly_installments(25000, 0.12, 3)
# 결과: 830.3577453212793
```
