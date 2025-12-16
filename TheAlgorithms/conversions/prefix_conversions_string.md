# `prefix_conversions_string.py` 코드 설명

이 문서는 `prefix_conversions_string.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 주어진 숫자를 사람이 읽기 쉬운 형태, 즉 가장 적절한 **SI 단위 접두사(SI prefix)** 또는 **이진 접두사(Binary prefix)**를 붙인 문자열로 변환하는 기능을 제공합니다.

## 목차
1.  단위 접두사란?
    -   SI 단위 접두사
    -   이진 접두사
2.  클래스 설명
    -   `BinaryUnit` (Enum)
    -   `SIUnit` (Enum)
3.  함수 설명
    -   `add_si_prefix(value)`
    -   `add_binary_prefix(value)`
4.  실행 방법
5.  코드 개선 제안

## 단위 접두사란?

### SI 단위 접두사

국제단위계(SI)에서 매우 크거나 작은 수를 간결하게 표현하기 위해 사용되는 접두사입니다. 10의 거듭제곱을 기반으로 합니다.
-   **예시**: 1,000 미터는 `1 kilo`미터, 1,000,000,000 바이트는 `1 giga`바이트.

### 이진 접두사

컴퓨터 과학 분야에서 데이터의 양을 표현할 때 주로 사용되며, 2의 거듭제곱을 기반으로 합니다.
-   **예시**: 1,024 바이트는 `1 kilo`바이트(정확히는 1 kibibyte), 1,048,576 바이트는 `1 mega`바이트(정확히는 1 mebibyte).

## 클래스 설명

### `BinaryUnit(Enum)`

이진 접두사와 그에 해당하는 2의 지수 값을 `Enum`(열거형)으로 정의합니다.
-   **예시**: `BinaryUnit.kilo`는 10 (2¹⁰), `BinaryUnit.mega`는 20 (2²⁰).

### `SIUnit(Enum)`

SI 단위 접두사와 그에 해당하는 10의 지수 값을 `Enum`으로 정의합니다.
-   **예시**: `SIUnit.kilo`는 3 (10³), `SIUnit.mega`는 6 (10⁶), `SIUnit.milli`는 -3 (10⁻³).
-   **`get_positive()` / `get_negative()`**: 양수 또는 음수 지수를 갖는 접두사만 필터링하여 딕셔너리로 반환하는 클래스 메서드를 포함합니다.

## 함수 설명

### `add_si_prefix(value: float) -> str`

주어진 숫자를 가장 적절한 SI 단위 접두사를 붙인 문자열로 변환합니다.

-   **알고리즘**:
    1.  가장 큰 접두사(yotta)부터 시작하여 순서대로 순회합니다.
    2.  입력된 `value`를 현재 접두사의 값(10의 거듭제곱)으로 나눕니다.
    3.  나눈 결과(`numerical_part`)가 1보다 크면, 해당 접두사가 가장 적절한 단위라고 판단하고, `"{결과값} {접두사 이름}"` 형태의 문자열을 반환합니다.
    4.  모든 접두사로 나누어도 결과가 1보다 작으면, 원래 숫자를 그대로 문자열로 반환합니다.

```python
>>> add_si_prefix(10000)
'10.0 kilo'
```

### `add_binary_prefix(value: float) -> str`

주어진 숫자를 가장 적절한 이진 접두사를 붙인 문자열로 변환합니다.

-   **알고리즘**: `add_si_prefix`와 유사하지만, 10의 거듭제곱 대신 2의 거듭제곱(`2**prefix.value`)을 사용하여 나눗셈을 수행합니다.

```python
>>> add_binary_prefix(65536)
'64.0 kilo'
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수와 클래스 메서드에 포함된 예제 코드가 실행되고, 정확성이 자동으로 테스트됩니다.

```bash
python prefix_conversions_string.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **`add_si_prefix`의 로직**: 현재 `add_si_prefix` 함수는 입력값이 양수이면 양수 접두사만, 음수이면 음수 접두사만 고려합니다. 하지만 `0.001`과 같은 양수 값은 음수 접두사(`milli`)를 사용해야 합니다. `abs(value)`를 기준으로 접두사 그룹을 선택하고, `value` 자체를 계산에 사용하도록 수정해야 합니다.

    ```python
    # 개선 제안 예시
    def add_si_prefix(value: float) -> str:
        if abs(value) >= 1:
            prefixes = SIUnit.get_positive()
        else:
            # 음수 접두사는 작은 값부터 큰 값 순으로 정렬해야 올바르게 동작
            prefixes = dict(sorted(SIUnit.get_negative().items(), key=lambda item: item[1]))
        
        for name_prefix, value_prefix in prefixes.items():
            numerical_part = value / (10**value_prefix)
            if abs(numerical_part) >= 1:
                return f"{str(numerical_part)} {name_prefix}"
        return str(value)
    ```

2.  **`prefix_conversions.py`와의 관계**: 이 스크립트는 `prefix_conversions.py`와 유사한 기능을 하지만, 변환 방향이 다릅니다. (`prefix_conversions.py`는 "1 giga"를 "1000 mega"로 변환). 두 파일의 이름을 더 명확하게 구분하거나(예: `convert_from_prefix`, `convert_to_prefix`), 하나의 파일로 통합하여 양방향 변환을 모두 지원하는 클래스나 함수 세트를 만드는 것을 고려할 수 있습니다.

3.  **출력 포맷**: `f"{str(numerical_part)} {name_prefix}"` 부분에서 `str()`을 사용하고 있습니다. `f-string`은 내부적으로 `str()`을 호출하므로 중복입니다. 또한, 소수점 자릿수를 제어하는 포맷팅(예: `f"{numerical_part:.2f}"`)을 추가하면 더 깔끔한 출력을 만들 수 있습니다.