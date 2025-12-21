# 캐니 엣지 검출 (Canny Edge Detection)

이 문서는 `canny.py` 파일에 구현된 **캐니 엣지 검출(Canny Edge Detection)** 알고리즘에 대해 설명합니다. 이 알고리즘은 이미지 처리에서 가장 널리 사용되는 가장자리 검출 알고리즘 중 하나로, 노이즈에 강하고 엣지를 정확하게 찾아내는 장점이 있습니다.

## 개요

캐니 엣지 검출은 다음 5단계로 이루어집니다:
1. **노이즈 제거 (Noise Reduction)**: 가우시안 필터를 사용하여 이미지의 노이즈를 제거합니다.
2. **그라디언트 계산 (Gradient Calculation)**: 소벨 필터를 사용하여 이미지의 강도 변화량(Gradient)과 방향을 계산합니다.
3. **비최대 억제 (Non-maximum Suppression)**: 엣지가 아닌 픽셀들을 제거하여 엣지를 얇게 만듭니다.
4. **이중 임계값 (Double Thresholding)**: 엣지를 강한 엣지, 약한 엣지, 엣지 아님으로 분류합니다.
5. **엣지 추적 (Edge Tracking by Hysteresis)**: 약한 엣지가 강한 엣지와 연결되어 있을 때만 최종 엣지로 간주합니다.

## 주요 함수 설명

### `gen_gaussian_kernel(k_size, sigma)`
- **목적**: 가우시안 스무딩을 위한 커널을 생성합니다.
- **매개변수**:
  - `k_size`: 커널의 크기 (홀수).
  - `sigma`: 가우시안 분포의 표준편차.

### `canny(image, threshold_low=15, threshold_high=30, weak=128, strong=255)`
- **목적**: 캐니 엣지 검출 알고리즘의 메인 함수입니다.
- **매개변수**:
  - `image`: 입력 그레이스케일 이미지.
  - `threshold_low`, `threshold_high`: 이중 임계값 처리에 사용되는 기준값.
  - `weak`, `strong`: 약한 엣지와 강한 엣지를 표시할 픽셀 값.

#### 알고리즘 상세 단계

1. **가우시안 필터링**: `img_convolve`와 `gen_gaussian_kernel`을 사용하여 이미지를 부드럽게 만듭니다.
2. **소벨 필터링**: `sobel_filter`를 사용하여 그라디언트(`sobel_grad`)와 방향(`sobel_theta`)을 구합니다. 방향은 라디안에서 각도로 변환됩니다.
3. **비최대 억제 (Non-maximum Suppression)**:
   - 각 픽셀에서 그라디언트 방향(0°, 45°, 90°, 135° 근사)을 확인합니다.
   - 해당 방향의 인접 픽셀들과 현재 픽셀의 그라디언트 강도를 비교합니다.
   - 현재 픽셀이 최댓값이 아니면 0으로 억제합니다.
4. **이중 임계값 (Double Thresholding)**:
   - `threshold_high` 이상: **강한 엣지 (Strong)**
   - `threshold_low` ~ `threshold_high`: **약한 엣지 (Weak)**
   - `threshold_low` 이하: 0 (엣지 아님)
5. **엣지 추적 (Edge Tracking)**:
   - 약한 엣지(`weak`) 픽셀 주변 8방향에 강한 엣지(`strong`)가 하나라도 있으면 해당 픽셀을 강한 엣지로 변경합니다.
   - 그렇지 않으면 0으로 제거합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:
1. `image_data/lena.jpg` 이미지를 그레이스케일 모드로 읽어옵니다.
2. `canny()` 함수를 호출하여 엣지를 검출합니다.
3. 결과 이미지를 OpenCV 창으로 보여줍니다.