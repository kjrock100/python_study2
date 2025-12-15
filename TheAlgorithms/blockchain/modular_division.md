# `modular_division.py` 코드 설명

이 문서는 `modular_division.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 모듈러 연산 환경에서 나눗셈, 즉 모듈러 곱셈 역원(modular multiplicative inverse)을 계산하는 알고리즘을 구현합니다.

## 목차
1.  모듈러 나눗셈이란?
2.  함수 설명
    -   `greatest_common_divisor(a, b)`
    -   `extended_gcd(a, b)`
    -   `extended_euclid(a, b)`
    -   `invert_modulo(a, n)`
    -   `modular_division(a, b, n)`
    -   `modular_division2(a, b, n)`
3.  실행 방법
4.  코드 개선 제안

## 모듈러 나눗셈이란?

모듈러 연산에서 `b / a (mod n)`을 계산하는 것은 `b * a⁻¹ (mod n)`을 계산하는 것과 같습니다. 여기서 `a⁻¹`은 `a`의 **모듈러 곱셈 역원**을 의미합니다.

`a`의 모듈러 곱셈 역원은 `a * x ≡ 1 (mod n)`을 만족하는 정수 `x`입니다. 이 역원은 `gcd(a, n) = 1`일 때만 존재합니다. 이 스크립트는 확장 유클리드 알고리즘을 사용하여 이 역원을 찾고, 이를 통해 모듈러 나눗셈을 수행합니다.

## 함수 설명

### `greatest_common_divisor(a, b)`

두 정수 `a`와 `b`의 최대공약수(GCD)를 계산합니다.

-   **알고리즘**: 유클리드 호제법(Euclidean Algorithm)을 사용합니다.
-   **반환값**: `int` 타입의 최대공약수.

### `extended_gcd(a, b)`

확장 유클리드 알고리즘을 구현한 함수입니다. `gcd(a, b)`와 함께, `ax + by = gcd(a, b)`를 만족하는 계수 `x`, `y`를 찾습니다.

-   **알고리즘**: 확장 유클리드 알고리즘(Extended Euclidean Algorithm)을 재귀적으로 구현합니다.
-   **반환값**: `(d, x, y)` 형태의 튜플. `d`는 `gcd(a, b)`입니다.

### `extended_euclid(a, b)`

`extended_gcd`와 유사하게 확장 유클리드 알고리즘을 구현했지만, 최대공약수를 제외한 계수 `x`, `y`만 반환합니다.

-   **알고리즘**: 확장 유클리드 알고리즘을 재귀적으로 구현합니다.
-   **반환값**: `(x, y)` 형태의 튜플. `ax + by = gcd(a, b)`를 만족합니다.

### `invert_modulo(a, n)`

`a`의 모듈러 곱셈 역원 `a⁻¹ (mod n)`을 계산합니다.

-   **알고리즘**: `extended_euclid(a, n)`를 호출하여 `ax + ny = gcd(a, n)`을 만족하는 `x`, `y`를 찾습니다. `gcd(a, n) = 1`일 때, `ax ≡ 1 (mod n)`이므로 `x`가 바로 모듈러 역원입니다.
-   **반환값**: `int` 타입의 모듈러 역원.

```python
>>> invert_modulo(2, 5)  # 2 * 3 = 6 ≡ 1 (mod 5)
3
```

### `modular_division(a, b, n)`

모듈러 나눗셈 `b / a (mod n)`을 계산합니다.

-   **전제 조건**: `gcd(a, n) = 1`이어야 합니다. 그렇지 않으면 `AssertionError`가 발생합니다.
-   **알고리즘**:
    1.  `extended_gcd(n, a)`를 호출하여 `nt + as = gcd(n, a)`를 만족하는 `s`를 찾습니다. `s`가 `a`의 역원입니다.
    2.  `x = (b * s) % n`을 계산하여 결과를 반환합니다.
-   **반환값**: `int` 타입의 모듈러 나눗셈 결과.

```python
>>> modular_division(4, 8, 5)  # 8 / 4 ≡ 8 * 4⁻¹ ≡ 8 * 4 ≡ 32 ≡ 2 (mod 5)
2
```

### `modular_division2(a, b, n)`

`modular_division`과 동일한 기능을 수행하지만, 내부적으로 `invert_modulo` 함수를 사용합니다.

-   **알고리즘**:
    1.  `invert_modulo(a, n)`를 호출하여 `a`의 역원을 구합니다.
    2.  역원을 `b`와 곱한 후 모듈러 `n` 연산을 수행합니다.
-   **반환값**: `int` 타입의 모듈러 나눗셈 결과.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 예제 코드가 실행되고 테스트됩니다.

```bash
python modular_division.py
```

## 코드 개선 제안

1.  **함수 중복 제거**: `extended_gcd`와 `extended_euclid`는 거의 동일한 알고리즘을 기반으로 합니다. `extended_gcd`가 더 많은 정보(GCD 자체)를 반환하므로, `extended_euclid`를 제거하고 모든 호출을 `extended_gcd`를 사용하도록 통일할 수 있습니다.

2.  **의존성 통합**: `modular_division`과 `modular_division2`는 같은 작업을 수행합니다. `invert_modulo`를 사용하는 `modular_division2`의 방식이 더 직관적이므로, `modular_division`을 제거하고 `modular_division2`의 이름을 `modular_division`으로 변경하여 코드를 단순화할 수 있습니다.

3.  **외부 의존성 명시**: 이 스크립트는 `diophantine_equation.py`에 있는 `greatest_common_divisor`와 `extended_gcd` 함수를 암묵적으로 사용하고 있습니다. 코드의 재사용성과 명확성을 위해 이 함수들을 직접 임포트(`from diophantine_equation import greatest_common_divisor, extended_gcd`)하거나, 이 파일 내에 유지할 경우 중복임을 명시하는 것이 좋습니다. 현재는 같은 파일 내에 중복 정의되어 있습니다.

아래는 위 제안들을 반영한 개선된 `invert_modulo` 함수 예시입니다.

```python
# 개선 제안 예시
def invert_modulo(a: int, n: int) -> int:
    """
    Finds the modular multiplicative inverse of a modulo n.
    a has a multiplicative inverse modulo n iff gcd(a,n) = 1.
    """
    d, x, y = extended_gcd(a, n)  # extended_gcd가 (d, x, y)를 반환한다고 가정
    if d != 1:
        raise ValueError(f"Modular inverse does not exist for {a} mod {n}")
    
    # ax + ny = 1  => ax ≡ 1 (mod n)
    # x가 음수일 수 있으므로 양수로 변환
    return x % n

def modular_division(a: int, b: int, n: int) -> int:
    """
    Calculates (b / a) mod n, which is (b * a⁻¹) mod n.
    """
    assert n > 1
    inverse_a = invert_modulo(a, n)
    return (b * inverse_a) % n
```