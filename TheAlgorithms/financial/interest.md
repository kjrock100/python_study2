# 이자 계산 (Interest Calculation)

이 문서는 `interest.py` 파일에 구현된 **단리(Simple Interest)** 및 **복리(Compound Interest)** 계산 알고리즘에 대해 설명합니다.

## 개요

금융 분야에서 이자를 계산하는 두 가지 기본적인 방법을 구현합니다.

## 주요 함수

### 1. `simple_interest(principal, daily_interest_rate, days_between_payments)`

- **목적**: 단리 방식으로 이자를 계산합니다.
- **공식**: $I = P \times r \times t$
- **매개변수**:
  - `principal` (float): 원금 ($P$). (0보다 커야 함)
  - `daily_interest_rate` (float): 일일 이자율 ($r$). (0 이상이어야 함)
  - `days_between_payments` (int): 기간(일수) ($t$). (0보다 커야 함)
- **반환값**: 계산된 이자 금액 (float).

### 2. `compound_interest(principal, nominal_annual_interest_rate_percentage, number_of_compounding_periods)`

- **목적**: 복리 방식으로 이자를 계산합니다.
- **공식**: $I = P \times ((1 + r)^n - 1)$
  - 여기서 $r$은 명목 연이율, $n$은 복리 횟수입니다.
- **매개변수**:
  - `principal` (float): 원금 ($P$). (0보다 커야 함)
  - `nominal_annual_interest_rate_percentage` (float): 명목 연이율 ($r$). (예: 5%는 0.05, 0 이상이어야 함)
  - `number_of_compounding_periods` (int): 복리 계산 횟수 ($n$). (0보다 커야 함)
- **반환값**: 계산된 이자 금액 (float).

## 예외 처리

두 함수 모두 입력값이 유효하지 않은 경우(예: 음수 원금, 음수 기간 등) `ValueError`를 발생시킵니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
# 단리 계산: 원금 18000, 이자율 6%, 3일
simple_interest(18000.0, 0.06, 3)
# 결과: 3240.0

# 복리 계산: 원금 10000, 이자율 5%, 3회 복리
compound_interest(10000.0, 0.05, 3)
# 결과: 1576.25...
```
