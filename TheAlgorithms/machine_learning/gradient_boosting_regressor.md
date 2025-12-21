# 그라디언트 부스팅 회귀 (Gradient Boosting Regressor)

이 문서는 `gradient_boosting_regressor.py` 파일에 구현된 **그라디언트 부스팅 회귀(Gradient Boosting Regressor)** 예제에 대해 설명합니다.

## 개요

이 예제는 사이킷런(scikit-learn)의 `GradientBoostingRegressor`를 사용하여 보스턴 주택 가격 데이터셋(Boston Housing Dataset)을 학습하고, 주택 가격을 예측하는 회귀 모델을 구현합니다.

## 주요 라이브러리

- `matplotlib`: 데이터 시각화 (예측 결과 그래프).
- `pandas`: 데이터 프레임 처리.
- `sklearn`: 머신러닝 모델 및 데이터셋, 평가 지표 (`load_boston`, `GradientBoostingRegressor`, `mean_squared_error`, `r2_score`, `train_test_split`).

## 주요 함수: `main`

### `main()`

- **목적**: 데이터 로드, 전처리, 모델 학습, 평가 및 시각화를 수행하는 메인 함수입니다.
- **동작 과정**:
  1. **데이터셋 로드**: `load_boston()`을 사용하여 보스턴 주택 가격 데이터를 불러옵니다.
  2. **데이터 프레임 생성**: 데이터를 `pandas.DataFrame`으로 변환하고 타겟 변수(`Price`)를 추가합니다.
  3. **데이터 탐색**: `head()`와 `describe()`를 사용하여 데이터의 일부와 통계적 요약을 출력합니다.
  4. **데이터 분할**: 전체 데이터를 학습용(Train)과 테스트용(Test)으로 75:25 비율로 나눕니다.
  5. **모델 생성 및 학습**:
     - `GradientBoostingRegressor` 모델을 생성합니다 (트리 개수 500, 최대 깊이 5, 학습률 0.01 등 설정).
     - `fit()` 메서드로 학습 데이터에 대해 모델을 학습시킵니다.
  6. **모델 평가**:
     - 학습 데이터와 테스트 데이터에 대한 점수(`score`)를 출력합니다.
     - 테스트 데이터에 대한 예측값(`y_pred`)을 생성합니다.
     - 평균 제곱 오차(MSE, `mean_squared_error`)와 결정 계수($R^2$, `r2_score`)를 계산하여 출력합니다.
  7. **결과 시각화**:
     - 실제 값(`y_test`)과 예측 값(`y_pred`)을 산점도(Scatter plot)로 그립니다.
     - 완벽한 예측을 나타내는 대각선 점선을 추가하여 모델의 성능을 시각적으로 확인합니다.

## 사용법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다. 실행 시 통계 정보와 평가 점수가 출력되고, 결과 그래프 창이 나타납니다.

```python
# 실행 예시
# (통계 정보 출력)
# Training score of GradientBoosting is : ...
# The test score of GradientBoosting is : ...
# Mean squared error: ...
# Test Variance score: ...
# (그래프 창 열림)
```

## 참고 사항
- `load_boston` 데이터셋은 윤리적인 문제로 인해 scikit-learn 1.2 버전부터 삭제되었습니다. 최신 환경에서는 대안 데이터셋(예: California Housing dataset)을 사용하거나 데이터를 직접 다운로드해야 할 수 있습니다.
