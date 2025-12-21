# 결정 트리 (Decision Tree)

이 문서는 `decision_tree.py` 파일에 구현된 **회귀 결정 트리 (Regression Decision Tree)** 알고리즘에 대해 설명합니다.

## 개요

이 코드는 기본적인 회귀 결정 트리를 구현합니다. 입력 데이터는 연속적인 레이블을 가진 1차원 데이터여야 하며, 결정 트리는 실수 입력을 실수 출력으로 매핑합니다.

## 주요 클래스: `Decision_Tree`

### `__init__(self, depth=5, min_leaf_size=5)`
- **목적**: 결정 트리 객체를 초기화합니다.
- **매개변수**:
  - `depth`: 트리의 최대 깊이 (기본값: 5).
  - `min_leaf_size`: 리프 노드가 되기 위한 최소 데이터 개수 (기본값: 5).
- **속성**:
  - `decision_boundary`: 분기 기준 값.
  - `left`, `right`: 왼쪽 및 오른쪽 자식 트리.
  - `prediction`: 리프 노드일 경우 예측 값.

### `mean_squared_error(self, labels, prediction)`
- **목적**: 주어진 예측 값에 대한 평균 제곱 오차(MSE)를 계산합니다.
- **매개변수**:
  - `labels`: 실제 레이블 값들 (1차원 numpy 배열).
  - `prediction`: 예측 값 (실수).
- **반환값**: MSE 값.

### `train(self, X, y)`
- **목적**: 주어진 데이터로 결정 트리를 학습시킵니다.
- **매개변수**:
  - `X`: 입력 데이터 (1차원 numpy 배열).
  - `y`: 레이블 데이터 (1차원 numpy 배열).
- **동작 원리**:
  1. 입력 데이터의 차원과 길이를 검사합니다.
  2. 데이터 개수가 `2 * min_leaf_size`보다 작거나 깊이가 1이면, 현재 노드를 리프 노드로 만들고 평균값을 예측 값으로 설정합니다.
  3. 가능한 모든 분기점을 순회하며 MSE를 최소화하는 최적의 분기점(`best_split`)을 찾습니다.
  4. 최적의 분기점을 기준으로 데이터를 나누고, 왼쪽과 오른쪽 자식 트리를 생성하여 재귀적으로 학습시킵니다.
  5. 더 이상 분기할 수 없으면 현재 노드의 평균값을 예측 값으로 설정합니다.

### `predict(self, x)`
- **목적**: 입력 값 `x`에 대한 예측 값을 반환합니다.
- **매개변수**: `x` (예측할 실수 값).
- **동작**:
  - 현재 노드가 리프 노드(`prediction`이 존재)이면 예측 값을 반환합니다.
  - 그렇지 않으면 `decision_boundary`와 비교하여 왼쪽 또는 오른쪽 자식 트리의 `predict` 함수를 재귀적으로 호출합니다.

## 테스트 클래스: `Test_Decision_Tree`

- `helper_mean_squared_error_test`: `mean_squared_error` 함수의 동작을 검증하기 위한 헬퍼 함수입니다.

## 사용법

`if __name__ == "__main__":` 블록에서 실행 예시를 확인할 수 있습니다.

1. `numpy`를 사용하여 사인(sin) 함수 형태의 샘플 데이터를 생성합니다.
2. `Decision_Tree` 객체를 생성하고 학습시킵니다.
3. 무작위 테스트 값들에 대해 예측을 수행하고 평균 오차를 출력합니다.

```python
X = np.arange(-1.0, 1.0, 0.005)
y = np.sin(X)

tree = Decision_Tree(depth=10, min_leaf_size=10)
tree.train(X, y)
# ... 예측 및 오차 계산 ...
```
