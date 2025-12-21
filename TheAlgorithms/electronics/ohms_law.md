# 옴의 법칙 (Ohm's Law)

이 문서는 `ohms_law.py` 파일에 구현된 **옴의 법칙(Ohm's Law)** 계산 알고리즘에 대해 설명합니다.

## 개요

옴의 법칙은 도체의 두 지점 사이의 전압($V$), 흐르는 전류($I$), 그리고 저항($R$) 사이의 관계를 설명하는 법칙입니다.

$$V = I \times R$$

이 코드는 세 가지 값 중 두 가지가 주어졌을 때 나머지 하나를 계산합니다.

## 주요 함수: `ohms_law`

### `ohms_law(voltage, current, resistance)`

- **목적**: 전압, 전류, 저항 중 알 수 없는 하나의 값을 계산합니다.
- **매개변수**:
  - `voltage`: 전압 ($V$).
  - `current`: 전류 ($A$).
  - `resistance`: 저항 ($\Omega$).
  - *주의*: 계산하고자 하는 값은 `0`으로 전달해야 합니다. 입력된 3개의 값 중 정확히 하나만 `0`이어야 합니다.
- **반환값**: `{변수명: 계산된 값}` 형태의 딕셔너리.

### 알고리즘 동작 원리

1. **유효성 검사**:
   - 입력된 세 값 중 `0`인 값이 정확히 하나인지 확인합니다. 그렇지 않으면 `ValueError`를 발생시킵니다.
   - 저항은 음수가 될 수 없으므로, `resistance < 0`인 경우 `ValueError`를 발생시킵니다.

2. **계산**:
   - `voltage`가 0인 경우: $V = I \times R$
   - `current`가 0인 경우: $I = V / R$
   - `resistance`가 0인 경우: $R = V / I$

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
# 전류 계산 (전압 10V, 저항 5Ω)
ohms_law(voltage=10, resistance=5, current=0)
# 결과: {'current': 2.0}

# 전압 계산 (전류 -1.5A, 저항 2Ω)
ohms_law(voltage=0, current=-1.5, resistance=2)
# 결과: {'voltage': -3.0}
```
