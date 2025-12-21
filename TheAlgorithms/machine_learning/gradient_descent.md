# 경사 하강법 (Gradient Descent)

이 문서는 `gradient_descent.py` 파일에 구현된 **경사 하강법(Gradient Descent)** 알고리즘에 대해 설명합니다. 이 코드는 선형 가설 함수(Linear Hypothesis Function)의 비용을 최소화하는 파라미터(가중치)를 찾습니다.

## 개요

경사 하강법은 비용 함수의 기울기(Gradient)를 따라 내려가며 최적의 파라미터를 찾는 최적화 알고리즘입니다. 이 예제에서는 다변수 선형 회귀(Linear Regression with multiple variables)를 위한 경사 하강법을 구현합니다.

## 주요 변수

- `train_data`: 학습에 사용되는 데이터셋. `((입력 특징 튜플), 출력값)` 형태의 튜플 리스트입니다.
- `test_data`: 모델 평가에 사용되는 테스트 데이터셋.
- `parameter_vector`: 모델의 파라미터(가중치) 리스트. `[theta_0, theta_1, theta_2, theta_3]` 형태이며, `theta_0`는 편향(Bias) 항입니다.
- `LEARNING_RATE`: 학습률(Alpha). 파라미터 업데이트 보폭을 결정합니다.

## 주요 함수

### `_hypothesis_value(data_input_tuple)`

- **목적**: 주어진 입력에 대한 가설 함수(예측값)를 계산합니다.
- **수식**: $h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots$
- **특징**: 입력 데이터에는 없는 편향(Bias) 항(`parameter_vector[0]`)을 별도로 처리하여 더합니다.

### `get_cost_derivative(index)`

- **목적**: 특정 파라미터(`index`)에 대한 비용 함수의 편미분값(기울기)을 계산합니다.
- **수식**: $\frac{\partial}{\partial \theta_j} J(\theta) = \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}$

### `run_gradient_descent()`

- **목적**: 경사 하강법을 실행하여 최적의 파라미터를 찾습니다.
- **동작**:
  1. 무한 루프(`while True`)를 돌며 파라미터를 업데이트합니다.
  2. 각 파라미터에 대해 기울기(`cost_derivative`)를 계산합니다.
  3. 파라미터 업데이트: $\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)$
  4. **수렴 조건**: `numpy.allclose`를 사용하여 파라미터 변화량이 매우 작아지면(`absolute_error_limit` 이내) 학습을 종료합니다.

### `test_gradient_descent()`

- **목적**: 학습된 파라미터를 사용하여 테스트 데이터에 대한 예측을 수행하고, 실제 값과 비교하여 출력합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 알고리즘을 실행하고 테스트 결과를 출력합니다.

```python
# 실행 결과 예시
# Number of iterations: ...
# Actual output value: 555
# Hypothesis output: ...
```

## 참고 사항
- 이 코드는 학습 데이터가 코드 내에 하드코딩되어 있습니다.
- 편향(Bias) 항 처리를 위해 인덱스 계산에 주의가 필요합니다 (`index - 1` 등).
