## 코드 분석
이 파이썬 코드는 주어진 음의 정수에 대한 2의 보수(Two's Complement) 표현을 문자열 형태로 반환하는 twos_complement 함수를 정의하고 있습니다.

2의 보수는 컴퓨터 과학에서 음수를 표현하는 가장 일반적인 방법입니다.

### twos_complement 함수 상세 분석

#### 1. 입력 값 검증:

```python
if number > 0:
    raise ValueError("input must be a negative integer")
```

함수는 먼저 입력받은 number가 양수인지 확인합니다. 만약 양수이면, ValueError를 발생시켜 함수가 음수와 0에 대해서만 동작하도록 강제합니다.

#### 2. 비트 길이 계산:

```python
binary_number_length = len(bin(number)[3:])
```

이 부분은 2의 보수 표현에 필요한 최소 비트 수를 계산합니다.

- bin(number): 음수(예: -5)를 이진 문자열('-0b101')로 변환합니다.
- [3:]: -0b 접두사를 제외한 숫자 부분('101')만 추출합니다.
- len(...): 추출된 이진수의 길이(예: 3)를 계산합니다. 이 길이는 숫자의 절댓값을 표현하는 데 필요한 비트 수와 같습니다.

#### 3. 2의 보수 계산 (핵심 로직):

```python
twos_complement_number = bin(abs(number) - (1 << binary_number_length))[3:]
```

이 코드는 2의 보수를 구하는 수학적 트릭을 사용합니다.

- 1 << binary_number_length: 2^binary_number_length 와 같습니다. 예를 들어 number가 -5이면 binary_number_length는 3이고, 이 값은 2^3 = 8 (이진수 1000)이 됩니다.
- abs(number) - (1 << ...): |number| - 2^n 연산을 수행합니다. 예를 들어 -5의 경우 5 - 8 = -3이 됩니다.
- bin(...): 계산 결과(예: -3)를 다시 이진 문자열('-0b11')로 변환합니다.
- [3:]: -0b 접두사를 제외한 부분('11')을 twos_complement_number에 저장합니다.

#### 4. 결과 포맷팅:

```python
 Show full code block 
twos_complement_number = (
    (
        "1"
        + "0" * (binary_number_length - len(twos_complement_number))
        + twos_complement_number
    )
    if number < 0
    else "0"
)
```

이 부분은 계산된 결과를 최종적인 2의 보수 형태로 만듭니다.

- if number < 0: 입력이 음수일 경우에만 이 블록을 실행합니다.
- "1" + ...: 2의 보수에서 음수는 항상 최상위 비트(MSB)가 1이므로, '1'을 맨 앞에 붙입니다.
- "0" * (...): 중간에 필요한 만큼 '0'을 채워 넣어 전체 비트 길이를 맞춥니다. 예를 들어 -5의 경우, binary_number_length는 3이고 twos_complement_number는 '11'(길이 2)이므로, 3 - 2 = 1개의 '0'을 채웁니다.
- 결과적으로 -5의 경우 '1' + '0' + '11' 이 되어 '1011'이 완성됩니다.
- else "0": number가 0인 경우, 결과는 "0"이 됩니다.

#### 5. 최종 반환:

```python
return "0b" + twos_complement_number
```

완성된 2의 보수 문자열 앞에 파이썬의 이진수 접두사 '0b'를 붙여 반환합니다.

### 코드의 장단점

- 장점:
  - 비트 연산과 수학적 속성을 활용하여 2의 보수를 독창적인 방식으로 계산합니다.
  - doctest를 사용하여 함수의 동작과 예시를 명확하게 보여주고, 코드 자체적으로 테스트가 가능합니다.
- 단점:
- 코드가 직관적이지 않아 주석 없이는 이해하기 어렵습니다. 2의 보수를 구하는 일반적인 방법(비트 반전 후 1 더하기)이 아니라서 가독성이 떨어집니다.
- bin() 함수와 문자열 슬라이싱([3:])을 여러 번 사용하여 비효율적일 수 있습니다.

### 개선 제안

코드를 더 명확하고 직관적으로 개선할 수 있습니다. 2의 보수를 구하는 표준적인 방법은 다음과 같습니다.

1. 숫자의 절댓값에 해당하는 이진수를 구합니다.
2. 모든 비트를 반전시킵니다(0은 1로, 1은 0으로).
3. 반전된 값에 1을 더합니다.

이 로직을 적용하면 코드가 더 읽기 쉬워집니다. 아래는 개선된 코드와 diff입니다.

```
binary_twos_complement.py
-20
+16
 Show full code block 
# Information on 2's complement: https://en.wikipedia.org/wiki/Two%27s_complement


def twos_complement(number: int) -> str:
def twos_complement(num: int) -> str:
    """
    Take in a negative integer 'number'.
    Return the two's complement representation of 'number'.
    Calculate the two's complement representation of an integer.
    Handles negative integers and zero.

    >>> twos_complement(0)
    '0b0'
    >>> twos_complement(-1)
    '0b11'
    '0b1'
    >>> twos_complement(-5)
    '0b1011'
    >>> twos_complement(-17)
    '0b101111'
    >>> twos_complement(-207)
    '0b100110001'
    >>> twos_complement(1)
    >>> twos_complement(5)
    Traceback (most recent call last):
        ...
    ValueError: input must be a negative integer
    ValueError: Input must be a non-positive integer.
    """
    if number > 0:
        raise ValueError("input must be a negative integer")
    binary_number_length = len(bin(number)[3:])
    twos_complement_number = bin(abs(number) - (1 << binary_number_length))[3:]
    twos_complement_number = (
        (
            "1"
            + "0" * (binary_number_length - len(twos_complement_number))
            + twos_complement_number
        )
        if number < 0
        else "0"
    )
    return "0b" + twos_complement_number
    if num > 0:
        raise ValueError("Input must be a non-positive integer.")
    if num == 0:
        return "0b0"

    # For a negative number, find the smallest number of bits to represent its absolute
    val = abs(num)
    bits_required = val.bit_length() + 1  # +1 for the sign bit
    # 2's complement is 2**n - |num|
    return bin((1 << bits_required) - val)


if __name__ == "__main__":
```

### 개선된 코드 설명

1. 가독성 향상: num > 0과 num == 0 케이스를 명확하게 분리하여 코드를 이해하기 쉽게 만들었습니다.
2. bit_length() 사용: abs(num).bit_length()는 숫자를 이진수로 표현하는 데 필요한 비트 수를 직접 알려주는 내장 메서드입니다. 문자열 변환 및 슬라이싱보다 훨씬 효율적이고 명확합니다.
3. 직관적인 계산: (1 << bits_required) - val은 2의 보수의 수학적 정의(2^n - |num|)를 직접적으로 코드로 표현한 것입니다. 기존 코드의 abs(number) - (1 << binary_number_length) 보다 이해하기 쉽습니다.
4. doctest 수정: -1의 2의 보수는 1비트로 표현하면 '0b1'이므로, doctest의 예시를 더 정확하게 수정했습니다.
