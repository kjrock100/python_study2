# 랜덤 포레스트 분류기 (Random Forest Classifier)

이 문서는 `random_forest_classifier.py` 파일에 구현된 **랜덤 포레스트(Random Forest)** 분류 알고리즘 예제에 대해 설명합니다.

## 개요

랜덤 포레스트는 여러 개의 결정 트리(Decision Tree)를 학습시키고 그 결과들을 종합하여 예측 성능을 높이는 앙상블(Ensemble) 학습 방법입니다. 이 예제에서는 `scikit-learn` 라이브러리를 사용하여 붓꽃(Iris) 데이터셋을 분류하는 모델을 학습시키고, 혼동 행렬(Confusion Matrix)을 통해 성능을 시각화합니다.

## 주요 라이브러리

- `matplotlib`: 결과 시각화 (혼동 행렬 그래프).
- `sklearn`:
  - `datasets`: 붓꽃 데이터셋 로드 (`load_iris`).
  - `ensemble`: 랜덤 포레스트 분류기 (`RandomForestClassifier`).
  - `metrics`: 모델 평가 및 시각화 (`plot_confusion_matrix`).
  - `model_selection`: 학습/테스트 데이터 분할 (`train_test_split`).

## 주요 함수: `main`

### `main()`

- **목적**: 데이터 로드, 전처리, 모델 학습 및 결과 시각화를 수행하는 메인 함수입니다.
- **동작 과정**:
  1. **데이터셋 로드**: `load_iris()`를 사용하여 붓꽃 데이터셋을 불러옵니다.
  2. **데이터 분할**: `train_test_split`을 사용하여 전체 데이터를 학습용(Train)과 테스트용(Test)으로 나눕니다. (테스트 비율: 30%)
  3. **모델 생성 및 학습**:
     - `RandomForestClassifier` 객체를 생성합니다. (트리 개수 `n_estimators=100`, 난수 시드 `random_state=42`)
     - `fit()` 메서드를 사용하여 학습 데이터(`x_train`, `y_train`)로 모델을 학습시킵니다.
  4. **결과 시각화**:
     - `plot_confusion_matrix`를 사용하여 테스트 데이터(`x_test`, `y_test`)에 대한 예측 결과를 혼동 행렬로 시각화합니다.
     - `normalize="true"` 옵션을 사용하여 각 클래스별 정답 비율을 표시합니다.
     - `plt.show()`로 그래프 창을 띄웁니다.

## 사용법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다. 실행 시 혼동 행렬 그래프가 팝업 창으로 나타납니다.

```python
# 실행 예시
# (그래프 창이 열림)
```

## 참고 사항
- `plot_confusion_matrix`는 최신 scikit-learn 버전(1.2 이상)에서 deprecated 되었으며, `ConfusionMatrixDisplay.from_estimator` 사용이 권장됩니다.
