# `simple_substitution_cipher.py` 코드 설명

이 문서는 `simple_substitution_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 가장 기본적인 형태의 치환 암호 중 하나인 **단일 문자 치환 암호(Simple Substitution Cipher)**를 구현합니다.

## 목차
1.  단일 문자 치환 암호란?
2.  함수 설명
    -   `checkValidKey(key)`
    -   `encryptMessage(key, message)`
    -   `decryptMessage(key, message)`
    -   `translateMessage(key, message, mode)`
    -   `getRandomKey()`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 단일 문자 치환 암호란?

단일 문자 치환 암호는 평문의 각 알파벳 문자를 암호문의 다른 특정 문자로 일대일 대응시켜 바꾸는 암호 방식입니다. 이 암호의 **키(key)**는 표준 알파벳(`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)이 어떻게 재배열되는지를 정의하는 순열(permutation)입니다.

예를 들어, 키가 `LFWOAY...`라면 'A'는 'L'로, 'B'는 'F'로, 'C'는 'W'로 치환됩니다.

## 함수 설명

### `checkValidKey(key: str) -> None`

제공된 `key`가 유효한 단일 문자 치환 암호 키인지 검사합니다.

-   **역할**: 키가 26개의 고유한 알파벳 문자로 구성된 순열인지 확인하여 암호화/복호화 과정의 오류를 방지합니다.
-   **알고리즘**: 키를 정렬한 결과와 표준 알파벳을 정렬한 결과가 동일한지 비교합니다. 동일하지 않으면, `sys.exit()`를 통해 프로그램을 즉시 종료합니다.

### `encryptMessage(key: str, message: str) -> str`

주어진 메시지를 **암호화**합니다. 이 함수는 `translateMessage`를 `mode='encrypt'`로 호출하는 간단한 래퍼(wrapper)입니다.

```python
>>> encryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
'Ilcrism Olcvs'
```

### `decryptMessage(key: str, message: str) -> str`

암호화된 메시지를 **복호화**합니다. 이 함수는 `translateMessage`를 `mode='decrypt'`로 호출하는 래퍼입니다.

```python
>>> decryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
'Harshil Darji'
```

### `translateMessage(key: str, message: str, mode: str) -> str`

암호화와 복호화의 핵심 로직을 모두 처리하는 범용 함수입니다.

-   **알고리즘**:
    1.  `mode` 값에 따라 원본 문자 집합(`charsA`)과 대상 문자 집합(`charsB`)을 결정합니다.
        -   **암호화(`encrypt`)**: `charsA`는 표준 알파벳, `charsB`는 `key`가 됩니다.
        -   **복호화(`decrypt`)**: `charsA`는 `key`, `charsB`는 표준 알파벳이 됩니다.
    2.  메시지의 각 문자를 순회합니다.
    3.  문자가 `charsA`에 포함되어 있으면, 해당 문자의 인덱스를 찾아 `charsB`에서 같은 인덱스에 있는 문자로 치환합니다.
    4.  대소문자를 구분하여 처리하며, 알파벳이 아닌 문자(공백, 기호 등)는 그대로 유지합니다.

### `getRandomKey() -> str`

유효한 단일 문자 치환 암호 키를 무작위로 생성합니다.

-   **알고리즘**: 표준 알파벳 리스트를 `random.shuffle()`을 사용하여 섞은 후, 다시 문자열로 결합하여 반환합니다.

### `main()`

사용자로부터 메시지와 모드(암호화/복호화)를 입력받아 암호화를 시연합니다. 키는 스크립트 내에 하드코딩되어 있습니다.

## 실행 방법

스크립트를 직접 실행하면 사용자 입력을 받아 암호화 또는 복호화를 수행합니다.

```bash
python simple_substitution_cipher.py
```

**실행 예시:**
```
Enter message: Hello World
Encrypt/Decrypt [e/d]: e

Encryption: 
Pcssi Bidsm
```

## 코드 개선 제안

1.  **오류 처리 방식 개선**: `checkValidKey` 함수는 오류가 발생하면 `sys.exit()`를 호출하여 프로그램을 강제 종료합니다. 이는 다른 모듈에서 이 함수를 재사용하기 어렵게 만듭니다. `ValueError`와 같은 예외(Exception)를 발생시키고, 호출하는 쪽에서 `try...except` 블록으로 처리하도록 수정하는 것이 더 유연한 설계입니다.

2.  **효율적인 문자열 처리**: `translateMessage` 함수 내에서 `translated += ...`와 같이 루프 안에서 문자열을 반복적으로 더하는 것은 성능에 비효율적입니다. 문자 조각들을 리스트에 저장한 후, 마지막에 `"".join()`을 사용하여 한 번에 합치는 것이 더 좋습니다. (이 스크립트에서는 이미 `translateMessage`가 그렇게 구현되어 있습니다. 좋은 예시입니다.)

3.  **코드 중복**: 이 스크립트는 `mono_alphabetic_ciphers.py`와 거의 동일한 기능을 수행합니다. 두 파일의 로직이 매우 유사하므로, 하나의 파일로 통합하여 코드 중복을 줄이는 것이 좋습니다. 이 파일은 키 유효성 검사와 랜덤 키 생성 기능이 추가되어 있어 더 완전한 구현입니다.

4.  **사용자 인터페이스 개선**: `main` 함수에서 키가 하드코딩되어 있습니다. 사용자로부터 키를 직접 입력받거나, `getRandomKey()`를 사용하여 랜덤 키를 생성하는 옵션을 제공하면 사용성이 향상됩니다.