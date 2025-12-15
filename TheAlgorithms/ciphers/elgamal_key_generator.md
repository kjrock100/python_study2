# `elgamal_key_generator.py` 코드 설명

이 문서는 `elgamal_key_generator.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 **엘가말(ElGamal) 공개키 암호 시스템**에 사용될 공개키와 개인키 쌍을 생성하고 파일로 저장하는 기능을 구현합니다.

## 목차
1.  엘가말 키 생성이란?
2.  함수 설명
    -   `primitive_root(p_val)`
    -   `generate_key(key_size)`
    -   `make_key_files(name, keySize)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 엘가말 키 생성이란?

엘가말은 비대칭 암호(공개키 암호) 시스템으로, 암호화와 복호화에 서로 다른 키를 사용합니다. 키 생성 과정은 다음과 같은 수학적 요소들을 기반으로 합니다.

1.  **매우 큰 소수 `p`**: 암호 시스템의 기반이 되는 큰 소수입니다.
2.  **생성자(Generator) `g`**: `p`의 **원시근(primitive root)** 중 하나로, 키 생성에 사용됩니다.
3.  **개인키 `d`**: 1과 `p-2` 사이에서 무작위로 선택된 정수로, 외부에 공개되지 않아야 합니다.
4.  **공개키 `e₂`**: `e₂ = g^d mod p` 공식을 통해 계산되며, 소수 `p`, 생성자 `g`와 함께 외부에 공개됩니다.

이 스크립트는 이 구성 요소들을 생성하여 파일에 저장하는 역할을 합니다.

> **참고**: 이 스크립트는 `rabin_miller.py`와 `cryptomath_module.py` 파일에 의존하여 소수 생성 및 모듈러 역원 계산을 수행합니다.

## 함수 설명

### `primitive_root(p_val: int) -> int`

주어진 소수 `p_val`에 대한 **원시근(primitive root)**을 찾습니다.

-   **알고리즘**:
    -   `3`부터 `p_val` 사이의 정수를 무작위로 선택하여 `g`로 삼습니다.
    -   `g`가 몇 가지 간단한 조건을 만족하는지 확인하고, 만족하면 `g`를 원시근으로 간주하고 반환합니다.
-   **주의**: 이 함수의 구현은 실제 원시근을 찾는 완전한 알고리즘이 아니며, 매우 단순화된 방식입니다. 실제 암호학적 응용에서는 더 엄격하고 정확한 방법으로 원시근을 찾아야 합니다.

### `generate_key(key_size: int) -> tuple[tuple, tuple]`

지정된 비트 크기(`key_size`)에 맞는 엘가말 공개키와 개인키 쌍을 생성합니다.

-   **알고리즘**:
    1.  `rabin_miller.generateLargePrime()`을 호출하여 `key_size` 비트의 큰 소수 `p`를 생성합니다.
    2.  `primitive_root(p)`를 호출하여 생성자 `e₁` (즉, `g`)을 찾습니다.
    3.  `3`과 `p` 사이에서 무작위 정수를 선택하여 개인키 `d`로 사용합니다.
    4.  `e₂ = (e₁^d mod p)`를 계산한 후, 이 값의 모듈러 곱셈 역원(`cryptomath.find_mod_inverse`)을 계산하여 공개키의 일부로 사용합니다.
        -   **참고**: 표준 엘가말에서는 `e₁^d mod p` 자체를 공개키로 사용하지만, 이 구현은 그 값의 모듈러 역원을 사용하고 있습니다. 이는 특정 프로토콜 변형일 수 있습니다.
    5.  생성된 값들을 튜플 형태로 묶어 공개키와 개인키를 반환합니다.

### `make_key_files(name: str, keySize: int) -> None`

지정된 이름(`name`)과 키 크기(`keySize`)로 키 파일을 생성합니다.

-   **동작**:
    1.  `generate_key()`를 호출하여 키 쌍을 생성합니다.
    2.  같은 이름의 키 파일(`{name}_pubkey.txt`, `{name}_privkey.txt`)이 이미 존재하는지 확인하고, 존재하면 경고 메시지를 출력하고 프로그램을 종료합니다.
    3.  공개키와 개인키를 각각의 파일에 쉼표로 구분된 문자열 형태로 저장합니다.

### `main()`

스크립트의 메인 실행 함수입니다. `make_key_files`를 호출하여 "elgamal"이라는 이름과 2048비트 크기로 키 파일을 생성합니다.

## 실행 방법

스크립트를 직접 실행하면 현재 디렉터리에 `elgamal_pubkey.txt`와 `elgamal_privkey.txt` 파일이 생성됩니다.

```bash
python elgamal_key_generator.py
```

**실행 결과 (콘솔 출력):**
```
Making key files...
Generating prime p...
Generating primitive root of p

Writing public key to file elgamal_pubkey.txt...
Writing private key to file elgamal_privkey.txt...
Key files generation successful
```

## 코드 개선 제안

1.  **`primitive_root` 함수 개선**: 현재 `primitive_root` 함수는 수학적으로 올바른 원시근을 보장하지 않습니다. 원시근을 정확히 찾으려면 `p-1`의 소인수분해를 이용하는 더 복잡한 알고리즘이 필요합니다. 실제 보안 환경에서는 이 함수를 신뢰할 수 있는 수학 라이브러리의 함수로 대체해야 합니다.

2.  **공개키 계산 방식 명확화**: `generate_key` 함수에서 공개키 `e₂`를 계산하는 방식이 표준 엘가말과 다릅니다. 주석을 통해 `e₂`가 `(e₁^d mod p)`의 모듈러 곱셈 역원임을 명확히 설명하면, 코드를 이해하는 데 도움이 됩니다.

3.  **오류 처리**: `primitive_root` 함수가 원시근을 찾지 못할 경우(이론적으로는 소수에 대해 항상 존재하지만, 이 구현에서는 실패 가능성이 있음) `None`을 반환할 수 있지만, `generate_key`에서는 이에 대한 처리 로직이 없습니다. `None`이 반환될 경우 예외를 발생시키거나 재시도하는 로직을 추가하면 안정성이 향상됩니다.

4.  **하드코딩된 값**: `min_primitive_root = 3`과 같이 하드코딩된 값들의 의미를 주석으로 설명하거나, 더 의미 있는 이름의 상수로 정의하는 것이 좋습니다.
