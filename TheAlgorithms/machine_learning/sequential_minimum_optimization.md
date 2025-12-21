# 순차적 최소 최적화 (Sequential Minimal Optimization - SMO)

이 문서는 `sequential_minimum_optimization.py` 파일에 구현된 **순차적 최소 최적화 (SMO)** 알고리즘에 대해 설명합니다.

## 개요

SMO는 서포트 벡터 머신(SVM) 학습 과정에서 발생하는 2차 계획법(Quadratic Programming, QP) 문제를 효율적으로 해결하기 위해 John Platt가 고안한 알고리즘입니다. 큰 QP 문제를 가능한 가장 작은 하위 문제(두 개의 라그랑주 승수 $\alpha$를 최적화하는 문제)로 분해하여 분석적으로 해결합니다.

## 주요 클래스

### `SmoSVM`

- **목적**: SMO 알고리즘을 사용하여 SVM 모델을 학습하고 예측을 수행합니다.
- **주요 매개변수**:
  - `train`: 학습 데이터 (첫 번째 열은 레이블, 나머지는 특징).
  - `kernel_func`: 사용할 커널 함수 객체 (`Kernel` 클래스).
  - `cost`: 슬랙 변수에 대한 비용 상수 ($C$).
  - `tolerance`: KKT 조건 위반 허용 오차.
- **주요 메서드**:
  - `fit()`: SMO 알고리즘을 실행하여 최적의 $\alpha$ 값들을 찾습니다. 두 개의 $\alpha$를 선택하고 업데이트하는 과정을 반복합니다.
  - `predict(test_samples)`: 학습된 모델을 사용하여 테스트 데이터의 클래스를 예측합니다.
  - `_choose_alphas()`: 최적화할 두 개의 $\alpha$ ($i_1, i_2$)를 선택하는 휴리스틱을 구현합니다.
  - `_get_new_alpha()`: 선택된 두 $\alpha$에 대해 제약 조건을 만족하면서 목적 함수를 최소화하는 새로운 값을 계산합니다.

### `Kernel`

- **목적**: SVM에서 데이터를 고차원 공간으로 매핑하기 위한 커널 함수를 제공합니다.
- **지원 커널**:
  - `linear`: 선형 커널 ($u^T v + c_0$)
  - `poly`: 다항 커널 ($(\gamma u^T v + c_0)^d$)
  - `rbf`: 방사 기저 함수 (RBF) 커널 ($\exp(-\gamma ||u-v||^2)$)

## 실행 예제

이 파일은 두 가지 테스트 함수를 포함하고 있습니다.

### 1. `test_cancel_data()`
- **데이터셋**: UCI Machine Learning Repository의 유방암(Breast Cancer) 데이터셋을 다운로드합니다. (코드 내 함수명 및 파일명에 `cancel`로 오타가 있으나 실제로는 Cancer 데이터입니다.)
- **과정**: 데이터를 전처리하고 RBF 커널을 사용하는 SVM을 학습시킨 후 정확도를 출력합니다.

### 2. `test_demonstration()`
- **데이터셋**: `sklearn.datasets`의 `make_blobs`와 `make_circles`를 사용하여 생성한 인공 데이터.
- **시각화**: 선형 커널과 RBF 커널, 그리고 서로 다른 비용($C$) 값에 따른 결정 경계(Decision Boundary)를 시각화하여 보여줍니다.

## 사용법

스크립트를 직접 실행하면 유방암 데이터셋에 대한 학습 결과와 시각화 데모가 실행됩니다.

```bash
python sequential_minimum_optimization.py
```

## 요구 사항
- `numpy`, `pandas`: 데이터 처리 및 행렬 연산.
- `matplotlib`: 결과 시각화.
- `sklearn`: 데이터 생성 및 전처리 (`StandardScaler`).
