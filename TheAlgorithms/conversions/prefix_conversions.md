# `prefix_conversions.py` 코드 설명

이 문서는 `prefix_conversions.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 **SI 단위 접두사(SI prefix)** 또는 **이진 접두사(Binary prefix)**가 붙은 값을 다른 접두사로 변환하는 기능을 제공합니다.

## 목차
1.  단위 접두사란?
    -   SI 단위 접두사
    -   이진 접두사
2.  클래스 설명
    -   `SI_Unit` (Enum)
    -   `Binary_Unit` (Enum)
3.  함수 설명
    -   `convert_si_prefix(known_amount, known_prefix, unknown_prefix)`
    -   `convert_binary_prefix(known_amount, known_prefix, unknown_prefix)`
4.  실행 방법
5.  코드 개선 제안

## 단위 접두사란?

### SI 단위 접두사

국제단위계(SI)에서 매우 크거나 작은 수를 간결하게 표현하기 위해 사용되는 접두사입니다. 10의 거듭제곱을 기반으로 합니다.
-   **예시**: 1 기가(giga)는 1,000 메가(mega)와 같습니다. (`1 * 10⁹ = 1000 * 10⁶`)

### 이진 접두사

컴퓨터 과학 분야에서 데이터의 양을 표현할 때 주로 사용되며, 2의 거듭제곱을 기반으로 합니다.
-   **예시**: 1 기비(gibi)는 1,024 메비(mebi)와 같습니다. (`1 * 2³⁰ = 1024 * 2²⁰`)

## 클래스 설명

### `SI_Unit(Enum)`

SI 단위 접두사와 그에 해당하는 10의 지수 값을 `Enum`(열거형)으로 정의합니다.
-   **예시**: `SI_Unit.kilo`는 3 (10³), `SI_Unit.mega`는 6 (10⁶).

### `Binary_Unit(Enum)`

이진 접두사와 그에 해당하는 10의 배수 지수 값을 `Enum`으로 정의합니다.
-   **예시**: `Binary_Unit.kilo`는 1 (2¹⁰), `Binary_Unit.mega`는 2 (2²⁰).

## 함수 설명

### `convert_si_prefix(known_amount, known_prefix, unknown_prefix)`

주어진 SI 접두사 값을 다른 SI 접두사 값으로 변환합니다.

-   **알고리즘**:
    1.  입력된 접두사 이름(문자열)을 `SI_Unit` Enum 멤버로 변환합니다.
    2.  `결과 = 입력값 * 10^(입력 접두사 지수 - 목표 접두사 지수)` 공식을 사용하여 값을 계산합니다.

```python
>>> convert_si_prefix(1, "giga", "mega")
1000.0
```

### `convert_binary_prefix(known_amount, known_prefix, unknown_prefix)`

주어진 이진 접두사 값을 다른 이진 접두사 값으로 변환합니다.

-   **알고리즘**:
    1.  입력된 접두사 이름(문자열)을 `Binary_Unit` Enum 멤버로 변환합니다.
    2.  `결과 = 입력값 * 2^((입력 접두사 지수 - 목표 접두사 지수) * 10)` 공식을 사용하여 값을 계산합니다.

```python
>>> convert_binary_prefix(1, "giga", "mega")
1024.0
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python prefix_conversions.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **`prefix_conversions_string.py`와의 관계**: 이 스크립트는 `prefix_conversions_string.py`와 유사한 기능을 하지만, 변환 방향이 다릅니다. (`prefix_conversions_string.py`는 숫자 `10000`을 "10.0 kilo"로 변환). 두 파일의 이름을 더 명확하게 구분하거나(예: `convert_between_prefixes`, `format_with_prefix`), 하나의 파일로 통합하여 양방향 변환을 모두 지원하는 클래스나 함수 세트를 만드는 것을 고려할 수 있습니다.

2.  **사용자 인터페이스 추가**: `if __name__ == "__main__"` 블록에 `argparse` 모듈을 사용하여 사용자가 커맨드 라인에서 직접 값과 접두사를 입력하여 변환을 수행할 수 있는 인터페이스를 제공하면 스크립트의 활용도가 높아집니다.

3.  **입력 유효성 검사**: `isinstance(known_prefix, str)`와 같은 검사는 잘 되어 있지만, 만약 Enum에 존재하지 않는 문자열이 입력될 경우 `KeyError`가 발생합니다. `try-except` 블록을 사용하여 더 친절한 오류 메시지를 제공할 수 있습니다.

    ```python
    # 개선 제안 예시
    try:
        if isinstance(known_prefix, str):
            known_prefix = SI_Unit[known_prefix.lower()]
    except KeyError:
        raise ValueError(f"Invalid prefix: {known_prefix}") from None
    ```