# Fermat's Little Theorem (페르마의 소정리)

이 문서는 `fermat_little_theorem.py` 파일에 구현된 **페르마의 소정리(Fermat's Little Theorem)**를 이용한 모듈러 나눗셈 예제에 대한 설명입니다.

## 개요

**페르마의 소정리**에 따르면, $p$가 소수이고 $b$가 $p$의 배수가 아닐 때 다음이 성립합니다.

$$ b^{p-1} \equiv 1 \pmod p $$

양변을 $b$로 나누면 다음과 같이 모듈러 역원(Modular Inverse)을 구할 수 있습니다.

$$ b^{p-2} \equiv b^{-1} \pmod p $$

따라서 모듈러 연산에서 나눗셈 $(a / b) \pmod p$는 곱셈 $(a \times b^{p-2}) \pmod p$로 변환하여 계산할 수 있습니다.

## 함수 설명

### `binary_exponentiation(a, n, mod)`

모듈러 거듭제곱 $(a^n) \pmod{mod}$을 $O(\log n)$ 시간 복잡도로 계산합니다.

#### 매개변수 (Parameters)

- `a`: 밑 (Base)
- `n`: 지수 (Exponent)
- `mod`: 모듈러 (Modulo)

#### 알고리즘 (Algorithm)

재귀적인 분할 정복 방식을 사용합니다.

1. $n=0$이면 1을 반환합니다.
2. $n$이 홀수이면 $a \times a^{n-1}$ 형태로 계산합니다.
3. $n$이 짝수이면 $(a^{n/2})^2$ 형태로 계산합니다.

## 실행 예시

파일을 실행하면 $p=701, a=10^9, b=10$인 경우에 대해 페르마의 소정리가 성립하는지 확인합니다.

```python
# p는 소수
p = 701
a = 1000000000
b = 10

# (a / b) % p 와 (a * b^(p-2)) % p 가 같은지 확인
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p)
```
