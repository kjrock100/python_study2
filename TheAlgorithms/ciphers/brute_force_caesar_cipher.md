# `brute_force_caesar_cipher.py` 코드 설명

이 문서는 `brute_force_caesar_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 **카이사르 암호(Caesar Cipher)**로 암호화된 메시지를 **전사 공격(Brute-Force Attack)** 방식으로 해독합니다.

## 목차
1.  카이사르 암호 전사 공격이란?
2.  함수 설명
    -   `decrypt(message)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 카이사르 암호 전사 공격이란?

카이사르 암호는 알파벳을 일정한 거리만큼 밀어서 문자를 치환하는 간단한 암호 방식입니다. 영어 알파벳의 경우, 가능한 키(이동 거리)는 0부터 25까지 총 26개뿐입니다.

**전사 공격**은 이처럼 키의 경우의 수가 적을 때, 가능한 모든 키를 하나씩 전부 시도하여 암호를 해독하는 방법입니다. 이 스크립트는 26개의 모든 키로 메시지를 복호화한 결과를 출력하여, 사용자가 그중에서 의미 있는 평문을 직접 찾을 수 있도록 합니다.

## 함수 설명

### `decrypt(message: str) -> None`

주어진 암호문을 가능한 모든 키(0~25)로 복호화하여 결과를 출력합니다.

-   **알고리즘**:
    1.  `0`부터 `25`까지의 모든 숫자를 `key`로 사용하여 루프를 실행합니다.
    2.  각 `key`에 대해, 입력된 `message`의 모든 문자를 순회합니다.
    3.  문자가 알파벳이면, 해당 문자의 인덱스에서 `key` 값을 뺍니다.
    4.  계산 결과가 음수이면, 알파벳 개수(26)를 더하여 순환(wrap-around)시킵니다.
    5.  새로운 인덱스에 해당하는 문자를 찾아 결과 문자열에 추가합니다.
    6.  문자가 알파벳이 아니면(공백, 기호 등), 그대로 결과 문자열에 추가합니다.
    7.  하나의 `key`에 대한 복호화가 완료되면, 해당 키와 함께 결과를 화면에 출력합니다.

### `main()`

사용자로부터 암호화된 메시지를 입력받아 `decrypt` 함수를 호출하는 메인 로직을 수행합니다.

-   **동작**:
    1.  사용자에게 "Encrypted message: " 프롬프트를 보여주고 입력을 받습니다.
    2.  입력된 메시지를 모두 대문자로 변환합니다.
    3.  `decrypt()` 함수를 호출하여 전사 공격을 시작합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자 입력을 받아 전사 공격을 수행합니다.

```bash
python brute_force_caesar_cipher.py
```

실행 후, 터미널에 해독할 암호문을 입력합니다.

```
Encrypted message: TMDETUX PMDVU
Decryption using Key #0: TMDETUX PMDVU
...
Decryption using Key #12: HARSHIL DARJI
...
Decryption using Key #25: UNEFUVY QNEWV
```

## 코드 개선 제안

1.  **함수 역할 분리**: 현재 `decrypt` 함수는 복호화 로직과 출력 로직을 모두 담당합니다. 이 함수가 복호화된 결과 리스트를 반환하도록 수정하고, 출력은 호출하는 쪽(예: `main` 함수)에서 담당하도록 하면 함수의 재사용성이 높아집니다.

2.  **효율적인 문자열 처리**: 루프 안에서 `translated = translated + ...`와 같이 문자열을 반복적으로 더하는 것은 성능에 비효율적입니다. 문자 조각들을 리스트에 저장한 후, 마지막에 `"".join()`을 사용하여 한 번에 합치는 것이 더 좋습니다.

    ```python
    # 개선 제안 예시
    def decrypt(message: str) -> list[str]:
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        all_decryptions = []
        for key in range(len(LETTERS)):
            translated_chars = []
            for symbol in message:
                if symbol in LETTERS:
                    num = (LETTERS.find(symbol) - key) % len(LETTERS)
                    translated_chars.append(LETTERS[num])
                else:
                    translated_chars.append(symbol)
            all_decryptions.append("".join(translated_chars))
        return all_decryptions
    ```

3.  **상수 위치**: `LETTERS` 상수는 `decrypt` 함수 내부에 정의되어 있습니다. 이 상수는 변하지 않으므로, 함수 바깥의 모듈 레벨에 정의하는 것이 더 일반적이고 효율적입니다.
