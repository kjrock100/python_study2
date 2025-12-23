# Area (면적 및 겉넓이) 알고리즘

이 문서는 `area.py` 파일에 구현된 다양한 기하학적 도형의 **면적(Area)** 및 **겉넓이(Surface Area)** 계산 알고리즘에 대한 설명입니다.

## 개요

정사각형, 직사각형, 삼각형, 원 등의 2차원 도형의 면적과 정육면체, 구, 원뿔, 원기둥 등의 3차원 도형의 겉넓이를 구하는 함수들을 제공합니다.

## 함수 설명

### 겉넓이 (Surface Area) 계산 함수

#### `surface_area_cube(side_length: float) -> float`

정육면체의 겉넓이를 계산합니다.

- **공식**: $6 \times a^2$ ($a$: 한 변의 길이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `surface_area_sphere(radius: float) -> float`

구의 겉넓이를 계산합니다.

- **공식**: $4 \times \pi \times r^2$ ($r$: 반지름)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `surface_area_hemisphere(radius: float) -> float`

반구의 겉넓이(곡면 + 밑면)를 계산합니다.

- **공식**: $3 \times \pi \times r^2$ ($r$: 반지름)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `surface_area_cone(radius: float, height: float) -> float`

원뿔의 겉넓이를 계산합니다.

- **공식**: $\pi r (r + \sqrt{h^2 + r^2})$ ($r$: 반지름, $h$: 높이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `surface_area_cylinder(radius: float, height: float) -> float`

원기둥의 겉넓이를 계산합니다.

- **공식**: $2 \pi r (h + r)$ ($r$: 반지름, $h$: 높이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

### 면적 (Area) 계산 함수

#### `area_rectangle(length: float, width: float) -> float`

직사각형의 넓이를 계산합니다.

- **공식**: $l \times w$ ($l$: 가로, $w$: 세로)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_square(side_length: float) -> float`

정사각형의 넓이를 계산합니다.

- **공식**: $a^2$ ($a$: 한 변의 길이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_triangle(base: float, height: float) -> float`

밑변과 높이가 주어졌을 때 삼각형의 넓이를 계산합니다.

- **공식**: $\frac{1}{2} \times b \times h$ ($b$: 밑변, $h$: 높이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_triangle_three_sides(side1: float, side2: float, side3: float) -> float`

세 변의 길이가 주어졌을 때 헤론의 공식(Heron's formula)을 사용하여 삼각형의 넓이를 계산합니다.

- **공식**: $\sqrt{s(s-a)(s-b)(s-c)}$ (단, $s = \frac{a+b+c}{2}$)
- **예외 처리**:
  - 입력값이 음수일 경우 `ValueError` 발생.
  - 세 변의 길이가 삼각형 성립 조건(두 변의 합 > 나머지 한 변)을 만족하지 않을 경우 `ValueError` 발생.

#### `area_parallelogram(base: float, height: float) -> float`

평행사변형의 넓이를 계산합니다.

- **공식**: $b \times h$ ($b$: 밑변, $h$: 높이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_trapezium(base1: float, base2: float, height: float) -> float`

사다리꼴의 넓이를 계산합니다.

- **공식**: $\frac{1}{2} (a + b) h$ ($a, b$: 윗변과 아랫변, $h$: 높이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_circle(radius: float) -> float`

원의 넓이를 계산합니다.

- **공식**: $\pi r^2$ ($r$: 반지름)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_ellipse(radius_x: float, radius_y: float) -> float`

타원의 넓이를 계산합니다.

- **공식**: $\pi \times a \times b$ ($a, b$: 장축과 단축의 반지름)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

#### `area_rhombus(diagonal_1: float, diagonal_2: float) -> float`

마름모의 넓이를 계산합니다.

- **공식**: $\frac{1}{2} \times d_1 \times d_2$ ($d_1, d_2$: 두 대각선의 길이)
- **예외 처리**: 입력값이 음수일 경우 `ValueError` 발생.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증하고, 각 도형에 대한 예제 계산 결과를 출력합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # verbose so we can see methods missing tests

    print("[DEMO] Areas of various geometric shapes: \n")
    print(f"Rectangle: {area_rectangle(10, 20) = }")
    # ... (생략) ...
    print(f"Cylinder: {surface_area_cylinder(10, 20) = }")
```
