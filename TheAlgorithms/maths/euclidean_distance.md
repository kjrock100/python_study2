# Euclidean Distance (유클리드 거리) 알고리즘

이 문서는 `euclidean_distance.py` 파일에 구현된 **유클리드 거리(Euclidean Distance)** 계산 알고리즘에 대한 설명입니다.

## 개요

**유클리드 거리**는 유클리드 공간에서 두 점 사이의 거리를 의미합니다. 피타고라스 정리를 일반화한 것으로 볼 수 있습니다.
두 점 $p = (p_1, p_2, \dots, p_n)$와 $q = (q_1, q_2, \dots, q_n)$ 사이의 거리는 다음과 같이 정의됩니다.

$$ d(p,q) = \sqrt{\sum\_{i=1}^n (q_i - p_i)^2} $$

## 함수 설명

이 파일은 NumPy를 사용하는 버전과 사용하지 않는 버전 두 가지를 제공합니다.

### `euclidean_distance(vector_1: Vector, vector_2: Vector) -> VectorOut`

**NumPy** 라이브러리를 사용하여 유클리드 거리를 계산합니다. 벡터화된 연산을 수행하므로 데이터가 클수록 효율적입니다.

#### 매개변수 (Parameters)

- `vector_1`: 첫 번째 벡터 (리스트, 튜플, 또는 NumPy 배열).
- `vector_2`: 두 번째 벡터.

#### 알고리즘 (Algorithm)

1. 입력 벡터를 NumPy 배열로 변환합니다.
2. 두 배열의 차이를 구하고 제곱합니다.
3. 제곱한 값들의 합을 구합니다.
4. 합의 제곱근(`np.sqrt`)을 반환합니다.

### `euclidean_distance_no_np(vector_1: Vector, vector_2: Vector) -> VectorOut`

NumPy 없이 순수 파이썬 기능만으로 유클리드 거리를 계산합니다.

#### 매개변수 (Parameters)

- `vector_1`: 첫 번째 벡터.
- `vector_2`: 두 번째 벡터.

#### 알고리즘 (Algorithm)

1. `zip()` 함수를 사용하여 두 벡터의 대응하는 요소들을 순회합니다.
2. 각 요소의 차이를 제곱하여 합산합니다.
3. 합계의 0.5승(제곱근)을 계산하여 반환합니다.

## 실행 및 벤치마크

파일을 직접 실행하면(`if __name__ == "__main__":`), `timeit` 모듈을 사용하여 두 함수의 성능을 비교하는 벤치마크가 실행됩니다.

```python
if __name__ == "__main__":
    benchmark()
```

일반적으로 대량의 데이터 처리에는 NumPy 버전이 훨씬 빠르지만, 벤치마크 예제와 같이 매우 작은 크기의 벡터(길이 3)에서는 NumPy 배열 생성 오버헤드로 인해 순수 파이썬 버전이 더 빠를 수도 있습니다.
