# Basic Maths (기초 수학) 알고리즘

이 문서는 `basic_maths.py` 파일에 구현된 기초적인 정수론 관련 알고리즘들에 대한 설명입니다.

## 개요

소인수분해, 약수의 개수, 약수의 합, 오일러 피 함수 등 정수론에서 자주 사용되는 기본적인 함수들을 제공합니다.

## 함수 설명

### `prime_factors(n: int) -> list`

주어진 정수 `n`의 소인수(Prime Factors)들을 찾아 리스트로 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 소인수분해할 양의 정수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: `n`이 0 이하인 경우 "Only positive integers have prime factors" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

1. 2로 나누어 떨어지는 동안 2를 리스트에 추가하고 `n`을 나눕니다.
2. 3부터 $\sqrt{n}$까지 2씩 증가시키며(`i`), `n`이 `i`로 나누어 떨어지는 동안 `i`를 리스트에 추가하고 `n`을 나눕니다.
3. 마지막으로 남은 `n`이 2보다 크다면 소수이므로 리스트에 추가합니다.

### `number_of_divisors(n: int) -> int`

주어진 정수 `n`의 약수의 개수를 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 약수의 개수를 구할 양의 정수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: `n`이 0 이하인 경우 "Only positive numbers are accepted" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

소인수분해를 이용하여 약수의 개수를 구합니다. $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$일 때, 약수의 개수는 $(a_1+1)(a_2+1)\cdots(a_k+1)$입니다.

### `sum_of_divisors(n: int) -> int`

주어진 정수 `n`의 모든 약수의 합을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 약수의 합을 구할 양의 정수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: `n`이 0 이하인 경우 "Only positive numbers are accepted" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

소인수분해를 이용하여 약수의 합을 구합니다. 등비수열의 합 공식을 활용합니다.
$n = p_1^{a_1} \cdots p_k^{a_k}$일 때, 약수의 합은 $\prod_{i=1}^{k} \frac{p_i^{a_i+1}-1}{p_i-1}$ 입니다.

### `euler_phi(n: int) -> int`

오일러 피 함수(Euler's Phi Function, $\phi(n)$) 값을 계산합니다. $\phi(n)$은 $n$ 이하의 양의 정수 중 $n$과 서로소인 수의 개수입니다.

#### 매개변수 (Parameters)

- `n` (`int`): 양의 정수입니다.

#### 알고리즘 (Algorithm)

`prime_factors` 함수를 사용하여 소인수를 구한 뒤, 다음 공식을 적용합니다.
$$ \phi(n) = n \prod\_{p|n} \left(1 - \frac{1}{p}\right) $$

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.
