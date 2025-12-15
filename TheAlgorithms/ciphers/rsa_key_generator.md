# `rsa_key_generator.py` 코드 설명

이 문서는 `rsa_key_generator.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 현대 공개키 암호 시스템의 대표적인 예인 **RSA 암호**에 사용될 공개키와 개인키 쌍을 생성하고 파일로 저장하는 기능을 구현합니다.

## 목차
1.  RSA 키 생성이란?
2.  함수 설명
    -   `generateKey(keySize)`
    -   `makeKeyFiles(name, keySize)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## RSA 키 생성이란?

RSA는 비대칭 암호(공개키 암호) 시스템으로, 암호화와 복호화에 서로 다른 키를 사용합니다. 키 생성 과정은 다음과 같은 수학적 단계를 거칩니다.

1.  **매우 큰 두 소수 `p`와 `q` 선택**: 암호의 보안성을 위해 암호학적으로 안전한 큰 소수를 생성합니다.
2.  **모듈러스 `n` 계산**: `n = p * q`를 계산합니다. `n`은 공개키와 개인키 모두에 사용됩니다.
3.  **오일러 피 함수 `φ(n)` 계산**: `φ(n) = (p-1) * (q-1)`을 계산합니다.
4.  **공개 지수 `e` 선택**: `1 < e < φ(n)` 이면서 `φ(n)`과 서로소인 정수 `e`를 무작위로 선택합니다.
5.  **개인 지수 `d` 계산**: `d * e ≡ 1 (mod φ(n))`을 만족하는 `d`를 계산합니다. 즉, `d`는 `e`의 모듈러 곱셈 역원입니다.

최종적으로 `(n, e)`는 공개키가 되고, `(n, d)`는 개인키가 됩니다.

> **참고**: 이 스크립트는 `rabin_miller.py`와 `cryptomath_module.py` 파일에 의존하여 소수 생성, 최대공약수(GCD), 모듈러 곱셈 역원 계산을 수행합니다.

## 함수 설명

### `generateKey(keySize: int) -> tuple[tuple[int, int], tuple[int, int]]`

지정된 비트 크기(`keySize`)에 맞는 RSA 공개키와 개인키 쌍을 생성합니다.

-   **알고리즘**:
    1.  `rabin_miller.generateLargePrime()`을 두 번 호출하여 `keySize` 비트의 큰 소수 `p`와 `q`를 생성합니다.
    2.  `n = p * q`를 계산합니다.
    3.  `φ(n) = (p-1) * (q-1)`과 서로소인 공개 지수 `e`를 무작위로 찾습니다.
    4.  `cryptomath_module.find_mod_inverse()`를 사용하여 `e`의 모듈러 곱셈 역원인 개인 지수 `d`를 계산합니다.
    5.  생성된 값들을 튜플 형태로 묶어 `(공개키, 개인키)`를 반환합니다.

### `makeKeyFiles(name: str, keySize: int) -> None`

지정된 이름(`name`)과 키 크기(`keySize`)로 키 파일을 생성합니다.

-   **동작**:
    1.  `generateKey()`를 호출하여 키 쌍을 생성합니다.
    2.  같은 이름의 키 파일(`{name}_pubkey.txt`, `{name}_privkey.txt`)이 이미 존재하는지 확인하고, 존재하면 경고 메시지를 출력하고 프로그램을 종료합니다.
    3.  공개키와 개인키를 각각의 파일에 `키크기,n,e` 또는 `키크기,n,d` 형식의 쉼표로 구분된 문자열로 저장합니다.

### `main()`

스크립트의 메인 실행 함수입니다. `makeKeyFiles`를 호출하여 "rsa"라는 이름과 1024비트 크기로 키 파일을 생성합니다.

## 실행 방법

스크립트를 직접 실행하면 현재 디렉터리에 `rsa_pubkey.txt`와 `rsa_privkey.txt` 파일이 생성됩니다.

```bash
python rsa_key_generator.py
```

**실행 결과 (콘솔 출력):**
```
Making key files...
Generating prime p...
Generating prime q...
Generating e that is relatively prime to (p - 1) * (q - 1)...
Calculating d that is mod inverse of e...

Writing public key to file rsa_pubkey.txt...
Writing private key to file rsa_privkey.txt...
Key files generation successful.
```

## 코드 개선 제안

1.  **코딩 스타일 일관성**: 함수 이름이 `generateKey`, `makeKeyFiles`와 같이 카멜 케이스(camelCase)로 작성되어 있습니다. 파이썬에서는 일반적으로 함수와 변수 이름에 스네이크 케이스(snake_case)를 사용하는 것이 권장됩니다(PEP 8). `generate_key`, `make_key_files`로 변경하면 다른 파이썬 코드와의 일관성을 높일 수 있습니다.

2.  **파일 쓰기 방식 개선**: `makeKeyFiles` 함수에서 파일에 문자열을 쓸 때 f-string을 사용하고 있습니다. 이는 현대적이고 좋은 방식입니다. 다만, `%` 포매팅을 사용하는 부분(`os.path.exists("%s_pubkey.txt" % (name))`)도 f-string으로 통일하면 코드 스타일이 더 일관성 있어집니다.

    ```python
    # 개선 제안 예시
    if os.path.exists(f"{name}_pubkey.txt") or os.path.exists(f"{name}_privkey.txt"):
        # ...
    ```

3.  **공개 지수 `e` 선택**: 현재 `e`를 무작위로 선택하고 있습니다. 이는 문제가 없지만, 실제 많은 RSA 구현에서는 성능상의 이유로 `e`를 `65537`과 같은 작은 소수로 고정하는 경우가 많습니다. 이 값을 사용하면 공개키 연산(암호화)이 더 빨라지는 장점이 있습니다.

4.  **하드코딩된 키 크기**: `main` 함수에서 키 크기가 `1024`로 하드코딩되어 있습니다. 커맨드 라인 인자(`sys.argv` 또는 `argparse`)를 통해 사용자가 키 크기를 직접 지정할 수 있도록 하면 스크립트의 유연성이 향상됩니다.