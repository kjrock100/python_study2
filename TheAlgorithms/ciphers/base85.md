# `base85.py` 코드 설명

이 문서는 `base85.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 표준 `base64` 라이브러리를 사용하여 **Base85 (Ascii85)** 인코딩 및 디코딩을 수행합니다.

## 목차
1.  Base85 인코딩이란?
2.  함수 설명
    -   `base85_encode(string)`
    -   `base85_decode(a85encoded)`
3.  실행 방법
4.  코드 개선 제안

## Base85 인코딩이란?

Base85는 85개의 출력 가능한 ASCII 문자를 사용하여 바이너리 데이터를 텍스트 형태로 표현하는 인코딩 방식입니다. 어도비(Adobe)의 포스트스크립트(PostScript)와 PDF 형식에서 널리 사용되어 **Ascii85**라고도 불립니다.

-   **원리**: 4바이트(32비트)의 바이너리 데이터를 5개의 Base85 문자로 변환합니다. 이 방식은 Base64보다 데이터 크기 증가율이 낮아 더 효율적입니다. (Base64는 3바이트를 4문자로, Base85는 4바이트를 5문자로 변환)
-   **용도**: 바이너리 데이터를 텍스트 기반 매체로 효율적으로 전송하거나 저장할 때 사용됩니다.

## 함수 설명

### `base85_encode(string: str) -> bytes`

주어진 UTF-8 문자열을 Base85로 **인코딩**합니다.

-   **알고리즘**:
    1.  입력 문자열(`string`)을 `.encode("utf-8")`를 사용하여 바이트 객체로 변환합니다.
    2.  `base64.a85encode()` 함수를 사용하여 이 바이트 객체를 Base85로 인코딩합니다.
    3.  결과로 얻은 Base85 인코딩된 바이트 객체를 반환합니다.

```python
>>> base85_encode("base 85")
b'@UX=h+?24'
```

### `base85_decode(a85encoded: bytes) -> str`

Base85로 인코딩된 바이트 객체를 원래의 UTF-8 문자열로 **디코딩**합니다.

-   **알고리즘**:
    1.  입력된 Base85 바이트 객체(`a85encoded`)를 `base64.a85decode()` 함수를 사용하여 원래의 바이트 객체로 디코딩합니다.
    2.  디코딩된 바이트 객체를 `.decode("utf-8")`를 사용하여 사람이 읽을 수 있는 문자열로 변환합니다.
    3.  결과 문자열을 반환합니다.

```python
>>> base85_decode(b"@UX=h+?24")
'base 85'
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python base85.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

이 스크립트는 파이썬 표준 라이브러리를 효과적으로 사용하여 매우 간결하고 명확합니다. 추가적인 개선을 고려한다면 다음과 같은 기능을 추가할 수 있습니다.

1.  **커맨드 라인 인터페이스 추가**: `argparse` 모듈을 사용하여 커맨드 라인에서 직접 문자열을 인코딩하거나 디코딩할 수 있는 인터페이스를 제공하면 스크립트의 사용성이 향상됩니다.

    ```python
    # 개선 제안 예시
    if __name__ == "__main__":
        import argparse
        import doctest
        
        doctest.testmod()

        parser = argparse.ArgumentParser(description="Base85 (Ascii85) encode or decode.")
        parser.add_argument("string", nargs="?", help="String to process.")
        parser.add_argument("-d", "--decode", action="store_true", help="Decode mode.")
        args = parser.parse_args()

        if args.string:
            if args.decode:
                print(base85_decode(args.string.encode("ascii")))
            else:
                print(base85_encode(args.string).decode("ascii"))
    ```

2.  **오류 처리 강화**: `base85_decode` 함수에 잘못된 Base85 문자열이 입력될 경우 `base64` 모듈 내부에서 예외가 발생할 수 있습니다. `try...except` 블록을 추가하여 이러한 오류를 명시적으로 처리하고 사용자에게 친절한 메시지를 보여줄 수 있습니다.
