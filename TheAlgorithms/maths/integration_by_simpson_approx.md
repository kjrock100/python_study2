# Simpson's Approximation (심슨 공식) 적분 알고리즘

이 문서는 `integration_by_simpson_approx.py` 파일에 구현된 **심슨 공식(Simpson's Rule)**을 이용한 수치 적분 알고리즘에 대한 설명입니다.

## 개요

**심슨 공식**은 수치 해석에서 정적분 값을 근사하는 방법 중 하나입니다. 적분 구간을 작은 구간으로 나누고, 각 구간을 2차 함수(포물선)로 근사하여 면적을 구합니다. 사다리꼴 공식보다 일반적으로 더 높은 정확도를 가집니다.

## 함수 설명

### `simpson_integration(function, a: float, b: float, precision: int = 4) -> float`

주어진 함수 `function`에 대해 구간 $[a, b]$에서의 정적분 값을 심슨 공식을 사용하여 근사 계산합니다.

#### 매개변수 (Parameters)

- `function` (`Callable`): 적분할 함수입니다. 실수(float) 또는 정수(int)를 입력받아 실수 또는 정수를 반환해야 합니다.
- `a` (`float` | `int`): 적분 구간의 하한(시작점)입니다.
- `b` (`float` | `int`): 적분 구간의 상한(끝점)입니다.
- `precision` (`int`): 결과값의 소수점 반올림 자릿수입니다. (기본값: 4)

#### 예외 처리 (Error Handling)

다음과 같은 경우 `AssertionError`가 발생합니다:

- `function`이 호출 가능한 객체(callable)가 아닌 경우.
- `a` 또는 `b`가 실수나 정수가 아닌 경우.
- `function(a)`의 반환값이 실수나 정수가 아닌 경우.
- `precision`이 양의 정수가 아닌 경우.

#### 알고리즘 (Algorithm)

1. 적분 구간을 `N_STEPS`(코드 내 상수로 1000으로 정의됨) 등분합니다. 각 구간의 너비 $h = (b - a) / N\_STEPS$를 계산합니다.
2. 양 끝점에서의 함수값 $f(a) + f(b)$를 초기 합계로 설정합니다.
3. 1부터 `N_STEPS - 1`까지 반복하며 중간 지점들의 함수값을 더합니다:
   - 홀수 번째 지점($x_1, x_3, \dots$)에는 가중치 **4**를 곱합니다.
   - 짝수 번째 지점($x_2, x_4, \dots$)에는 가중치 **2**를 곱합니다.
4. 최종 합계에 $\frac{h}{3}$을 곱하여 적분 값을 구합니다.
5. 지정된 `precision`에 맞춰 반올림하여 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
