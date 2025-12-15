# `hill_cipher.py` 코드 설명

이 문서는 `hill_cipher.py` 파이썬 스크립트에 포함된 `HillCipher` 클래스를 설명합니다. 이 스크립트는 선형대수학의 행렬 연산을 기반으로 하는 다중 문자 치환 암호인 **힐 암호(Hill Cipher)**를 구현합니다.

## 목차
1.  힐 암호란?
2.  `HillCipher` 클래스
    -   `__init__(encrypt_key)`
    -   `replace_letters(letter)`
    -   `replace_digits(num)`
    -   `check_determinant()`
    -   `process_text(text)`
    -   `encrypt(text)`
    -   `make_decrypt_key()`
    -   `decrypt(text)`
3.  실행 방법
4.  코드 개선 제안

## 힐 암호란?

힐 암호는 평문을 여러 개의 블록으로 나눈 뒤, 각 블록을 숫자 벡터로 변환하고, 이 벡터에 암호화 키 역할을 하는 정사각 행렬을 곱하여 암호화하는 방식입니다.

**암호화 과정**:
1.  평문을 N글자씩 블록으로 나눕니다. (N은 키 행렬의 차원)
2.  각 블록의 문자들을 숫자 벡터로 변환합니다. (A=0, B=1, ..., 9=35)
3.  `암호화된 벡터 = (키 행렬 × 평문 벡터) mod 36` 공식을 사용하여 암호화된 벡터를 계산합니다.
4.  암호화된 벡터의 숫자들을 다시 문자로 변환하여 암호문을 만듭니다.

복호화를 위해서는 키 행렬의 **모듈러 곱셈 역행렬**이 필요하며, 이는 키 행렬의 행렬식(determinant)이 모듈러 값(이 스크립트에서는 36)과 서로소일 때만 존재합니다.

> **참고**: 이 스크립트는 `numpy` 라이브러리를 사용하여 행렬 연산을 수행합니다.

## `HillCipher` 클래스

힐 암호화 및 복호화 기능을 캡슐화한 클래스입니다.

### `__init__(encrypt_key: numpy.ndarray)`

클래스 인스턴스를 초기화합니다.
-   `encrypt_key`: 암호화에 사용할 NxN 크기의 `numpy` 배열.
-   `check_determinant()`를 호출하여 키 행렬의 유효성을 검사합니다.

### `replace_letters(letter: str) -> int`

알파벳 또는 숫자를 해당하는 정수로 변환합니다. (A=0, ..., Z=25, 0=26, ..., 9=35)

### `replace_digits(num: int) -> str`

정수를 해당하는 알파벳 또는 숫자로 변환합니다.

### `check_determinant()`

키 행렬의 행렬식이 모듈러 36에 대해 곱셈 역원을 갖는지(즉, 36과 서로소인지) 확인합니다. 역원이 존재하지 않으면 `ValueError`를 발생시켜 유효하지 않은 키임을 알립니다.

### `process_text(text: str) -> str`

입력 텍스트를 암호화/복호화에 적합한 형태로 전처리합니다.
-   **동작**:
    1.  텍스트를 대문자로 변환하고, 알파벳과 숫자만 남깁니다.
    2.  텍스트의 길이가 키 행렬의 차원(`break_key`)의 배수가 되도록, 필요하면 마지막 문자를 반복하여 추가합니다.

### `encrypt(text: str) -> str`

주어진 텍스트를 힐 암호로 **암호화**합니다.

-   **알고리즘**:
    1.  `process_text`로 텍스트를 전처리합니다.
    2.  텍스트를 `break_key` 크기의 블록으로 나눕니다.
    3.  각 블록을 숫자 벡터로 변환하고, 키 행렬과 곱한 후 모듈러 36 연산을 수행합니다.
    4.  결과 벡터를 다시 문자열로 변환하여 암호문을 생성합니다.

### `make_decrypt_key() -> numpy.ndarray`

암호화 키 행렬의 **모듈러 곱셈 역행렬**을 계산하여 복호화 키를 생성합니다.

-   **알고리즘**:
    1.  키 행렬의 행렬식(`det`)을 계산합니다.
    2.  행렬식의 모듈러 36 곱셈 역원(`det_inv`)을 찾습니다.
    3.  `복호화 키 = (det_inv * det * 키의 역행렬) mod 36` 공식을 사용하여 복호화 키를 계산합니다.

### `decrypt(text: str) -> str`

암호화된 텍스트를 원래의 평문으로 **복호화**합니다.

-   **알고리즘**: `encrypt`와 유사하지만, 암호화 키 대신 `make_decrypt_key`로 생성된 복호화 키를 사용하여 행렬 곱셈을 수행합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자로부터 키 행렬의 차원과 각 행의 값을 입력받은 후, 암호화 또는 복호화를 수행할 수 있는 대화형 메뉴가 나타납니다.

```bash
python hill_cipher.py
```

**실행 예시:**
```
Enter the order of the encryption key: 2
Enter each row of the encryption key with space separated integers
2 5
1 6
Would you like to encrypt or decrypt some text? (1 or 2)

1. Encrypt
2. Decrypt
1
What text would you like to encrypt?: hello
Your encrypted text is:
85FF00
```

## 코드 개선 제안

1.  **`greatest_common_divisor` 함수**: 이 스크립트 내에 `gcd` 함수가 구현되어 있지만, 파이썬 3.9 이상에서는 `math.gcd`를 사용하는 것이 더 표준적이고 간결합니다.

2.  **모듈러 역원 계산**: `make_decrypt_key` 함수에서 모듈러 곱셈 역원을 찾기 위해 `for` 루프를 사용합니다. 이 부분은 `cryptomath_module.py`에 구현된 확장 유클리드 알고리즘(`find_mod_inverse`)을 사용하면 더 효율적이고 수학적으로 안정적입니다.

3.  **오류 처리**: `main` 함수에서 사용자가 숫자가 아닌 값을 입력하면 `ValueError`가 발생하여 프로그램이 비정상 종료됩니다. `try-except` 블록을 사용하여 사용자 입력을 검증하면 프로그램의 안정성을 높일 수 있습니다.

4.  **클래스 변수와 인스턴스 변수**: `key_string`, `modulus`, `to_int`는 모든 `HillCipher` 인스턴스에서 공유되는 클래스 변수입니다. 이는 올바른 사용법이지만, `break_key`와 같이 인스턴스마다 달라지는 값은 `__init__`에서 `self.break_key`로 명확히 초기화하는 것이 좋습니다. (현재 코드에서는 이미 잘 되어 있습니다.)

5.  **문자 집합 확장성**: 현재 문자 집합(`key_string`)은 영문 대문자와 숫자로 고정되어 있습니다. 이를 클래스 생성자의 인자로 받아 사용자가 직접 문자 집합을 지정할 수 있도록 하면 암호의 유연성과 확장성이 향상됩니다.

