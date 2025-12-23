# Euler's Totient Function (오일러 피 함수) 알고리즘

이 문서는 `eulers_totient.py` 파일에 구현된 **오일러 피 함수(Euler's Totient Function)** 계산 알고리즘에 대한 설명입니다.

## 개요

**오일러 피 함수** $\phi(n)$은 $n$ 이하의 양의 정수 중에서 $n$과 서로소(최대공약수가 1)인 수의 개수를 나타내는 함수입니다.

## 함수 설명

### `totient(n: int) -> list`

1부터 `n-1`까지의 정수에 대해 오일러 피 함수 값을 계산하여 리스트로 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 계산할 범위의 상한값입니다. (반환된 리스트는 인덱스 `n`까지 존재하지만, 실제 유효한 계산값은 `n-1`까지입니다.)

#### 반환값 (Returns)

- `list`: 인덱스 `i`에 $\phi(i)$ 값이 저장된 리스트입니다.

#### 알고리즘 (Algorithm)

이 구현은 **선형 체(Linear Sieve)** 알고리즘을 사용하여 $O(n)$ 시간 복잡도로 값을 계산합니다.

1. `is_prime` 리스트를 `True`로 초기화하고, `totients` 리스트를 `i - 1`로 초기화합니다. (소수 $p$에 대해 $\phi(p) = p - 1$이므로)
2. 2부터 `n`까지 순회하며 다음을 수행합니다:
   - 현재 수 `i`가 소수이면 `primes` 리스트에 추가합니다.
   - 현재 발견된 소수들(`primes`)을 순회하며 `i * p`에 대한 값을 계산합니다:
     - `i * p >= n`이면 중단합니다 (범위 초과 방지).
     - **경우 1**: `i`가 `p`로 나누어 떨어지는 경우 ($p$가 `i`의 약수)
       - 공식: $\phi(i \cdot p) = \phi(i) \cdot p$
       - `totients[i * p] = totients[i] * p`
       - 더 이상의 소수는 확인하지 않고 중단합니다 (각 합성수는 최소 소인수에 의해서만 걸러짐).
     - **경우 2**: `i`가 `p`로 나누어 떨어지지 않는 경우 ($i$와 $p$는 서로소)
       - 공식: $\phi(i \cdot p) = \phi(i) \cdot \phi(p) = \phi(i) \cdot (p - 1)$
       - `totients[i * p] = totients[i] * (p - 1)`

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
n = 10
totient_calculation = totient(n)
for i in range(1, n):
    print(f"{i} has {totient_calculation[i]} relative primes.")
```

**출력 결과:**

```
1 has 0 relative primes.
2 has 1 relative primes.
...
9 has 6 relative primes.
```

_참고_: 수학적으로 $\phi(1) = 1$이지만, 이 코드의 구현상 `totients[1]`은 0으로 계산됩니다.
