# `trafid_cipher.py` 코드 설명

이 문서는 `trafid_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 비피드 암호(Bifid Cipher)를 3차원으로 확장한 형태인 **트리피드 암호(Trifid Cipher)**를 구현합니다.

## 목차
1.  트리피드 암호란?
2.  함수 설명
    -   `__prepare(message, alphabet)`
    -   `__encryptPart(messagePart, character2Number)`
    -   `__decryptPart(messagePart, character2Number)`
    -   `encryptMessage(message, alphabet, period)`
    -   `decryptMessage(message, alphabet, period)`
3.  실행 방법
4.  코드 개선 제안

## 트리피드 암호란?

트리피드 암호는 각 문자를 3x3x3 큐브(또는 3개의 3x3 격자)에서의 좌표로 변환하여 암호화하는 방식입니다. 27개의 문자(보통 알파벳 26자와 '.' 또는 '+' 같은 기호 하나)를 사용합니다.

**암호화 과정**:
1.  **좌표 변환**: 평문을 `period`(주기) 크기의 블록으로 나눕니다. 각 블록의 문자들을 3자리 숫자 좌표(예: 'A' -> '111')로 변환합니다.
2.  **좌표 재배열**: 각 블록 내에서, 모든 문자의 첫 번째 좌표들을 먼저 나열하고, 그 뒤에 두 번째 좌표들, 마지막으로 세 번째 좌표들을 나열하여 하나의 긴 숫자 시퀀스를 만듭니다.
3.  **암호문 변환**: 재배열된 숫자 시퀀스를 세 개씩 묶어 새로운 좌표로 만들고, 이 좌표에 해당하는 문자를 찾아 암호문을 완성합니다.

복호화는 이 과정의 역순으로 진행됩니다.

## 함수 설명

### `__prepare(message, alphabet)`

암호화/복호화를 시작하기 전에 입력값(메시지, 알파벳)을 검증하고 필요한 데이터 구조(조회용 딕셔너리)를 생성하는 내부 헬퍼 함수입니다.

-   **동작**:
    -   메시지와 알파벳에서 공백을 제거하고 대문자로 변환합니다.
    -   알파벳의 길이가 27인지, 메시지의 모든 문자가 알파벳에 포함되어 있는지 확인합니다.
    -   문자를 3자리 숫자 좌표로 변환하는 `character2Number` 딕셔너리와 그 반대인 `number2Character` 딕셔너리를 생성하여 반환합니다.

### `__encryptPart(messagePart, character2Number)`

메시지의 한 블록(`messagePart`)을 암호화 과정의 2단계(좌표 재배열)까지 수행합니다.

-   **알고리즘**:
    1.  블록의 각 문자를 `character2Number`를 이용해 3자리 숫자 좌표로 변환합니다.
    2.  모든 첫 번째 좌표, 모든 두 번째 좌표, 모든 세 번째 좌표를 각각 모아서 하나의 긴 숫자 문자열로 이어 붙여 반환합니다.

### `__decryptPart(messagePart, character2Number)`

암호문의 한 블록을 복호화 과정의 2단계(좌표 재배열)까지 수행합니다. `__encryptPart`의 역과정입니다.

### `encryptMessage(message, alphabet, period)`

주어진 메시지를 트리피드 암호로 **암호화**합니다.

-   **알고리즘**:
    1.  `__prepare`를 호출하여 초기 설정을 합니다.
    2.  메시지를 `period` 크기의 블록으로 나눕니다.
    3.  각 블록에 대해 `__encryptPart`를 호출하여 재배열된 숫자 문자열을 얻고, 이를 모두 합칩니다.
    4.  합쳐진 숫자 문자열을 3자리씩 잘라 `number2Character` 딕셔너리를 이용해 문자로 변환하여 최종 암호문을 생성합니다.

### `decryptMessage(message, alphabet, period)`

암호화된 메시지를 원래의 평문으로 **복호화**합니다.

-   **알고리즘**:
    1.  암호문을 `period` 크기의 블록으로 나눕니다.
    2.  각 블록에 대해 `__decryptPart`를 호출하여 원래 순서의 좌표 그룹(첫 번째 좌표들, 두 번째 좌표들, 세 번째 좌표들)을 얻습니다.
    3.  이 좌표 그룹들을 재조합하여 원래의 3자리 숫자 좌표들을 복원합니다.
    4.  복원된 각 3자리 숫자 좌표를 `number2Character`를 이용해 문자로 변환하여 평문을 생성합니다.

## 실행 방법

스크립트를 직접 실행하면 미리 정의된 메시지와 알파벳을 사용하여 암호화 및 복호화 과정을 시연하고 결과를 출력합니다.

```bash
python trafid_cipher.py
```

**실행 결과:**
```
Encrypted: SUYUSZDAZOHWTYHARTA.MY.XOJ.Y.G.
Decrypted: DEFENDTHEEASTWALLOFTHECASTLE.
```

## 코드 개선 제안

1.  **함수 분리와 네이밍**: `__encryptPart`와 `__decryptPart`는 이름과 달리 암호화/복호화의 일부만 수행합니다. 이 함수들의 역할을 더 명확하게 반영하는 이름(예: `rearrange_coords_for_encrypt`)으로 변경하고, 주석을 통해 그 역할을 명확히 설명하는 것이 좋습니다. 또한, `__prepare` 함수는 클래스로 묶어 관련 데이터와 메서드를 캡슐화하면 더 구조적인 코드가 될 수 있습니다.

2.  **효율적인 문자열 처리**: `__encryptPart`와 `decryptMessage` 등 여러 함수에서 `+=` 연산자를 사용하여 루프 안에서 문자열을 반복적으로 더하고 있습니다. 이는 성능에 비효율적입니다. 문자 조각들을 리스트에 저장한 후, 마지막에 `"".join()`을 사용하여 한 번에 합치는 것이 더 좋습니다.

3.  **오류 처리 방식**: `__prepare` 함수는 오류가 발생하면 `KeyError`나 `ValueError`를 발생시킵니다. 이는 좋은 방식이지만, 호출하는 쪽에서 이 예외들을 `try...except` 블록으로 처리하는 로직을 추가하면 프로그램의 안정성이 더욱 향상됩니다. (예: `main` 블록에서)

4.  **슬라이싱 로직**: `encryptMessage`와 `decryptMessage`에서 `range(0, len(message) + 1, period)`와 같이 슬라이싱을 위해 `+ 1`을 사용하는 부분은 약간 혼란을 줄 수 있습니다. `range(0, len(message), period)`로도 동일하게 동작하며 더 직관적입니다.

    ```python
    # 개선 제안 예시 (encryptMessage)
    encrypted_numeric_parts = []
    for i in range(0, len(message), period):
        part = message[i : i + period]
        encrypted_numeric_parts.append(__encryptPart(part, character2Number))
    encrypted_numeric = "".join(encrypted_numeric_parts)
    ```