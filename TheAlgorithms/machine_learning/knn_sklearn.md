# K-최근접 이웃 (Scikit-learn)

이 문서는 `knn_sklearn.py` 파일에 구현된 **Scikit-learn 라이브러리**를 이용한 K-최근접 이웃(KNN) 분류기 예제에 대해 설명합니다.

## 개요

이 코드는 머신러닝 라이브러리인 `scikit-learn`을 사용하여 KNN 알고리즘을 간단하게 구현하는 방법을 보여줍니다. 붓꽃(Iris) 데이터셋을 사용하여 모델을 학습시키고, 새로운 데이터 포인트의 클래스를 예측합니다.

## 주요 라이브러리

- **`sklearn.datasets`**: `load_iris` 함수를 통해 예제 데이터셋을 불러옵니다.
- **`sklearn.model_selection`**: `train_test_split` 함수로 데이터를 학습용과 테스트용으로 분할합니다.
- **`sklearn.neighbors`**: `KNeighborsClassifier` 클래스를 사용하여 KNN 모델을 생성합니다.

## 알고리즘 실행 과정

1.  **데이터 로드**: `load_iris()` 함수로 붓꽃 데이터셋을 불러옵니다.

2.  **데이터 분할**: 데이터를 학습(train) 데이터와 테스트(test) 데이터로 나눕니다.

3.  **모델 생성 및 학습**:
    -   `KNeighborsClassifier` 객체를 생성합니다. 이 예제에서는 가장 가까운 이웃 1개(`n_neighbors=1`)만 보도록 설정합니다.
    -   `fit()` 메서드를 사용하여 학습 데이터(`X_train`, `y_train`)로 모델을 학습시킵니다.

4.  **예측**:
    -   분류할 새로운 데이터 포인트 `X_new`를 정의합니다.
    -   학습된 모델의 `predict()` 메서드를 사용하여 `X_new`의 클래스를 예측합니다.

5.  **결과 출력**: 예측된 클래스에 해당하는 붓꽃의 이름을 출력합니다.

## 사용법

스크립트를 직접 실행하면, `X_new`에 대한 예측 결과가 출력됩니다.

```python
# 실행 결과 예시
# New array:
#  [[1, 2, 1, 4], [2, 3, 4, 5]]
#
# Target Names Prediction:
#  ['setosa' 'virginica']
```
