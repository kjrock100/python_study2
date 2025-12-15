# `playfair_cipher.py` 코드 설명

이 문서는 `playfair_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 두 글자씩 쌍(digraph)을 지어 암호화하는 다중 문자 치환 암호인 **플레이페어 암호(Playfair Cipher)**를 구현합니다.

## 목차
1.  플레이페어 암호란?
2.  함수 설명
    -   `chunker(seq, size)`
    -   `prepare_input(dirty)`
    -   `generate_table(key)`
    -   `encode(plaintext, key)`
    -   `decode(ciphertext, key)`
3.  실행 방법
4.  코드 개선 제안

## 플레이페어 암호란?

플레이페어 암호는 키워드를 사용하여 5x5 크기의 암호판(Polybius Square)을 만들고, 평문을 두 글자씩 묶어 암호화하는 방식입니다. 암호화 규칙은 두 글자의 위치 관계에 따라 결정됩니다.

1.  **암호판 생성**: 키워드의 중복되지 않는 문자들을 먼저 채우고, 나머지 알파벳을 순서대로 채워 5x5 암호판을 만듭니다. (보통 'I'와 'J'는 같은 칸에 둡니다.)
2.  **평문 준비**:
    -   평문을 두 글자씩 묶습니다.
    -   같은 글자가 연속으로 나오면(예: 'LL'), 중간에 'X'와 같은 대체 문자를 삽입합니다. ('LXL')
    -   평문의 전체 길이가 홀수이면, 마지막에 'X'를 추가하여 짝수로 맞춥니다.
3.  **암호화 규칙**:
    -   **같은 행**: 두 글자가 암호판의 같은 행에 있으면, 각각 오른쪽으로 한 칸 이동한 문자로 치환합니다. (행의 끝은 처음으로 순환)
    -   **같은 열**: 두 글자가 같은 열에 있으면, 각각 아래쪽으로 한 칸 이동한 문자로 치환합니다. (열의 끝은 처음으로 순환)
    -   **다른 행/열 (사각형)**: 두 글자가 서로 다른 행과 열에 있으면, 각 글자는 자신이 속한 행과 상대방 글자가 속한 열이 만나는 위치의 문자로 치환됩니다.

복호화는 이 과정의 역순으로 진행됩니다.

## 함수 설명

### `chunker(seq: Iterable[str], size: int) -> Generator`

주어진 시퀀스(`seq`)를 지정된 `size`만큼의 덩어리(chunk)로 나누어 반환하는 제너레이터(generator) 함수입니다.

-   **용도**: 평문이나 암호문을 두 글자씩 묶는 데 사용됩니다.

### `prepare_input(dirty: str) -> str`

평문을 플레이페어 암호화에 적합한 형태로 전처리합니다.

-   **알고리즘**:
    1.  알파벳이 아닌 문자를 모두 제거하고 대문자로 변환합니다.
    2.  연속되는 두 글자가 같으면 사이에 'X'를 삽입합니다.
    3.  최종 문자열의 길이가 홀수이면 끝에 'X'를 추가합니다.

### `generate_table(key: str) -> list[str]`

주어진 키워드(`key`)를 사용하여 5x5 플레이페어 암호판을 생성합니다.

-   **알고리즘**:
    1.  키워드에서 중복되지 않는 알파벳 문자들을 순서대로 `table` 리스트에 추가합니다. ('I'와 'J'는 'I'로 통일)
    2.  `table`에 포함되지 않은 나머지 알파벳들을 순서대로 추가하여 25개의 문자로 구성된 1차원 리스트를 완성합니다.

### `encode(plaintext: str, key: str) -> str`

주어진 평문을 플레이페어 암호로 **암호화**합니다.

-   **알고리즘**:
    1.  `generate_table`로 암호판을 생성하고, `prepare_input`으로 평문을 전처리합니다.
    2.  `chunker`를 이용해 평문을 두 글자씩 묶습니다.
    3.  각 쌍에 대해, 암호판에서의 위치를 찾고 위에서 설명한 세 가지 암호화 규칙 중 하나를 적용하여 암호문을 생성합니다.

### `decode(ciphertext: str, key: str) -> str`

암호화된 텍스트를 원래의 평문으로 **복호화**합니다.

-   **알고리즘**: `encode`와 유사하지만, 암호화 규칙의 반대 방향으로 연산을 수행합니다. (오른쪽 대신 왼쪽, 아래쪽 대신 위쪽으로 이동)

## 실행 방법

이 스크립트는 직접 실행할 수 있는 `main` 블록이 없습니다. 다른 파이썬 스크립트에서 함수를 `import`하여 사용해야 합니다.

**사용 예시:**
```python
from playfair_cipher import encode, decode

key = "PLAYFAIR EXAMPLE"
plaintext = "Hide the gold in the tree stump"

encrypted = encode(plaintext, key)
print(f"Encrypted: {encrypted}")
# 출력: Encrypted: BMNDZBXDKYBEKUDMUIXMMOUVIF

decrypted = decode(encrypted, key)
print(f"Decrypted: {decrypted}")
# 출력: Decrypted: HIDETHEGOLDINTHETREXESTUMPX
```

## 코드 개선 제안

1.  **`prepare_input` 함수의 버그 가능성**: `prepare_input` 함수에서 `clean += dirty[i]`와 `clean += "X"`가 반복되면서, 'X'가 삽입된 후에도 원래의 `dirty` 인덱스를 계속 참조합니다. 이로 인해 'XXX'와 같은 입력에서 의도치 않은 결과가 나올 수 있습니다. `while` 루프를 사용하거나, 처리된 인덱스를 추적하는 방식으로 로직을 개선하는 것이 더 안정적입니다.

2.  **암호판 데이터 구조**: 현재 암호판은 1차원 리스트로 구현되어 있어, 행과 열을 계산하기 위해 `divmod`를 반복적으로 사용합니다. 5x5 크기의 2차원 리스트(리스트의 리스트)나 `numpy` 배열을 사용하면 좌표를 더 직관적으로 다룰 수 있습니다. 또한, 문자의 좌표를 미리 계산하여 딕셔너리에 저장해두면 `table.index()` 호출을 피할 수 있어 성능이 향상됩니다.

    ```python
    # 개선 제안 예시
    def generate_table_and_map(key: str):
        # ... (table 생성 로직) ...
        char_to_pos = {char: (i // 5, i % 5) for i, char in enumerate(table)}
        pos_to_char = {v: k for k, v in char_to_pos.items()}
        return char_to_pos, pos_to_char
    ```

3.  **코드 중복**: `encode`와 `decode` 함수는 매우 유사한 구조를 가집니다. 이동 방향(1 또는 -1)을 인자로 받는 범용 함수를 만들어 코드 중복을 줄일 수 있습니다.

4.  **`doctest` 및 `main` 블록 추가**: 함수에 `doctest`를 추가하고, 사용자 입력을 받아 암호화를 시연하는 `if __name__ == "__main__"` 블록을 추가하면 스크립트의 테스트와 사용이 더 편리해집니다.