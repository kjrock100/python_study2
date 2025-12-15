# `shuffled_shift_cipher.py` 코드 설명

이 문서는 `shuffled_shift_cipher.py` 파이썬 스크립트에 포함된 `ShuffledShiftCipher` 클래스를 설명합니다. 이 스크립트는 카이사르 암호(Caesar Cipher)를 변형하여, 키워드를 기반으로 문자 집합을 복잡하게 섞은 후 이동(shift) 암호화를 수행하는 독창적인 알고리즘을 구현합니다.

## 목차
1.  셔플 시프트 암호란?
2.  `ShuffledShiftCipher` 클래스
    -   `__init__(passcode)`
    -   `__passcode_creator()`
    -   `__make_key_list()`
    -   `__make_shift_key()`
    -   `encrypt(plaintext)`
    -   `decrypt(encoded_message)`
3.  실행 방법
4.  코드 개선 제안

## 셔플 시프트 암호란?

이 암호는 표준 카이사르 암호의 취약점인 전사 공격(brute-force attack)을 어렵게 만들기 위해 설계되었습니다. 암호화 과정은 다음과 같습니다.

1.  **패스코드(Passcode) 생성**: 암호화의 기반이 되는 무작위 문자열(패스코드)을 생성합니다.
2.  **치환 알파벳 생성 (`__make_key_list`)**:
    -   패스코드에 포함된 고유한 문자들을 "중단점(breakpoint)"으로 사용합니다.
    -   기본 문자 집합(알파벳, 숫자, 기호 등)을 순회하다가 중단점을 만나면, 그때까지 쌓인 문자열을 뒤집어서 새로운 치환 알파벳에 추가합니다.
    -   이 과정을 반복하여 예측하기 어려운 순서의 새로운 치환 알파벳(`key_list`)을 만듭니다.
3.  **이동 키(Shift Key) 생성 (`__make_shift_key`)**:
    -   패스코드의 각 문자를 ASCII 값으로 변환하고, 홀수 번째 값들의 부호를 바꾸어 모두 더한 값을 최종 이동 키로 사용합니다.
4.  **암호화/복호화**:
    -   생성된 치환 알파벳(`key_list`) 상에서, 계산된 이동 키만큼 문자를 이동시켜 암호화 또는 복호화를 수행합니다.

이 방식은 치환 알파벳의 경우의 수가 매우 크고(97! 이상), 이동 키 또한 패스코드에 따라 달라지므로 전사 공격이 거의 불가능해집니다.

## `ShuffledShiftCipher` 클래스

셔플 시프트 암호화 및 복호화 기능을 캡슐화한 클래스입니다.

### `__init__(passcode: str | None = None)`

클래스 인스턴스를 초기화합니다.
-   사용자가 `passcode`를 제공하면 그것을 사용하고, 제공하지 않으면 `__passcode_creator`를 호출하여 무작위 패스코드를 생성합니다.
-   생성된 패스코드를 기반으로 `__make_key_list`와 `__make_shift_key`를 호출하여 치환 알파벳과 이동 키를 미리 계산해 둡니다.

### `__passcode_creator() -> list[str]`

10~20자 길이의 무작위 패스코드를 생성하여 리스트 형태로 반환합니다.

### `__make_key_list() -> list[str]`

위에서 설명한 "중단점과 뒤집기" 알고리즘을 사용하여 복잡하게 섞인 치환 알파벳 리스트를 생성합니다.

### `__make_shift_key() -> int`

패스코드를 기반으로 암호화/복호화에 사용할 정수 이동 키를 계산합니다.

### `encrypt(plaintext: str) -> str`

주어진 평문을 **암호화**합니다.

-   **알고리즘**: 평문의 각 문자에 대해, `__key_list`에서의 위치를 찾고 `__shift_key`만큼 오른쪽으로 이동(양수 방향)시킨 위치의 문자로 치환합니다.

### `decrypt(encoded_message: str) -> str`

암호화된 메시지를 **복호화**합니다.

-   **알고리즘**: 암호문의 각 문자에 대해, `__key_list`에서의 위치를 찾고 `__shift_key`만큼 왼쪽으로 이동(음수 방향)시킨 위치의 문자로 치환합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 클래스의 예제 코드가 실행되고, 암호화-복호화 과정의 정확성이 자동으로 테스트됩니다.

```bash
python shuffled_shift_cipher.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **`__make_key_list` 함수의 복잡성**: 이 함수의 로직은 독창적이지만, `temp_list.extend(i)`와 같이 문자열을 문자 리스트로 확장하는 부분은 불필요합니다. `temp_list`에 문자열을 직접 추가하고, 뒤집을 때 `"".join(temp_list)[::-1]`과 같이 처리하는 것이 더 직관적일 수 있습니다.

    ```python
    # 개선 제안 예시
    def __make_key_list(self) -> list[str]:
        key_list_options = "..."
        breakpoints = sorted(set(self.__passcode))
        shuffled_list = []
        temp_chunk = ""
        for char in key_list_options:
            temp_chunk += char
            if char in breakpoints or char == key_list_options[-1]:
                shuffled_list.extend(list(temp_chunk[::-1]))
                temp_chunk = ""
        return shuffled_list
    ```

2.  **`__neg_pos` 함수 이름**: 함수 이름이 "negative position"을 의미하는 것 같지만, 실제로는 값의 부호를 바꾸는 역할을 합니다. `alternate_signs`나 `negate_alternate_elements`와 같이 더 명확한 이름으로 변경하면 코드의 의도를 파악하기 쉬워집니다.

3.  **입력 유효성 검사**: `encrypt`와 `decrypt` 함수는 입력된 문자가 `__key_list`에 반드시 존재한다고 가정합니다. 만약 `__key_list`에 없는 문자(예: 일부 특수 문자)가 입력되면 `ValueError`가 발생합니다. `try-except` 블록을 사용하여 이러한 문자를 무시하거나 특정 문자로 대체하도록 처리하면 프로그램의 안정성이 향상됩니다.

4.  **클래스 활용도**: 현재 클래스는 패스코드가 한 번 정해지면 변경할 수 없습니다. 패스코드를 변경하고 관련 키들을 다시 생성하는 메서드(예: `reset_passcode(new_passcode)`)를 추가하면 클래스의 유연성이 높아집니다.