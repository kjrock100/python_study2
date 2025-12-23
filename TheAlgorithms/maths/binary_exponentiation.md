# Binary Exponentiation (Recursive) 알고리즘

이 문서는 `binary_exponentiation.py` 파일에 구현된 **이진 거듭제곱(Binary Exponentiation)** 알고리즘에 대한 설명입니다.

## 개요

**이진 거듭제곱**은 $a^n$을 $O(\log n)$의 시간 복잡도로 효율적으로 계산하는 방법입니다. 이 파일에서는 **재귀(Recursion)**를 사용한 구현을 제공합니다.

## 함수 설명

### `binary_exponentiation(a, n)`

밑(base) `a`를 지수(exponent) `n`만큼 거듭제곱한 값을 반환합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 밑 (Base)
- `n` (`int`): 지수 (Exponent)

#### 알고리즘 (Algorithm)

재귀적인 분할 정복(Divide and Conquer) 방식을 사용합니다.

1. **기저 사례 (Base Case)**: `n`이 0이면 1을 반환합니다. ($a^0 = 1$)
2. **재귀 단계 (Recursive Step)**:
   - `n`이 홀수인 경우: `binary_exponentiation(a, n - 1)`을 호출하고 그 결과에 `a`를 곱하여 반환합니다.
   - `n`이 짝수인 경우: `binary_exponentiation(a, n / 2)`를 호출하여 반환값 `b`를 구한 뒤, `b * b`를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 밑과 지수를 입력받아 결과를 출력합니다.

```python
if __name__ == "__main__":
    try:
        BASE = int(input("Enter Base : ").strip())
        POWER = int(input("Enter Power : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    RESULT = binary_exponentiation(BASE, POWER)
    print(f"{BASE}^({POWER}) : {RESULT}")
```
