# 선형 판별 분석 (Linear Discriminant Analysis)

이 문서는 `linear_discriminant_analysis.py` 파일에 구현된 **선형 판별 분석 (LDA)** 알고리즘에 대해 설명합니다.

## 개요

선형 판별 분석은 데이터를 클래스별로 가장 잘 구분할 수 있는 축을 찾아 차원을 축소하거나 분류하는 기법입니다. 이 코드는 1차원 입력 변수에 대한 LDA 분류기를 처음부터 구현합니다.

### 데이터에 대한 가정
1. 입력 변수는 가우시안(정규) 분포를 따릅니다.
2. 각 클래스의 입력 변수에 대한 분산은 동일합니다.
3. 학습 데이터의 클래스 비율은 실제 문제를 대표합니다.

## 주요 함수

### 데이터 생성
- **`gaussian_distribution(mean, std_dev, instance_count)`**: 주어진 평균과 표준편차를 따르는 가우시안 분포 데이터를 생성합니다.
- **`y_generator(class_count, instance_count)`**: 각 데이터에 해당하는 클래스 레이블(0, 1, 2...)을 생성합니다.

### 모델 학습 (통계량 계산)
LDA 모델 학습은 학습 데이터로부터 통계량을 추정하는 과정입니다.
- **`calculate_mean(instance_count, items)`**: 각 클래스별 평균($\mu$)을 계산합니다.
- **`calculate_probabilities(instance_count, total_count)`**: 각 클래스에 속할 확률($P(y=k)$)을 계산합니다.
- **`calculate_variance(items, means, total_count)`**: 모든 클래스에 공통으로 적용되는 분산($\sigma^2$)을 계산합니다. (합동 분산, Pooled Variance)

### 예측
- **`predict_y_values(x_items, means, variance, probabilities)`**: 판별 함수(Discriminant Function)를 사용하여 새로운 데이터의 클래스를 예측합니다.
  - 판별 함수 수식: $D_k(x) = x \cdot \frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \ln(P(y=k))$
  - 가장 큰 판별 값을 가진 클래스로 분류합니다.

### 평가
- **`accuracy(actual_y, predicted_y)`**: 실제 레이블과 예측 레이블을 비교하여 정확도를 계산합니다.

## 실행 방법 (`main` 함수)

이 스크립트는 대화형 콘솔 프로그램으로 실행됩니다.

1. **클래스 수 입력**: 생성할 데이터 그룹의 개수를 입력합니다.
2. **표준편차 입력**: 모든 클래스에 공통으로 적용될 표준편차를 입력합니다.
3. **인스턴스 수 및 평균 입력**: 각 클래스별 데이터 개수와 평균값을 입력합니다.
4. **결과 출력**:
   - 생성된 데이터 분포 및 레이블
   - 계산된 실제 평균, 확률, 분산
   - 예측 결과 및 정확도

```python
# 실행 예시 (콘솔 입력)
# Enter the number of classes (Data Groupings): 2
# Enter the value of standard deviation...: 1.0
# Enter The number of instances for class_1: 10
# ...
```

## 참고 사항
- 이 구현은 1차원 데이터에 특화되어 있으며, 다차원 데이터에 대한 LDA(행렬 연산 포함)와는 계산 방식이 단순화되어 있습니다.
```

<!--
[PROMPT_SUGGESTION]이 코드에서 1차원 데이터뿐만 아니라 다차원 데이터를 처리할 수 있도록 LDA 알고리즘을 확장해줘[/PROMPT_SUGGESTION]
[PROMPT_SUGGESTION]사이킷런(scikit-learn)의 `LinearDiscriminantAnalysis`를 사용하여 동일한 작업을 수행하는 코드를 작성해줘[/PROMPT_SUGGESTION]
