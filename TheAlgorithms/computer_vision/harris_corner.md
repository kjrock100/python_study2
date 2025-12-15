# `harris_corner.py` 코드 설명

이 문서는 `harris_corner.py` 파이썬 스크립트에 포함된 `Harris_Corner` 클래스를 설명합니다. 이 스크립트는 이미지에서 코너(모서리)와 같은 주요 특징점을 검출하는 컴퓨터 비전 알고리즘인 **해리스 코너 검출기(Harris Corner Detector)**를 구현합니다.

## 목차
1.  해리스 코너 검출기란?
2.  `Harris_Corner` 클래스
    -   `__init__(k, window_size)`
    -   `detect(img_path)`
3.  실행 방법
4.  코드 개선 제안

## 해리스 코너 검출기란?

해리스 코너 검출기는 이미지의 특정 지점에서 작은 윈도우를 모든 방향으로 이동시켰을 때, 픽셀 값의 변화가 큰 지점을 '코너'로 판단하는 알고리즘입니다.

**알고리즘 원리**:
1.  이미지의 각 픽셀에 대해 x 방향과 y 방향의 그래디언트(기울기)를 계산합니다.
2.  각 픽셀 주변의 작은 윈도우(neighborhood) 내에서 그래디언트 정보를 사용하여 2x2 구조 텐서 행렬 `M`을 구성합니다.
3.  이 행렬 `M`의 행렬식(determinant)과 대각합(trace)을 사용하여 각 픽셀에 대한 코너 응답 함수 `R`을 계산합니다.
    -   `R = det(M) - k * (trace(M))²`
4.  `R` 값이 특정 임계값(threshold)보다 크면 해당 픽셀을 코너로 간주합니다.
    -   `R`이 크고 양수이면: 코너
    -   `R`이 크고 음수이면: 엣지(edge)
    -   `|R|`이 작으면: 평탄한(flat) 영역

## `Harris_Corner` 클래스

해리스 코너 검출 알고리즘을 캡슐화한 클래스입니다.

### `__init__(self, k: float, window_size: int)`

클래스 인스턴스를 초기화합니다.
-   `k`: 코너 응답 함수 `R`을 계산하는 데 사용되는 상수. 일반적으로 0.04에서 0.06 사이의 값을 사용합니다.
-   `window_size`: 코너를 검출할 때 고려할 주변 픽셀 윈도우의 크기.

### `detect(self, img_path: str) -> tuple[cv2.Mat, list[list[int]]]`

지정된 이미지 경로에서 코너를 검출하고, 검출된 코너가 표시된 이미지와 코너 좌표 리스트를 반환합니다.

-   **알고리즘**:
    1.  `cv2.imread()`를 사용하여 이미지를 그레이스케일로 불러옵니다.
    2.  `np.gradient()`를 사용하여 이미지의 x, y 방향 그래디언트(`dx`, `dy`)를 계산합니다.
    3.  그래디언트를 기반으로 `ixx`(`dx²`), `iyy`(`dy²`), `ixy`(`dx*dy`)를 계산합니다.
    4.  이미지의 모든 픽셀을 순회하면서, 각 픽셀 주변의 `window_size` 크기 윈도우 내에서 `ixx`, `iyy`, `ixy`의 합(`wxx`, `wyy`, `wxy`)을 구합니다. 이 값들이 구조 텐서 행렬 `M`의 요소가 됩니다.
    5.  `R = (wxx*wyy - wxy²) - k * (wxx + wyy)²` 공식을 사용하여 코너 응답 값 `R`을 계산합니다.
    6.  `R`이 특정 임계값(여기서는 0.5)보다 크면 해당 픽셀을 코너로 판단하고, `corner_list`에 추가하며 이미지에 파란색 점을 찍습니다.

## 실행 방법

1.  **필요한 라이브러리 설치**:
    ```bash
    pip install numpy opencv-python
    ```
2.  **스크립트 수정**:
    -   `if __name__ == "__main__"` 블록의 `"path_to_image"` 부분을 실제 이미지 파일 경로로 변경합니다.
3.  **실행**:
    ```bash
    python harris_corner.py
    ```
    스크립트를 실행하면 `detect.png`라는 이름으로 코너가 표시된 이미지가 저장됩니다.

## 코드 개선 제안

1.  **효율성 개선**: `detect` 함수 내의 이중 `for` 루프는 이미지의 모든 픽셀을 순회하며 매번 `sum()` 연산을 수행하므로, 이미지 크기가 클 경우 매우 비효율적입니다. 이 과정은 `cv2.cornerHarris()`라는 OpenCV 내장 함수를 사용하면 고도로 최적화된 C++ 코드로 훨씬 빠르게 수행할 수 있습니다. 교육적인 목적의 구현으로는 훌륭하지만, 실제 적용 시에는 내장 함수 사용을 고려하는 것이 좋습니다.

    ```python
    # OpenCV 내장 함수 사용 예시
    def detect_fast(self, img_path: str):
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        
        # 해리스 코너 검출
        dst = cv2.cornerHarris(gray, self.window_size, 3, self.k)
        
        # 결과 이미지에 코너 표시
        img[dst > 0.01 * dst.max()] = [0, 0, 255] # 임계값은 조절 가능
        
        return img, np.argwhere(dst > 0.01 * dst.max())
    ```

2.  **`__init__`의 `k` 값 검증**: 현재 `__init__` 메서드는 `k` 값이 정확히 `0.04` 또는 `0.06`일 때만 허용합니다. 실제로는 이 두 값 사이의 어떤 `float` 값도 유효하므로, `if not 0.04 <= k <= 0.06:`과 같이 범위를 검사하는 것이 더 유연하고 올바른 방식입니다.

3.  **하드코딩된 임계값**: `detect` 함수 내에서 코너를 판단하는 임계값(`r > 0.5`)이 하드코딩되어 있습니다. 이 값은 이미지에 따라 달라져야 할 수 있으므로, `detect` 함수의 인자로 받거나 클래스 생성 시 설정할 수 있도록 하면 유연성이 향상됩니다.

4.  **`k` 값 중복**: `detect` 함수 내에서 `k = 0.04`로 다시 정의하고 있습니다. 이는 `__init__`에서 설정한 `self.k`를 무시하게 만듭니다. 이 줄을 제거하고 `self.k`를 사용해야 클래스의 의도대로 동작합니다.

    ```diff
    --- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/computer_vision/harris_corner.py
    +++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/computer_vision/harris_corner.py
    @@ -42,7 +42,6 @@
        ixx = dx**2
        iyy = dy**2
        ixy = dx * dy
        offset = self.window_size // 2
        for y in range(offset, h - offset):
            for x in range(offset, w - offset):

                det = (wxx * wyy) - (wxy**2)
                trace = wxx + wyy
                r = det - self.k * (trace**2)
                # Can change the value
                if r > 0.5:
                    corner_list.append([x, y, r])

    ```

