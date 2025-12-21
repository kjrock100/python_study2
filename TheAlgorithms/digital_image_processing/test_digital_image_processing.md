# 디지털 이미지 처리 테스트 (Digital Image Processing Tests)

이 문서는 `test_digital_image_processing.py` 파일에 구현된 단위 테스트(Unit Tests)에 대해 설명합니다. 이 파일은 `digital_image_processing` 패키지 내의 다양한 이미지 처리 알고리즘들이 올바르게 동작하는지 검증하기 위해 작성되었습니다.

## 개요

이 테스트 코드는 `pytest` 프레임워크를 기반으로 작성되었으며, OpenCV(`cv2`), NumPy, Pillow(`PIL`) 라이브러리를 사용하여 이미지 처리 함수의 입출력을 검증합니다. 테스트 대상이 되는 알고리즘에는 필터링, 엣지 검출, 색상 변환, 리사이징 등이 포함됩니다.

## 주요 테스트 함수 설명

### `test_convert_to_negative()`
- **대상**: `convert_to_negative` 모듈.
- **내용**: 이미지를 반전(Negative)시킨 결과 배열에 유효한 값이 존재하는지(`any()`) 확인합니다.

### `test_change_contrast()`
- **대상**: `change_contrast` 모듈.
- **내용**: PIL 이미지 객체의 대비를 조절한 후, 반환된 객체가 PIL Image 형식인지 문자열 표현을 통해 확인합니다.

### `test_gen_gaussian_kernel()`
- **대상**: `canny` 모듈의 `gen_gaussian_kernel` 함수.
- **내용**: 생성된 가우시안 커널 배열이 비어있지 않은지 확인합니다.

### `test_canny()`
- **대상**: `canny` 모듈의 엣지 검출 함수.
- **내용**: 그레이스케일 이미지를 입력받아 캐니 엣지 검출을 수행하고, 결과 배열에 엣지가 검출되었는지 확인합니다.

### `test_gen_gaussian_kernel_filter()`
- **대상**: `gaussian_filter` 모듈.
- **내용**: 가우시안 필터를 적용한 결과 이미지가 유효한지 확인합니다.

### `test_convolve_filter()`
- **대상**: `convolve` 모듈.
- **내용**: 라플라시안(Laplacian) 커널을 사용하여 컨볼루션 연산을 수행하고, 결과가 유효한지 확인합니다.

### `test_median_filter()`
- **대상**: `median_filter` 모듈.
- **내용**: 미디언 필터를 적용한 결과가 유효한지 확인합니다.

### `test_sobel_filter()`
- **대상**: `sobel_filter` 모듈.
- **내용**: 소벨 필터를 적용하여 그라디언트(Gradient)와 방향(Theta)을 계산하고, 두 결과 배열이 모두 유효한지 확인합니다.

### `test_sepia()`
- **대상**: `sepia` 모듈.
- **내용**: 세피아 톤 변환을 수행하고 결과가 유효한지 확인합니다.

### `test_burkes()`
- **대상**: `dithering.burkes` 모듈.
- **내용**: 버크(Burke's) 디더링 알고리즘을 수행하고 결과 이미지가 생성되었는지 확인합니다.

### `test_nearest_neighbour()`
- **대상**: `resize` 모듈.
- **내용**: 최근접 이웃 보간법을 사용하여 이미지 크기를 조절하고 결과가 생성되었는지 확인합니다.

## 테스트 실행 방법

터미널에서 다음 명령어를 실행하여 테스트를 수행할 수 있습니다:

```bash
pytest test_digital_image_processing.py
```

또는 모든 테스트를 실행하려면:

```bash
pytest
```
