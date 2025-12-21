# 식생 지수 계산 (Index Calculation)

이 문서는 `index_calculation.py` 파일에 구현된 **식생 지수 계산(Index Calculation)** 알고리즘에 대해 설명합니다. 이 코드는 정밀 농업이나 원격 탐사(Remote Sensing) 분야에서 식생의 활력도나 상태를 분석하기 위해 사용되는 다양한 지수들을 계산하는 클래스를 제공합니다.

## 개요

식생 지수(Vegetation Index)는 두 개 이상의 파장 대역(Band)의 반사율 값을 조합하여 식생의 특성을 강조하는 스펙트럼 변환입니다. 이 코드는 가시광선(Red, Green, Blue)과 근적외선(NIR), 적색 경계(Red Edge) 대역의 데이터를 입력받아 수십 가지의 다양한 지수를 계산할 수 있습니다.

## 클래스: `IndexCalculation`

### `__init__(self, red=None, green=None, blue=None, redEdge=None, nir=None)`
- **목적**: 클래스 인스턴스를 생성하고 각 파장 대역의 데이터를 초기화합니다.
- **매개변수**: 각 파장 대역(Red, Green, Blue, RedEdge, NIR)에 해당하는 데이터(주로 NumPy 배열).

### `setMatrices(self, ...)`
- **목적**: 클래스 내부에 저장된 파장 대역 데이터를 업데이트합니다.

### `calculation(self, index="", ...)`
- **목적**: 지정된 이름(`index`)에 해당하는 식생 지수를 계산하여 반환합니다.
- **매개변수**:
  - `index`: 계산할 지수의 약어 (예: "NDVI", "EVI").
  - 나머지 파장 데이터들은 선택적으로 입력받아 업데이트할 수 있습니다.
- **동작**: 내부 딕셔너리(`funcs`)를 통해 문자열 키를 해당 계산 메서드에 매핑하여 실행합니다.

## 주요 식생 지수 예시

이 클래스는 약 40여 개의 지수를 지원합니다. 대표적인 몇 가지는 다음과 같습니다:

- **NDVI (Normalized Difference Vegetation Index)**: 정규 식생 지수. 가장 널리 사용되며 식생의 유무와 활력도를 나타냅니다.
  - 공식: $(NIR - Red) / (NIR + Red)$
- **GNDVI (Green NDVI)**: 녹색 식생 지수. Red 대신 Green 채널을 사용합니다.
  - 공식: $(NIR - Green) / (NIR + Green)$
- **EVI (Enhanced Vegetation Index)**: 향상된 식생 지수. 대기 영향과 토양 배경 신호를 보정합니다.
- **SAVI (Soil Adjusted Vegetation Index)** 계열: 토양의 영향을 보정한 지수들 (MSAVI, OSAVI 등).
- **RGB 기반 지수**: NIR 데이터 없이 가시광선만으로 계산하는 지수들 (GLI, VARI 등).

## 사용법

코드 하단의 주석에 포함된 예시를 참고하면 다음과 같이 사용할 수 있습니다:

```python
import numpy as np
from index_calculation import IndexCalculation

# 1. 데이터 준비 (예시: 모든 값이 동일한 더미 데이터)
red     = np.ones((100, 100)) * 0.1
nir     = np.ones((100, 100)) * 0.5
# ... 다른 밴드들도 필요에 따라 준비

# 2. 클래스 인스턴스 생성
cl = IndexCalculation(red=red, nir=nir)

# 3. 지수 계산 (NDVI 예시)
ndvi_result = cl.calculation("NDVI")
print(ndvi_result)
```