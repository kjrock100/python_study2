# `simple_keyword_cypher.py` 코드 설명

이 문서는 `simple_keyword_cypher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 키워드를 사용하여 치환 규칙을 만드는 **단순 키워드 암호(Simple Keyword Cipher)**를 구현합니다.

## 목차
1.  단순 키워드 암호란?
2.  함수 설명
    -   `remove_duplicates(key)`
    -   `create_cipher_map(key)`
    -   `encipher(message, cipher_map)`
    -   `decipher(message, cipher_map)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 단순 키워드 암호란?

단순 키워드 암호는 단일 문자 치환 암호의 일종으로, 키워드를 사용하여 치환 알파벳을 생성합니다.

1.  **키워드 처리**: 키워드에서 중복된 문자를 제거합니다. (예: `Goodbye` -> `Godbye`)
2.  **치환 알파벳 생성**: 처리된 키워드를 표준 알파벳의 시작 부분에 놓고, 그 뒤에 키워드에 포함되지 않은 나머지 알파벳 문자들을 순서대로 추가합니다.
    -   키: `Goodbye`
    -   처리된 키: `GODBYE`
    -   치환 알파벳: `GODBYEACFHIKLMNPQRSTUVWXZ`
3.  **암호화**: 표준 알파벳(`A, B, C, ...`)을 위에서 만든 치환 알파벳에 일대일로 매핑하여 평문을 암호문으로 변환합니다.
    -   `A` -> `G`, `B` -> `O`, `C` -> `D`, ...

이 스크립트의 구현은 2단계에서 약간의 차이가 있습니다. 키워드를 치환 알파벳의 시작 부분에 두는 대신, 표준 알파벳의 첫 문자부터 키워드의 문자로 매핑하고, 나머지 문자들을 순환적으로 매핑합니다.

## 함수 설명

### `remove_duplicates(key: str) -> str`

주어진 키워드에서 중복된 알파벳 문자를 제거합니다.

-   **알고리즘**: 문자열을 순회하면서, 이전에 등장하지 않은 알파벳 문자만 새로운 문자열에 추가합니다. 공백은 유지됩니다.

### `create_cipher_map(key: str) -> dict[str, str]`

주어진 키워드를 사용하여 치환 규칙을 담은 딕셔너리(cipher map)를 생성합니다.

-   **알고리즘**:
    1.  `remove_duplicates`를 호출하여 키워드를 처리합니다.
    2.  표준 알파벳의 첫 문자부터 순서대로, 처리된 키워드의 문자로 매핑합니다. (예: `A`->`G`, `B`->`O`, `C`->`D`, ...)
    3.  키워드 매핑이 끝나면, 나머지 표준 알파벳 문자들을 아직 매핑되지 않은 표준 알파벳의 처음부터 순환적으로 매핑합니다.

### `encipher(message: str, cipher_map: dict[str, str]) -> str`

주어진 메시지를 생성된 `cipher_map`을 이용해 **암호화**합니다.

-   **알고리즘**: 메시지의 각 문자를 `cipher_map`에서 찾아 해당하는 암호문 문자로 치환합니다. `cipher_map`에 없는 문자(공백, 기호 등)는 그대로 유지됩니다.

### `decipher(message: str, cipher_map: dict[str, str]) -> str`

암호화된 메시지를 **복호화**합니다.

-   **알고리즘**:
    1.  `cipher_map`의 키와 값을 뒤집어 복호화용 맵을 만듭니다.
    2.  이 새로운 맵을 사용하여 암호문을 원래의 평문으로 치환합니다.

### `main()`

사용자로부터 메시지, 키, 모드(암호화/복호화)를 입력받아 암호화를 시연하는 대화형 인터페이스를 제공합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 정확성을 테스트한 후, 사용자 입력을 받아 암호화를 수행합니다.

```bash
python simple_keyword_cypher.py
```

**실행 예시:**
```
Enter message to encode or decode: Hello World
Enter keyword: keyword
Encipher or decipher? E/D: e
JGNNQ YQTNF
```

## 코드 개선 제안

1.  **`create_cipher_map` 로직의 복잡성**: `create_cipher_map` 함수의 두 번째 `for` 루프는 `offset`을 계속 변경하면서 문자를 찾는 로직이 복잡하고 이해하기 어렵습니다. 키워드에 사용된 문자와 사용되지 않은 나머지 알파벳을 `set` 연산을 통해 명확히 분리한 후, 이를 순서대로 매핑하는 방식이 더 간결하고 직관적입니다.

    ```python
    # 개선 제안 예시
    import string

    def create_cipher_map_simple(key: str) -> dict[str, str]:
        key = remove_duplicates(key.upper()).replace(" ", "")
        alphabet = string.ascii_uppercase
        
        # 키워드에 없는 나머지 알파벳
        remaining_alphabet = [ch for ch in alphabet if ch not in key]
        
        # 치환 알파벳 생성
        cipher_alphabet = key + "".join(remaining_alphabet)
        
        # 표준 알파벳과 치환 알파벳을 매핑
        return {std_char: cipher_char for std_char, cipher_char in zip(alphabet, cipher_alphabet)}
    ```
    > **참고**: 위 예시는 표준 키워드 암호 생성 방식이며, 원래 코드의 독특한 매핑 방식과는 다릅니다. 원래 로직을 유지하면서 가독성을 높이려면, `while` 루프의 동작을 명확히 설명하는 주석을 추가하는 것이 좋습니다.

2.  **`remove_duplicates` 함수 개선**: `remove_duplicates` 함수는 `ch.isalpha()`를 사용하여 알파벳만 처리하지만, 공백도 특별히 유지합니다. 이 로직은 `set`을 사용하여 더 간결하게 작성할 수 있습니다.

    ```python
    # 개선 제안 예시
    def remove_duplicates_simple(key: str) -> str:
        seen = set()
        result = []
        for char in key:
            if char.isalpha() and char.upper() not in seen:
                seen.add(char.upper())
                result.append(char)
            elif char == ' ':
                result.append(char)
        return "".join(result)
    ```

3.  **오류 처리**: `main` 함수에서 사용자가 'e'나 'd'가 아닌 다른 값을 입력하면 `KeyError`가 발생합니다. `try-except` 블록을 사용하여 이 오류를 처리하고 사용자에게 친절한 안내 메시지를 보여주면 프로그램의 안정성이 향상됩니다.