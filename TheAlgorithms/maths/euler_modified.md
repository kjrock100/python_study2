# Euler Modified Method (수정된 오일러 방법) 알고리즘

이 문서는 `euler_modified.py` 파일에 구현된 **수정된 오일러 방법(Modified Euler Method)**, 또는 **호인 방법(Heun's Method)** 알고리즘에 대한 설명입니다.

## 개요

기본적인 오일러 방법은 구현이 간단하지만 오차가 클 수 있습니다. 수정된 오일러 방법은 **예측-수정(Predictor-Corrector)** 방식을 사용하여 근사해의 정확도를 높인 방법입니다.

## 함수 설명

### `euler_modified(ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float) -> np.array`

수정된 오일러 방법을 사용하여 주어진 구간에서 상미분방정식(ODE)의 수치 해를 계산합니다.

#### 매개변수 (Parameters)

- `ode_func` (`Callable`): $y' = f(x, y)$ 형태의 상미분방정식을 정의하는 함수입니다.
- `y0` (`float`): $y$의 초기값입니다 ($y(x_0) = y_0$).
- `x0` (`float`): $x$의 초기값입니다.
- `step_size` (`float`): $x$의 증가값(단계 크기, $h$)입니다.
- `x_end` (`float`): 계산을 종료할 $x$의 값입니다.

#### 반환값 (Returns)

- `np.array`: 각 단계별 $x$에 대응하는 $y$의 근사해들이 담긴 NumPy 배열입니다.

#### 알고리즘 (Algorithm)

1. 전체 구간 길이와 단계 크기를 이용하여 반복 횟수 $N$을 계산합니다.
2. 결과 배열 `y`를 초기화하고 초기값 `y0`를 설정합니다.
3. $N$번 반복하며 다음 과정을 수행합니다:
   - **예측 단계 (Predictor)**: 기본 오일러 공식을 사용하여 다음 지점의 임시 값($y_{predict}$)을 예측합니다.
     $$ y\_{predict} = y_k + h \cdot f(x_k, y_k) $$
   - **수정 단계 (Corrector)**: 현재 기울기와 예측된 지점의 기울기의 평균을 사용하여 값을 수정합니다.
     $$ y*{k+1} = y_k + \frac{h}{2} \left( f(x_k, y_k) + f(x*{k+1}, y\_{predict}) \right) $$
   - $x$ 값을 업데이트합니다 ($x_{k+1} = x_k + h$).
4. 계산된 `y` 배열을 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

**사용 예시:**

```python
# 미분방정식 y' = -2*x*(y^2)
def f1(x, y):
    return -2 * x * (y**2)

# 초기값 y(0)=1.0, x=0에서 x=1.0까지 0.2 간격으로 계산
y = euler_modified(f1, 1.0, 0.0, 0.2, 1.0)
print(y[-1])
```
