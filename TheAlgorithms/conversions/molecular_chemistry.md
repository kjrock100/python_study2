# `molecular_chemistry.py` 코드 설명

이 문서는 `molecular_chemistry.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 분자 화학에서 자주 사용되는 기본적인 계산, 특히 **이상 기체 법칙(Ideal Gas Law)**과 **노르말 농도(Normality)** 변환과 관련된 함수들을 제공합니다.

## 목차
1.  주요 개념
    -   노르말 농도
    -   이상 기체 법칙
2.  함수 설명
    -   `molarity_to_normality(nfactor, moles, volume)`
    -   `moles_to_pressure(volume, moles, temperature)`
    -   `moles_to_volume(pressure, moles, temperature)`
    -   `pressure_and_volume_to_temperature(...)`
3.  실행 방법
4.  코드 개선 제안

## 주요 개념

### 노르말 농도 (Normality)

노르말 농도는 용액의 농도를 나타내는 단위 중 하나로, 용액 1리터에 포함된 용질의 **당량(equivalent)** 수를 의미합니다. 몰 농도(molarity)와 다음과 같은 관계를 가집니다.

`노르말 농도 = 몰 농도 * n-factor`

-   **몰 농도**: 용액 1리터에 포함된 용질의 몰(mole) 수.
-   **n-factor (당량 인자)**: 화학 반응에서 한 분자가 제공할 수 있는 반응 단위의 수 (예: 산의 경우 H⁺ 이온 수, 염기의 경우 OH⁻ 이온 수).

### 이상 기체 법칙 (Ideal Gas Law)

이상 기체의 상태를 설명하는 방정식으로, 압력(P), 부피(V), 몰수(n), 온도(T) 간의 관계를 나타냅니다.

`PV = nRT`

-   `P`: 압력 (atm)
-   `V`: 부피 (litres)
-   `n`: 몰수 (moles)
-   `R`: 기체 상수 (이 스크립트에서는 약 0.0821 L·atm/(K·mol))
-   `T`: 절대 온도 (kelvin)

이 스크립트의 함수들은 이 공식을 변형하여 각 변수를 계산합니다.

## 함수 설명

### `molarity_to_normality(nfactor: int, moles: float, volume: float) -> float`

몰 농도를 노르말 농도로 변환합니다.

-   **알고리즘**: `(moles / volume)`으로 몰 농도를 계산한 후, `nfactor`를 곱하여 노르말 농도를 구하고 반올림하여 반환합니다.

### `moles_to_pressure(volume: float, moles: float, temperature: float) -> float`

이상 기체 법칙을 사용하여 주어진 부피, 몰수, 온도로부터 압력을 계산합니다.

-   **알고리즘**: `P = (nRT) / V` 공식을 사용하여 압력을 계산하고 반올림하여 반환합니다.

### `moles_to_volume(pressure: float, moles: float, temperature: float) -> float`

이상 기체 법칙을 사용하여 주어진 압력, 몰수, 온도로부터 부피를 계산합니다.

-   **알고리즘**: `V = (nRT) / P` 공식을 사용하여 부피를 계산하고 반올림하여 반환합니다.

### `pressure_and_volume_to_temperature(pressure: float, moles: float, volume: float) -> float`

이상 기체 법칙을 사용하여 주어진 압력, 몰수, 부피로부터 온도를 계산합니다.

-   **알고리즘**: `T = (PV) / (nR)` 공식을 사용하여 온도를 계산하고 반올림하여 반환합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python molecular_chemistry.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **'매직 넘버' 제거**: 이상 기체 상수 `0.0821`이 여러 함수에 하드코딩되어 있습니다. 이 값을 `IDEAL_GAS_CONSTANT = 0.0821`과 같이 모듈 수준의 상수로 정의하면, 코드의 가독성이 향상되고 값을 변경해야 할 때 한 곳만 수정하면 되므로 유지보수가 용이해집니다.

2.  **입력 유효성 검사**: 현재 함수들은 입력값의 유효성을 검사하지 않습니다. 예를 들어, `volume`이나 `moles`가 0 또는 음수이거나, `temperature`가 절대 영도(0 켈빈) 이하일 경우 물리적으로 의미가 없거나 0으로 나누는 오류가 발생할 수 있습니다. 각 함수의 시작 부분에 입력값의 범위를 확인하는 로직을 추가하면 프로그램의 안정성이 향상됩니다.

    ```python
    # 예시
    def moles_to_pressure(volume: float, moles: float, temperature: float) -> float:
        if volume <= 0:
            raise ValueError("Volume must be positive.")
        if temperature < 0:
            raise ValueError("Temperature must be in Kelvin and non-negative.")
        # ... (이후 계산 로직)
    ```

3.  **`round()` 함수의 동작**: `round()` 함수는 파이썬 3에서 "round half to even" 방식을 따릅니다 (예: `round(2.5)`는 2, `round(3.5)`는 4). 이는 통계적 편향을 줄이기 위한 것이지만, 일반적인 사사오입과 다를 수 있음을 인지하고 사용해야 합니다. 만약 특정 소수점 자리까지의 정밀도가 필요하다면, `round(..., ndigits)`와 같이 자릿수를 명시하는 것이 좋습니다.