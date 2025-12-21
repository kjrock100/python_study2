# 램버트 타원체 거리 (Lambert's Ellipsoidal Distance)

이 문서는 `lamberts_ellipsoidal_distance.py` 파일에 구현된 **램버트 타원체 거리** 계산 알고리즘에 대해 설명합니다.

## 개요

지구를 완벽한 구(Sphere)가 아닌 타원체(Ellipsoid)로 가정하여 두 지점 사이의 최단 거리를 계산하는 방법입니다. 하버사인(Haversine) 공식보다 더 정확하며, 수천 킬로미터 거리에서 약 10미터 내외의 오차를 가집니다.

이 알고리즘은 긴 거리(Long lines)에 대한 램버트 공식(Lambert's formula)을 사용합니다.

## 주요 함수: `lamberts_ellipsoidal_distance`

### `lamberts_ellipsoidal_distance(lat1, lon1, lat2, lon2) -> float`

- **목적**: 타원체 표면을 따라 두 지점 사이의 최단 거리를 계산합니다.
- **매개변수**:
  - `lat1`, `lon1`: 첫 번째 지점의 위도와 경도.
  - `lat2`, `lon2`: 두 번째 지점의 위도와 경도.
- **반환값**: 두 지점 사이의 거리 (미터).

### 알고리즘 동작 원리

1. **상수 정의 (WGS84)**:
   - `AXIS_A`: 장반경 (적도 반지름).
   - `AXIS_B`: 단반경 (극 반지름).
   - `flattening`: 편평률 ($f = (a - b) / a$).

2. **매개변수 위도 (Parametric Latitude) 계산**:
   - 지구가 납작한 정도를 고려하여 위도를 보정합니다.
   - $\tan(\beta) = (1 - f) \tan(\phi)$

3. **중심각 ($\sigma$) 계산**:
   - `haversine_distance` 함수를 사용하여 구면 거리 근사치를 구한 뒤, 이를 적도 반지름으로 나누어 라디안 단위의 중심각을 얻습니다.

4. **보정값 계산 (X, Y)**:
   - 램버트 공식을 사용하여 타원체 효과에 대한 보정항 $X$와 $Y$를 계산합니다.
   - $P = (\beta_1 + \beta_2) / 2$
   - $Q = (\beta_2 - \beta_1) / 2$
   - $X = (\sigma - \sin(\sigma)) \frac{\sin^2 P \cos^2 Q}{\cos^2(\sigma/2)}$
   - $Y = (\sigma + \sin(\sigma)) \frac{\cos^2 P \sin^2 Q}{\sin^2(\sigma/2)}$

5. **최종 거리 계산**:
   - $d = R (\sigma - \frac{f}{2}(X + Y))$

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

```python
distance = lamberts_ellipsoidal_distance(37.774856, -122.424227, 40.713019, -74.012647)
# 결과: 약 4,138,992 미터 (샌프란시스코 -> 뉴욕)
```

## 참고 사항
- 이 코드는 중심각 $\sigma$를 계산하기 위해 `geodesy/haversine_distance.py`에 의존합니다.
- 빈센티(Vincenty) 공식보다는 덜 정밀하지만 계산 복잡도가 낮아 긴 거리 계산에 효율적입니다.
