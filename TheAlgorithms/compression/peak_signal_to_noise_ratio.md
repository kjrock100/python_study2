# `peak_signal_to_noise_ratio.py` 코드 설명

이 문서는 `peak_signal_to_noise_ratio.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 두 이미지 간의 품질 차이를 측정하는 데 사용되는 **최대 신호 대 잡음비(Peak Signal-to-Noise Ratio, PSNR)**를 계산하는 기능을 구현합니다.

## 목차
1.  PSNR이란?
2.  함수 설명
    -   `psnr(original, contrast)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## PSNR이란?

PSNR은 주로 이미지나 비디오의 손실 압축 후 품질을 평가하는 데 사용되는 공학적인 척도입니다. 원본 데이터와 압축된 데이터 간의 차이를 측정하며, 값이 높을수록 원본과의 차이가 적고 품질이 좋다는 것을 의미합니다.

PSNR은 **평균 제곱 오차(Mean Squared Error, MSE)**를 기반으로 계산됩니다.

-   **MSE**: 두 이미지의 같은 위치에 있는 픽셀 값들의 차이를 제곱하여 평균 낸 값입니다.
-   **PSNR 공식**: `PSNR = 20 * log₁₀(MAX / sqrt(MSE))`
    -   `MAX`: 픽셀이 가질 수 있는 최대값 (일반적으로 8비트 이미지에서는 255)
    -   `MSE`: 두 이미지 간의 평균 제곱 오차

## 함수 설명

### `psnr(original: np.ndarray, contrast: np.ndarray) -> float`

원본 이미지와 비교 대상 이미지(압축 또는 변형된 이미지)를 입력받아 PSNR 값을 계산합니다.

-   **인자**:
    -   `original`: 원본 이미지의 `numpy` 배열.
    -   `contrast`: 비교할 이미지의 `numpy` 배열.

-   **알고리즘**:
    1.  `numpy`를 사용하여 두 이미지 배열 간의 MSE를 계산합니다.
    2.  만약 MSE가 0이면(두 이미지가 완전히 동일하면), 100을 반환하여 완벽한 품질을 나타냅니다.
    3.  MSE가 0이 아니면, 위에서 설명한 PSNR 공식을 사용하여 값을 계산하고 반환합니다.

### `main()`

미리 정의된 이미지 파일들을 읽어와 `psnr` 함수를 호출하고, 두 가지 다른 테스트 케이스에 대한 PSNR 값을 출력합니다.

-   **동작**:
    1.  `image_data` 디렉터리에서 원본 이미지와 압축된 이미지를 `cv2.imread()`를 사용하여 로드합니다.
    2.  `psnr` 함수를 호출하여 각 쌍의 이미지에 대한 PSNR 값을 계산하고, 결과를 dB(데시벨) 단위로 출력합니다.

## 실행 방법

스크립트를 직접 실행하면 두 쌍의 이미지에 대한 PSNR 계산 결과를 출력합니다.

1.  **필요한 라이브러리 설치**:
    ```bash
    pip install numpy opencv-python
    ```
2.  **준비**: 스크립트와 같은 디렉터리 내에 `image_data` 폴더를 만들고, `original_image.png`, `compressed_image.png`, `PSNR-example-base.png`, `PSNR-example-comp-10.jpg` 파일을 위치시킵니다.
3.  **실행**:
    ```bash
    python peak_signal_to_noise_ratio.py
    ```

**실행 결과:**
```
-- First Test --
PSNR value is 29.73... dB

-- Second Test --
PSNR value is 31.53... dB
```

## 코드 개선 제안

1.  **입력 타입 오류**: `psnr` 함수의 타입 힌트는 `float`으로 되어 있지만, 실제로는 `numpy.ndarray`를 입력으로 받습니다. 타입 힌트를 `np.ndarray`로 수정해야 코드의 의도가 명확해집니다.

    ```diff
    --- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/compression/peak_signal_to_noise_ratio.py
    +++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/compression/peak_signal_to_noise_ratio.py
    @@ -11,7 +11,7 @@
 import numpy as np
 
 
-def psnr(original: float, contrast: float) -> float:
+def psnr(original: np.ndarray, contrast: np.ndarray) -> float:
     mse = np.mean((original - contrast) ** 2)
     if mse == 0:
         return 100

    ```

2.  **이미지 채널 처리**: `cv2.imread()`는 기본적으로 BGR 순서의 3채널 컬러 이미지를 로드합니다. `psnr` 함수는 채널을 구분하지 않고 전체 배열에 대해 MSE를 계산합니다. 만약 각 채널(Blue, Green, Red)에 대해 개별적으로 PSNR을 계산하거나, 그레이스케일 이미지로 변환하여 계산하는 것이 더 일반적인 접근 방식일 수 있습니다. 현재 방식은 모든 채널의 픽셀 값을 하나의 큰 집합으로 보고 오차를 계산합니다.

3.  **하드코딩된 파일 경로**: `main` 함수에서 이미지 파일 경로가 하드코딩되어 있습니다. `sys.argv`나 `argparse` 모듈을 사용하여 사용자가 커맨드 라인에서 직접 비교할 두 이미지의 경로를 지정하도록 만들면 스크립트의 활용도가 크게 향상됩니다.