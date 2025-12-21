# 하버사인 거리 (Haversine Distance)

이 문서는 `haversine_distance.py` 파일에 구현된 **하버사인 거리** 계산 알고리즘에 대해 설명합니다.

## 개요

하버사인 공식(Haversine Formula)은 구(Sphere) 형태의 표면에서 두 지점 사이의 대원 거리(Great Circle Distance)를 구하는 공식입니다. 지구는 완벽한 구가 아니지만, 이 공식은 계산이 빠르고 짧은 거리에서는 오차가 적어 널리 사용됩니다.

이 구현에서는 지구의 타원체적 특성을 일부 반영하기 위해 위도를 보정하여 계산합니다.

## 주요 함수: `haversine_distance`

### `haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float`

- **목적**: 위도와 경도로 주어진 두 지점 사이의 거리를 미터(m) 단위로 계산합니다.
- **매개변수**:
  - `lat1`, `lon1`: 첫 번째 지점의 위도와 경도.
  - `lat2`, `lon2`: 두 번째 지점의 위도와 경도.
- **반환값**: 두 지점 사이의 거리 (미터).

### 알고리즘 동작 원리

1. **상수 정의 (WGS84 기준)**:
   - `AXIS_A`: 지구 장반경 (적도 반지름).
   - `AXIS_B`: 지구 단반경 (극 반지름).
   - `RADIUS`: 계산에 사용할 반지름 (적도 반지름).

2. **위도 보정 (Parametric Latitude)**:
   - 지구의 편평률(`flattening`)을 계산합니다.
   - 입력받은 위도(`lat`)를 라디안으로 변환한 뒤, 편평률을 적용하여 **매개변수 위도(Parametric Latitude)** `phi`를 구합니다. 이는 지구가 타원체임을 감안하여 위도를 보정하는 과정입니다.

3. **하버사인 공식 적용**:
   - 위도 차이와 경도 차이의 절반에 대한 사인 제곱 값을 구합니다.
   - 하버사인 공식을 통해 중심각에 대응하는 `h_value`를 계산합니다.
   - 아크사인(`asin`) 함수를 사용하여 거리를 구하고 반지름을 곱해 최종 거리를 반환합니다.

## 사용법

`if __name__ == "__main__":` 블록은 `doctest`를 실행하여 함수가 올바르게 동작하는지 검증합니다.

예시:
```python
from collections import namedtuple
point_2d = namedtuple("point_2d", "lat lon")
SAN_FRANCISCO = point_2d(37.774856, -122.424227)
YOSEMITE = point_2d(37.864742, -119.537521)

distance = haversine_distance(SAN_FRANCISCO.lat, SAN_FRANCISCO.lon, YOSEMITE.lat, YOSEMITE.lon)
# 결과: 약 254,352 미터
```
