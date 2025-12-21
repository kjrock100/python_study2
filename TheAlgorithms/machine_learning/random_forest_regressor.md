# 랜덤 포레스트 회귀 (Random Forest Regressor)

이 문서는 `random_forest_regressor.py` 파일에 구현된 **랜덤 포레스트 회귀(Random Forest Regressor)** 예제에 대해 설명합니다.

## 개요

랜덤 포레스트는 여러 개의 결정 트리(Decision Tree)를 결합하여 예측의 정확도를 높이는 앙상블(Ensemble) 기법입니다. 회귀(Regression) 문제에서는 각 트리의 예측값들의 평균을 최종 예측값으로 사용합니다.

이 예제는 `scikit-learn` 라이브러리를 사용하여 보스턴 주택 가격 데이터셋(Boston Housing Dataset)을 학습하고, 주택 가격을 예측하는 회귀 모델을 구현합니다.

## 주요 라이브러리

- `sklearn.datasets`: 예제 데이터셋(`load_boston`)을 불러옵니다.
- `sklearn.ensemble`: 랜덤 포레스트 회귀 모델(`RandomForestRegressor`)을 제공합니다.
- `sklearn.model_selection`: 데이터를 학습용과 테스트용으로 분할하는 `train_test_split` 함수를 제공합니다.
- `sklearn.metrics`: 모델 성능 평가를 위한 지표(`mean_absolute_error`, `mean_squared_error`)를 제공합니다.

## 주요 함수: `main`

### `main()`

- **목적**: 데이터 로드, 모델 학습, 예측 및 평가의 전체 과정을 수행합니다.
- **동작 과정**:
  1. **데이터셋 로드**: `load_boston()` 함수를 사용하여 보스턴 주택 가격 데이터를 불러옵니다.
  2. **데이터 분할**: 불러온 데이터를 학습 데이터(70%)와 테스트 데이터(30%)로 분할합니다.
  3. **모델 생성 및 학습**:
     - 300개의 결정 트리로 구성된 `RandomForestRegressor` 모델을 생성합니다.
     - `fit()` 메서드를 사용하여 학습 데이터로 모델을 학습시킵니다.
  4. **예측**: 학습된 모델을 사용하여 테스트 데이터의 주택 가격을 예측합니다.
  5. **성능 평가**:
     - 예측값과 실제값의 차이를 평가하기 위해 **평균 절대 오차(Mean Absolute Error, MAE)**와 **평균 제곱 오차(Mean Squared Error, MSE)**를 계산하여 출력합니다.

## 사용법

스크립트를 직접 실행하면 모델의 예측 성능 지표가 콘솔에 출력됩니다.

```python
# 실행 결과 예시
# dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
# Mean Absolute Error:  2.13...
# Mean Square Error  :  9.37...
```

## 참고 사항
- `load_boston` 데이터셋은 scikit-learn 1.2 버전부터 윤리적인 문제로 인해 삭제되었습니다. 최신 버전의 라이브러리를 사용하는 경우, `fetch_california_housing`과 같은 다른 데이터셋으로 대체하여 코드를 실행해야 할 수 있습니다.
