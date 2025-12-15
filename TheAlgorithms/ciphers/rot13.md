# `rot13.py` 코드 설명

이 문서는 `rot13.py` 파이썬 스크립트에 포함된 `dencrypt` 함수를 설명합니다. 이 스크립트는 카이사르 암호(Caesar Cipher)의 특별한 경우인 **ROT13 암호**를 구현합니다.

## 목차
1.  ROT13 암호란?
2.  함수 설명
    -   `dencrypt(s, n)`
3.  실행 방법
4.  코드 개선 제안

## ROT13 암호란?

ROT13("rotate by 13 places")은 각 문자를 알파벳 상에서 13자리 뒤의 문자로 치환하는 간단한 치환 암호입니다. 이는 키가 13으로 고정된 카이사르 암호와 같습니다.

ROT13의 가장 큰 특징은 **상호적(reciprocal)**이라는 점입니다. 영어 알파벳은 26자이므로, ROT13을 두 번 적용하면 원래의 텍스트로 돌아옵니다. 이 때문에 암호화(encryption)와 복호화(decryption)에 동일한 함수를 사용할 수 있습니다.

이 암호는 보안 목적이 아니라, 스포일러나 농담, 퍼즐의 정답 등을 간단히 숨기는 용도로 주로 사용됩니다.

## 함수 설명

### `dencrypt(s: str, n: int = 13) -> str`

주어진 문자열을 지정된 `n`만큼 회전시켜 암호화 또는 복호화합니다. 함수 이름은 "decrypt"와 "encrypt"의 합성어입니다.

-   **인자**:
    -   `s`: 변환할 문자열.
    -   `n` (선택): 회전시킬 자리 수. 기본값은 `13`으로, ROT13을 수행합니다.

-   **알고리즘**:
    1.  입력 문자열(`s`)의 각 문자를 순회합니다.
    2.  문자가 대문자 알파벳이면, 해당 문자의 순서에 `n`을 더하고 26으로 나눈 나머지를 구해 새로운 문자를 찾습니다.
    3.  문자가 소문자 알파벳이면, 위와 동일한 과정을 소문자 알파벳 내에서 수행합니다.
    4.  문자가 알파벳이 아니면(공백, 숫자, 기호 등), 그대로 결과 문자열에 추가합니다.
    5.  변환된 모든 문자를 합쳐 최종 문자열을 반환합니다.

```python
>>> dencrypt("My secret bank account number is 173-52946 so don't tell anyone!!")
"Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!"

>>> dencrypt("Zl frperg onax nppbhag ahzore vf 173-52946 fb qba'g gryy nalbar!!")
"My secret bank account number is 173-52946 so don't tell anyone!!"
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수의 정확성을 테스트한 후, 사용자로부터 메시지를 입력받아 ROT13 변환을 시연합니다.

```bash
python rot13.py
```

**실행 예시:**
```
Enter message: Hello World
Encryption: Uryyb Jbeyq
Decryption:  Hello World
```

## 코드 개선 제안

1.  **함수 이름 명확화**: `dencrypt`라는 이름은 독창적이지만, `rotate`나 `rot13`과 같이 더 표준적이고 명확한 이름으로 변경하면 코드의 의도를 파악하기 쉬워집니다.

2.  **코드 중복 제거**: 대문자와 소문자를 처리하는 로직이 거의 동일하게 반복됩니다. 이 부분을 하나의 로직으로 통합하여 코드 중복을 줄일 수 있습니다.

    ```python
    # 개선 제안 예시
    def rotate(text: str, shift: int = 13) -> str:
        rotated_chars = []
        for char in text:
            if 'a' <= char <= 'z':
                start = ord('a')
                rotated_char = chr(start + (ord(char) - start + shift) % 26)
            elif 'A' <= char <= 'Z':
                start = ord('A')
                rotated_char = chr(start + (ord(char) - start + shift) % 26)
            else:
                rotated_char = char
            rotated_chars.append(rotated_char)
        return "".join(rotated_chars)
    ```

3.  **`string.maketrans` 활용**: 더 파이썬다운(Pythonic) 방식으로, `string.maketrans`와 `str.translate`를 사용하면 루프 없이 매우 간결하고 효율적으로 ROT13 변환을 구현할 수 있습니다.

    ```python
    # maketrans를 사용한 개선 제안 예시
    import string

    def rot13_fast(text: str) -> str:
        rot13_map = str.maketrans(
            string.ascii_lowercase + string.ascii_uppercase,
            string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
            string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
        )
        return text.translate(rot13_map)
    ```