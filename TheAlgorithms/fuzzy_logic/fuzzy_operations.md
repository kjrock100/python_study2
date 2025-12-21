# 퍼지 연산 (Fuzzy Operations)

이 문서는 `fuzzy_operations.py` 파일에 구현된 **퍼지 논리 연산** 예제에 대해 설명합니다. 이 스크립트는 `scikit-fuzzy` 라이브러리를 사용하여 두 개의 퍼지 집합을 생성하고 다양한 퍼지 연산을 수행한 후, 그 결과를 시각화합니다.

## 개요

퍼지 논리에서 사용되는 기본적인 집합 연산들을 구현하고 그래프로 보여줍니다.

## 요구 사항

- `scikit-fuzzy`
- `numpy`
- `matplotlib`

## 코드 동작 과정

1. **논의 영역(Universe of Discourse) 생성**:
   - `numpy.linspace`를 사용하여 0부터 75까지의 범위를 생성합니다.

2. **퍼지 집합 정의**:
   - `young`: [0, 25, 50]을 기준으로 하는 삼각형 소속 함수(Triangular Membership Function).
   - `middle_aged`: [25, 50, 75]를 기준으로 하는 삼각형 소속 함수.
   - `skfuzzy.membership.trimf` 함수를 사용합니다.

3. **퍼지 연산 수행**:
   - **합집합 (Union)**: `fuzz.fuzzy_or` (Max 연산)
   - **교집합 (Intersection)**: `fuzz.fuzzy_and` (Min 연산)
   - **여집합 (Complement)**: `fuzz.fuzzy_not` (1 - Membership)
   - **차집합 (Difference)**: $A - B = A \cap B^c$
   - **대수적 합 (Algebraic Sum)**: $A + B - AB$
   - **대수적 곱 (Algebraic Product)**: $A \times B$
   - **유계 합 (Bounded Sum)**: $\min(1, A + B)$
   - **유계 차 (Bounded Difference)**: $\max(0, A - B)$

4. **시각화**:
   - `matplotlib.pyplot`을 사용하여 원본 퍼지 집합과 각 연산의 결과를 서브플롯(Subplot)으로 그려서 보여줍니다.

## 사용법

스크립트를 실행하면 `matplotlib` 창이 열리며 각 연산의 결과 그래프가 표시됩니다.

```bash
python fuzzy_operations.py
```

## 주의 사항
- `scikit-fuzzy` 라이브러리가 설치되어 있지 않으면 `ImportError`가 발생할 수 있으나, 코드 내 `try-except` 블록이 있어 `fuzz`가 `None`이 될 수 있습니다. 이 경우 이후 연산에서 에러가 발생할 것입니다.
