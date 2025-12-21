# 베지에 곡선 (Bézier Curve)

이 문서는 `bezier_curve.py` 파일에 구현된 **베지에 곡선** 생성 및 시각화 알고리즘에 대해 설명합니다.

## 개요

베지에 곡선은 컴퓨터 그래픽스에서 부드러운 곡선을 모델링하는 데 널리 사용되는 매개변수 곡선입니다. 주어진 제어점(Control Points)들의 가중치 합으로 정의되며, 제어점들은 곡선의 형태를 결정합니다.

이 구현은 2차원 xy 평면에서의 베지에 곡선을 다룹니다.

## 주요 클래스: `BezierCurve`

### `__init__(list_of_points: list[tuple[float, float]])`
- **목적**: 베지에 곡선 객체를 초기화합니다.
- **매개변수**:
  - `list_of_points`: 곡선을 제어할 (x, y) 좌표 튜플의 리스트입니다.
- **속성**:
  - `degree`: 곡선의 차수 (제어점 개수 - 1). 차수가 1이면 직선이 됩니다.

### `basis_function(t: float) -> list[float]`
- **목적**: 시간 `t`에서의 각 제어점에 대한 기저 함수(Basis Function) 값을 계산합니다.
- **설명**: 베지에 곡선은 번스타인 다항식(Bernstein polynomial)을 기저 함수로 사용합니다.
  - $B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$
- **매개변수**: `t` (0과 1 사이의 값).
- **반환값**: 각 제어점에 대응하는 가중치 리스트. 모든 가중치의 합은 1이어야 합니다.

### `bezier_curve_function(t: float) -> tuple[float, float]`
- **목적**: 시간 `t`에서의 곡선 상의 좌표 (x, y)를 계산합니다.
- **동작**:
  - 각 제어점의 좌표에 해당 기저 함수 값(가중치)을 곱한 뒤 모두 더하여 현재 위치를 구합니다.
  - $P(t) = \sum_{i=0}^{n} B_{i,n}(t) \cdot P_i$

### `plot_curve(step_size: float = 0.01)`
- **목적**: `matplotlib`를 사용하여 베지에 곡선과 제어점을 시각화합니다.
- **매개변수**:
  - `step_size`: 곡선을 그릴 때 `t`를 증가시키는 간격. 작을수록 곡선이 부드럽게 그려집니다.
- **동작**:
  - `t`를 0부터 1까지 `step_size`만큼 증가시키며 곡선 상의 점들을 계산하고 연결하여 그립니다.
  - 제어점은 산점도(Scatter plot)로 표시합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 다양한 차수의 베지에 곡선을 그리는 예시를 확인할 수 있습니다.

```python
# 1차 베지에 곡선 (직선)
BezierCurve([(1, 2), (3, 5)]).plot_curve()

# 2차 베지에 곡선 (포물선 형태)
BezierCurve([(0, 0), (5, 5), (5, 0)]).plot_curve()

# 3차 베지에 곡선
BezierCurve([(0, 0), (5, 5), (5, 0), (2.5, -2.5)]).plot_curve()
```

## 요구 사항
- `scipy`: 조합(combination) 계산을 위해 사용 (`scipy.special.comb`).
- `matplotlib`: 그래프 출력을 위해 사용.
