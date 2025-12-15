# `cryptomath_module.py` 코드 설명

이 문서는 `cryptomath_module.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 아핀 암호(Affine Cipher)와 같은 다른 암호화 알고리즘에서 사용되는 기본적인 정수론(number theory) 함수들을 제공하는 유틸리티 모듈입니다.

## 목차
1.  모듈의 역할
2.  함수 설명
    -   `gcd(a, b)`
    -   `find_mod_inverse(a, m)`
3.  사용 방법
4.  코드 개선 제안

## 모듈의 역할

이 모듈은 암호학 계산에 필수적인 두 가지 핵심 수학 함수를 제공합니다.
-   **최대공약수(GCD)** 계산
-   **모듈러 곱셈 역원(Modular Multiplicative Inverse)** 계산

이 함수들은 다른 스크립트에서 `import`하여 재사용하도록 설계되었습니다.

## 함수 설명

### `gcd(a: int, b: int) -> int`

두 정수 `a`와 `b`의 **최대공약수(Greatest Common Divisor)**를 계산합니다.

-   **알고리즘**: **유클리드 호제법(Euclidean Algorithm)**을 사용합니다. `b % a`와 `a`를 새로운 `a`와 `b`로 계속 치환하여 `a`가 0이 될 때까지 반복합니다. 최종적으로 남는 `b` 값이 최대공약수입니다.
-   **용도**: 두 수가 서로소인지 판별하는 등 정수론의 기본적인 연산에 사용됩니다.

### `find_mod_inverse(a: int, m: int) -> int`

`a`의 **모듈러 곱셈 역원**을 모듈러 `m`에 대해 찾습니다. 즉, `(a * x) % m == 1`을 만족하는 정수 `x`를 계산합니다.

-   **알고리즘**: **확장 유클리드 알고리즘(Extended Euclidean Algorithm)**을 사용합니다. 이 알고리즘은 `ax + my = gcd(a, m)`을 만족하는 `x`와 `y`를 찾습니다. 만약 `gcd(a, m)`이 1이라면, `ax ≡ 1 (mod m)`이 성립하므로 `x`가 바로 모듈러 역원이 됩니다.
-   **오류 처리**: 모듈러 역원은 `gcd(a, m) == 1`일 때만 존재합니다. 만약 두 수가 서로소가 아니면, `ValueError`를 발생시켜 역원이 존재하지 않음을 알립니다.
-   **용도**: 아핀 암호와 같은 암호에서 복호화 키를 계산하는 데 필수적으로 사용됩니다.

## 사용 방법

이 스크립트는 직접 실행하기보다는 다른 파이썬 파일에서 모듈로 가져와서 사용합니다.

**예시 (`affine_cipher.py`에서 사용):**
```python
from . import cryptomath_module as cryptomath

# ...

def check_keys(keyA, keyB, mode):
    # ...
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        # ...

def decrypt_message(key, message):
    # ...
    modInverseOfkeyA = cryptomath.find_mod_inverse(keyA, len(SYMBOLS))
    # ...
```

## 코드 개선 제안

1.  **`doctest` 추가**: 각 함수에 `doctest`를 추가하면 모듈의 정확성을 자체적으로 검증할 수 있어 유지보수성과 신뢰성이 향상됩니다.

    ```python
    # 개선 제안 예시
    def gcd(a: int, b: int) -> int:
        """
        >>> gcd(12, 8)
        4
        >>> gcd(60, 48)
        12
        """
        while a != 0:
            a, b = b % a, a
        return b
    ```

2.  **알고리즘 주석**: `find_mod_inverse` 함수 내부에 확장 유클리드 알고리즘의 각 변수(`u1`, `v1` 등)가 어떤 역할을 하는지에 대한 간략한 주석을 추가하면 코드를 처음 보는 사람이 알고리즘을 이해하는 데 도움이 됩니다.
