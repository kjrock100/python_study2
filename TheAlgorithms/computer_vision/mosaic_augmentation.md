# `mosaic_augmentation.py` 코드 설명

이 문서는 `mosaic_augmentation.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 컴퓨터 비전, 특히 객체 탐지(object detection) 모델의 훈련 데이터 양과 다양성을 늘리기 위한 고급 **데이터 증강(Data Augmentation)** 기법인 **모자이크 증강(Mosaic Augmentation)**을 구현합니다.

## 목차
1.  모자이크 증강이란?
2.  함수 설명
    -   `get_dataset(label_dir, img_dir)`
    -   `update_image_and_anno(...)`
    -   `random_chars(number_char)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 모자이크 증강이란?

모자이크 증강은 4개의 다른 훈련 이미지를 무작위로 잘라내어 하나의 큰 이미지로 합치는 데이터 증강 기법입니다. 이는 YOLOv4와 같은 최신 객체 탐지 모델에서 성능을 크게 향상시키는 데 사용되었습니다.

**장점**:
-   **작은 객체 탐지 성능 향상**: 원본 이미지를 리사이즈하여 붙여넣기 때문에, 모델이 평소보다 작은 크기의 객체를 학습할 기회가 늘어납니다.
-   **배치 정규화(Batch Normalization) 효과 증대**: 4개의 다른 이미지에서 온 통계 정보를 한 번에 처리하므로, 배치 정규화가 더 효과적으로 동작합니다.
-   **컨텍스트 다양성 증가**: 모델이 객체를 인식할 때 주변 컨텍스트에 덜 의존하도록 훈련됩니다.

이 스크립트는 4개의 이미지를 무작위로 선택하고, 무작위 분할점을 기준으로 잘라 하나의 모자이크 이미지로 만든 후, 각 이미지에 있던 바운딩 박스 좌표도 새로운 이미지에 맞게 변환합니다.

## 함수 설명

### `get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]`

지정된 디렉터리에서 이미지 경로와 해당 이미지의 바운딩 박스 주석(annotation)을 불러옵니다.

-   **알고리즘**:
    1.  `label_dir`에서 모든 `.txt` 주석 파일을 찾습니다.
    2.  각 주석 파일을 읽어 YOLO 형식(`class_id x_center y_center width height`)의 바운딩 박스 정보를 파싱하여, `xmin, ymin, xmax, ymax` 형식으로 변환합니다.
    3.  해당 주석 파일에 매칭되는 이미지 경로를 `img_dir`에서 구성합니다.
    4.  모든 이미지 경로 리스트와 변환된 주석 리스트를 튜플 형태로 반환합니다.

### `update_image_and_anno(...)`

4개의 이미지와 주석을 결합하여 하나의 모자이크 이미지와 새로운 주석을 생성합니다.

-   **알고리즘**:
    1.  **분할점 생성**: `scale_range` 내에서 무작위로 x, y 분할점을 생성합니다. 이 점이 4개 이미지가 만나는 교차점이 됩니다.
    2.  **이미지 배치**:
        -   4개의 이미지를 각각 리사이즈하여 모자이크 캔버스의 4분면(top-left, top-right, bottom-left, bottom-right)에 배치합니다.
    3.  **바운딩 박스 변환**: 각 이미지의 바운딩 박스 좌표를 새로운 모자이크 이미지의 전체 좌표계에 맞게 스케일링하고 이동시킵니다.
    4.  **작은 박스 필터링**: 변환된 바운딩 박스 중에서 너무 작아진 것들(`filter_scale` 기준)을 제거합니다.
    5.  최종적으로 생성된 모자이크 이미지, 변환된 주석 리스트, 그리고 첫 번째 이미지의 경로를 반환합니다.

### `random_chars(number_char: int = 32) -> str`

지정된 길이의 무작위 문자열을 생성하는 유틸리티 함수입니다.

-   **용도**: 증강된 이미지와 주석 파일이 겹치지 않도록 고유한 파일 이름을 생성하는 데 사용됩니다.

### `main()`

전체 모자이크 증강 과정을 실행하는 메인 함수입니다.

-   **동작**:
    1.  `get_dataset`을 호출하여 원본 데이터를 불러옵니다.
    2.  `NUMBER_IMAGES` 횟수만큼 루프를 돌면서, 매번 4개의 이미지를 무작위로 선택하여 `update_image_and_anno`를 호출합니다.
    3.  생성된 모자이크 이미지와 주석을 `OUTPUT_DIR`에 새로운 파일로 저장합니다.
        -   주석은 다시 YOLO 형식으로 변환되어 `.txt` 파일로 저장됩니다.

## 실행 방법

1.  **필요한 라이브러리 설치**:
    ```bash
    pip install numpy opencv-python
    ```
2.  **스크립트 설정**:
    -   스크립트 상단의 `LABEL_DIR`, `IMG_DIR`, `OUTPUT_DIR` 상수를 실제 데이터셋 경로에 맞게 수정합니다.
    -   `NUMBER_IMAGES`를 생성할 모자이크 이미지의 수로 설정합니다.
3.  **실행**:
    ```bash
    python mosaic_augmentation.py
    ```

## 코드 개선 제안

1.  **하드코딩된 경로 및 파라미터 제거**: `LABEL_DIR`, `IMG_DIR`, `OUTPUT_DIR`, `NUMBER_IMAGES` 등 주요 설정값들이 코드에 하드코딩되어 있습니다. `argparse` 모듈을 사용하여 이들을 커맨드 라인 인자로 받도록 수정하면, 스크립트를 수정하지 않고도 다양한 설정으로 쉽게 실행할 수 있어 재사용성이 크게 향상됩니다.

    ```python
    # argparse 사용 예시
    import argparse

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Mosaic augmentation for object detection.")
        parser.add_argument("--label_dir", required=True, help="Path to label directory.")
        parser.add_argument("--image_dir", required=True, help="Path to image directory.")
        parser.add_argument("--output_dir", required=True, help="Path to save augmented data.")
        parser.add_argument("--num_images", type=int, default=250, help="Number of mosaic images to generate.")
        args = parser.parse_args()
        
        # main() 함수 로직을 여기에 구현하거나, args를 전달하여 호출
    ```

2.  **`update_image_and_anno` 함수의 복잡성**: 이 함수는 4개의 분기에 대해 거의 동일한 로직을 반복하고 있어 코드가 길고 복잡합니다. 각 분면(quadrant)에 대한 정보를 (시작/끝 좌표, 스케일 팩터 등) 리스트나 튜플로 정의하고, 이를 순회하는 루프로 리팩토링하면 코드 중복을 줄이고 가독성을 높일 수 있습니다.

3.  **바운딩 박스 형식 변환 로직**: `get_dataset`에서는 YOLO 형식을 `xmin, ymin, xmax, ymax`으로 변환하고, `main`에서는 다시 YOLO 형식으로 변환합니다. 이 변환 로직들을 별도의 유틸리티 함수(예: `yolo_to_xyxy`, `xyxy_to_yolo`)로 분리하면 코드가 더 명확해지고 재사용하기 좋습니다.

4.  **파일 저장 경로**: `main` 함수에서 `cv2.imwrite(f"{file_root}.jpg", ...)`와 같이 파일 경로를 구성할 때, `OUTPUT_DIR`이 존재하지 않으면 오류가 발생할 수 있습니다. `os.makedirs(OUTPUT_DIR, exist_ok=True)`를 사용하여 디렉터리가 없으면 생성하도록 하는 로직을 추가하면 안정성이 향상됩니다.

