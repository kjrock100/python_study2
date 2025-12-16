# `temperature_conversions.py` 코드 설명

이 문서는 `temperature_conversions.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 섭씨(Celsius), 화씨(Fahrenheit), 켈빈(Kelvin), 란씨(Rankine), 열씨(Réaumur) 등 다양한 온도 단위를 서로 변환하는 함수들을 제공합니다.

## 목차
1.  온도 단위 변환 원리
2.  함수 설명
    -   `celsius_to_*`
    -   `fahrenheit_to_*`
    -   `kelvin_to_*`
    -   `rankine_to_*`
    -   `reaumur_to_*`
3.  실행 방법
4.  코드 개선 제안

## 온도 단위 변환 원리

각 온도 단위는 서로 다른 기준점(물의 어는점, 끓는점 등)과 간격을 가지고 있습니다. 이 스크립트의 함수들은 각 단위 간의 표준 변환 공식을 사용하여 값을 변환합니다.

-   **섭씨(°C) ↔ 화씨(°F)**: `°F = °C * 9/5 + 32`
-   **섭씨(°C) ↔ 켈빈(K)**: `K = °C + 273.15`
-   **화씨(°F) ↔ 란씨(°R)**: `°R = °F + 459.67`
-   **켈빈(K) ↔ 란씨(°R)**: `°R = K * 9/5`
-   **섭씨(°C) ↔ 열씨(°Ré)**: `°C = °Ré * 1.25`

다른 모든 변환은 이 기본 공식들을 조합하여 이루어집니다.

## 함수 설명

이 스크립트는 각 변환 방향에 대해 별도의 함수를 제공합니다. 모든 함수는 비슷한 구조를 가집니다.

-   **입력**: 변환할 온도 값(`float`)과 반올림할 소수점 자릿수(`ndigits`, 기본값 2).
-   **알고리즘**:
    1.  입력값을 `float()`를 사용하여 실수로 변환합니다.
    2.  해당 단위에 맞는 표준 변환 공식을 적용합니다.
    3.  `round()` 함수를 사용하여 결과를 지정된 소수점 자릿수까지 반올림하여 반환합니다.

### `celsius_to_*`
-   `celsius_to_fahrenheit(celsius, ndigits)`
-   `celsius_to_kelvin(celsius, ndigits)`
-   `celsius_to_rankine(celsius, ndigits)`

### `fahrenheit_to_*`
-   `fahrenheit_to_celsius(fahrenheit, ndigits)`
-   `fahrenheit_to_kelvin(fahrenheit, ndigits)`
-   `fahrenheit_to_rankine(fahrenheit, ndigits)`

... (켈빈, 란씨, 열씨에 대한 나머지 함수들도 동일한 패턴을 따릅니다.)

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python temperature_conversions.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **코드 중복 제거 및 범용 변환 함수**: 현재 스크립트는 모든 변환 쌍에 대해 별도의 함수를 가지고 있어 코드 중복이 매우 많습니다. **섭씨(Celsius)** 또는 **켈빈(Kelvin)**을 공통의 기준 단위로 사용하여, 모든 단위를 먼저 기준 단위로 변환한 후 다시 목표 단위로 변환하는 범용 함수를 만들면 코드를 훨씬 간결하고 유지보수하기 쉽게 만들 수 있습니다.

    ```python
    # 범용 변환 함수 예시
    CONVERSION_FACTORS = {
        "celsius": {"to_kelvin": lambda c: c + 273.15, "from_kelvin": lambda k: k - 273.15},
        "fahrenheit": {"to_kelvin": lambda f: (f - 32) * 5/9 + 273.15, "from_kelvin": lambda k: (k - 273.15) * 9/5 + 32},
        # ... 다른 단위들 ...
    }

    def convert_temperature(value: float, from_unit: str, to_unit: str, ndigits: int = 2) -> float:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # 1. 입력 단위를 켈빈으로 변환
        kelvin_value = CONVERSION_FACTORS[from_unit]["to_kelvin"](value)
        
        # 2. 켈빈을 목표 단위로 변환
        result = CONVERSION_FACTORS[to_unit]["from_kelvin"](kelvin_value)
        
        return round(result, ndigits)
    ```

2.  **입력 처리**: 모든 함수가 `float(celsius)`와 같이 입력을 `float`으로 변환하고 있습니다. 이는 유연성을 제공하지만, `doctest`에서 볼 수 있듯이 숫자로 변환할 수 없는 문자열("celsius")이 입력되면 `ValueError`가 발생합니다. 범용 함수를 만들 경우, 함수 시작 부분에서 한 번만 입력값의 유효성을 검사하는 것이 더 효율적입니다.

3.  **'매직 넘버' 제거**: `273.15`, `459.67`과 같은 변환 상수들을 의미 있는 이름의 전역 상수(예: `ABSOLUTE_ZERO_CELSIUS = -273.15`)로 정의하면 코드의 가독성과 명확성이 향상됩니다.