# Binary Exponentiation (Modular) 알고리즘

이 문서는 `binary_exp_mod.py` 파일에 구현된 **모듈러 거듭제곱(Modular Exponentiation)** 알고리즘에 대한 설명입니다.

## 개요

**모듈러 거듭제곱**은 $a^n \pmod b$를 효율적으로 계산하는 방법입니다. 단순히 $a$를 $n$번 곱하는 $O(n)$ 방식 대신, 지수를 반으로 나누어가며 계산하는 **이진 거듭제곱(Binary Exponentiation)** 방식을 사용하여 $O(\log n)$의 시간 복잡도로 계산합니다. 암호학 등 큰 수의 거듭제곱 연산이 필요한 분야에서 필수적으로 사용됩니다.

## 함수 설명

### `bin_exp_mod(a, n, b)`

밑(base) `a`를 지수(exponent) `n`만큼 거듭제곱한 후, 모듈러(modulus) `b`로 나눈 나머지를 반환합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 밑 (Base)
- `n` (`int`): 지수 (Exponent)
- `b` (`int`): 모듈러 (Modulus, 나누는 수)

#### 예외 처리 (Error Handling)

- **AssertionError**: `b`가 0일 경우 "This cannot accept modulo that is == 0" 메시지와 함께 에러가 발생합니다.

#### 알고리즘 (Algorithm)

재귀적인 분할 정복(Divide and Conquer) 방식을 사용합니다.

1. **기저 사례 (Base Case)**: `n`이 0이면 1을 반환합니다. ($a^0 = 1$)
2. **재귀 단계 (Recursive Step)**:
   - `n`이 홀수인 경우: $a^n = a \times a^{n-1}$ 임을 이용하여, `bin_exp_mod(a, n-1, b)` 결과에 `a`를 곱하고 `b`로 나눈 나머지를 반환합니다.
   - `n`이 짝수인 경우: $a^n = (a^{n/2})^2$ 임을 이용하여, `bin_exp_mod(a, n/2, b)`를 호출하여 반환값 `r`을 구한 뒤, `r * r`을 `b`로 나눈 나머지를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 밑, 지수, 모듈러 값을 입력받아 결과를 출력합니다.

```python
if __name__ == "__main__":
    try:
        BASE = int(input("Enter Base : ").strip())
        POWER = int(input("Enter Power : ").strip())
        MODULO = int(input("Enter Modulo : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    print(bin_exp_mod(BASE, POWER, MODULO))
```

**실행 예시:**
($3^4 = 81$, $81 \pmod 5 = 1$)
