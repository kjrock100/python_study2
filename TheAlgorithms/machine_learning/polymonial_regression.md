# 다항 회귀 (Polynomial Regression)

이 문서는 `polymonial_regression.py` 파일에 구현된 **다항 회귀(Polynomial Regression)** 예제에 대해 설명합니다.

## 개요

다항 회귀는 독립 변수(X)와 종속 변수(y) 간의 관계를 $n$차 다항식으로 모델링하는 회귀 분석 기법입니다. 데이터가 비선형적인 패턴을 보일 때 유용합니다. 이 예제에서는 직급(Position level)에 따른 연봉(Salary) 데이터를 사용하여, 직급이 높아질수록 급격히 상승하는 연봉을 예측하는 모델을 만듭니다.

## 주요 라이브러리

- `pandas`: 데이터셋 로드 및 처리.
- `matplotlib`: 데이터 및 회귀선 시각화.
- `sklearn`:
  - `LinearRegression`: 선형 회귀 모델.
  - `PolynomialFeatures`: 다항 특징 생성 (예: $x, x^2, x^3, ...$).
  - `train_test_split`: 데이터 분할 (이 코드에서는 선언만 되고 실제 학습에는 전체 데이터를 사용함).

## 실행 과정

1.  **데이터 로드**: `pandas.read_csv`를 사용하여 웹에 있는 `position_salaries.csv` 파일을 불러옵니다.
    - `X`: 직급 레벨 (Position level)
    - `y`: 연봉 (Salary)
2.  **데이터 분할**: `train_test_split`을 호출하여 훈련/테스트 세트를 나누지만, 이 예제에서는 시각화를 위해 전체 데이터 `X`와 `y`를 사용하여 모델을 학습시킵니다.
3.  **다항 특징 변환**:
    - `PolynomialFeatures(degree=4)`를 사용하여 입력 데이터 `X`를 4차 다항식 특징(`X_poly`)으로 변환합니다.
    - 1차원 데이터 $x$가 $[1, x, x^2, x^3, x^4]$ 형태의 특징 벡터로 확장됩니다.
4.  **모델 학습**: 변환된 데이터 `X_poly`와 타겟 `y`를 사용하여 선형 회귀 모델(`pol_reg`)을 학습시킵니다.
5.  **시각화 (`viz_polymonial`)**:
    - 실제 데이터 포인트를 빨간색 점으로 표시합니다.
    - 학습된 다항 회귀 모델의 예측 곡선을 파란색 선으로 그립니다.
6.  **예측**:
    - 직급 레벨 `5.5`에 대한 연봉을 예측합니다.

## 사용법

스크립트를 실행하면 결과 그래프가 나타나고, 코드 내부적으로 5.5 레벨에 대한 예측을 수행합니다.

```python
if __name__ == "__main__":
    viz_polymonial()
    
    # 새로운 결과 예측 (예: 레벨 5.5)
    # pol_reg.predict(poly_reg.fit_transform([[5.5]]))
    # 예상 출력값: 약 132148.43
```

## 참고 사항
- 파일명에 오타가 있습니다 (`polymonial` -> `polynomial`).
- 데이터셋이 작기 때문에 전체 데이터를 사용하여 학습하고 시각화하는 방식으로 구현되어 있습니다.
