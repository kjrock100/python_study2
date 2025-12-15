# `diophantine_equation.py` 코드 설명

이 문서는 `diophantine_equation.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 선형 디오판토스 방정식 `ax + by = c`의 정수 해를 구하는 알고리즘을 구현합니다.

## 목차
1.  디오판토스 방정식이란?
2.  함수 설명
    -   `greatest_common_divisor(a, b)`
    -   `extended_gcd(a, b)`
    -   `diophantine(a, b, c)`
    -   `diophantine_all_soln(a, b, c, n)`
3.  실행 방법
4.  코드 개선 제안

## 디오판토스 방정식이란?

디오판토스 방정식은 정수 계수를 가지며 정수 해를 구하는 다항 방정식입니다. 이 스크립트에서는 가장 기본적인 형태인 **선형 디오판토스 방정식** `ax + by = c`를 다룹니다.

이 방정식은 `gcd(a, b)` (a와 b의 최대공약수)가 `c`를 나눌 때만 정수 해 `(x, y)`를 가집니다.

## 함수 설명

### `greatest_common_divisor(a, b)`

두 정수 `a`와 `b`의 최대공약수(GCD)를 계산합니다.

-   **알고리즘**: 유클리드 호제법(Euclidean Algorithm)을 사용합니다. `a`를 `b`로 나눈 나머지를 계속해서 계산하여 나머지가 0이 될 때의 제수(나누는 수)가 최대공약수가 되는 원리를 이용합니다.
-   **반환값**: `int` 타입의 최대공약수.

```python
>>> greatest_common_divisor(10, 6)
2
>>> greatest_common_divisor(121, 11)
11
```

### `extended_gcd(a, b)`

확장 유클리드 알고리즘을 구현한 함수입니다. 이 함수는 `gcd(a, b)`를 계산할 뿐만 아니라, `ax + by = gcd(a, b)`를 만족하는 정수 `x`와 `y`를 함께 찾습니다.

-   **알고리즘**: 확장 유클리드 알고리즘(Extended Euclidean Algorithm)을 재귀적으로 구현합니다.
-   **반환값**: `(d, x, y)` 형태의 튜플. 여기서 `d`는 `gcd(a, b)`이며, `x`와 `y`는 `ax + by = d`를 만족하는 계수입니다.

```python
>>> extended_gcd(10, 6)
(2, -1, 2)  # 10*(-1) + 6*2 = 2
```

### `diophantine(a, b, c)`

디오판토스 방정식 `ax + by = c`의 **하나의 특정 해(particular solution)** `(x, y)`를 찾습니다.

-   **전제 조건**: `c`가 `gcd(a, b)`로 나누어 떨어져야 합니다. 그렇지 않으면 `AssertionError`가 발생합니다.
-   **알고리즘**:
    1.  `extended_gcd(a, b)`를 호출하여 `d, x', y'`를 얻습니다. (`ax' + by' = d`)
    2.  `c`가 `d`로 나누어 떨어지므로, `c = r * d`인 `r`을 찾습니다. (`r = c / d`)
    3.  양변에 `r`을 곱하면 `a(x'r) + b(y'r) = dr = c`가 됩니다.
    4.  따라서, 해는 `x = x' * r`, `y = y' * r` 입니다.
-   **반환값**: `(float, float)` 형태의 튜플로 된 해.

```python
>>> diophantine(10, 6, 14)
(-7.0, 14.0)  # 10*(-7.0) + 6*(14.0) = -70 + 84 = 14
```

### `diophantine_all_soln(a, b, c, n)`

디오판토스 방정식 `ax + by = c`의 **모든 일반 해(general solutions)** 중에서 `n`개를 찾아 출력합니다.

-   **알고리즘**:
    1.  `diophantine(a, b, c)`를 이용해 특정 해 `(x0, y0)`를 구합니다.
    2.  `d = gcd(a, b)`를 계산합니다.
    3.  모든 해는 다음 형태로 표현될 수 있습니다. (단, `t`는 임의의 정수)
        -   `x = x0 + t * (b / d)`
        -   `y = y0 - t * (a / d)`
    4.  `t`를 `0`부터 `n-1`까지 증가시키면서 `n`개의 해를 계산하고 출력합니다.
-   **반환값**: `None`. 해를 콘솔에 직접 출력합니다.

```python
>>> diophantine_all_soln(10, 6, 14, 4)
-7.0 14.0
-4.0 9.0
-1.0 4.0
2.0 -1.0
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 예제 코드가 실행되고 테스트됩니다.

```bash
python diophantine_equation.py
```

## 코드 개선 제안

1.  **정수형 반환**: `diophantine` 함수는 정수 해를 찾는 것이 목적이므로, `float` 대신 `int`를 반환하는 것이 더 명확합니다. `c / d` 연산을 정수 나눗셈 `c // d`으로 변경하면 됩니다.

2.  **해를 반환하도록 수정**: `diophantine_all_soln` 함수는 현재 해를 출력만 합니다. 이 함수가 해의 리스트를 반환하도록 수정하면 다른 코드에서 재사용하기가 더 용이해집니다.

    ```python
    # 개선 제안 예시
    def diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> list[tuple[int, int]]:
        (x0_f, y0_f) = diophantine(a, b, c)  # diophantine이 정수를 반환한다고 가정
        x0, y0 = int(x0_f), int(y0_f)
        d = greatest_common_divisor(a, b)
        p = a // d
        q = b // d
        
        solutions = []
        for i in range(n):
            x = x0 + i * q
            y = y0 - i * p
            solutions.append((x, y))
        return solutions
    ```