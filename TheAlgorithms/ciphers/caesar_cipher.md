# `caesar_cipher.py` 코드 설명

이 문서는 `caesar_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 가장 널리 알려진 고전 암호 중 하나인 **카이사르 암호(Caesar Cipher)**의 암호화, 복호화, 그리고 전사 공격(brute-force) 기능을 구현합니다.

## 목차
1.  카이사르 암호란?
2.  함수 설명
    -   `encrypt(input_string, key, alphabet)`
    -   `decrypt(input_string, key, alphabet)`
    -   `brute_force(input_string, alphabet)`
3.  실행 방법
4.  코드 개선 제안

## 카이사르 암호란?

카이사르 암호는 각 문자를 알파벳 상에서 일정한 거리만큼 밀어서 다른 문자로 치환하는 간단한 **치환 암호**입니다. 여기서 '밀어내는 거리'를 **키(key)**라고 합니다.

예를 들어, 키가 3일 경우 'A'는 'D'로, 'B'는 'E'로 치환됩니다. 알파벳의 끝을 넘어가면 다시 처음으로 돌아옵니다 (예: 'X' -> 'A').

## 함수 설명

### `encrypt(input_string: str, key: int, alphabet: str | None = None) -> str`

주어진 문자열을 카이사르 암호로 **암호화**합니다.

-   **알고리즘**:
    1.  사용할 알파벳 집합(`alphabet`)을 결정합니다. 지정되지 않으면 기본 알파벳(대소문자)을 사용합니다.
    2.  입력 문자열의 각 문자를 순회합니다.
    3.  문자가 알파벳 집합에 포함되어 있으면, 다음 공식을 사용하여 새로운 문자의 인덱스를 계산합니다.
        -   `새로운 인덱스 = (기존 인덱스 + key) % 알파벳 길이`
    4.  계산된 인덱스에 해당하는 문자를 결과 문자열에 추가합니다.
    5.  문자가 알파벳 집합에 없으면(공백, 기호 등), 그대로 결과 문자열에 추가합니다.

```python
>>> encrypt('The quick brown fox jumps over the lazy dog', 8)
'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'
```

### `decrypt(input_string: str, key: int, alphabet: str | None = None) -> str`

카이사르 암호로 암호화된 문자열을 **복호화**합니다.

-   **알고리즘**:
    -   이 함수는 `encrypt` 함수를 재치있게 재사용합니다. `key` 값을 음수로 만들어 `encrypt` 함수를 호출하면, 문자를 반대 방향으로 밀어내는 효과가 있어 복호화가 수행됩니다.
    -   `key *= -1`
    -   `return encrypt(input_string, key, alphabet)`

```python
>>> decrypt('bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo', 8)
'The quick brown fox jumps over the lazy dog'
```

### `brute_force(input_string: str, alphabet: str | None = None) -> dict[int, str]`

암호문을 가능한 모든 키로 복호화하여 **전사 공격(Brute-Force Attack)**을 수행합니다.

-   **역할**: 키를 모를 때, 모든 가능한 키(1부터 알파벳 길이까지)를 시도하여 복호화된 모든 결과를 보여줍니다. 사용자는 이 결과들 중에서 의미 있는 문장을 찾아 원래의 평문과 키를 유추할 수 있습니다.
-   **알고리즘**:
    1.  `1`부터 알파벳 길이까지의 모든 숫자를 `key`로 사용하여 루프를 실행합니다.
    2.  각 `key`에 대해 `decrypt` 함수를 호출하여 복호화된 메시지를 얻습니다.
    3.  결과를 `key`를 키로, 복호화된 메시지를 값으로 하는 딕셔너리에 저장합니다.
    4.  모든 키에 대한 시도가 끝나면 딕셔너리를 반환합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자 친화적인 메뉴 인터페이스가 나타납니다.

```bash
python caesar_cipher.py
```

메뉴에서 암호화(1), 복호화(2), 전사 공격(3) 중 원하는 작업을 선택하고, 안내에 따라 메시지와 키를 입력하면 됩니다.

## 코드 개선 제안

1.  **효율적인 문자열 처리**: `encrypt` 함수 내에서 `result += character`와 같이 루프 안에서 문자열을 반복적으로 더하는 것은 성능에 비효율적입니다. 문자 조각들을 리스트에 저장한 후, 마지막에 `"".join()`을 사용하여 한 번에 합치는 것이 더 좋습니다.

    ```python
    # 개선 제안 예시
    def encrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
        alpha = alphabet or ascii_letters
        result_chars = []
        alpha_len = len(alpha)
        for character in input_string:
            if character not in alpha:
                result_chars.append(character)
            else:
                new_key = (alpha.index(character) + key) % alpha_len
                result_chars.append(alpha[new_key])
        return "".join(result_chars)
    ```

2.  **`brute_force` 함수와 `brute_force_caesar_cipher.py`의 관계**: 이 파일의 `brute_force` 함수는 `brute_force_caesar_cipher.py`의 `decrypt` 함수와 거의 동일한 역할을 합니다. 두 스크립트의 기능을 통합하거나, 이 파일의 `brute_force` 함수가 `brute_force_caesar_cipher.py`의 기능을 대체하도록 하여 코드 중복을 줄일 수 있습니다. 이 파일의 구현이 딕셔너리를 반환하므로 더 재사용성이 높습니다.

3.  **사용자 입력 유효성 검사**: `main` 블록에서 `key`를 입력받을 때 `int()` 변환에 실패할 경우(예: 사용자가 문자를 입력) `ValueError`가 발생하여 프로그램이 비정상 종료됩니다. `try-except` 블록을 사용하여 이러한 입력을 처리하면 프로그램의 안정성을 높일 수 있습니다.

    ```python
    # 개선 제안 예시
    try:
        key = int(input("Please enter off-set: ").strip())
    except ValueError:
        print("Invalid off-set. Please enter a number.")
        continue
    ```

4.  **알파벳 사용자 정의**: 현재 메뉴 인터페이스에서는 기본 알파벳만 사용합니다. 사용자가 직접 암호화에 사용할 알파벳을 지정할 수 있는 옵션을 추가하면 함수의 유연성을 더 잘 활용할 수 있습니다.
