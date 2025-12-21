# 유사도 검색 (Similarity Search)

이 문서는 `similarity_search.py` 파일에 구현된 **유사도 검색(Similarity Search)** 알고리즘에 대해 설명합니다.

## 개요

유사도 검색은 주어진 벡터 집합에서 가장 가까운 벡터를 찾는 알고리즘으로, 자연어 처리(NLP) 등 다양한 분야에서 사용됩니다. 이 구현에서는 **유클리드 거리(Euclidean Distance)**를 사용하여 벡터 간의 거리를 계산하고, 가장 가까운 벡터와 그 거리를 반환합니다.

## 주요 함수

### `euclidean(input_a: np.ndarray, input_b: np.ndarray) -> float`

- **목적**: 두 벡터 `input_a`와 `input_b` 사이의 유클리드 거리를 계산합니다.
- **수식**: $\sqrt{\sum (a_i - b_i)^2}$
- **매개변수**:
  - `input_a`: 첫 번째 벡터 (NumPy 배열).
  - `input_b`: 두 번째 벡터 (NumPy 배열).
- **반환값**: 두 벡터 사이의 거리 (실수형).

### `similarity_search(dataset: np.ndarray, value_array: np.ndarray) -> list`

- **목적**: `value_array`에 있는 각 벡터에 대해 `dataset`에서 가장 가까운 벡터를 찾습니다.
- **매개변수**:
  - `dataset`: 검색 대상이 되는 벡터들의 집합 (NumPy 배열).
  - `value_array`: 가장 가까운 이웃을 찾고자 하는 쿼리 벡터들의 집합 (NumPy 배열).
- **반환값**: 각 쿼리 벡터에 대한 결과 리스트. 각 결과는 `[가장 가까운 벡터, 거리]` 형태입니다.
- **예외 처리**:
  - 차원(Dimension)이 다를 경우 `ValueError` 발생.
  - 모양(Shape)이 호환되지 않을 경우 `ValueError` 발생.
  - 데이터 타입(dtype)이 다를 경우 `TypeError` 발생.

## 사용 예시

```python
import numpy as np
from similarity_search import similarity_search

dataset = np.array([[0, 0], [1, 1], [2, 2]])
value_array = np.array([[0, 1]])

results = similarity_search(dataset, value_array)
print(results)
# 출력: [[[0, 0], 1.0]]
# (0, 1)과 가장 가까운 벡터는 (0, 0)이며, 거리는 1.0입니다.
```

## 요구 사항
- `numpy`: 배열 연산 및 데이터 처리를 위해 필요합니다.
