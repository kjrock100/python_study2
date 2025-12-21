# 줄리아 집합 (Julia Sets)

이 문서는 `julia_sets.py` 파일에 구현된 **줄리아 집합** 생성 및 시각화 알고리즘에 대해 설명합니다.

## 개요

줄리아 집합은 복소수 평면에서 정의된 프랙탈의 일종입니다. 이 코드는 2차 다항식($f(z) = z^2 + c$)과 지수 맵($f(z) = e^z + c$)에 대한 줄리아 집합을 계산하고 `matplotlib`를 사용하여 시각화합니다.

알고리즘은 복소평면의 각 점 $z_0$에서 시작하여 함수를 반복적으로 적용($z_{n+1} = f(z_n)$)했을 때, 그 값이 특정 임계값(탈출 반경, escape radius)을 벗어나는지 여부를 판별하여 집합을 그립니다.

## 주요 함수

### `eval_exponential(c_parameter, z_values)`
- **목적**: 지수 함수 $e^z + c$를 계산합니다.
- **매개변수**: 상수 `c_parameter`와 현재 $z$ 값들의 배열 `z_values`.

### `eval_quadratic_polynomial(c_parameter, z_values)`
- **목적**: 2차 다항식 $z^2 + c$를 계산합니다.
- **매개변수**: 상수 `c_parameter`와 현재 $z$ 값들의 배열 `z_values`.

### `prepare_grid(window_size, nb_pixels)`
- **목적**: 시각화할 복소수 평면의 그리드를 생성합니다.
- **매개변수**:
  - `window_size`: 실수부와 허수부의 범위 ($\pm$ `window_size`).
  - `nb_pixels`: 그리드의 해상도 (픽셀 수).
- **반환값**: 복소수 좌표가 담긴 2차원 `numpy` 배열.

### `iterate_function(eval_function, function_params, nb_iterations, z_0, infinity=None)`
- **목적**: 주어진 함수를 지정된 횟수만큼 반복 적용합니다.
- **동작**:
  - `numpy`의 벡터화 연산을 사용하여 그리드 전체에 대해 동시에 계산을 수행합니다.
  - 계산 중 값이 너무 커지거나(overflow) 정의되지 않은 값(NaN)이 되는 경우를 처리하기 위해 `infinity` 값을 사용합니다.

### `show_results(function_label, function_params, escape_radius, z_final)`
- **목적**: 최종 계산된 $z$ 값들의 절댓값이 탈출 반경보다 작은지 확인하여 이미지를 생성하고 출력합니다.
- **도구**: `matplotlib.pyplot.matshow`를 사용합니다.

## 실행 예시

스크립트를 실행하면 다음과 같은 줄리아 집합들이 순차적으로 표시됩니다:

1. **Cauliflower Julia Set**: $c = 0.25$ 인 경우.
2. **Polynomial Example 1**: $c = -0.4 + 0.6i$ 인 경우.
3. **Polynomial Example 2**: $c = -0.1 + 0.651i$ 인 경우.
4. **Exponential Map**: $c = -2.0$ 인 지수 함수 맵.

## 주의 사항

- **경고 무시**: 반복 계산 중 발생하는 오버플로우 경고 등을 무시하기 위해 `ignore_overflow_warnings()` 함수가 사용됩니다. 이는 `numpy`를 사용한 고속 연산 과정에서 자연스럽게 발생하는 현상을 처리하기 위함입니다.
- **의존성**: 이 코드를 실행하려면 `numpy`와 `matplotlib` 라이브러리가 필요합니다.
