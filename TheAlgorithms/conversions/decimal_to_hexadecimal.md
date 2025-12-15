# `decimal_to_hexadecimal.py` 코드 설명

이 문서는 `decimal_to_hexadecimal.py` 파이썬 스크립트에 포함된 `decimal_to_hexadecimal` 함수를 설명합니다. 이 스크립트는 10진수 정수를 16진수 문자열 표현으로 변환하는 기능을 구현합니다.

## 목차
1.  10진수에서 16진수로의 변환 원리
2.  함수 설명
    -   `decimal_to_hexadecimal(decimal)`
3.  실행 방법
4.  코드 개선 제안

## 10진수에서 16진수로의 변환 원리

10진수를 16진수로 변환하는 일반적인 방법은 **나눗셈과 나머지 연산**을 반복하는 것입니다.

1.  10진수를 16으로 나눕니다.
2.  이때 발생하는 **나머지**(0~15)가 16진수의 가장 낮은 자리 숫자가 됩니다. (10~15는 A~F로 표현)
3.  **몫**을 다시 16으로 나누고, 나머지를 다음 자리 숫자로 사용합니다.
4.  몫이 0이 될 때까지 이 과정을 반복합니다.
5.  얻어진 나머지들을 역순으로 이어 붙이면 최종 변환 결과가 됩니다.

**예시 (37을 16진수로 변환):**
-   37 / 16 = 몫 2, 나머지 5
-   2 / 16 = 몫 0, 나머지 2
-   나머지를 역순으로 결합: `25` -> `0x25`

## 함수 설명

### `decimal_to_hexadecimal(decimal: float) -> str`

10진수 정수(또는 정수형 float)를 입력받아 해당하는 16진수 문자열을 반환합니다.

-   **알고리즘**:
    1.  **유효성 검사**: `assert` 문을 사용하여 입력값이 정수 또는 정수와 동일한 `float`인지 확인합니다.
    2.  **음수 처리**: 입력값이 음수이면, `negative` 플래그를 `True`로 설정하고 값을 양수로 바꿉니다.
    3.  **변환**:
        -   `while` 루프를 사용하여 `decimal`이 0보다 클 동안 반복합니다.
        -   `divmod(decimal, 16)`을 사용하여 몫과 나머지(`remainder`)를 구합니다.
        -   미리 정의된 `values` 딕셔너리를 사용하여 나머지에 해당하는 16진수 문자(0-9, a-f)를 찾습니다.
        -   찾은 문자를 결과 문자열(`hexadecimal`)의 맨 앞에 추가합니다. (나머지를 역순으로 결합하는 효과)
    4.  **결과 반환**: 변환된 문자열에 "0x" 또는 "-0x" 접두사를 붙여 최종 16진수 표현 문자열을 만들어 반환합니다.

```python
>>> decimal_to_hexadecimal(37)
'0x25'
>>> decimal_to_hexadecimal(-256)
'-0x100'
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python decimal_to_hexadecimal.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **파이썬 내장 함수 사용**: 이 변환은 파이썬의 내장 함수 `hex()`를 사용하여 훨씬 간단하게 구현할 수 있습니다. `hex(number)`는 정수를 "0x" 접두사가 붙은 16진수 문자열로 직접 변환해 줍니다. 교육적인 목적의 구현으로는 훌륭하지만, 실제 코드에서는 내장 함수를 사용하는 것이 더 간결하고 효율적입니다.

    ```python
    # 내장 함수를 사용한 개선 제안 예시
    def decimal_to_hex_fast(decimal: int) -> str:
        """
        Convert an integer to its hexadecimal representation using Python's built-in hex().
        """
        if not isinstance(decimal, int):
            # float도 허용하려면 int(decimal) == decimal 체크 추가
            raise TypeError("Input must be an integer.")
        return hex(decimal)
    ```

2.  **입력 유효성 검사 방식**: `assert` 문은 주로 디버깅 목적으로 사용되며, `-O` 옵션으로 파이썬을 실행하면 비활성화될 수 있습니다. 사용자 입력과 같이 예측 불가능한 데이터를 처리할 때는 `if` 문과 `raise TypeError` 또는 `raise ValueError`를 사용하는 것이 더 안정적입니다.

3.  **`values` 딕셔너리**: `values` 딕셔너리는 잘 동작하지만, `string.hexdigits`나 `"0123456789abcdef"`와 같은 문자열을 사용하여 인덱싱하는 것도 간결한 대안이 될 수 있습니다.

    ```python
    # 문자열 인덱싱을 사용한 개선 제안 예시
    HEX_CHARS = "0123456789abcdef"
    # ...
    hexadecimal = HEX_CHARS[remainder] + hexadecimal
    ```