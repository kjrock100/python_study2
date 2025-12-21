# K-평균 군집화 (K-Means Clustering)

이 문서는 `k_means_clust.py` 파일에 구현된 **K-평균 군집화** 알고리즘에 대해 설명합니다.

## 개요

K-평균 군집화는 데이터를 $k$개의 군집(Cluster)으로 묶는 비지도 학습 알고리즘입니다. 각 군집은 중심점(Centroid)을 가지며, 데이터 포인트들은 가장 가까운 중심점에 할당됩니다. 이 과정은 중심점이 더 이상 변하지 않거나 지정된 반복 횟수에 도달할 때까지 반복됩니다.

## 주요 함수

### `get_initial_centroids(data, k, seed=None)`
- **목적**: 데이터셋에서 무작위로 $k$개의 포인트를 선택하여 초기 중심점으로 설정합니다.
- **매개변수**:
  - `data`: 입력 데이터 (2D numpy 배열).
  - `k`: 군집의 개수.
  - `seed`: 난수 생성을 위한 시드값 (재현성 보장).

### `assign_clusters(data, centroids)`
- **목적**: 각 데이터 포인트에 대해 가장 가까운 중심점을 찾아 군집을 할당합니다.
- **동작**: 유클리드 거리를 사용하여 각 데이터와 모든 중심점 간의 거리를 계산하고, 최소 거리를 가진 중심점의 인덱스를 반환합니다.

### `revise_centroids(data, k, cluster_assignment)`
- **목적**: 각 군집에 할당된 데이터 포인트들의 평균(Mean)을 계산하여 새로운 중심점을 구합니다.

### `compute_heterogeneity(data, k, centroids, cluster_assignment)`
- **목적**: 군집화의 품질을 평가하기 위해 이질성(Heterogeneity, 또는 관성/Inertia)을 계산합니다.
- **수식**: 각 데이터 포인트와 할당된 중심점 사이의 거리의 제곱합입니다. 값이 작을수록 군집화가 잘 된 것입니다.

### `kmeans(data, k, initial_centroids, maxiter=500, ...)`
- **목적**: K-평균 알고리즘의 메인 루프를 실행합니다.
- **알고리즘 동작**:
  1. 초기 중심점으로 시작합니다.
  2. `maxiter`만큼 또는 수렴할 때까지 다음을 반복합니다:
     - **할당 단계**: `assign_clusters`를 호출하여 데이터 포인트를 군집에 할당합니다.
     - **업데이트 단계**: `revise_centroids`를 호출하여 중심점을 갱신합니다.
     - **수렴 확인**: 군집 할당이 이전 반복과 동일하면 종료합니다.
     - (옵션) 이질성 값을 기록하거나 진행 상황을 출력합니다.

### `ReportGenerator(df, ClusteringVariables, FillMissingReport=None)`
- **목적**: 군집화 결과를 분석하기 위한 보고서(DataFrame)를 생성합니다.
- **기능**: 각 군집별로 변수들의 평균, 표준편차, 분위수(Quantile) 등 다양한 통계량을 계산하여 엑셀 형식 등으로 내보내기 좋은 형태로 정리합니다.

## 사용법

코드 내의 `if False:` 블록을 `if True:`로 변경하거나 별도의 스크립트에서 다음과 같이 실행할 수 있습니다.

```python
from sklearn import datasets
import numpy as np
from k_means_clust import get_initial_centroids, kmeans, plot_heterogeneity

# 데이터 로드
dataset = datasets.load_iris()
data = dataset["data"]
k = 3

# 초기화 및 실행
initial_centroids = get_initial_centroids(data, k, seed=0)
centroids, cluster_assignment = kmeans(
    data, k, initial_centroids, verbose=True
)
```

## 요구 사항
- `numpy`, `pandas`, `matplotlib`, `sklearn` 라이브러리가 필요합니다.
