# `baconian_cipher.py` 코드 설명

이 문서는 `baconian_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 프랜시스 베이컨이 고안한 **베이컨 암호(Bacon's Cipher)**를 구현합니다.

## 목차
1.  베이컨 암호란?
2.  주요 데이터 구조
3.  함수 설명
    -   `encode(word)`
    -   `decode(coded)`
4.  실행 방법
5.  코드 개선 제안

## 베이컨 암호란?

베이컨 암호는 각 문자를 'A'와 'B' 두 종류의 문자로 이루어진 5글자 시퀀스로 치환하는 암호화 방식입니다. 이는 일종의 스테가노그래피(steganography, 데이터를 다른 데이터에 숨기는 기술)로, 두 가지 다른 서체나 표현 방식을 사용해 메시지를 숨기는 데 사용될 수 있습니다.

이 스크립트에서는 알파벳 'a'부터 'z'까지 각 문자에 고유한 5글자 'A'/'B' 코드를 할당하여 암호화를 수행합니다.

## 주요 데이터 구조

### `encode_dict`

알파벳 소문자와 공백을 키(key)로, 해당하는 5글자 베이컨 코드(또는 공백)를 값(value)으로 갖는 딕셔너리입니다. 암호화 과정에서 문자를 코드로 변환하기 위한 조회 테이블로 사용됩니다.

```python
{
    "a": "AAAAA",
    "b": "AAAAB",
    ...
    "z": "BABBB",
    " ": " ",
}
```

### `decode_dict`

`encode_dict`의 키와 값을 뒤집어 생성한 딕셔너리입니다. 5글자 베이컨 코드를 키로, 해당하는 문자를 값으로 갖습니다. 복호화 과정에서 코드를 다시 문자로 변환하는 데 사용됩니다.

## 함수 설명

### `encode(word: str) -> str`

주어진 문자열을 베이컨 암호로 **인코딩(암호화)**합니다.

-   **알고리즘**:
    1.  입력된 문자열(`word`)을 모두 소문자로 변환합니다.
    2.  문자열의 각 문자를 순회하면서, 해당 문자가 알파벳이거나 공백인지 확인합니다.
    3.  `encode_dict`를 사용하여 문자에 해당하는 5글자 코드를 찾아 결과 문자열에 추가합니다.
    4.  만약 알파벳이나 공백이 아닌 문자가 발견되면, `Exception`을 발생시켜 프로그램을 중단시킵니다.

```python
>>> encode("hello")
'AABBBAABAAABABAABABAABBAB'
```

### `decode(coded: str) -> str`

베이컨 암호로 암호화된 문자열을 원래의 평문으로 **디코딩(복호화)**합니다.

-   **알고리즘**:
    1.  입력된 암호문(`coded`)이 'A', 'B', 공백으로만 구성되어 있는지 확인합니다. 다른 문자가 있으면 `Exception`을 발생시킵니다.
    2.  암호문을 공백 기준으로 단어별로 나눕니다.
    3.  각 단어에 대해, 5글자씩 잘라 `decode_dict`에서 해당하는 문자를 찾아냅니다.
    4.  복원된 문자들을 조합하여 원래의 단어를 만들고, 단어 사이에 공백을 추가하여 전체 문장을 복원합니다.

```python
>>> decode("AABBBAABAAABABAABABAABBAB")
'hello'
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python baconian_cipher.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **오류 처리 방식 개선**: 현재 코드에서는 `raise Exception(...)`을 사용하여 일반적인 예외를 발생시킵니다. `ValueError`와 같이 더 구체적인 예외 타입을 사용하면, 이 코드를 다른 모듈에서 사용할 때 오류를 더 정교하게 처리할 수 있습니다.

    ```python
    # 개선 제안 예시
    def encode(word: str) -> str:
        # ...
        if not (letter.isalpha() or letter == " "):
            raise ValueError("Input contains non-alphabetic characters or symbols.")
        # ...
    ```

2.  **`decode` 함수 로직 단순화**: `decode` 함수의 단어 처리 로직은 `while` 루프 대신 리스트 컴프리헨션과 `join`을 사용하여 더 간결하고 파이썬답게 작성할 수 있습니다.

    ```python
    # 개선 제안 예시
    def decode(coded: str) -> str:
        if set(coded) - {"A", "B", " "}:
            raise ValueError("Input contains characters other than 'A', 'B', or space.")
        
        decoded_words = []
        for word in coded.split(' '):
            # 5글자씩 쪼개서 리스트로 만듦
            chunks = [word[i:i+5] for i in range(0, len(word), 5)]
            # 각 chunk를 디코딩하고 합침
            decoded_words.append("".join(decode_dict[chunk] for chunk in chunks))
            
        return " ".join(decoded_words)
    ```

3.  **대소문자 구분 없는 디코딩**: 현재 `decode` 함수는 'A'와 'B'만 허용합니다. `coded.upper()`를 사용하여 입력을 대문자로 통일하면, 사용자가 'a'나 'b'를 입력해도 정상적으로 처리할 수 있어 유연성이 높아집니다.
