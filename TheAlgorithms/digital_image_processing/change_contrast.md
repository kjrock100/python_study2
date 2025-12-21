# 이미지 대비 조절 (Change Contrast)

이 문서는 `change_contrast.py` 파일에 구현된 이미지 대비(Contrast) 조절 알고리즘에 대해 설명합니다. 이 코드는 Python의 이미지 처리 라이브러리인 **Pillow (PIL)**를 사용합니다.

## 개요

이미지의 대비를 높이거나 낮추는 알고리즘입니다. 대비를 높이면 밝은 부분은 더 밝게, 어두운 부분은 더 어둡게 되어 이미지가 선명해집니다.

## 주요 함수: `change_contrast`

### `change_contrast(img: Image, level: int) -> Image`
- **목적**: PIL 이미지 객체의 대비를 주어진 레벨에 따라 조절합니다.
- **매개변수**:
  - `img`: 원본 PIL Image 객체.
  - `level`: 대비 조절 강도. (일반적으로 -255 ~ 255 범위 사용 권장)
- **동작 원리**:
  1. **보정 계수(Factor) 계산**:
     - 입력된 `level` 값을 기반으로 대비 보정 계수를 계산합니다.
     - 공식: $F = \frac{259(level + 255)}{255(259 - level)}$
     - 이 공식은 표준적인 대비 조절 알고리즘에서 사용되는 수식입니다.
  2. **대비 변환 함수 정의 (`contrast`)**:
     - 각 픽셀 값 `c`에 대해 연산을 수행합니다.
     - 공식: $R' = 128 + F(c - 128)$
     - 픽셀 값의 중간값인 128을 기준으로, 차이를 증폭시키거나 감소시킵니다.
  3. **적용**: `img.point(contrast)`를 호출하여 이미지의 모든 픽셀에 위 변환 함수를 적용합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

1. `image_data/lena.jpg` 이미지를 불러옵니다.
2. `change_contrast` 함수를 호출하여 대비를 **170**으로 설정합니다. (높은 대비)
3. 결과 이미지를 `image_data/lena_high_contrast.png`로 저장합니다.

## 참고 사항

- **PIL (Python Imaging Library)**: 이 코드를 실행하려면 `Pillow` 라이브러리가 설치되어 있어야 합니다.
  ```bash
  pip install Pillow
  ```
