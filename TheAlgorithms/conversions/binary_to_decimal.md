# `binary_to_decimal.py` 코드 설명

이 문서는 `binary_to_decimal.py` 파이썬 스크립트에 포함된 `bin_to_decimal` 함수를 설명합니다. 이 스크립트는 2진수 형태의 문자열을 10진수 정수로 변환하는 기능을 구현합니다.

## 목차
1.  2진수에서 10진수로의 변환 원리
2.  함수 설명
    -   `bin_to_decimal(bin_string)`
3.  실행 방법
4.  코드 개선 제안

## 2진수에서 10진수로의 변환 원리

2진수는 각 자리수가 2의 거듭제곱을 나타냅니다. 10진수로 변환하기 위해서는 각 자리의 숫자(0 또는 1)에 해당하는 2의 거듭제곱 값을 곱한 후 모두 더하면 됩니다.

예를 들어, 2진수 `101`은 다음과 같이 계산됩니다.
`(1 * 2²) + (0 * 2¹) + (1 * 2⁰) = 4 + 0 + 1 = 5`

이 스크립트는 이 원리를 반복적인 연산을 통해 구현합니다.

## 함수 설명

### `bin_to_decimal(bin_string: str) -> int`

2진수 문자열을 입력받아 해당하는 10진수 정수를 반환합니다.

-   **알고리즘**:
    1.  **입력 처리**: 입력된 문자열의 양 끝 공백을 제거하고, 음수 부호(`-`)가 있는지 확인합니다.
    2.  **유효성 검사**: 문자열이 비어있거나, '0'과 '1' 이외의 문자를 포함하고 있는지 확인하여 `ValueError`를 발생시킵니다.
    3.  **변환**:
        -   `decimal_number`를 0으로 초기화합니다.
        -   2진수 문자열의 각 문자를 왼쪽부터 순회하면서, `decimal_number = 2 * decimal_number + 현재 숫자` 공식을 반복적으로 적용합니다. 이는 호너의 방법(Horner's method)과 유사한 방식으로, 효율적으로 10진수 값을 계산합니다.
    4.  **결과 반환**: 처음에 음수 부호가 있었다면, 계산된 값에 음수 부호를 붙여 반환합니다.

```python
>>> bin_to_decimal("101")
5
>>> bin_to_decimal("-11101")
-29
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python binary_to_decimal.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **파이썬 내장 함수 사용**: 이 변환은 파이썬의 내장 함수 `int()`를 사용하여 훨씬 간단하게 구현할 수 있습니다. `int(binary_string, 2)`는 2진수 문자열을 10진수 정수로 직접 변환해 줍니다. 교육적인 목적의 구현으로는 훌륭하지만, 실제 코드에서는 내장 함수를 사용하는 것이 더 간결하고 효율적입니다.

    ```python
    # 내장 함수를 사용한 개선 제안 예시
    def bin_to_decimal_fast(bin_string: str) -> int:
        """
        Convert a binary value to its decimal equivalent using Python's built-in int().
        """
        bin_string = str(bin_string).strip()
        if not bin_string:
            raise ValueError("Empty string was passed to the function")
        
        # int()는 음수 부호를 직접 처리하지 못하므로 따로 처리
        is_negative = bin_string.startswith("-")
        if is_negative:
            bin_string = bin_string[1:]

        try:
            decimal_value = int(bin_string, 2)
            return -decimal_value if is_negative else decimal_value
        except ValueError:
            raise ValueError("Non-binary value was passed to the function") from None
    ```

2.  **입력 타입 처리**: `str(bin_string)`을 사용하여 입력을 문자열로 강제 변환하고 있습니다. 이는 유연성을 제공하지만, 함수가 명시적으로 `str` 타입을 기대한다면, 함수 시작 부분에서 `isinstance(bin_string, str)`와 같은 타입 체크를 추가하는 것이 더 명확할 수 있습니다. (현재 `doctest`는 다양한 입력을 가정하고 있으므로 현재 방식도 유효합니다.)