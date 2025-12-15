# `mixed_keyword_cypher.py` 코드 설명

이 문서는 `mixed_keyword_cypher.py` 파이썬 스크립트에 포함된 `mixed_keyword` 함수를 설명합니다. 이 스크립트는 키워드를 사용하여 알파벳을 재배열하고, 이를 기반으로 문자를 치환하는 **혼합 키워드 암호(Mixed Keyword Cipher)**를 구현합니다.

## 목차
1.  혼합 키워드 암호란?
2.  함수 설명
    -   `mixed_keyword(key, pt)`
3.  실행 방법
4.  코드 개선 제안

## 혼합 키워드 암호란?

혼합 키워드 암호는 키워드를 사용하여 표준 알파벳 순서를 섞은 다음, 이 새로운 알파벳 순서를 기반으로 문자를 치환하는 방식입니다. 이 스크립트의 구현은 다음과 같은 독특한 방식으로 알파벳을 재배열합니다.

1.  **키워드 처리**: 키워드에서 중복된 문자를 제거합니다. (예: `college` -> `coleg`)
2.  **알파벳 확장**: 처리된 키워드 뒤에, 키워드에 포함되지 않은 나머지 알파벳 문자들을 순서대로 추가하여 26개의 고유한 문자로 이루어진 새로운 시퀀스를 만듭니다.
3.  **표 생성**: 이 시퀀스를 키워드의 길이만큼의 열(column)을 갖는 표(grid)에 위에서 아래로, 왼쪽에서 오른쪽으로 채워 넣습니다.
4.  **치환 맵 생성**: 표준 알파벳(`A, B, C, ...`) 순서와, 위에서 만든 표를 **세로로 읽은 순서**를 매핑하여 최종 치환 규칙을 만듭니다.
5.  **암호화**: 이 치환 규칙에 따라 평문을 암호문으로 변환합니다.

## 함수 설명

### `mixed_keyword(key: str = "college", pt: str = "UNIVERSITY") -> str`

주어진 키워드(`key`)와 평문(`pt`)을 사용하여 혼합 키워드 암호화를 수행합니다.

-   **알고리즘**:
    1.  키워드와 평문을 모두 대문자로 변환합니다.
    2.  키워드에서 중복 문자를 제거하여 `temp` 리스트를 생성합니다.
    3.  `temp` 리스트 뒤에 나머지 알파벳을 추가하여 26개의 고유한 문자로 구성된 전체 시퀀스를 만듭니다.
    4.  이 시퀀스를 `len(temp)`개의 열을 갖는 2차원 리스트(`modalpha`)로 재구성합니다.
    5.  `modalpha`를 세로로 읽으면서 표준 알파벳과 매핑되는 딕셔너리 `d`를 생성합니다.
    6.  생성된 딕셔너리 `d`를 사용하여 평문의 각 문자를 치환하여 암호문을 생성하고 반환합니다.

## 실행 방법

스크립트를 직접 실행하면 `key="college"`, `pt="UNIVERSITY"`를 사용하여 암호화를 수행하고, 생성된 치환 맵과 최종 암호문을 출력합니다.

```bash
python mixed_keyword_cypher.py
```

**실행 결과:**
```
{'A': 'C', 'B': 'A', 'C': 'I', 'D': 'P', 'E': 'U', 'F': 'Z', 'G': 'O', 'H': 'B', 'I': 'J', 'J': 'Q', 'K': 'V', 'L': 'L', 'M': 'D', 'N': 'K', 'O': 'R', 'P': 'W', 'Q': 'E', 'R': 'F', 'S': 'M', 'T': 'S', 'U': 'X', 'V': 'G', 'W': 'H', 'X': 'N', 'Y': 'T', 'Z': 'Y'}
XKJGUFMJST
```

## 코드 개선 제안

현재 코드는 동작은 하지만, 변수명이 모호하고 로직이 복잡하여 이해하고 유지보수하기 어렵습니다. 또한, `doctest`가 반환값 형식이 맞지 않아 실패합니다. 아래는 가독성과 정확성을 크게 향상시킨 리팩토링 제안입니다.

1.  **명확한 함수 분리**: 키 생성 로직과 암호화 로직을 별도의 함수로 분리하면 코드가 훨씬 명확해집니다.
2.  **알고리즘 단순화**: 복잡한 `for` 루프와 인덱스 계산 대신, `itertools`나 `numpy`를 사용하거나 더 직관적인 리스트 조작으로 알고리즘을 단순화할 수 있습니다.
3.  **의미 있는 변수명**: `temp`, `s`, `d`와 같은 변수명을 `unique_key_chars`, `row`, `cipher_map` 등으로 변경하여 코드의 의도를 명확히 전달해야 합니다.
4.  **`doctest` 수정**: `doctest`는 함수가 반환하는 값을 테스트합니다. 현재 함수는 `print(d)`를 포함하고 있어 테스트가 실패합니다. `print` 문을 제거하고, 함수가 암호문만 반환하도록 수정해야 합니다.

**리팩토링된 코드 예시:**

```python
import string
from itertools import zip_longest

def create_cipher_map(key: str) -> dict[str, str]:
    """
    Creates the substitution map based on the mixed keyword.
    """
    key = key.upper()
    
    # 1. Create the full sequence: unique key chars + rest of the alphabet
    unique_key_chars = sorted(set(key), key=key.index)
    alphabet = string.ascii_uppercase
    full_sequence = unique_key_chars + [ch for ch in alphabet if ch not in unique_key_chars]

    # 2. Create the grid (table)
    num_cols = len(unique_key_chars)
    # Use zip_longest to handle non-uniform column lengths
    grid = list(zip_longest(*[iter(full_sequence)] * num_cols, fillvalue=None))

    # 3. Read the grid vertically to create the cipher alphabet
    cipher_alphabet = []
    for col_idx in range(num_cols):
        for row_idx in range(len(grid)):
            if grid[row_idx][col_idx] is not None:
                cipher_alphabet.append(grid[row_idx][col_idx])

    # 4. Create the final mapping
    return {std_char: cipher_char for std_char, cipher_char in zip(alphabet, cipher_alphabet)}

def mixed_keyword_encrypt(key: str, plaintext: str) -> str:
    """
    Encrypts plaintext using the mixed keyword cipher.
    >>> mixed_keyword_encrypt("college", "UNIVERSITY")
    'XKJGUFMJST'
    """
    cipher_map = create_cipher_map(key)
    plaintext = plaintext.upper()
    
    encrypted_chars = [cipher_map.get(char, char) for char in plaintext]
    return "".join(encrypted_chars)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    key = "college"
    pt = "UNIVERSITY"
    encrypted_text = mixed_keyword_encrypt(key, pt)
    print(f"Cipher map for key '{key}':\n{create_cipher_map(key)}")
    print(f"Plaintext: {pt}")
    print(f"Encrypted: {encrypted_text}")
```