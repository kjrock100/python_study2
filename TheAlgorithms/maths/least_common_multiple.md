# Least Common Multiple (최소공배수) 알고리즘

이 문서는 `least_common_multiple.py` 파일에 구현된 **최소공배수(LCM)** 계산 알고리즘에 대한 설명입니다.

## 개요

**최소공배수(LCM)**는 두 정수의 공통된 배수 중에서 가장 작은 양의 정수를 의미합니다. 이 파일은 반복문을 이용한 느린 방법과 최대공약수(GCD)를 이용한 빠른 방법 두 가지를 제공하고 비교합니다.

## 함수 설명

### `least_common_multiple_slow(first_num: int, second_num: int) -> int`

반복문을 사용하여 최소공배수를 구하는 단순한(Brute-force) 방식입니다.

#### 매개변수 (Parameters)

- `first_num` (`int`): 첫 번째 정수
- `second_num` (`int`): 두 번째 정수

#### 알고리즘 (Algorithm)

1. 두 수 중 더 큰 수를 초기값(`common_mult`)으로 설정합니다.
2. `common_mult`가 두 수로 모두 나누어 떨어질 때까지, 더 큰 수만큼 계속 더해나갑니다.
3. 조건을 만족하는 `common_mult`를 반환합니다.

이 방식은 두 수의 최소공배수가 클 경우 반복 횟수가 많아져 비효율적입니다.

### `greatest_common_divisor(a: int, b: int) -> int`

유클리드 호제법을 사용하여 최대공약수(GCD)를 구하는 헬퍼 함수입니다. 빠른 LCM 계산을 위해 사용됩니다.

### `least_common_multiple_fast(first_num: int, second_num: int) -> int`

최대공약수(GCD)를 이용하여 최소공배수를 효율적으로 계산합니다.

#### 알고리즘 (Algorithm)

다음 공식을 사용합니다:
$$ \text{lcm}(a, b) = \frac{|a \cdot b|}{\gcd(a, b)} $$
코드에서는 중간 계산 결과가 너무 커지는 것을 방지하기 위해 `first_num // gcd(...) * second_num` 순서로 연산합니다.

## 벤치마크 및 테스트

파일을 직접 실행하면(`if __name__ == "__main__":`), 두 함수의 성능을 비교하는 벤치마크와 단위 테스트가 실행됩니다.

### `benchmark()`

`timeit` 모듈을 사용하여 `slow` 버전과 `fast` 버전의 실행 시간을 측정하고 출력합니다.

### `TestLeastCommonMultiple`

`unittest` 모듈을 사용하여 여러 테스트 케이스에 대해 두 함수의 결과가 예상값과 일치하는지 검증합니다.

```python
if __name__ == "__main__":
    benchmark()
    unittest.main()
```
