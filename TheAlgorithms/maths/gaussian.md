# Gaussian Function (가우스 함수) 알고리즘

이 문서는 `gaussian.py` 파일에 구현된 **가우스 함수(Gaussian Function)** 계산 알고리즘에 대한 설명입니다.

## 개요

**가우스 함수**는 정규 분포(Normal Distribution)를 나타내는 함수로, 통계학, 자연과학, 공학 등 다양한 분야에서 널리 사용됩니다. 종 모양(bell curve)의 그래프를 가지며, 중심(평균, $\mu$)과 너비(표준 편차, $\sigma$)에 의해 모양이 결정됩니다.

수식은 다음과 같습니다:
$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} $$

## 함수 설명

### `gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> int`

주어진 입력값 `x`에 대한 가우스 함수 값을 계산하여 반환합니다.

> **참고**: 코드의 타입 힌트에는 반환값이 `int`로 표기되어 있으나, 실제로는 부동소수점(`float`) 또는 NumPy 배열(`numpy.ndarray`)을 반환합니다.

#### 매개변수 (Parameters)

- `x`: 입력 변수. 숫자(int, float) 또는 NumPy 배열이 될 수 있습니다.
- `mu` (`float`): 평균(Mean) 또는 기댓값. 분포의 중심을 나타냅니다. (기본값: 0.0)
- `sigma` (`float`): 표준 편차(Standard Deviation). 분포의 너비를 나타냅니다. (기본값: 1.0)

#### 반환값 (Returns)

- 계산된 가우스 함수 값 (확률 밀도).

#### 알고리즘 (Algorithm)

NumPy 라이브러리의 `exp`, `pi`, `sqrt` 함수를 사용하여 가우스 함수 공식을 직접 구현했습니다.

1. 정규화 상수 $\frac{1}{\sqrt{2\pi\sigma^2}}$를 계산합니다.
2. 지수 부분 $e^{-\frac{(x-\mu)^2}{2\sigma^2}}$를 계산합니다.
3. 두 값을 곱하여 결과를 반환합니다.

## 사용 예시

이 함수는 단일 숫자뿐만 아니라 NumPy 배열도 지원하므로, 이미지 처리(가우시안 블러 등)에도 활용될 수 있습니다.

```python
import numpy as np
x = np.arange(5)
print(gaussian(x))
# 출력: [0.39894228 0.24197072 0.05399097 0.00443185 0.00013383]
```

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
