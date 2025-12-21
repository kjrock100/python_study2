# 양방향 필터 (Bilateral Filter)

이 문서는 `bilateral_filter.py` 파일에 구현된 **양방향 필터(Bilateral Filter)** 알고리즘에 대해 설명합니다. 이 필터는 이미지를 부드럽게 만들면서도(노이즈 제거), 엣지(가장자리)를 선명하게 유지하는 데 효과적인 비선형 필터입니다.

## 개요

일반적인 가우시안 블러는 픽셀 간의 **공간적 거리(Spatial Distance)**만을 고려하여 가중치를 부여하기 때문에 엣지 부분도 뭉개지는 단점이 있습니다. 반면, 양방향 필터는 **픽셀 값의 차이(Intensity Difference)**도 함께 고려합니다. 즉, 픽셀 값이 급격하게 변하는 엣지 부분에서는 가중치를 낮게 주어 엣지를 보존합니다.

## 주요 함수 설명

### `vec_gaussian(img: np.ndarray, variance: float) -> np.ndarray`
- **목적**: 입력 배열의 각 요소에 대해 가우시안 함수 값을 계산합니다.
- **수식**: $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{x^2}{2\sigma^2}}$

### `get_slice(img: np.ndarray, x: int, y: int, kernel_size: int) -> np.ndarray`
- **목적**: 이미지의 `(x, y)` 좌표를 중심으로 `kernel_size` 크기의 정사각형 영역(윈도우)을 추출합니다.

### `get_gauss_kernel(kernel_size: int, spatial_variance: float) -> np.ndarray`
- **목적**: 공간적 거리에 따른 가중치를 담은 가우시안 커널을 생성합니다.
- **동작**: 커널의 중심에서 거리가 멀어질수록 값이 작아지는 2차원 배열을 반환합니다.

### `bilateral_filter(...)`
- **목적**: 양방향 필터링을 수행하는 메인 함수입니다.
- **매개변수**:
  - `img`: 0과 1 사이의 값으로 정규화된 2D 이미지.
  - `spatial_variance`: 공간적 거리에 대한 분산 ($\sigma_s^2$). 클수록 넓은 영역을 흐리게 합니다.
  - `intensity_variance`: 픽셀 값 차이에 대한 분산 ($\sigma_r^2$). 클수록 색상 차이가 큰 픽셀들도 섞이게 됩니다.
  - `kernel_size`: 커널의 크기 (홀수).
- **알고리즘 단계**:
  1. `get_gauss_kernel`로 공간 가중치(`gaussKer`)를 미리 계산합니다.
  2. 이미지의 각 픽셀을 순회합니다 (가장자리 제외).
  3. 현재 픽셀 주변의 윈도우(`imgS`)를 가져옵니다.
  4. **밝기 차이 계산**: 주변 픽셀들과 중심 픽셀 간의 값 차이(`imgI`)를 구하고, 이에 대한 가우시안 가중치(`imgIG`)를 계산합니다.
  5. **최종 가중치**: 공간 가중치와 밝기 차이 가중치를 곱합니다 (`weights = gaussKer * imgIG`).
  6. 가중 평균을 구하여 결과 픽셀 값으로 설정합니다.

## 사용법

터미널에서 다음과 같이 실행할 수 있습니다:

```bash
python bilateral_filter.py [filename] [spatial_variance] [intensity_variance] [kernel_size]
```

- **인자**:
  - `filename`: 이미지 파일 경로 (기본값: `../image_data/lena.jpg`)
  - `spatial_variance`: 공간 분산 (기본값: 1.0)
  - `intensity_variance`: 밝기 분산 (기본값: 1.0)
  - `kernel_size`: 커널 크기 (기본값: 5)

실행 시 원본 이미지와 필터링된 이미지가 OpenCV 창으로 표시됩니다.