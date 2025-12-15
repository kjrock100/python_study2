# `decimal_to_binary_recursion.py` 코드 설명

이 문서는 `decimal_to_binary_recursion.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 10진수 정수를 2진수 문자열로 변환하는 과정을 **재귀(recursion)**를 사용하여 구현합니다.

## 목차
1.  재귀를 이용한 10진수에서 2진수로의 변환 원리
2.  함수 설명
    -   `binary_recursive(decimal)`
    -   `main(number)`
3.  실행 방법
4.  코드 개선 제안

## 재귀를 이용한 10진수에서 2진수로의 변환 원리

10진수를 2진수로 변환하는 재귀적 방법은 다음과 같은 원리를 따릅니다.

1.  **종료 조건(Base Case)**: 변환할 숫자가 0 또는 1이면, 그 숫자 자체가 2진수 표현이므로 반환합니다.
2.  **재귀 단계(Recursive Step)**:
    -   숫자를 2로 나눈 **몫**에 대해 재귀적으로 함수를 다시 호출합니다.
    -   숫자를 2로 나눈 **나머지**를 구합니다.
    -   재귀 호출의 결과 뒤에 나머지를 문자열로 이어 붙입니다.

**예시 (10을 2진수로 변환):**
-   `binary_recursive(10)` -> `binary_recursive(5)` + "0"
-   `binary_recursive(5)` -> `binary_recursive(2)` + "1"
-   `binary_recursive(2)` -> `binary_recursive(1)` + "0"
-   `binary_recursive(1)` -> "1" (종료 조건)
-   결과: "1" + "0" + "1" + "0" -> "1010"

## 함수 설명

### `binary_recursive(decimal: int) -> str`

양의 10진수 정수를 2진수 문자열로 변환하는 재귀 함수입니다.

-   **알고리즘**:
    1.  입력값을 `int()`를 사용하여 정수로 변환합니다.
    2.  입력된 정수가 0 또는 1이면, 해당 숫자를 문자열로 반환하여 재귀를 종료합니다.
    3.  `divmod(decimal, 2)`를 사용하여 몫(`div`)과 나머지(`mod`)를 구합니다.
    4.  몫(`div`)에 대해 `binary_recursive`를 다시 호출하고, 그 결과 뒤에 나머지(`mod`)를 문자열로 이어 붙여 반환합니다.

### `main(number: str) -> str`

사용자 입력을 처리하고, `binary_recursive` 함수를 호출하여 최종적인 2진수 표현(접두사 포함)을 만드는 래퍼(wrapper) 함수입니다.

-   **동작**:
    1.  입력값의 유효성을 검사합니다. (빈 문자열, 숫자가 아닌 값 등)
    2.  음수 부호(`-`)가 있는지 확인하고 처리합니다.
    3.  `binary_recursive`를 호출하여 핵심 변환을 수행합니다.
    4.  결과에 "0b" 또는 "-0b" 접두사를 붙여 표준적인 2진수 표현 문자열을 만들어 반환합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python decimal_to_binary_recursion.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **파이썬 내장 함수 사용**: 이 변환은 파이썬의 내장 함수 `bin()`을 사용하여 훨씬 간단하게 구현할 수 있습니다. `bin(number)`는 정수를 "0b" 접두사가 붙은 2진수 문자열로 직접 변환해 줍니다. 교육적인 목적의 재귀 구현으로는 훌륭하지만, 실제 코드에서는 내장 함수를 사용하는 것이 더 간결하고 효율적입니다.

    ```python
    # 내장 함수를 사용한 개선 제안 예시
    def decimal_to_binary_fast(number: int) -> str:
        """
        Convert an integer to its binary representation using Python's built-in bin().
        """
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        return bin(number)
    ```

2.  **`main` 함수의 입력 처리**: `main` 함수는 `str(number).strip()`을 사용하여 입력을 문자열로 강제 변환하고 있습니다. 이는 유연성을 제공하지만, 함수가 명시적으로 `int`나 `str` 타입을 기대한다면, 함수 시그니처를 `main(number: int | str)`와 같이 더 명확하게 하고 내부에서 타입을 확인하는 것이 좋습니다.

3.  **`binary_recursive`의 입력 처리**: `binary_recursive` 함수 내부에서 `int(decimal)`을 호출하고 있습니다. 재귀 함수의 경우, 내부 호출 시에는 항상 올바른 타입(정수)이 전달되므로, 이 변환은 초기 호출 시에만 필요합니다. `main` 함수에서 이미 정수로 변환하므로, `binary_recursive`에서는 이 변환을 생략하여 재귀 호출의 오버헤드를 약간 줄일 수 있습니다.