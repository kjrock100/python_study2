# 가우시안 나이브 베이즈 분류기 (Gaussian Naive Bayes Classifier)

이 문서는 `gaussian_naive_bayes.py` 파일에 구현된 **가우시안 나이브 베이즈(Gaussian Naive Bayes)** 분류 알고리즘 예제에 대해 설명합니다.

## 개요

나이브 베이즈 분류기는 베이즈 정리(Bayes' theorem)를 적용한 확률적 분류 알고리즘입니다. 특징(Feature)들이 서로 독립적이라는 '나이브(Naive)'한 가정을 바탕으로 합니다. 가우시안 나이브 베이즈는 특징들이 정규 분포(Gaussian Distribution)를 따른다고 가정할 때 사용됩니다.

이 예제에서는 `scikit-learn` 라이브러리를 사용하여 붓꽃(Iris) 데이터셋을 분류하는 모델을 학습시키고, 그 결과를 시각화합니다.

## 주요 라이브러리

- `sklearn`: 머신러닝 알고리즘 및 데이터셋 로드 (`GaussianNB`, `load_iris`, `train_test_split`, `plot_confusion_matrix`).
- `matplotlib`: 결과 시각화 (혼동 행렬 출력).

## 주요 함수: `main`

### `main()`

- **목적**: 가우시안 나이브 베이즈 모델을 학습시키고 성능을 평가하는 전체 과정을 실행합니다.
- **동작 과정**:
  1. **데이터셋 로드**: `load_iris()`를 사용하여 붓꽃 데이터셋을 불러옵니다.
  2. **데이터 분할**: `train_test_split`을 사용하여 전체 데이터를 학습용(Train)과 테스트용(Test)으로 나눕니다. (테스트 비율: 30%)
  3. **모델 학습**:
     - `GaussianNB` 객체를 생성합니다.
     - `fit()` 메서드를 사용하여 학습 데이터(`x_train`, `y_train`)로 모델을 학습시킵니다.
  4. **결과 시각화**:
     - `plot_confusion_matrix`를 사용하여 테스트 데이터(`x_test`, `y_test`)에 대한 예측 결과를 혼동 행렬(Confusion Matrix)로 시각화합니다.
     - 정규화된(Normalized) 혼동 행렬을 파란색 계열(`cmap="Blues"`)로 출력합니다.

## 사용법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다. 실행 시 혼동 행렬 그래프가 팝업 창으로 나타납니다.

```python
# 실행 예시
# (그래프 창이 열림)
```

## 참고 사항
- `plot_confusion_matrix`는 최신 scikit-learn 버전에서 `ConfusionMatrixDisplay.from_estimator`로 대체되었습니다.
