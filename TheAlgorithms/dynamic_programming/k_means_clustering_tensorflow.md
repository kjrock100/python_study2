# 텐서플로우를 이용한 K-평균 클러스터링 (K-Means Clustering using TensorFlow)

이 문서는 `k_means_clustering_tensorflow.py` 파일에 구현된 **K-평균 클러스터링** 알고리즘에 대해 설명합니다. 이 코드는 TensorFlow 프레임워크(버전 1.x 스타일)를 사용하여 클러스터링을 수행합니다.

## 개요

K-평균 클러스터링은 주어진 데이터를 $k$개의 클러스터로 묶는 비지도 학습 알고리즘입니다. 각 클러스터는 중심점(Centroid)을 가지며, 각 데이터 포인트는 가장 가까운 중심점에 할당됩니다.

## 주요 함수: `TFKMeansCluster`

### `TFKMeansCluster(vectors, noofclusters)`
- **목적**: 입력 벡터들을 주어진 개수의 클러스터로 그룹화합니다.
- **매개변수**:
  - `vectors`: $n \times k$ 차원의 2D NumPy 배열 (n은 벡터의 수, k는 차원).
  - `noofclusters`: 생성할 클러스터의 개수 (정수).
- **반환값**:
  - `centroids`: 최종 계산된 클러스터의 중심점들.
  - `assignments`: 각 벡터가 할당된 클러스터 인덱스 리스트.

### 알고리즘 동작 원리

이 코드는 TensorFlow의 계산 그래프(Computational Graph)를 생성하고 세션(Session)을 통해 실행하는 방식을 따릅니다.

1. **초기화**:
   - 입력된 벡터들 중 무작위로 `noofclusters`개를 선택하여 초기 중심점(`centroids`)으로 설정합니다.
   - 각 벡터의 클러스터 할당 정보(`assignments`)를 저장할 변수를 생성합니다.

2. **그래프 구성**:
   - **평균 계산**: `tf.reduce_mean`을 사용하여 벡터들의 평균을 구하는 연산을 정의합니다 (새로운 중심점 계산용).
   - **거리 계산**: 유클리드 거리(Euclidean distance)를 계산하는 연산을 정의합니다.
   - **클러스터 할당**: 중심점들과의 거리를 비교하여 가장 가까운 클러스터 인덱스(`argmin`)를 찾는 연산을 정의합니다.

3. **반복 수행 (Expectation-Maximization)**:
   - 총 100회 반복(`noofiterations`)하며 다음 두 단계를 수행합니다.
   - **E-Step (Expectation)**:
     - 모든 벡터에 대해 각 중심점까지의 거리를 계산합니다.
     - 각 벡터를 가장 가까운 중심점의 클러스터에 할당합니다.
   - **M-Step (Maximization)**:
     - 각 클러스터에 할당된 벡터들을 모읍니다.
     - 해당 벡터들의 평균을 계산하여 중심점의 위치를 업데이트합니다.

4. **결과 반환**:
   - 반복이 끝나면 최종 중심점과 할당 결과를 반환합니다.

## 참고 사항

- **TensorFlow 버전**: 이 코드는 `tf.Session()`, `tf.initialize_all_variables()`, `tf.sub()` 등 TensorFlow 1.x 버전의 API를 사용하고 있습니다. TensorFlow 2.x 환경에서 실행하려면 호환성 모드를 사용하거나 코드를 마이그레이션해야 합니다.
- **성능**: 반복문 내에서 `sess.run()`을 빈번하게 호출하는 구조로 되어 있어, 데이터가 많을 경우 속도가 느릴 수 있습니다. 벡터화된 연산으로 최적화할 여지가 있습니다.
