이 코드는 정수(integer)에 대한 세 가지 종류의 비트 시프트(bit shift) 연산을 구현하고, 그 결과를 이진수 문자열로 반환하는 함수들을 담고 있습니다.

## 파일 분석 (binary_shifts.py)

이 파일은 세 가지 주요 함수로 구성되어 있습니다.

1. logical_left_shift: 논리 좌측 시프트 (Logical Left Shift)
2. logical_right_shift: 논리 우측 시프트 (Logical Right Shift)
3. arithmetic_right_shift: 산술 우측 시프트 (Arithmetic Right Shift)

각 함수에 대해 자세히 살펴보겠습니다.

### 1. logical_left_shift 함수

```python
def logical_left_shift(number: int, shift_amount: int) -> str:
    """
    Take in 2 positive integers.
    'number' is the integer to be logically left shifted 'shift_amount' times.
    i.e. (number << shift_amount)
    Return the shifted binary representation.
    ...
    """
    if number < 0 or shift_amount < 0:
        raise ValueError("both inputs must be positive integers")

    binary_number = str(bin(number))
    binary_number += "0" * shift_amount
    return binary_number
```

#### 기능 설명

이 함수는 주어진 양의 정수 number를 shift_amount 만큼 논리적 좌측 시프트를 수행합니다.

- 논리적 좌측 시프트는 숫자의 이진 표현에서 모든 비트를 왼쪽으로 지정된 횟수만큼 이동시키는 연산입니다.
- 왼쪽으로 비트가 이동하면서 비게 되는 오른쪽 끝자리들은 항상 0으로 채워집니다.
- 이 연산은 number * (2 ** shift_amount) 와 동일한 효과를 가집니다.

#### 코드 분석

- if number < 0 or shift_amount < 0:: 함수는 양의 정수만 처리하도록 설계되었으므로, 음수가 입력되면 ValueError를 발생시킵니다.
- binary_number = str(bin(number)): number를 0b 접두사가 붙은 이진수 문자열로 변환합니다. (예: 17 -> '0b10001')
- binary_number += "0" * shift_amount: 변환된 이진수 문자열 뒤에 shift_amount 개수만큼 문자 '0'을 추가합니다. 이는 왼쪽으로 시프트하고 오른쪽을 0으로 채우는 과정을 문자열 연산으로 흉내 낸 것입니다.

#### 개선 제안

현재 코드는 문자열 연산을 사용하여 시프트 연산을 시뮬레이션합니다. Python의 내장 비트 시프트 연산자 <<를 사용하면 더 직접적이고 효율적으로 구현할 수 있습니다.

```
--- a/d:\01.study\kjrock100\python_study\TheAlgorithms\bit_manipulation\binary_shifts.py
+++ b/d:\01.study\kjrock100\python_study\TheAlgorithms\bit_manipulation\binary_shifts.py
@@ -19,8 +19,7 @@
     if number < 0 or shift_amount < 0:
         raise ValueError("both inputs must be positive integers")
 
-    binary_number = str(bin(number))
-    binary_number += "0" * shift_amount
-    return binary_number
+    # Python의 << 연산자는 논리적 좌측 시프트와 동일하게 동작합니다.
+    return bin(number << shift_amount)
 
 
 def logical_right_shift(number: int, shift_amount: int) -> str:
```

참고: 위 수정안을 적용하면 logical_left_shift(0, 1)의 결과가 기존 '0b00'에서 '0b0'으로 변경됩니다. 0은 몇 번을 시프트해도 0이므로 '0b0'이 수학적으로 더 정확한 표현입니다. 기존 코드의 결과('0b00')는 문자열 연산 방식 때문에 나타나는 특징입니다.

### 2. logical_right_shift 함수

```python
def logical_right_shift(number: int, shift_amount: int) -> str:
    """
    Take in positive 2 integers.
    'number' is the integer to be logically right shifted 'shift_amount' times.
    i.e. (number >>> shift_amount)
    Return the shifted binary representation.
    ...
    """
    if number < 0 or shift_amount < 0:
        raise ValueError("both inputs must be positive integers")

    binary_number = str(bin(number))[2:]
    if shift_amount >= len(binary_number):
        return "0b0"
    shifted_binary_number = binary_number[: len(binary_number) - shift_amount]
    return "0b" + shifted_binary_number
```

#### 기능 설명

이 함수는 주어진 양의 정수 number를 shift_amount 만큼 논리적 우측 시프트를 수행합니다.

- 논리적 우측 시프트는 숫자의 이진 표현에서 모든 비트를 오른쪽으로 지정된 횟수만큼 이동시키는 연산입니다.
- 오른쪽으로 이동하면서 범위를 벗어나는 비트들은 버려지고, 비게 되는 왼쪽 끝자리들은 항상 0으로 채워집니다.
- 이 연산은 number // (2 ** shift_amount) (정수 나눗셈)와 동일한 효과를 가집니다.

#### 코드 분석

- binary_number = str(bin(number))[2:]: number를 이진수 문자열로 변환하고, 접두사 0b를 제거합니다. (예: 17 -> '10001')
- if shift_amount >= len(binary_number):: 만약 시프트할 양이 이진수의 길이보다 크거나 같으면 모든 비트가 사라지므로 결과는 0이 됩니다. 따라서 '0b0'을 반환합니다.
- shifted_binary_number = binary_number[: len(binary_number) - shift_amount]: 문자열 슬라이싱을 이용해 오른쪽에서 shift_amount 만큼의 문자를 잘라냅니다. 이것이 우측 시프트의 효과입니다.
- return "0b" + shifted_binary_number: 결과 문자열에 다시 0b를 붙여 반환합니다.

#### 개선 제안

이 함수 역시 Python의 내장 비트 시프트 연산자 >>를 사용하면 더 간결하게 작성할 수 있습니다. Python에서 양의 정수에 대한 >> 연산은 논리적 우측 시프트와 동일하게 동작합니다.

```
--- a/d:\01.study\kjrock100\python_study\TheAlgorithms\bit_manipulation\binary_shifts.py
+++ b/d:\01.study\kjrock100\python_study\TheAlgorithms\bit_manipulation\binary_shifts.py
@@ -43,11 +43,8 @@
     if number < 0 or shift_amount < 0:
         raise ValueError("both inputs must be positive integers")
 
-    binary_number = str(bin(number))[2:]
-    if shift_amount >= len(binary_number):
-        return "0b0"
-    shifted_binary_number = binary_number[: len(binary_number) - shift_amount]
-    return "0b" + shifted_binary_number
+    # Python에서 양의 정수에 대한 >> 연산자는 논리적 우측 시프트와 동일합니다.
+    return bin(number >> shift_amount)
 
 
 def arithmetic_right_shift(number: int, shift_amount: int) -> str:
```

### 3. arithmetic_right_shift 함수

```python
def arithmetic_right_shift(number: int, shift_amount: int) -> str:
    """
    Take in 2 integers.
    'number' is the integer to be arithmetically right shifted 'shift_amount' times.
    i.e. (number >> shift_amount)
    Return the shifted binary representation.
    ...
    """
    if number >= 0:  # Get binary representation of positive number
        binary_number = "0" + str(bin(number)).strip("-")[2:]
    else:  # Get binary (2's complement) representation of negative number
        binary_number_length = len(bin(number)[3:])  # Find 2's complement of number
        binary_number = bin(abs(number) - (1 << binary_number_length))[3:]
        binary_number = (
            "1" + "0" * (binary_number_length - len(binary_number)) + binary_number
        )

    if shift_amount >= len(binary_number):
        return "0b" + binary_number[0] * len(binary_number)
    return (
        "0b"
        + binary_number[0] * shift_amount
        + binary_number[: len(binary_number) - shift_amount]
    )
```

#### 기능 설명

이 함수는 주어진 정수 number를 shift_amount 만큼 산술 우측 시프트를 수행합니다.

- 산술 우측 시프트는 부호를 유지하는 우측 시프트 연산입니다.
- 논리적 우측 시프트와 유사하게 비트를 오른쪽으로 이동시키지만, 비게 되는 왼쪽 최상위 비트(MSB, Most Significant Bit)를 기존의 최상위 비트 값으로 채웁니다.
- 최상위 비트는 부호 비트(양수: 0, 음수: 1)이므로, 이 연산을 통해 숫자의 부호가 유지됩니다.

#### 코드 분석

- 이 함수는 양수와 음수를 다르게 처리하여 2의 보수(2's complement) 표현을 문자열로 직접 만듭니다. 이 과정이 다소 복잡합니다.
- if number >= 0:: 양수인 경우, 이진수 앞에 부호 비트 0을 추가합니다.
- else:: 음수인 경우, 2의 보수 표현을 계산하여 부호 비트 1로 시작하는 이진수 문자열을 만듭니다.
- 그 후, 문자열 연산을 통해 시프트를 수행합니다. binary_number[0] * shift_amount 부분은 부호 비트를 복사하여 왼쪽에 채워 넣는 산술 시프트의 핵심 동작을 구현한 것입니다.

#### 개선 제안

Python의 >> 연산자는 정수에 대해 이미 산술 우측 시프트를 수행합니다. 따라서 이 복잡한 문자열 처리 로직은 내장 연산자를 사용하여 간단하게 대체할 수 있습니다.

```
--- a/d:\01.study\kjrock100\python_study\TheAlgorithms\bit_manipulation\binary_shifts.py
+++ b/d:\01.study\kjrock100\python_study\TheAlgorithms\bit_manipulation\binary_shifts.py
@@ -66,21 +66,8 @@
     >>> arithmetic_right_shift(-1983, 4)
     '0b111110000100'
     """
-    if number >= 0:  # Get binary representation of positive number
-        binary_number = "0" + str(bin(number)).strip("-")[2:]
-    else:  # Get binary (2's complement) representation of negative number
-        binary_number_length = len(bin(number)[3:])  # Find 2's complement of number
-        binary_number = bin(abs(number) - (1 << binary_number_length))[3:]
-        binary_number = (
-            "1" + "0" * (binary_number_length - len(binary_number)) + binary_number
-        )
-
-    if shift_amount >= len(binary_number):
-        return "0b" + binary_number[0] * len(binary_number)
-    return (
-        "0b"
-        + binary_number[0] * shift_amount
-        + binary_number[: len(binary_number) - shift_amount]
-    )
+    # Python의 >> 연산자는 산술 우측 시프트를 수행합니다.
+    # bin()은 음수에 대해 '-0b...' 형태로 반환하므로, 이를 직접 사용하면 됩니다.
+    return bin(number >> shift_amount)
 
 
 if __name__ == "__main__":
```

참고: 이 수정안을 적용하면 doctest의 결과와 달라질 수 있습니다. 예를 들어 arithmetic_right_shift(-17, 2)의 결과는 bin(-17 >> 2) 즉, bin(-5)가 되어 '-0b101'을 반환합니다. 기존 코드의 결과('0b111011')는 특정 비트 길이를 가정한 2의 보수 표현입니다. Python의 bin() 함수는 음수에 대해 - 부호를 사용하므로, 2의 보수 형태의 문자열을 원한다면 별도의 포맷팅 함수가 필요합니다. 하지만 연산 자체는 >>로 간단히 처리할 수 있습니다.

#### 종합 요약

- 목표: 코드는 비트 시프트 연산의 원리를 보여주기 위해 작성되었습니다.
- 구현: Python의 내장 비트 연산자 대신 문자열 조작을 통해 시프트 연산을 시뮬레이션하고 있습니다. 이는 교육적인 목적에는 부합할 수 있습니다.
- 실용성 및 개선: 실제 프로그래밍에서는 Python이 제공하는 강력한 내장 비트 연산자 (<<, >>)를 사용하는 것이 훨씬 효율적이고 간결하며 Pythonic한 방법입니다.
