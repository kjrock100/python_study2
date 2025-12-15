# `base32.py` 코드 설명

이 문서는 `base32.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 표준 `base64` 라이브러리를 사용하여 **Base32** 인코딩 및 디코딩을 수행합니다.

## 목차
1.  Base32 인코딩이란?
2.  함수 설명
    -   `base32_encode(string)`
    -   `base32_decode(encoded_bytes)`
3.  실행 방법
4.  코드 개선 제안

## Base32 인코딩이란?

Base32는 32개의 출력 가능한 문자(알파벳 대문자 A-Z와 숫자 2-7)를 사용하여 바이너리 데이터를 텍스트 형태로 표현하는 인코딩 방식입니다.

-   **원리**: 데이터의 5비트 묶음을 하나의 Base32 문자로 변환합니다. 8비트 바이트 경계와 맞지 않기 때문에, 인코딩된 문자열의 끝에는 패딩 문자(`=`)가 추가될 수 있습니다.
-   **용도**: Base64와 유사하지만, 모든 문자가 대문자이므로 파일 시스템이나 URL 등에서 대소문자를 구분하지 않는 환경에 더 적합합니다.

## 함수 설명

### `base32_encode(string: str) -> bytes`

주어진 UTF-8 문자열을 Base32로 **인코딩**합니다.

-   **알고리즘**:
    1.  입력 문자열(`string`)을 `.encode("utf-8")`를 사용하여 바이트 객체로 변환합니다.
    2.  `base64.b32encode()` 함수를 사용하여 이 바이트 객체를 Base32로 인코딩합니다.
    3.  결과로 얻은 Base32 인코딩된 바이트 객체를 반환합니다.

```python
>>> base32_encode("Hello World!")
b'JBSWY3DPEBLW64TMMQQQ===='
```

### `base32_decode(encoded_bytes: bytes) -> str`

Base32로 인코딩된 바이트 객체를 원래의 UTF-8 문자열로 **디코딩**합니다.

-   **알고리즘**:
    1.  입력된 Base32 바이트 객체(`encoded_bytes`)를 `base64.b32decode()` 함수를 사용하여 원래의 바이트 객체로 디코딩합니다.
    2.  디코딩된 바이트 객체를 `.decode("utf-8")`를 사용하여 사람이 읽을 수 있는 문자열로 변환합니다.
    3.  결과 문자열을 반환합니다.

```python
>>> base32_decode(b'JBSWY3DPEBLW64TMMQQQ====')
'Hello World!'
```

## 실행 방법

스크립트를 직접 실행하면 "Hello World!" 문자열을 인코딩하고 다시 디코딩하는 과정을 시연하고 결과를 출력합니다.

```bash
python base32.py
```

**실행 결과:**
```
b'JBSWY3DPEBLW64TMMQQQ===='
Hello World!
```

## 코드 개선 제안

1.  **자동화된 테스트 추가**: 현재 `if __name__ == "__main__"` 블록은 간단한 시연만 수행합니다. `doctest` 모듈을 사용하여 함수 내의 예제 코드를 자동으로 테스트하도록 변경하면 코드의 정확성과 안정성을 쉽게 검증할 수 있습니다.

    ```python
    # 개선 제안 예시
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
    ```

2.  **커맨드 라인 인터페이스 추가**: `argparse` 모듈을 사용하여 커맨드 라인에서 직접 문자열을 인코딩하거나 디코딩할 수 있는 인터페이스를 제공하면 스크립트의 사용성이 향상됩니다.

    ```python
    # 개선 제안 예시
    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description="Base32 encode or decode.")
        parser.add_argument("string", help="String to process.")
        parser.add_argument("-d", "--decode", action="store_true", help="Decode mode.")
        args = parser.parse_args()

        if args.decode:
            print(base32_decode(args.string.encode("ascii")))
        else:
            print(base32_encode(args.string).decode("ascii"))
    ```

3.  **오류 처리 강화**: `base32_decode` 함수에 잘못된 Base32 문자열(예: 잘못된 문자 포함, 잘못된 패딩)이 입력될 경우 `binascii.Error`가 발생할 수 있습니다. `try...except` 블록을 추가하여 이러한 오류를 처리하고 사용자에게 친절한 메시지를 보여줄 수 있습니다.
