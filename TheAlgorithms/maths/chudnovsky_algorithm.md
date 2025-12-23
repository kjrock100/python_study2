# Chudnovsky Algorithm (추드노프스키 알고리즘)

이 문서는 `chudnovsky_algorithm.py` 파일에 구현된 **추드노프스키 알고리즘(Chudnovsky Algorithm)**에 대한 설명입니다.

## 개요

**추드노프스키 알고리즘**은 파이($\pi$)의 자릿수를 매우 빠르게 계산하는 방법 중 하나입니다. 라마누잔의 공식을 기반으로 하며, 한 번의 반복(iteration)으로 약 14자리의 정확한 파이 값을 얻을 수 있어 효율성이 매우 높습니다.

## 함수 설명

### `pi(precision: int) -> str`

주어진 정밀도(`precision`)까지 파이($\pi$) 값을 계산하여 문자열로 반환합니다.

#### 매개변수 (Parameters)

- `precision` (`int`): 계산할 파이의 자릿수입니다. 양의 정수여야 합니다.

#### 예외 처리 (Error Handling)

- **TypeError**: `precision`이 정수가 아닌 경우 "Undefined for non-integers" 에러가 발생합니다.
- **ValueError**: `precision`이 1보다 작은 경우 "Undefined for non-natural numbers" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

이 알고리즘은 파이썬의 `decimal` 모듈을 사용하여 고정밀 연산을 수행합니다.

1. **초기 설정**:

   - `getcontext().prec`를 사용하여 연산 정밀도를 설정합니다.
   - 반복 횟수 `num_iterations`를 계산합니다. (반복당 약 14자리를 얻으므로 `ceil(precision / 14)`로 설정)
   - 상수항 `constant_term`을 계산합니다 ($426880 \times \sqrt{10005}$).

2. **반복 계산 (Iterative Calculation)**:

   - 수열의 각 항을 반복적으로 계산하여 `partial_sum`에 더합니다.
   - **Multinomial Term**: $\frac{(6k)!}{(3k)! (k!)^3}$
   - **Linear Term ($L_k$)**: $L_{k+1} = L_k + 545140134$ (초기값: 13591409)
   - **Exponential Term ($X_k$)**: $X_{k+1} = X_k \times -262537412640768000$ (초기값: 1)

   각 반복(`k`)마다 다음 값을 누적합니다:
   $$ \text{partial_sum} += \frac{\text{multinomial_term} \times \text{linear_term}}{\text{exponential_term}} $$

3. **결과 반환**:
   - 최종적으로 `constant_term / partial_sum`을 계산하여 파이 값을 구합니다.
   - 문자열로 변환한 뒤 마지막 문자를 제외하고 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`), 파이의 첫 50자리를 계산하여 출력합니다.

```python
if __name__ == "__main__":
    n = 50
    print(f"The first {n} digits of pi is: {pi(n)}")
```

**출력 예시:**
`The first 50 digits of pi is: 3.1415926535897932384626433832795028841971693993751`
