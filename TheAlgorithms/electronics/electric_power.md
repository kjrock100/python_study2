# 전력 (Electric Power)

이 문서는 `electric_power.py` 파일에 구현된 **전력(Electric Power)** 계산 알고리즘에 대해 설명합니다.

## 개요

전력($P$), 전압($V$), 전류($I$) 사이의 관계는 다음과 같습니다:

$$P = V \times I$$

이 코드는 세 가지 값 중 두 가지가 주어졌을 때 나머지 하나를 계산합니다.

## 주요 함수: `electric_power`

### `electric_power(voltage, current, power)`

- **목적**: 전압, 전류, 전력 중 알 수 없는 하나의 값을 계산합니다.
- **매개변수**:
  - `voltage`: 전압 ($V$).
  - `current`: 전류 ($A$).
  - `power`: 전력 ($W$).
  - *주의*: 계산하고자 하는 값은 `0`으로 전달해야 합니다. 입력된 3개의 값 중 정확히 하나만 `0`이어야 합니다.
- **반환값**: `result(name, value)` 형태의 `namedtuple`.

### 알고리즘 동작 원리

1. **유효성 검사**:
   - 입력된 세 값 중 `0`인 값이 정확히 하나인지 확인합니다. 그렇지 않으면 `ValueError`를 발생시킵니다.
   - 전력은 음수가 될 수 없으므로, `power < 0`인 경우 `ValueError`를 발생시킵니다.

2. **계산**:
   - `voltage`가 0인 경우: $V = P / I$
   - `current`가 0인 경우: $I = P / V$
   - `power`가 0인 경우: $P = |V \times I|$ (절댓값 사용, 소수점 둘째 자리까지 반올림)

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
# 전압 계산 (전류 2A, 전력 5W)
electric_power(voltage=0, current=2, power=5)
# 결과: result(name='voltage', value=2.5)

# 전력 계산 (전압 2V, 전류 2A)
electric_power(voltage=2, current=2, power=0)
# 결과: result(name='power', value=4.0)
```
