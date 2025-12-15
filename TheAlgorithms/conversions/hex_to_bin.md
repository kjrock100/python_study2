# `hex_to_bin.py` 코드 설명

이 문서는 `hex_to_bin.py` 파이썬 스크립트에 포함된 `hex_to_bin` 함수를 설명합니다. 이 스크립트는 16진수 형태의 문자열을 2진수 정수로 변환하는 기능을 구현합니다.

## 목차
1.  16진수에서 2진수로의 변환 원리
2.  함수 설명
    -   `hex_to_bin(hex_num)`
3.  실행 방법
4.  코드 개선 제안

## 16진수에서 2진수로의 변환 원리

16진수를 2진수로 변환하는 가장 간단한 방법은 각 16진수 자리를 4자리의 2진수로 변환하여 이어 붙이는 것입니다.

하지만 이 스크립트는 다른 접근 방식을 사용합니다.
1.  **16진수 -> 10진수**: 먼저 16진수 문자열을 10진수 정수로 변환합니다.
2.  **10진수 -> 2진수**: 변환된 10진수 정수를 다시 2진수로 변환합니다.

## 함수 설명

### `hex_to_bin(hex_num: str) -> int`

16진수 문자열을 입력받아 해당하는 2진수 값을 정수 형태로 반환합니다.

-   **알고리즘**:
    1.  **입력 처리**: 입력된 문자열의 양 끝 공백을 제거하고, 음수 부호(`-`)가 있는지 확인합니다.
    2.  **16진수 -> 10진수 변환**:
        -   `try-except` 블록을 사용하여 `int(hex_num, 16)`을 호출합니다. 이는 16진수 문자열을 10진수 정수로 변환합니다.
        -   유효하지 않은 16진수 문자열이 입력되면 `ValueError`를 발생시킵니다.
    3.  **10진수 -> 2진수 변환**:
        -   `while` 루프를 사용하여 10진수 값을 2로 계속 나누면서 나머지를 구합니다.
        -   나머지를 결과 문자열(`bin_str`)의 앞에 계속 추가하여 2진수 문자열을 만듭니다.
    4.  **결과 반환**: 최종적으로 만들어진 2진수 문자열을 다시 정수로 변환하여 반환합니다. 음수였을 경우, 음수 부호를 붙여 반환합니다.

```python
>>> hex_to_bin("AC")
10101100
>>> hex_to_bin("-fFfF")
-1111111111111111
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python hex_to_bin.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **파이썬 내장 함수 사용**: 이 변환은 파이썬의 내장 함수를 조합하여 훨씬 간단하게 구현할 수 있습니다. `int(hex_num, 16)`으로 10진수로 변환한 다음, `bin()` 함수를 사용하여 2진수 문자열로 변환하는 방식입니다.

    ```python
    # 내장 함수를 사용한 개선 제안 예시
    def hex_to_bin_fast(hex_num: str) -> str:
        """
        Convert a hexadecimal string to its binary string representation using built-ins.
        """
        hex_num = hex_num.strip()
        if not hex_num:
            raise ValueError("No value was passed to the function")

        is_negative = hex_num.startswith("-")
        if is_negative:
            hex_num = hex_num[1:]

        try:
            decimal_value = int(hex_num, 16)
            binary_value = bin(decimal_value) # "0b..." 형태의 문자열 반환
            return f"-{binary_value}" if is_negative else binary_value
        except ValueError:
            raise ValueError("Invalid value was passed to the function") from None
    ```

2.  **반환 타입**: 현재 함수는 2진수 값을 `int` 타입으로 반환합니다. 이는 `0b101`과 같은 2진수 표현이 아니라, 10진수 `101`을 의미하므로 혼동을 줄 수 있습니다. 2진수 표현은 일반적으로 문자열(`str`)로 다루므로, `bin()` 함수처럼 "0b" 접두사가 붙은 문자열을 반환하는 것이 더 명확하고 표준적입니다.

3.  **효율적인 문자열 처리**: `bin_str = str(int_num % 2) + bin_str`와 같이 루프 안에서 문자열을 앞에 더하는 것은 성능에 비효율적입니다. 문자 조각들을 리스트에 추가한 후, `"".join(reversed(my_list))`와 같이 처리하는 것이 더 좋습니다.