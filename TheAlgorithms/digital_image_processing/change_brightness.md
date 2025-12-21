# 이미지 밝기 조절 (Change Brightness)

이 문서는 `change_brightness.py` 파일에 구현된 이미지 밝기 조절 알고리즘에 대해 설명합니다. 이 코드는 Python의 이미지 처리 라이브러리인 **Pillow (PIL)**를 사용합니다.

## 개요

이미지의 각 픽셀 값에 특정 상수(`level`)를 더하거나 빼서 이미지를 밝게 또는 어둡게 만듭니다.

## 주요 함수: `change_brightness`

### `change_brightness(img: Image, level: float) -> Image`
- **목적**: PIL 이미지 객체의 밝기를 주어진 레벨만큼 조절합니다.
- **매개변수**:
  - `img`: 원본 PIL Image 객체.
  - `level`: 밝기 조절 강도 (-255.0 ~ 255.0). 양수면 밝아지고, 음수면 어두워집니다.
- **동작 원리**:
  1. **유효성 검사**: `level`이 -255와 255 사이인지 확인합니다.
  2. **밝기 변환 함수 정의 (`brightness`)**:
     - 각 픽셀 값 `c`에 대해 연산을 수행합니다.
     - 코드상의 수식: `128 + level + (c - 128)`
     - *설명*: 수식적으로는 `c + level`과 동일합니다. 즉, 현재 픽셀 값에 `level` 값을 더합니다. (작성자가 대비 조절 공식과 혼동했거나, 중간값 128을 기준으로 생각한 것으로 보입니다.)
  3. **적용**: `img.point(brightness)`를 호출하여 이미지의 모든 픽셀에 위 변환 함수를 적용합니다. `point` 메서드는 각 픽셀 값을 변환하는 효율적인 방법입니다.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

1. `image_data/lena.jpg` 이미지를 불러옵니다.
2. `change_brightness` 함수를 호출하여 밝기를 **100**만큼 증가시킵니다.
3. 결과 이미지를 `image_data/lena_brightness.png`로 저장합니다.

## 참고 사항

- **PIL (Python Imaging Library)**: 이 코드를 실행하려면 `Pillow` 라이브러리가 설치되어 있어야 합니다.
  ```bash
  pip install Pillow
  ```
