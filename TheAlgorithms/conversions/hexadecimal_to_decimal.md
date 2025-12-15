# `hexadecimal_to_decimal.py` 코드 설명

이 문서는 `hexadecimal_to_decimal.py` 파이썬 스크립트에 포함된 `hex_to_decimal` 함수를 설명합니다. 이 스크립트는 16진수 형태의 문자열을 10진수 정수로 변환하는 기능을 구현합니다.

## 목차
1.  16진수에서 10진수로의 변환 원리
2.  함수 설명
    -   `hex_to_decimal(hex_string)`
3.  실행 방법
4.  코드 개선 제안

## 16진수에서 10진수로의 변환 원리

16진수는 각 자리수가 16의 거듭제곱을 나타냅니다. 10진수로 변환하기 위해서는 각 자리의 숫자(0-9, A-F)에 해당하는 16의 거듭제곱 값을 곱한 후 모두 더하면 됩니다.

예를 들어, 16진수 `1A`는 다음과 같이 계산됩니다.
`(1 * 16¹) + (10 * 16⁰) = 16 + 10 = 26`

이 스크립트는 이 원리를 반복적인 연산을 통해 구현합니다.

## 함수 설명

### `hex_to_decimal(hex_string: str) -> int`

16진수 문자열을 입력받아 해당하는 10진수 정수를 반환합니다.

-   **알고리즘**:
    1.  **입력 처리**: 입력된 문자열의 양 끝 공백을 제거하고 모두 소문자로 변환합니다. 음수 부호(`-`)가 있는지 확인합니다.
    2.  **유효성 검사**: 문자열이 비어있거나, 16진수 문자(0-9, a-f) 이외의 문자를 포함하고 있는지 확인하여 `ValueError`를 발생시킵니다.
    3.  **변환**:
        -   `decimal_number`를 0으로 초기화합니다.
        -   16진수 문자열의 각 문자를 왼쪽부터 순회하면서, `decimal_number = 16 * decimal_number + 현재 문자의 10진수 값` 공식을 반복적으로 적용합니다. 이는 호너의 방법(Horner's method)과 유사한 방식으로, 효율적으로 10진수 값을 계산합니다.
    4.  **결과 반환**: 처음에 음수 부호가 있었다면, 계산된 값에 음수 부호를 붙여 반환합니다.

```python
>>> hex_to_decimal("a")
10
>>> hex_to_decimal("-Ff")
-255
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python hexadecimal_to_decimal.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **파이썬 내장 함수 사용**: 이 변환은 파이썬의 내장 함수 `int()`를 사용하여 훨씬 간단하게 구현할 수 있습니다. `int(hex_string, 16)`은 16진수 문자열을 10진수 정수로 직접 변환해 줍니다. 교육적인 목적의 구현으로는 훌륭하지만, 실제 코드에서는 내장 함수를 사용하는 것이 더 간결하고 효율적입니다.

    ```python
    # 내장 함수를 사용한 개선 제안 예시
    def hex_to_decimal_fast(hex_string: str) -> int:
        """
        Convert a hexadecimal string to its decimal equivalent using Python's built-in int().
        """
        hex_string = hex_string.strip()
        if not hex_string:
            raise ValueError("Empty string was passed to the function")

        try:
            return int(hex_string, 16)
        except ValueError:
            raise ValueError("Non-hexadecimal value was passed to the function") from None
    ```

2.  **`hex_table` 생성**: `hex_table` 딕셔너리를 리스트 컴프리헨션으로 생성하는 것은 간결하고 좋은 방법입니다. `string.hexdigits`를 사용하여 더 간단하게 만들 수도 있습니다.

    ```python
    # string 모듈을 사용한 hex_table 생성 예시
    import string
    hex_table = {char: i for i, char in enumerate(string.hexdigits[:16])}
    ```

3.  **입력 타입 처리**: `str(hex_string)`을 사용하여 입력을 문자열로 강제 변환하는 대신, 함수 시그니처에 `str` 타입 힌트가 있으므로, 함수 시작 부분에서 `isinstance(hex_string, str)`와 같은 타입 체크를 추가하여 명시적으로 문자열만 처리하도록 할 수 있습니다.