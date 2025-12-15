# `decimal_to_any.py` 코드 설명

이 문서는 `decimal_to_any.py` 파이썬 스크립트에 포함된 `decimal_to_any` 함수를 설명합니다. 이 스크립트는 10진수 양의 정수를 2진법부터 36진법까지의 다른 진법으로 변환하는 기능을 구현합니다.

## 목차
1.  10진수에서 다른 진법으로의 변환 원리
2.  함수 설명
    -   `decimal_to_any(num, base)`
3.  실행 방법
4.  코드 개선 제안

## 10진수에서 다른 진법으로의 변환 원리

10진수를 다른 진법(base)으로 변환하는 일반적인 방법은 **나눗셈과 나머지 연산**을 반복하는 것입니다.

1.  10진수를 변환하려는 진법의 수(`base`)로 나눕니다.
2.  이때 발생하는 **나머지**가 새로운 진법의 가장 낮은 자리 숫자가 됩니다.
3.  **몫**을 다시 `base`로 나누고, 나머지를 다음 자리 숫자로 사용합니다.
4.  몫이 0이 될 때까지 이 과정을 반복합니다.
5.  얻어진 나머지들을 역순으로 이어 붙이면 최종 변환 결과가 됩니다.

10 이상의 나머지 값은 알파벳(A=10, B=11, ...)으로 표현합니다.

## 함수 설명

### `decimal_to_any(num: int, base: int) -> str`

양의 10진수 정수를 지정된 `base`의 문자열 표현으로 변환합니다.

-   **인자**:
    -   `num`: 변환할 양의 10진수 정수.
    -   `base`: 변환할 진법 (2 이상 36 이하).

-   **알고리즘**:
    1.  **유효성 검사**: `num`과 `base`가 유효한 타입과 범위 내에 있는지 확인하고, 그렇지 않으면 `TypeError`나 `ValueError`를 발생시킵니다.
    2.  **변환**:
        -   `while` 루프를 사용하여 `num`을 `base`로 계속 나누면서 몫과 나머지를 구합니다.
        -   나머지가 10 이상이면, `ALPHABET_VALUES` 딕셔너리를 참조하여 해당하는 알파벳 문자로 변환합니다.
        -   계산된 나머지(또는 문자)를 결과 문자열(`new_value`)의 앞에 계속 추가합니다.
    3.  **결과 반환**: 최종적으로 만들어진 문자열을 반환합니다.

> **주의**: 현재 함수의 `while` 루프 조건(`while div != 1`)과 내부 로직은 다소 복잡하고, 일부 경우(예: `num=0`)에 대해 올바르게 동작하지 않을 수 있습니다. (개선 제안 참조)

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수의 예제 코드가 실행되고, `if __name__ == "__main__"` 블록의 `assert` 문을 통해 0부터 999까지의 숫자에 대한 변환 정확성이 자동으로 테스트됩니다.

```bash
python decimal_to_any.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **알고리즘 로직 단순화**: 현재 `while` 루프의 조건과 내부 분기문은 매우 복잡하고 직관적이지 않습니다. "몫이 0이 될 때까지 반복"하는 표준 알고리즘으로 재작성하면 코드가 훨씬 간결하고 정확해집니다.

2.  **`ALPHABET_VALUES` 딕셔너리 개선**: 현재 딕셔너리는 키가 문자열(`'10'`)로 되어 있어 `str()` 변환이 필요합니다. 또한, 0-9까지의 숫자도 포함하는 하나의 문자열이나 리스트를 만들어 인덱싱하는 것이 더 효율적입니다.

**리팩토링된 코드 예시:**

```python
def decimal_to_any_simple(num: int, base: int) -> str:
    """
    A simpler and more correct implementation to convert a positive integer
    to another base as a string.
    """
    # 유효성 검사 (기존 코드와 유사)
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("Input number must be an integer.")
    if num < 0:
        raise ValueError("Input number must be a positive integer.")
    if not isinstance(base, int) or isinstance(base, bool):
        raise TypeError("Base must be an integer.")
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36.")

    if num == 0:
        return "0"

    # 0-9, A-Z 까지의 문자를 포함하는 문자열
    ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    while num > 0:
        num, remainder = divmod(num, base)
        result += ALPHABET[remainder]

    # 나머지를 역순으로 이어 붙여야 하므로 최종 결과를 뒤집음
    return result[::-1]
```

3.  **입력 유효성 검사 개선**: `isinstance(num, float)` 검사는 `int()` 변환 시 `TypeError`가 발생하므로 중복될 수 있습니다. 또한, `bool` 타입은 `int`의 하위 클래스이므로 `isinstance(num, bool)` 체크를 추가하여 `True`/`False`가 `1`/`0`으로 처리되는 것을 막는 것이 더 안전합니다.

4.  **`main` 블록의 테스트**: `assert` 문을 사용하여 자동화된 테스트를 포함한 것은 매우 좋은 방법입니다. 이는 코드 변경 시 회귀(regression)를 방지하는 데 큰 도움이 됩니다.

