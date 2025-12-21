# 전하 캐리어 농도 (Carrier Concentration)

이 문서는 `carrier_concentration.py` 파일에 구현된 반도체의 **전하 캐리어 농도** 계산 알고리즘에 대해 설명합니다.

## 개요

반도체 물리학에서 전자 농도($n$), 정공 농도($p$), 그리고 진성 캐리어 농도($n_i$) 사이에는 질량 작용의 법칙(Mass Action Law)이 성립합니다.

$$n \cdot p = n_i^2$$

이 코드는 이 공식을 사용하여 세 가지 값 중 두 가지가 주어졌을 때 나머지 하나를 계산합니다.

## 주요 함수: `carrier_concentration`

### `carrier_concentration(electron_conc, hole_conc, intrinsic_conc)`

- **목적**: 전자 농도, 정공 농도, 진성 농도 중 알 수 없는 하나의 값을 계산합니다.
- **매개변수**:
  - `electron_conc`: 전자 농도 ($n$).
  - `hole_conc`: 정공 농도 ($p$).
  - `intrinsic_conc`: 진성 캐리어 농도 ($n_i$).
  - *주의*: 계산하고자 하는 값은 `0`으로 전달해야 합니다. 입력된 3개의 값 중 정확히 하나만 `0`이어야 합니다.
- **반환값**: `(변수명, 계산된 값)` 형태의 튜플.

### 알고리즘 동작 원리

1. **유효성 검사**:
   - 입력된 세 값 중 `0`인 값이 정확히 하나인지 확인합니다. 그렇지 않으면 `ValueError`를 발생시킵니다.
   - 모든 농도 값은 음수가 될 수 없으므로, 음수 입력 시 `ValueError`를 발생시킵니다.

2. **계산**:
   - `electron_conc`가 0인 경우: $n = n_i^2 / p$
   - `hole_conc`가 0인 경우: $p = n_i^2 / n$
   - `intrinsic_conc`가 0인 경우: $n_i = \sqrt{n \cdot p}$

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
# 진성 농도 계산 (전자 농도 25, 정공 농도 100)
carrier_concentration(25, 100, 0)
# 결과: ('intrinsic_conc', 50.0)

# 전자 농도 계산 (정공 농도 1600, 진성 농도 200)
carrier_concentration(0, 1600, 200)
# 결과: ('electron_conc', 25.0)
```
