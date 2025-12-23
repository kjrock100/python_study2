# Gamma Recursive (감마 함수 - 재귀) 알고리즘

이 문서는 `gamma_recursive.py` 파일에 구현된 **감마 함수(Gamma Function)** 계산 알고리즘(재귀적 방법)에 대한 설명입니다.

## 개요

**감마 함수** $\Gamma(z)$는 팩토리얼 함수를 복소수 평면으로 확장한 특수 함수입니다. 양의 정수 $n$에 대해 $\Gamma(n) = (n-1)!$이 성립합니다.
이 구현은 재귀 호출을 사용하여 정수와 반정수(half-integer, 예: 0.5, 1.5)에 대한 감마 함수 값을 계산합니다.

## 함수 설명

### `gamma(num: float) -> float`

주어진 숫자 `num`의 감마 함수 값을 재귀적으로 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `num` (`float`): 감마 함수 값을 계산할 양의 정수 또는 반정수입니다.

#### 예외 처리 (Error Handling)

1. **ValueError**: `num`이 0 이하인 경우 "math domain error" 발생.
2. **OverflowError**: `num`이 171.5보다 큰 경우 "math range error" 발생 (파이썬의 부동소수점 표현 한계 초과).
3. **NotImplementedError**: `num`이 정수나 반정수가 아닌 경우 (예: 1.1) 발생.

#### 알고리즘 (Algorithm)

재귀적 성질 $\Gamma(x) = (x-1)\Gamma(x-1)$을 이용합니다.

1. **유효성 검사**: 입력값이 양수인지, 범위 내에 있는지, 정수 또는 반정수인지 확인합니다.
2. **기저 사례 (Base Cases)**:
   - `num == 0.5`: $\sqrt{\pi}$를 반환합니다. ($\Gamma(1/2) = \sqrt{\pi}$)
   - `num == 1`: 1.0을 반환합니다. ($\Gamma(1) = 0! = 1$)
3. **재귀 단계 (Recursive Step)**:
   - `(num - 1) * gamma(num - 1)`을 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest`를 수행한 후, 사용자 입력을 받아 감마 함수 값을 계산하는 반복문이 실행됩니다.

```python
if __name__ == "__main__":
    from doctest import testmod

    testmod()
    num = 1.0
    while num:
        num = float(input("Gamma of: "))
        print(f"gamma({num}) = {gamma(num)}")
        print("\nEnter 0 to exit...")
```
