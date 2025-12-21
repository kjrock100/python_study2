# 가장 가까운 두 점 사이의 거리 (Closest Pair of Points)

이 문서는 `closest_pair_of_points.py` 파일에 구현된 **가장 가까운 두 점 사이의 거리** 알고리즘에 대해 설명합니다. 이 알고리즘은 분할 정복(Divide and Conquer) 방식을 사용하여 2차원 평면상의 $n$개의 점들 중 가장 가까운 두 점 사이의 거리를 효율적으로 계산합니다.

## 개요

모든 점 쌍의 거리를 계산하는 브루트 포스(Brute Force) 방식은 $O(n^2)$의 시간이 걸리지만, 분할 정복 방식을 사용하면 $O(n \log n)$의 시간 복잡도로 문제를 해결할 수 있습니다.

## 주요 함수 설명

### `euclidean_distance_sqr(point1, point2)`
- **목적**: 두 점 사이의 유클리드 거리의 제곱을 계산합니다.
- **특징**: 거리 비교 시 제곱근 연산(`sqrt`)은 비용이 많이 들기 때문에, 비교 단계에서는 제곱된 값을 사용하여 성능을 최적화합니다.

### `column_based_sort(array, column=0)`
- **목적**: 점들의 리스트를 특정 좌표축(X 또는 Y)을 기준으로 정렬합니다.
- **매개변수**: `column=0`이면 X축 기준, `column=1`이면 Y축 기준으로 정렬합니다.

### `dis_between_closest_pair(points, points_counts, min_dis=float("inf"))`
- **목적**: 점의 개수가 적을 때(Base case) 사용되는 브루트 포스 방식의 거리 계산 함수입니다.
- **동작**: 이중 반복문을 통해 모든 점 쌍의 거리를 계산하고 최솟값을 찾습니다.

### `dis_between_closest_in_strip(points, points_counts, min_dis=float("inf"))`
- **목적**: 분할된 두 영역의 경계(Strip)에 있는 점들 사이의 최소 거리를 구합니다.
- **최적화**: Y 좌표 기준으로 정렬된 점들을 사용하여, 각 점에 대해 Y 좌표 차이가 현재 최소 거리(`min_dis`)보다 작은 인접한 점들(최대 6~7개)만 검사합니다. 이를 통해 효율성을 높입니다.

### `closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts)`
- **목적**: 분할 정복을 수행하는 핵심 재귀 함수입니다.
- **알고리즘 단계**:
  1. **Base Case**: 점의 개수가 3개 이하이면 `dis_between_closest_pair`를 호출하여 해결합니다.
  2. **Divide**: 점들을 중간 지점(`mid`)을 기준으로 왼쪽과 오른쪽으로 나눕니다.
  3. **Conquer**: 재귀적으로 왼쪽과 오른쪽 부분의 최소 거리(`closest_in_left`, `closest_in_right`)를 구합니다.
  4. **Combine**:
     - 왼쪽과 오른쪽의 최소 거리 중 더 작은 값(`closest_pair_dis`)을 선택합니다.
     - 분할선(중간 지점의 X 좌표)으로부터 거리가 `closest_pair_dis`보다 작은 점들을 추려내어 `cross_strip` 리스트를 만듭니다.
     - `dis_between_closest_in_strip` 함수를 통해 띠 영역 내에서의 최소 거리(`closest_in_strip`)를 구합니다.
     - 최종적으로 `closest_pair_dis`와 `closest_in_strip` 중 더 작은 값을 반환합니다.

### `closest_pair_of_points(points, points_counts)`
- **목적**: 알고리즘의 진입점(Wrapper) 함수입니다.
- **동작**:
  1. 입력된 점들을 X축과 Y축 기준으로 각각 미리 정렬합니다.
  2. `closest_pair_of_points_sqr` 함수를 호출하여 최소 거리의 제곱을 구합니다.
  3. 최종 결과에 제곱근을 취하여 실제 거리를 반환합니다.

## 시간 복잡도

- **전처리(정렬)**: $O(n \log n)$
- **분할 정복**: $T(n) = 2T(n/2) + O(n)$ $\rightarrow$ $O(n \log n)$
- **총 시간 복잡도**: $O(n \log n)$

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

1. 점들의 리스트(`points`)를 정의합니다.
2. `closest_pair_of_points` 함수를 호출하여 가장 가까운 두 점 사이의 거리를 계산하고 출력합니다.
