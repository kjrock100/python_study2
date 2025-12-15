# `vigenere_cipher.py` 코드 설명

이 문서는 `vigenere_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 키워드를 사용하여 암호화를 수행하는 다중 문자 치환 암호인 **비즈네르 암호(Vigenère Cipher)**를 구현합니다.

## 목차
1.  비즈네르 암호란?
2.  함수 설명
    -   `translateMessage(key, message, mode)`
    -   `encryptMessage(key, message)`
    -   `decryptMessage(key, message)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 비즈네르 암호란?

비즈네르 암호는 카이사르 암호를 확장한 형태로, 하나의 키(이동 거리) 대신 여러 개의 키를 순환적으로 사용하는 **다중 문자 치환 암호**입니다. 암호화에 사용될 키워드의 각 문자가 서로 다른 이동 거리를 결정합니다.

예를 들어, 평문이 "HELLO"이고 키워드가 "KEY"라면:
-   'H'는 'K'(알파벳 10번째)만큼 이동합니다.
-   'E'는 'E'(알파벳 4번째)만큼 이동합니다.
-   'L'는 'Y'(알파벳 24번째)만큼 이동합니다.
-   'L'는 다시 'K'만큼 이동합니다. (키워드 순환)
-   'O'는 다시 'E'만큼 이동합니다.

이 방식은 단일 문자 치환 암호에 비해 문자 빈도 분석을 훨씬 더 어렵게 만듭니다.

## 함수 설명

### `translateMessage(key: str, message: str, mode: str) -> str`

암호화와 복호화의 핵심 로직을 모두 처리하는 범용 함수입니다.

-   **알고리즘**:
    1.  메시지의 각 문자를 순회하면서, 키워드의 인덱스(`keyIndex`)도 함께 순환시킵니다.
    2.  문자가 알파벳이면, 해당 문자의 알파벳 순서(`num`)를 찾습니다.
    3.  `mode` 값에 따라 `num`에 키 문자의 알파벳 순서를 더하거나(`encrypt`) 뺍니다(`decrypt`).
    4.  계산 결과를 알파벳 개수(26)로 나눈 나머지를 구해 새로운 문자를 찾습니다.
    5.  원래 문자의 대소문자를 유지하여 변환된 문자를 결과 리스트에 추가합니다.
    6.  문자가 알파벳이 아니면(공백, 기호 등), 그대로 결과 리스트에 추가합니다.
    7.  모든 문자를 처리한 후, 결과 리스트를 하나의 문자열로 합쳐 반환합니다.

### `encryptMessage(key: str, message: str) -> str`

주어진 메시지를 **암호화**합니다. 이 함수는 `translateMessage`를 `mode='encrypt'`로 호출하는 간단한 래퍼(wrapper)입니다.

```python
>>> encryptMessage('HDarji', 'This is Harshil Darji from Dharmaj.')
'Akij ra Odrjqqs Gaisq muod Mphumrs.'
```

### `decryptMessage(key: str, message: str) -> str`

암호화된 메시지를 **복호화**합니다. 이 함수는 `translateMessage`를 `mode='decrypt'`로 호출하는 래퍼입니다.

```python
>>> decryptMessage('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
'This is Harshil Darji from Dharmaj.'
```

### `main()`

사용자로부터 메시지, 키, 모드(암호화/복호화)를 입력받아 암호화를 시연하는 대화형 인터페이스를 제공합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자 입력을 받아 암호화 또는 복호화를 수행합니다.

```bash
python vigenere_cipher.py
```

**실행 예시:**
```
Enter message: Hello World
Enter key [alphanumeric]: key
Encrypt/Decrypt [e/d]: e

Encrypted message:
Rijvs Uyvjn
```

## 코드 개선 제안

1.  **키 유효성 검사**: 현재 코드는 키에 알파벳이 아닌 문자(숫자, 기호)가 포함될 경우 `LETTERS.find()`가 `-1`을 반환하여 의도치 않은 결과(잘못된 이동)를 낳습니다. `main` 함수에서 키를 입력받은 후, `key.isalpha()` 등을 사용하여 키가 알파벳으로만 구성되었는지 확인하는 로직을 추가하면 프로그램의 안정성이 향상됩니다.

    ```python
    # main 함수 개선 제안 예시
    key = input("Enter key [alphabetic only]: ")
    if not key.isalpha():
        print("Error: Key must contain only letters.")
        return # 또는 sys.exit()
    ```

2.  **`main` 함수 입력 처리**: 사용자가 모드로 'e'나 'd'가 아닌 다른 값을 입력하면 아무 작업도 수행하지 않고 종료됩니다. 사용자에게 잘못된 입력임을 알리는 메시지를 추가하면 더 친절한 인터페이스가 됩니다.

3.  **코드 가독성**: `translateMessage` 함수는 잘 작성되었지만, `num += ...`와 `num -= ...` 부분을 하나의 식으로 통합하고 연산자만 바꾸는 방식으로 리팩토링하면 코드 중복을 약간 더 줄일 수 있습니다. 하지만 현재 방식도 충분히 명확합니다.

4.  **모듈화**: `main` 함수를 제외한 암호화/복호화 관련 함수들은 다른 스크립트에서 재사용하기 좋은 구조로 되어 있습니다. `doctest`를 추가하여 각 함수의 정확성을 보장하면 더 견고한 모듈이 될 수 있습니다.