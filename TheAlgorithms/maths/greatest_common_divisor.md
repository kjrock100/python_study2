# Greatest Common Divisor (최대공약수) 알고리즘

이 문서는 `greatest_common_divisor.py` 파일에 구현된 **최대공약수(GCD)** 계산 알고리즘에 대한 설명입니다.

## 개요

**최대공약수(GCD)**는 두 개 이상의 정수의 공통 약수 중에서 가장 큰 양의 정수를 의미합니다. 유클리드 호제법(Euclidean algorithm)은 두 수의 최대공약수를 구하는 효율적인 방법입니다.

## 함수 설명

### `greatest_common_divisor(a: int, b: int) -> int`

재귀 호출(Recursion)을 사용하여 두 정수의 최대공약수를 계산합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 첫 번째 정수
- `b` (`int`): 두 번째 정수

#### 알고리즘 (Algorithm)

1. `a`가 0이면 `b`의 절대값을 반환합니다.
2. 그렇지 않으면 `greatest_common_divisor(b % a, a)`를 재귀적으로 호출합니다.
   - 이는 일반적인 `gcd(a, b)` 구현에서 `b`가 0이 될 때까지 `gcd(b, a % b)`를 호출하는 것과 순서가 약간 다르지만, 원리는 동일합니다.

### `gcd_by_iterative(x: int, y: int) -> int`

반복문(Iteration)을 사용하여 두 정수의 최대공약수를 계산합니다. 재귀 호출에 의한 스택 오버플로우 위험이 없으며 메모리 효율적입니다.

#### 매개변수 (Parameters)

- `x` (`int`): 첫 번째 정수
- `y` (`int`): 두 번째 정수

#### 알고리즘 (Algorithm)

1. `y`가 0이 될 때까지 다음을 반복합니다:
   - `x`와 `y`를 교체하되, 새로운 `y`는 `x % y` (나머지)가 됩니다. (`x, y = y, x % y`)
2. `y`가 0이 되면 `x`의 절대값을 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 쉼표로 구분된 두 정수를 입력받아 결과를 출력합니다.

```python
if __name__ == "__main__":
    main()
# 입력 예시: 24, 40
# 출력:
# greatest_common_divisor(24, 40) = 8
# By iterative gcd(24, 40) = 8
```
