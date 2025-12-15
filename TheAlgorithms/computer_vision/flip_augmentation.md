# `flip_augmentation.py` 코드 설명

이 문서는 `flip_augmentation.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 컴퓨터 비전 작업, 특히 객체 탐지(object detection)를 위한 **데이터 증강(Data Augmentation)** 기법 중 하나인 **이미지 뒤집기(Flip Augmentation)**를 구현합니다.

## 목차
1.  플립 증강(Flip Augmentation)이란?
2.  함수 설명
    -   `get_dataset(label_dir, img_dir)`
    -   `update_image_and_anno(img_list, anno_list, flip_type)`
    -   `random_chars(number_char)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 플립 증강(Flip Augmentation)이란?

데이터 증강은 기존 훈련 데이터에 약간의 변형을 가하여 데이터의 양을 인위적으로 늘리는 기술입니다. 이를 통해 모델이 더 다양한 패턴을 학습하여 과적합(overfitting)을 방지하고 일반화 성능을 높일 수 있습니다.

**플립 증강**은 이미지를 수평 또는 수직으로 뒤집는 가장 간단하면서도 효과적인 데이터 증강 방법 중 하나입니다. 객체 탐지 데이터셋에 이 기법을 적용할 때는, 이미지를 뒤집는 것뿐만 아니라 이미지 내의 객체 위치를 나타내는 **바운딩 박스(bounding box) 좌표**도 함께 변환해주어야 합니다.

## 함수 설명

### `get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]`

지정된 디렉터리에서 이미지 경로와 해당 이미지의 바운딩 박스 주석(annotation)을 불러옵니다.

-   **알고리즘**:
    1.  `label_dir`에서 모든 `.txt` 주석 파일을 찾습니다.
    2.  각 주석 파일을 읽어 YOLO 형식(`class_id x_center y_center width height`)의 바운딩 박스 정보를 파싱합니다.
    3.  해당 주석 파일에 매칭되는 이미지 경로를 `img_dir`에서 구성합니다.
    4.  모든 이미지 경로 리스트와 주석 리스트를 튜플 형태로 반환합니다.

### `update_image_and_anno(img_list: list, anno_list: list, flip_type: int) -> tuple[list, list, list]`

이미지와 해당 바운딩 박스 주석을 지정된 방향으로 뒤집습니다.

-   **인자**:
    -   `flip_type`: 뒤집기 유형. `1`은 수평 뒤집기, `0`은 수직 뒤집기입니다.
-   **알고리즘**:
    1.  입력된 모든 이미지를 순회합니다.
    2.  `cv2.flip()` 함수를 사용하여 이미지를 뒤집습니다.
    3.  `flip_type`에 따라 바운딩 박스의 중심 좌표를 변환합니다.
        -   **수평 뒤집기**: `새로운 x_center = 1 - 기존 x_center`
        -   **수직 뒤집기**: `새로운 y_center = 1 - 기존 y_center`
    4.  변환된 이미지 리스트, 주석 리스트, 그리고 원본 경로 리스트를 반환합니다.

### `random_chars(number_char: int = 32) -> str`

지정된 길이의 무작위 문자열을 생성하는 유틸리티 함수입니다.

-   **용도**: 증강된 이미지와 주석 파일이 겹치지 않도록 고유한 파일 이름을 생성하는 데 사용됩니다.

### `main()`

전체 플립 증강 과정을 실행하는 메인 함수입니다.

-   **동작**:
    1.  `get_dataset`을 호출하여 원본 데이터를 불러옵니다.
    2.  `update_image_and_anno`를 호출하여 모든 이미지와 주석을 뒤집습니다.
    3.  변환된 각 이미지와 주석을 `OUTPUT_DIR`에 새로운 파일로 저장합니다.
        -   이미지는 `.jpg` 형식으로 저장됩니다.
        -   주석은 YOLO 형식의 `.txt` 파일로 저장됩니다.

## 실행 방법

1.  **필요한 라이브러리 설치**:
    ```bash
    pip install opencv-python
    ```
2.  **스크립트 설정**:
    -   스크립트 상단의 `LABEL_DIR`, `IMAGE_DIR`, `OUTPUT_DIR` 상수를 실제 데이터셋 경로에 맞게 수정합니다.
    -   `FLIP_TYPE`을 `1`(수평) 또는 `0`(수직)으로 설정합니다.
3.  **실행**:
    ```bash
    python flip_augmentation.py
    ```

## 코드 개선 제안

1.  **하드코딩된 경로 및 파라미터 제거**: `LABEL_DIR`, `IMAGE_DIR`, `OUTPUT_DIR`, `FLIP_TYPE`과 같은 주요 설정값들이 코드에 하드코딩되어 있습니다. `argparse` 모듈을 사용하여 이들을 커맨드 라인 인자로 받도록 수정하면, 스크립트를 수정하지 않고도 다양한 설정으로 쉽게 실행할 수 있어 재사용성이 크게 향상됩니다.

    ```python
    # argparse 사용 예시
    import argparse

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Flip augmentation for object detection.")
        parser.add_argument("--label_dir", required=True, help="Path to label directory.")
        parser.add_argument("--image_dir", required=True, help="Path to image directory.")
        parser.add_argument("--output_dir", required=True, help="Path to save augmented data.")
        parser.add_argument("--flip_type", type=int, default=1, help="0 for vertical, 1 for horizontal.")
        args = parser.parse_args()
        
        # main() 함수 로직을 여기에 구현하거나, args를 전달하여 호출
    ```

2.  **파일 저장 경로 오류 수정**: `main` 함수에서 `cv2.imwrite(f"/{file_root}.jpg", ...)`와 같이 파일 경로가 슬래시(`/`)로 시작합니다. 이는 파일 시스템의 루트 디렉터리에 저장하려는 시도로, 대부분의 경우 권한 오류를 발생시킵니다. `f"{file_root}.jpg"`로 수정하여 현재 작업 디렉터리 또는 `OUTPUT_DIR`에 상대적인 경로로 저장해야 합니다.

    ```diff
    --- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/computer_vision/flip_augmentation.py
    +++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/computer_vision/flip_augmentation.py
    @@ -35,12 +35,12 @@
         letter_code = random_chars(32)
         file_name = paths[index].split(os.sep)[-1].rsplit(".", 1)[0]
         file_root = f"{OUTPUT_DIR}/{file_name}_FLIP_{letter_code}"
-        cv2.imwrite(f"/{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])
+        cv2.imwrite(f"{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])
         print(f"Success {index+1}/{len(new_images)} with {file_name}")
         annos_list = []
         for anno in new_annos[index]:
             obj = f"{anno[0]} {anno[1]} {anno[2]} {anno[3]} {anno[4]}"
             annos_list.append(obj)
-        with open(f"/{file_root}.txt", "w") as outfile:
+        with open(f"{file_root}.txt", "w") as outfile:
             outfile.write("\n".join(line for line in annos_list))
    ```

3.  **바운딩 박스 형식 변환**: `get_dataset`에서 YOLO 형식을 내부 형식으로 변환하고, `main`에서 다시 YOLO 형식으로 변환하여 저장하는 과정이 있습니다. 이 변환 로직을 별도의 유틸리티 함수(예: `yolo_to_xyxy`, `xyxy_to_yolo`)로 분리하면 코드가 더 명확해지고 재사용하기 좋습니다.

