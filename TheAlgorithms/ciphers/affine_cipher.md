# `affine_cipher.py` 코드 설명

이 문서는 `affine_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 단일 치환 암호의 일종인 **아핀 암호(Affine Cipher)**를 구현합니다.

## 목차
1.  아핀 암호란?
2.  함수 설명
    -   `check_keys(keyA, keyB, mode)`
    -   `encrypt_message(key, message)`
    -   `decrypt_message(key, message)`
    -   `get_random_key()`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 아핀 암호란?

아핀 암호는 각 문자를 다른 문자로 치환하는 **단일 치환 암호**입니다. 암호화는 다음의 수학적 함수를 통해 이루어집니다.

`암호문(C) = (평문(P) * keyA + keyB) mod m`

여기서,
-   `P`: 평문 문자의 숫자 값 (알파벳 순서)
-   `keyA`, `keyB`: 암호화에 사용되는 두 개의 정수 키
-   `m`: 기호 집합의 크기 (이 스크립트에서는 `len(SYMBOLS)`)

복호화(해독)가 가능하려면, `keyA`와 `m`이 반드시 **서로소(relatively prime)**여야 합니다. 즉, `gcd(keyA, m) = 1`이어야 합니다.

## 함수 설명

### `check_keys(keyA, keyB, mode)`

암호화 또는 복호화에 사용될 키 `keyA`와 `keyB`가 유효한지 검사합니다.

-   **역할**: 키의 유효성을 검증하여 암호화/복호화 과정의 오류를 방지합니다.
-   **검사 항목**:
    1.  `keyA`가 1이거나 `keyB`가 0인 경우, 암호가 약해지므로 경고합니다.
    2.  키 값들이 유효한 범위 내에 있는지 확인합니다.
    3.  `keyA`와 기호 집합의 크기(`len(SYMBOLS)`)가 서로소인지 확인합니다. (`gcd(keyA, len(SYMBOLS)) == 1`)
-   **동작**: 유효하지 않은 키가 발견되면, 메시지를 출력하고 `sys.exit()`를 통해 프로그램을 즉시 종료합니다.

### `encrypt_message(key, message)`

주어진 `key`와 `message`를 사용하여 아핀 암호화(Encryption)를 수행합니다.

-   **알고리즘**:
    1.  하나의 정수 `key`를 `divmod`를 이용해 `keyA`와 `keyB`로 분리합니다.
    2.  `check_keys`를 호출하여 키를 검증합니다.
    3.  메시지의 각 문자에 대해, 기호 집합(`SYMBOLS`)에 포함된 경우 다음 공식을 적용합니다.
        -   `새로운 인덱스 = (기존 인덱스 * keyA + keyB) % len(SYMBOLS)`
    4.  기호 집합에 없는 문자는 그대로 둡니다.

### `decrypt_message(key, message)`

주어진 `key`와 암호화된 `message`를 사용하여 복호화(Decryption)를 수행합니다.

-   **알고리즘**:
    1.  `keyA`와 `keyB`를 `key`로부터 분리합니다.
    2.  `cryptomath.find_mod_inverse()`를 사용하여 `keyA`의 모듈러 곱셈 역원을 찾습니다. 이는 복호화에 필수적입니다.
    3.  암호문의 각 문자에 대해, 기호 집합에 포함된 경우 다음 공식을 적용합니다.
        -   `새로운 인덱스 = ((기존 인덱스 - keyB) * 모듈러 역원) % len(SYMBOLS)`
    4.  기호 집합에 없는 문자는 그대로 둡니다.

### `get_random_key()`

아핀 암호에 사용할 수 있는 유효한 랜덤 키를 생성합니다.

-   **역할**: 사용자가 직접 키를 선택하는 대신, 암호학적으로 안전한 키를 자동으로 생성합니다.
-   **동작**: `keyA`가 기호 집합 크기와 서로소가 될 때까지 `keyA`와 `keyB`를 무작위로 생성한 후, 두 키를 하나의 정수로 결합하여 반환합니다.

### `main()`

사용자로부터 메시지, 키, 모드(암호화/복호화)를 입력받아 암호화를 시연합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`가 실행되어 함수의 정확성을 테스트합니다.

```bash
python affine_cipher.py
```

`main()` 함수의 주석을 해제하면, 사용자 입력을 통해 암호화를 직접 실행해볼 수 있습니다.

```
Enter message: This is a test!
Enter key [2000 - 9000]: 4545
Encrypt/Decrypt [E/D]: e

Encrypted text:
V_p{v_p{v pF}vF_
```

> **참고**: 이 스크립트는 `cryptomath_module.py` 파일에 의존하여 최대공약수(`gcd`)와 모듈러 곱셈 역원(`find_mod_inverse`)을 계산합니다.

## 코드 개선 제안

1.  **오류 처리 방식 개선**: `check_keys` 함수는 오류가 발생하면 `sys.exit()`를 호출하여 프로그램을 강제 종료합니다. 이는 다른 모듈에서 이 함수를 재사용하기 어렵게 만듭니다. `ValueError`와 같은 예외(Exception)를 발생시키고, 호출하는 쪽에서 `try...except` 블록으로 처리하도록 수정하는 것이 더 유연한 설계입니다.

    ```python
    # 개선 제안 예시
    def check_keys(keyA: int, keyB: int, mode: str) -> None:
        if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
            raise ValueError(
                f"Key A {keyA} and the symbol set size {len(SYMBOLS)} "
                "are not relatively prime. Choose a different key."
            )
        # ... 다른 검사들 ...
    ```

2.  **키 분리 로직 명확화**: `encrypt_message`와 `decrypt_message` 함수 내에서 `keyA, keyB = divmod(key, len(SYMBOLS))`를 사용하여 키를 분리하는 로직이 반복됩니다. 이 로직을 별도의 헬퍼 함수(예: `get_keys_from_int(key)`)로 분리하면 코드 중복을 줄이고 가독성을 높일 수 있습니다.

3.  **상수 관리**: `SYMBOLS`와 같은 중요한 상수는 대문자로 작성되어 있지만, 프로그램의 다른 설정값(예: 키 범위)들도 상수로 정의하여 관리하면 유지보수가 용이해집니다.

4.  **사용자 인터페이스 개선**: `main` 함수에서 키 입력 범위를 `[2000 - 9000]`으로 제한하고 있지만, `get_random_key` 함수는 다른 범위의 키를 생성할 수 있습니다. 사용자에게 키의 유효한 범위와 조건을 더 명확하게 안내하거나, `get_random_key`를 사용하여 키를 자동으로 생성해주는 옵션을 제공하면 사용성이 향상됩니다.
