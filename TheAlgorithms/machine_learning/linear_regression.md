# 선형 회귀 (Linear Regression)

이 문서는 `linear_regression.py` 파일에 구현된 **선형 회귀(Linear Regression)** 알고리즘에 대해 설명합니다.

## 개요

선형 회귀는 종속 변수(y)와 하나 이상의 독립 변수(x) 간의 관계를 모델링하는 가장 기본적인 회귀 분석 기법입니다. 이 코드는 **경사 하강법(Gradient Descent)**을 사용하여 데이터셋에 가장 잘 맞는 직선(최적의 파라미터 $\theta$)을 찾습니다.

이 예제에서는 CS:GO 게임의 플레이어 데이터(ADR vs Rating)를 사용하여, ADR(라운드당 평균 데미지)을 통해 Rating(평점)을 예측하는 모델을 학습합니다.

## 주요 함수

### `collect_dataset()`
- **목적**: GitHub에 호스팅된 CSV 파일에서 CS:GO 데이터셋을 다운로드하고 파싱합니다.
- **반환값**: 데이터를 담고 있는 numpy 행렬.

### `run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)`
- **목적**: 경사 하강법의 한 단계를 수행하여 파라미터 $\theta$를 업데이트합니다.
- **수식**: $\theta := \theta - \alpha \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) x^{(i)}$
- **매개변수**:
  - `alpha`: 학습률 (Learning Rate).
  - `theta`: 현재 파라미터 벡터 (가중치).

### `sum_of_square_error(data_x, data_y, len_data, theta)`
- **목적**: 현재 파라미터 $\theta$에 대한 비용(오차)을 계산합니다.
- **수식**: 평균 제곱 오차 (MSE) 기반의 비용 함수 $J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$

### `run_linear_regression(data_x, data_y)`
- **목적**: 지정된 반복 횟수(`iterations`)만큼 경사 하강법을 반복하여 모델을 학습시킵니다.
- **설정**:
  - `iterations`: 100,000회
  - `alpha`: 0.0001550
- **출력**: 매 반복마다 오차를 출력하여 학습 진행 상황을 보여줍니다.

## 실행 과정 (`main` 함수)

1. **데이터 수집**: `collect_dataset()`을 호출하여 데이터를 가져옵니다.
2. **데이터 전처리**:
   - 입력 데이터(`data_x`)에 편향(Bias) 항을 위한 1로 채워진 열을 추가합니다.
   - 타겟 데이터(`data_y`)를 분리합니다.
3. **모델 학습**: `run_linear_regression()`을 호출하여 최적의 $\theta$를 찾습니다.
4. **결과 출력**: 학습된 최종 파라미터 벡터(가중치)를 출력합니다.

## 사용법

이 스크립트는 `requests` 라이브러리를 사용하여 데이터를 다운로드하므로, 인터넷 연결이 필요하며 해당 라이브러리가 설치되어 있어야 합니다.

```bash
pip install requests numpy
```

스크립트 실행:
```python
# 실행 결과 예시
# At Iteration 1 - Error is ...
# ...
# Resultant Feature vector :
# 0.xxx
# 0.xxx
```
