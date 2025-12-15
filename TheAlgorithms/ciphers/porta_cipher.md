# `porta_cipher.py` 코드 설명

이 문서는 `porta_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 비즈네르 암호와 유사한 다중 문자 치환 암호의 일종인 **포르타 암호(Porta Cipher)**를 구현합니다.

## 목차
1.  포르타 암호란?
2.  주요 데이터 구조
3.  함수 설명
    -   `generate_table(key)`
    -   `get_position(table, char)`
    -   `get_opponent(table, char)`
    -   `encrypt(key, words)`
    -   `decrypt(key, words)`
4.  실행 방법
5.  코드 개선 제안

## 포르타 암호란?

포르타 암호는 16세기에 지오반니 바티스타 델라 포르타가 고안한 다중 문자 치환 암호입니다. 이 암호는 키워드의 각 문자에 따라 서로 다른 치환 알파벳 테이블을 선택하고, 이를 순환적으로 사용하여 평문을 암호화합니다.

포르타 암호의 가장 큰 특징은 **상호 암호(reciprocal cipher)**라는 점입니다. 즉, 암호화 과정과 복호화 과정이 완전히 동일합니다. 어떤 문자를 특정 키로 암호화하여 다른 문자를 얻었다면, 그 암호화된 문자를 동일한 키로 다시 암호화하면 원래의 문자로 돌아옵니다.

**암호화 과정**:
1.  **테이블 선택**: 키워드의 첫 번째 문자에 해당하는 포르타 테이블을 선택합니다.
2.  **치환**: 평문의 첫 번째 문자를 선택된 테이블을 사용하여 치환합니다.
3.  **반복**: 키워드의 다음 문자에 해당하는 테이블을 선택하고, 평문의 다음 문자를 치환합니다. 이 과정을 평문이 끝날 때까지 반복하며, 키워드는 순환적으로 사용됩니다.

## 주요 데이터 구조

### `alphabet`

포르타 암호의 핵심인 13개의 치환 테이블을 정의하는 딕셔너리입니다.
-   **키**: 'A'부터 'Z'까지의 알파벳. 두 개의 키(예: 'A', 'B')가 하나의 테이블을 공유합니다.
-   **값**: `(상단 알파벳, 하단 알파벳)` 형태의 튜플.
    -   상단 알파벳은 항상 'A'부터 'M'까지입니다.
    -   하단 알파벳은 키에 따라 순환적으로 이동(shift)된 'N'부터 'Z'까지의 알파벳입니다.

## 함수 설명

### `generate_table(key: str) -> list[tuple[str, str]]`

주어진 키워드(`key`)에 해당하는 포르타 테이블의 리스트를 생성합니다.

-   **알고리즘**: 키워드의 각 문자를 `alphabet` 딕셔너리에서 찾아 해당하는 테이블(튜플)을 리스트에 추가하여 반환합니다.

### `get_position(table: tuple[str, str], char: str) -> tuple[int, int]`

특정 포르타 테이블에서 주어진 문자의 위치(행, 열)를 찾습니다.

-   **반환값**: `(행 인덱스, 열 인덱스)` 형태의 튜플. 행은 0(상단) 또는 1(하단)입니다.

### `get_opponent(table: tuple[str, str], char: str) -> str`

주어진 테이블에서 특정 문자의 **대응 문자(opponent)**를 찾습니다.

-   **알고리즘**:
    -   문자가 상단 행에 있으면, 같은 열의 하단 행에 있는 문자를 반환합니다.
    -   문자가 하단 행에 있으면, 같은 열의 상단 행에 있는 문자를 반환합니다.

### `encrypt(key: str, words: str) -> str`

주어진 평문을 포르타 암호로 **암호화**합니다.

-   **알고리즘**:
    1.  `generate_table`로 키에 해당하는 테이블 리스트를 만듭니다.
    2.  평문의 각 문자를 순회하면서, 키워드도 순환적으로 순회합니다.
    3.  현재 키 문자에 해당하는 테이블을 사용하여, `get_opponent` 함수로 평문 문자를 치환합니다.
    4.  치환된 문자들을 모아 암호문을 생성합니다.

### `decrypt(key: str, words: str) -> str`

암호화된 텍스트를 **복호화**합니다.

-   **알고리즘**: 포르타 암호는 상호 암호이므로, 복호화는 암호화와 완전히 동일합니다. 이 함수는 단순히 `encrypt` 함수를 다시 호출합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자로부터 키와 암호화할 텍스트를 입력받아 암호화 및 복호화 과정을 시연합니다.

```bash
python porta_cipher.py
```

**실행 예시:**
```
Enter key: marvin
Enter text to encrypt: jessica
Encrypted: QRACRWU
Decrypted with key: JESSICA
```

## 코드 개선 제안

1.  **`alphabet` 딕셔너리 생성 자동화**: 현재 `alphabet` 딕셔너리는 26개의 항목이 모두 하드코딩되어 있어 길고 반복적입니다. 이 구조는 규칙성을 가지므로, 루프를 사용하여 동적으로 생성할 수 있습니다. 이렇게 하면 코드가 훨씬 간결해지고 유지보수가 쉬워집니다.

    ```python
    # 개선 제안 예시
    import string

    def create_porta_tables() -> dict[str, tuple[str, str]]:
        tables = {}
        upper_half = string.ascii_uppercase[:13]
        lower_half = string.ascii_uppercase[13:]
        for i in range(13):
            # 하단 알파벳을 순환시킴
            shifted_lower = lower_half[-(i):] + lower_half[:-(i)]
            table = (upper_half, shifted_lower)
            # 두 개의 키가 하나의 테이블을 공유
            tables[string.ascii_uppercase[i*2]] = table
            tables[string.ascii_uppercase[i*2+1]] = table
        return tables

    alphabet = create_porta_tables()
    ```

2.  **비-알파벳 문자 처리**: 현재 코드는 입력(`words`)에 알파벳 대문자만 있다고 가정합니다. 공백, 숫자, 특수문자가 포함될 경우 `ValueError`가 발생합니다. `get_opponent` 함수에서 알파벳이 아닌 문자는 그대로 반환하도록 수정하면 프로그램의 안정성이 향상됩니다.

3.  **효율성**: `get_position` 함수는 매번 `index()`를 호출하여 문자를 찾습니다. 키워드가 길고 메시지가 매우 길 경우, 각 테이블에 대한 문자-위치 맵을 미리 만들어두면(예: 딕셔너리 사용) 성능을 개선할 수 있습니다. 하지만 현재 구현은 가독성이 좋고 대부분의 경우 충분히 빠릅니다.