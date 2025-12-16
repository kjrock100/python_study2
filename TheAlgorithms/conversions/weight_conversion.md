# `weight_conversion.py` 코드 설명

이 문서는 `weight_conversion.py` 파이썬 스크립트에 포함된 `weight_conversion` 함수를 설명합니다. 이 스크립트는 킬로그램(Kilogram), 그램(Gram), 파운드(Pound) 등 다양한 무게 단위를 서로 변환하는 기능을 제공합니다.

## 목차
1.  스크립트의 역할 및 변환 원리
2.  주요 데이터 구조
    -   `KILOGRAM_CHART`
    -   `WEIGHT_TYPE_CHART`
3.  함수 설명
    -   `weight_conversion(from_type, to_type, value)`
4.  실행 방법
5.  코드 개선 제안

## 스크립트의 역할 및 변환 원리

이 스크립트는 다양한 무게 단위를 입력받아 원하는 다른 단위로 변환하는 범용 변환기입니다.

변환은 **킬로그램(kilogram)**을 공통의 기준 단위로 사용하여 2단계로 이루어집니다.
1.  입력된 단위(`from_type`)의 값을 킬로그램으로 변환합니다.
2.  킬로그램으로 변환된 값을 다시 목표 단위(`to_type`)로 변환합니다.

**공식**: `결과 = 입력값 * (입력단위 -> kg 변환 계수) * (kg -> 목표단위 변환 계수)`

## 주요 데이터 구조

### `KILOGRAM_CHART`

**킬로그램에서** 다른 단위로 변환할 때 사용하는 변환 계수를 저장하는 딕셔너리입니다.
-   **예시**: 1 킬로그램은 1000 그램이므로, `KILOGRAM_CHART["gram"]`의 값은 `1000`입니다.

### `WEIGHT_TYPE_CHART`

다른 단위에서 **킬로그램으로** 변환할 때 사용하는 변환 계수를 저장하는 딕셔너리입니다.
-   **예시**: 1 그램은 0.001 킬로그램이므로, `WEIGHT_TYPE_CHART["gram"]`의 값은 `0.001`입니다.

## 함수 설명

### `weight_conversion(from_type: str, to_type: str, value: float) -> float`

주어진 `value`를 `from_type`에서 `to_type`으로 변환합니다.

-   **알고리즘**:
    1.  **유효성 검사**: `from_type`과 `to_type` 문자열이 변환 딕셔너리에 존재하는지 확인하고, 없으면 `ValueError`를 발생시킵니다.
    2.  **변환 수행**: 위에서 설명한 공식을 사용하여 최종 값을 계산하고 반환합니다.
        -   `value * WEIGHT_TYPE_CHART[from_type] * KILOGRAM_CHART[to_type]`

```python
>>> weight_conversion("kilogram","gram",1)
1000
>>> weight_conversion("pound","kilogram",4)
1.814368
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python weight_conversion.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **데이터 구조 단순화**: 현재 `KILOGRAM_CHART`와 `WEIGHT_TYPE_CHART` 두 개의 딕셔너리를 사용하고 있습니다. `WEIGHT_TYPE_CHART`는 `KILOGRAM_CHART`의 역수 관계(`1 / KILOGRAM_CHART[unit]`)와 거의 동일하므로, 하나의 기준 딕셔너리만 유지하고 다른 하나는 동적으로 계산하거나, `length_conversion.py`처럼 `(from_base, to_base)` 형태의 `namedtuple`을 사용하여 하나의 딕셔너리로 통합할 수 있습니다.

    ```python
    # namedtuple을 사용한 개선 제안 예시
    from collections import namedtuple

    Conversion = namedtuple("Conversion", "from_kg to_kg")
    WEIGHT_CONVERSION = {
        "kilogram": Conversion(1, 1),
        "gram": Conversion(1000, 0.001),
        # ... 다른 단위들 ...
    }

    def weight_conversion_simple(from_type: str, to_type: str, value: float) -> float:
        # ...
        return value * WEIGHT_CONVERSION[from_type].to_kg * WEIGHT_CONVERSION[to_type].from_kg
    ```

2.  **입력 정규화**: `length_conversion.py`와 같이, 사용자가 "Kilogram", "kilogram", "KG" 등 다양한 형태로 단위를 입력해도 모두 "kilogram"으로 인식하도록 입력 문자열을 소문자로 변환하고, 별칭 딕셔너리를 사용하는 로직을 추가하면 사용성이 향상됩니다.

3.  **사용자 인터페이스 추가**: `if __name__ == "__main__"` 블록에 `argparse` 모듈을 사용하여 사용자가 커맨드 라인에서 직접 값과 단위를 입력하여 변환을 수행할 수 있는 인터페이스를 제공하면 스크립트의 활용도가 높아집니다.

4.  **부동 소수점 정밀도**: `doctest` 예제에서 `0.7873658640000001`과 같이 부동 소수점 연산으로 인한 미세한 오차가 보입니다. 이는 정상적인 동작이지만, 만약 특정 소수점 자리까지의 결과가 필요하다면, 함수 마지막에 `round()`를 사용하여 반올림하는 옵션을 추가할 수 있습니다.