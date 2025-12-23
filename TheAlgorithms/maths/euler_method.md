# Euler Method (오일러 방법) 알고리즘

이 문서는 `euler_method.py` 파일에 구현된 **오일러 방법(Euler's Method)** 알고리즘에 대한 설명입니다.

## 개요

**오일러 방법**은 초기값이 주어진 상미분방정식(ODE)을 풀기 위한 1차 수치적 절차입니다. 이는 상미분방정식의 수치 적분을 위한 가장 기본적인 명시적(explicit) 방법입니다.

## 함수 설명

### `explicit_euler(ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float) -> np.ndarray`

오일러 방법을 사용하여 각 단계에서의 ODE 수치 해를 계산합니다.

#### 매개변수 (Parameters)

- `ode_func` (`Callable`): x와 y의 함수로서의 상미분방정식입니다 ($y' = f(x, y)$).
- `y0` (`float`): y의 초기값입니다 ($y(x_0) = y_0$).
- `x0` (`float`): x의 초기값입니다.
- `step_size` (`float`): x의 증가값(단계 크기, $h$)입니다.
- `x_end` (`float`): 계산할 x의 최종 값입니다.

#### 반환값 (Returns)

- `np.ndarray`: 각 x 단계에 대한 y의 해가 담긴 배열입니다.

#### 알고리즘 (Algorithm)

1. `x_end`, `x0`, `step_size`를 기반으로 단계 수 $N$을 계산합니다.
2. 해를 저장할 크기 $N+1$의 배열 `y`를 초기화합니다.
3. 초기 조건 `y[0] = y0`를 설정합니다.
4. $N$번 반복하며 다음을 수행합니다:
   - 공식 $y_{k+1} = y_k + h \cdot f(x_k, y_k)$를 사용하여 다음 $y$ 값을 계산합니다.
   - $x$를 업데이트합니다: $x_{k+1} = x_k + h$
5. 배열 `y`를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

**사용 예시:**

```python
# 미분방정식 y' = y (정확한 해는 y = e^x)
def f(x, y):
    return y

# 초기값 y(0)=1, x=0에서 x=5까지 0.01 간격으로 계산
y = explicit_euler(f, 1.0, 0.0, 0.01, 5)
print(y[-1]) # e^5의 근사값 출력
```
