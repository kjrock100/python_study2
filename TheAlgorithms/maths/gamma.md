# Gamma Function (Integral) 알고리즘

이 문서는 `gamma.py` 파일에 구현된 **감마 함수(Gamma Function)** 계산 알고리즘(적분 이용)에 대한 설명입니다.

## 개요

**감마 함수** $\Gamma(z)$는 팩토리얼 함수를 복소수 평면으로 확장한 특수 함수입니다. 실수부 $Re(z) > 0$인 복소수에 대해 다음과 같은 적분으로 정의됩니다.

$$ \Gamma(z) = \int_0^\infty x^{z-1} e^{-x} dx $$

이 구현은 `scipy.integrate.quad` 함수를 사용하여 위 적분을 수치적으로 계산합니다.

## 함수 설명

### `gamma(num: float) -> float`

주어진 숫자 `num`에 대한 감마 함수 값을 적분을 통해 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `num` (`float`): 감마 함수 값을 계산할 실수입니다. (단, 0보다 커야 합니다.)

#### 예외 처리 (Error Handling)

- **ValueError**: `num`이 0 이하인 경우 "math domain error" 에러가 발생합니다. 감마 함수는 0 이하의 정수에서 정의되지 않으며, 이 구현에서는 0 이하의 모든 수에 대해 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력값 `num`이 0 이하인지 확인합니다.
2. `scipy.integrate.quad`를 사용하여 0부터 무한대(`numpy.inf`)까지 `integrand` 함수를 적분합니다.
3. 적분 결과값(값, 오차 중 값만)을 반환합니다.

### `integrand(x: float, z: float) -> float`

감마 함수의 피적분 함수입니다.

$$ f(x; z) = x^{z-1} e^{-x} $$

#### 매개변수 (Parameters)

- `x` (`float`): 적분 변수.
- `z` (`float`): 감마 함수의 입력값 (고정된 매개변수).

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    from doctest import testmod

    testmod()
```
