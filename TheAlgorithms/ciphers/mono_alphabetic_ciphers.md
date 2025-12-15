# `mono_alphabetic_ciphers.py` 코드 설명

이 문서는 `mono_alphabetic_ciphers.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 가장 기본적인 형태의 치환 암호 중 하나인 **단일 문자 치환 암호(Monoalphabetic Substitution Cipher)**를 구현합니다.

## 목차
1.  단일 문자 치환 암호란?
2.  함수 설명
    -   `translate_message(key, message, mode)`
    -   `encrypt_message(key, message)`
    -   `decrypt_message(key, message)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 단일 문자 치환 암호란?

단일 문자 치환 암호는 평문의 각 알파벳 문자를 암호문의 다른 특정 문자로 일대일 대응시켜 바꾸는 암호 방식입니다. 이 암호의 **키(key)**는 표준 알파벳(`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)이 어떻게 재배열되는지를 정의하는 순열(permutation)입니다.

예를 들어, 키가 `QWERTY...`라면 'A'는 'Q'로, 'B'는 'W'로, 'C'는 'E'로 치환됩니다.

## 함수 설명

### `translate_message(key: str, message: str, mode: Literal["encrypt", "decrypt"]) -> str`

암호화와 복호화의 핵심 로직을 모두 처리하는 범용 함수입니다.

-   **알고리즘**:
    1.  `mode` 값에 따라 원본 문자 집합(`chars_a`)과 대상 문자 집합(`chars_b`)을 결정합니다.
        -   **암호화(`encrypt`)**: `chars_a`는 표준 알파벳, `chars_b`는 `key`가 됩니다.
        -   **복호화(`decrypt`)**: `chars_a`는 `key`, `chars_b`는 표준 알파벳이 됩니다.
    2.  메시지의 각 문자를 순회합니다.
    3.  문자가 `chars_a`에 포함되어 있으면, 해당 문자의 인덱스를 찾아 `chars_b`에서 같은 인덱스에 있는 문자로 치환합니다.
    4.  대소문자를 구분하여 처리하며, 알파벳이 아닌 문자(공백, 기호 등)는 그대로 유지합니다.

### `encrypt_message(key: str, message: str) -> str`

주어진 메시지를 **암호화**합니다. 이 함수는 `translate_message`를 `mode='encrypt'`로 호출하는 간단한 래퍼(wrapper)입니다.

```python
>>> encrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
'Pcssi Bidsm'
```

### `decrypt_message(key: str, message: str) -> str`

암호화된 메시지를 **복호화**합니다. 이 함수는 `translate_message`를 `mode='decrypt'`로 호출하는 래퍼입니다.

```python
>>> decrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Pcssi Bidsm")
'Hello World'
```

### `main()`

미리 정의된 메시지와 키를 사용하여 암호화 또는 복호화 과정을 시연하고 결과를 출력합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 정확성을 테스트한 후, `main` 함수가 실행되어 하드코딩된 예제의 결과를 보여줍니다.

```bash
python mono_alphabetic_ciphers.py
```

**실행 결과:**
```
Using the key QWERTYUIOPASDFGHJKLZXCVBNM, the decrypted message is: Itssg Vgksr
```

## 코드 개선 제안

1.  **코드 중복**: 이 스크립트는 `simple_substitution_cipher.py`와 거의 동일한 기능을 수행합니다. 두 파일의 로직이 매우 유사하므로, 하나의 파일로 통합하여 코드 중복을 줄이는 것이 좋습니다. `translate_message` 함수를 사용하는 이 구현이 더 간결하고 재사용성이 높습니다.

2.  **키 유효성 검사**: 현재 코드는 제공된 `key`가 26개의 고유한 알파벳 문자로 구성된 유효한 순열이라고 가정합니다. `simple_substitution_cipher.py`에 있는 `checkValidKey`와 같은 함수를 추가하여 키의 유효성을 검사하면 프로그램의 안정성이 크게 향상됩니다.

3.  **사용자 인터페이스**: `main` 함수는 현재 하드코딩된 값으로만 동작합니다. `input()` 함수를 사용하여 사용자로부터 메시지, 키, 모드를 직접 입력받도록 수정하면 스크립트의 활용도가 높아집니다.

4.  **변수명 명확화**: `chars_a`와 `chars_b`라는 변수명은 다소 모호합니다. `source_alphabet`과 `target_alphabet`과 같이 더 의미 있는 이름으로 변경하면 코드의 가독성이 향상됩니다.

    ```python
    # 개선 제안 예시
    def translate_message(key: str, message: str, mode: Literal["encrypt", "decrypt"]) -> str:
        if mode == "decrypt":
            source_alphabet, target_alphabet = key, LETTERS
        else:
            source_alphabet, target_alphabet = LETTERS, key
        # ... (이후 로직)
    ```
