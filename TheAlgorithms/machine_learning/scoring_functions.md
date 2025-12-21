# 평가 함수 (Scoring Functions)

이 문서는 `scoring_functions.py` 파일에 구현된 다양한 **평가 함수(Scoring Functions)**에 대해 설명합니다. 이 함수들은 예측값과 실제값 사이의 차이를 계산하여 머신러닝 모델의 성능을 평가하는 데 사용됩니다.

## 개요

회귀(Regression) 모델의 성능을 측정하기 위해 주로 사용되는 지표들(MAE, MSE, RMSE, RMSLE, MBD)과 분류(Classification) 모델의 정확도를 측정하는 함수가 포함되어 있습니다.

## 주요 함수

### 1. 평균 절대 오차 (MAE - Mean Absolute Error)
`mae(predict, actual)`

- **설명**: 예측값과 실제값의 차이(오차)의 절댓값 평균입니다.
- **특징**: 오차의 크기를 그대로 반영하며, 이상치(Outlier)에 덜 민감합니다.
- **수식**: $\frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$

### 2. 평균 제곱 오차 (MSE - Mean Squared Error)
`mse(predict, actual)`

- **설명**: 예측값과 실제값의 차이를 제곱하여 평균을 낸 값입니다.
- **특징**: 오차를 제곱하므로 큰 오차에 대해 더 큰 페널티를 부여합니다.
- **수식**: $\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

### 3. 평균 제곱근 오차 (RMSE - Root Mean Squared Error)
`rmse(predict, actual)`

- **설명**: MSE에 제곱근(Root)을 씌운 값입니다.
- **특징**: 실제 값과 동일한 단위를 가지므로 해석하기 쉽습니다.
- **수식**: $\sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$

### 4. 평균 제곱근 로그 오차 (RMSLE - Root Mean Square Logarithmic Error)
`rmsle(predict, actual)`

- **설명**: 예측값과 실제값에 1을 더한 후 로그를 취하여 RMSE를 계산합니다.
- **특징**:
  - 값의 스케일이 클 때 유용합니다.
  - 과소 예측(Under-prediction)에 대해 과대 예측(Over-prediction)보다 더 큰 페널티를 부여합니다.
- **수식**: $\sqrt{\frac{1}{n} \sum_{i=1}^{n} (\log(p_i + 1) - \log(a_i + 1))^2}$

### 5. 평균 편향 편차 (MBD - Mean Bias Deviation)
`mbd(predict, actual)`

- **설명**: 모델이 실제값보다 과대평가하는지 과소평가하는지를 나타내는 지표입니다.
- **특징**:
  - 양수(+): 과대 예측 (Over-prediction)
  - 음수(-): 과소 예측 (Under-prediction)
- **수식**: $\frac{\sum (p_i - a_i) / n}{\sum a_i / n} \times 100$

### 6. 정확도 (Manual Accuracy)
`manual_accuracy(predict, actual)`

- **설명**: 예측값과 실제값이 정확히 일치하는 비율을 계산합니다.
- **특징**: 주로 분류 문제에서 사용됩니다.

## 요구 사항
- `numpy`: 배열 연산 및 수학 함수(`mean`, `square`, `sqrt`, `log` 등) 사용.

## 사용 예시

```python
actual = [1, 2, 3]
predict = [1, 4, 3]
print(mae(predict, actual)) # 출력: 0.666...
```
