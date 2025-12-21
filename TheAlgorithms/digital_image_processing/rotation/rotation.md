# 이미지 회전 및 아핀 변환 (Image Rotation & Affine Transformation)

이 문서는 `rotation.py` 파일에 구현된 이미지 변환 알고리즘에 대해 설명합니다. 파일명은 회전(Rotation)이지만, 실제 코드는 3개의 대응점을 이용한 **아핀 변환(Affine Transformation)**을 수행합니다. 아핀 변환은 회전뿐만 아니라 크기 조절(Scaling), 이동(Translation), 전단(Shearing)을 포함하는 선형 변환입니다.

## 개요

OpenCV의 `getAffineTransform` 함수를 사용하여 변환 전의 점 3개와 변환 후의 점 3개를 매핑하는 행렬을 구하고, 이를 이미지에 적용하여 기하학적 변환을 수행합니다.

## 주요 함수: `get_rotation`

### `get_rotation(img, pt1, pt2, rows, cols)`
- **목적**: 입력 이미지에 아핀 변환을 적용합니다.
- **매개변수**:
  - `img`: 입력 이미지 (NumPy 배열).
  - `pt1`: 변환 전의 좌표 3개 (3x2 NumPy 배열, `float32`).
  - `pt2`: 변환 후의 좌표 3개 (3x2 NumPy 배열, `float32`).
  - `rows`: 출력 이미지의 너비(또는 높이) 설정값.
  - `cols`: 출력 이미지의 높이(또는 너비) 설정값.
- **동작**:
  1. `cv2.getAffineTransform(pt1, pt2)`: 두 세트의 점(`pt1`, `pt2`)을 입력받아 2x3 변환 행렬(`matrix`)을 계산합니다.
  2. `cv2.warpAffine(img, matrix, (rows, cols))`: 계산된 행렬을 사용하여 이미지를 변환합니다.
     - *주의*: `cv2.warpAffine`의 세 번째 인자는 `(width, height)` 순서입니다. 코드에서는 `(rows, cols)`로 전달하고 있어, 변수명과 실제 역할(너비/높이) 간의 관계 확인이 필요할 수 있습니다.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

1. **이미지 로드**: `image_data/lena.jpg`를 읽어오고 그레이스케일로 변환합니다.
2. **좌표 정의**: 변환을 위한 기준점들을 정의합니다 (`pts1` ~ `pts4`).
   - `pts1`: 원본 이미지에서의 삼각형 좌표.
   - `pts2`, `pts3`, `pts4`: 변환 후의 삼각형 좌표들.
3. **변환 수행**:
   - `pts1` -> `pts2`
   - `pts2` -> `pts3`
   - `pts2` -> `pts4`
   위의 조합으로 `get_rotation` 함수를 호출하여 다양한 변환 결과를 생성합니다.
4. **결과 출력**: `matplotlib`를 사용하여 원본 이미지와 3가지 변환된 이미지를 2x2 격자로 보여줍니다.
