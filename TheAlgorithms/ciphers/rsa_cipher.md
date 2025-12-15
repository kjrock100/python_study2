# `rsa_cipher.py` 코드 설명

이 문서는 `rsa_cipher.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 현대 공개키 암호 시스템의 대표적인 예인 **RSA 암호**를 사용하여 메시지를 암호화하고 복호화하는 기능을 구현합니다.

## 목차
1.  RSA 암호란?
2.  함수 설명
    -   `get_blocks_from_text(message, block_size)`
    -   `get_text_from_blocks(block_ints, message_length, block_size)`
    -   `encrypt_message(message, key, blockSize)`
    -   `decrypt_message(encrypted_blocks, message_length, key, block_size)`
    -   `read_key_file(key_filename)`
    -   `encrypt_and_write_to_file(...)`
    -   `read_from_file_and_decrypt(...)`
3.  실행 방법
4.  코드 개선 제안

## RSA 암호란?

RSA는 두 개의 매우 큰 소수의 곱을 이용하는 비대칭 암호(공개키 암호) 시스템입니다. 암호화에는 공개키를, 복호화에는 개인키를 사용하여 안전한 통신을 가능하게 합니다.

**키 생성**:
1.  매우 큰 두 소수 `p`와 `q`를 선택합니다.
2.  `n = p * q`를 계산합니다.
3.  오일러 피 함수 값 `φ(n) = (p-1) * (q-1)`을 계산합니다.
4.  `1 < e < φ(n)` 이면서 `φ(n)`과 서로소인 정수 `e`를 선택합니다. (`(n, e)`가 공개키)
5.  `d * e ≡ 1 (mod φ(n))`을 만족하는 `d`를 계산합니다. (`(n, d)`가 개인키)

**암호화/복호화**:
-   **암호화**: `암호문(C) = 평문(M)^e mod n`
-   **복호화**: `평문(M) = 암호문(C)^d mod n`

이 스크립트는 `rsa_key_generator.py`를 통해 생성된 키를 사용하여 이 과정을 수행합니다.

## 함수 설명

### `get_blocks_from_text(message, block_size)`

문자열 메시지를 RSA 암호화에 적합한 숫자 블록의 리스트로 변환합니다.

-   **알고리즘**:
    1.  메시지를 `block_size` 크기의 블록으로 나눕니다.
    2.  각 블록의 문자들을 바이트로 변환하고, 이를 하나의 큰 정수로 결합합니다. (예: "ABC" -> `A*256² + B*256¹ + C*256⁰`)

### `get_text_from_blocks(block_ints, message_length, block_size)`

숫자 블록 리스트를 다시 원래의 문자열 메시지로 변환합니다. `get_blocks_from_text`의 역과정입니다.

### `encrypt_message(message, key, blockSize)`

주어진 메시지를 RSA 공개키로 **암호화**합니다.

-   **알고리즘**:
    1.  `get_blocks_from_text`를 사용하여 메시지를 숫자 블록으로 변환합니다.
    2.  각 숫자 블록 `B`에 대해 `C = B^e mod n` 공식을 사용하여 암호화된 블록을 계산합니다.
    3.  암호화된 블록들의 리스트를 반환합니다.

### `decrypt_message(encrypted_blocks, message_length, key, block_size)`

암호화된 숫자 블록들을 RSA 개인키로 **복호화**합니다.

-   **알고리즘**:
    1.  각 암호화된 블록 `C`에 대해 `M = C^d mod n` 공식을 사용하여 원래의 숫자 블록 `M`을 복원합니다.
    2.  `get_text_from_blocks`를 사용하여 복원된 숫자 블록들을 최종 텍스트 메시지로 변환합니다.

### `read_key_file(key_filename)`

공개키 또는 개인키 파일에서 키 정보(키 크기, n, e 또는 d)를 읽어옵니다.

### `encrypt_and_write_to_file(...)`

메시지를 암호화하고 그 결과를 파일에 씁니다.

-   **동작**:
    1.  공개키 파일을 읽습니다.
    2.  키 크기와 블록 크기를 비교하여 암호화 가능 여부를 확인합니다.
    3.  `encrypt_message`를 호출하여 메시지를 암호화합니다.
    4.  결과를 `원본 메시지 길이_블록 크기_암호화된 블록들` 형식의 문자열로 만들어 파일에 저장합니다.

### `read_from_file_and_decrypt(...)`

파일에서 암호문을 읽어와 복호화합니다.

-   **동작**:
    1.  개인키 파일을 읽습니다.
    2.  암호문 파일에서 메타데이터(메시지 길이, 블록 크기)와 암호화된 블록들을 파싱합니다.
    3.  `decrypt_message`를 호출하여 복호화를 수행하고 결과를 반환합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자에게 암호화 또는 복호화 모드를 선택하라는 메뉴가 나타납니다.

```bash
python rsa_cipher.py
```

-   **암호화(e)**: `rsa_pubkey.txt` 파일이 없으면 자동으로 생성합니다. 사용자로부터 메시지를 입력받아 암호화하고, 결과를 `encrypted_file.txt`에 저장합니다.
-   **복호화(d)**: `encrypted_file.txt`와 `rsa_privkey.txt` 파일을 사용하여 복호화를 수행하고, 결과를 `rsa_decryption.txt`에 저장합니다.

> **참고**: 이 스크립트는 `rsa_key_generator.py`에 의존하여 키 파일을 생성합니다.

## 코드 개선 제안

1.  **블록 크기 검증 로직**: `encrypt_and_write_to_file`과 `read_from_file_and_decrypt` 함수에서 `key_size < block_size * 8` 조건을 검사합니다. RSA 암호화의 요구 조건은 평문 블록(정수)이 모듈러스 `n`보다 작아야 한다는 것입니다. 현재의 비트 크기 비교는 이 조건을 근사적으로 만족시키지만, 더 정확하게는 `get_blocks_from_text`에서 생성된 각 숫자 블록이 `n`보다 작은지 직접 확인하는 것이 더 안전합니다.

2.  **오류 처리**: `main` 함수에서 사용자가 숫자가 아닌 키를 입력하거나, 파일이 존재하지 않을 때 발생하는 오류를 `try-except` 블록으로 처리하면 프로그램의 안정성이 향상됩니다. 예를 들어, `read_key_file`에서 `FileNotFoundError`를 처리할 수 있습니다.

3.  **코드 중복**: `encrypt_and_write_to_file`과 `read_from_file_and_decrypt` 함수에 키 크기와 블록 크기를 비교하는 로직이 중복됩니다. 이 검증 로직을 별도의 헬퍼 함수로 분리하면 좋습니다.

4.  **하드코딩된 파일 이름**: `main` 함수에서 "rsa_pubkey.txt", "encrypted_file.txt" 등 파일 이름이 하드코딩되어 있습니다. 이들을 커맨드 라인 인자로 받거나 사용자에게 직접 입력받도록 수정하면 스크립트의 유연성이 크게 향상됩니다.

5.  **인코딩 방식**: `message.encode("ascii")`를 사용하고 있어 ASCII 범위를 벗어나는 문자(예: 한글)는 처리할 수 없습니다. 더 넓은 범위를 지원하는 "utf-8"과 같은 인코딩을 사용하도록 변경할 수 있지만, 이 경우 블록 변환 방식도 함께 수정해야 합니다.