# Euclidean GCD (유클리드 호제법) 알고리즘

이 문서는 `euclidean_gcd.py` 파일에 구현된 **유클리드 호제법(Euclidean Algorithm)**을 이용한 최대공약수(GCD) 계산 알고리즘에 대한 설명입니다.

## 개요

**유클리드 호제법**은 2개의 자연수 또는 정식(整式)의 최대공약수를 구하는 알고리즘의 하나입니다. 두 수가 서로 상대방 수를 나누어서 원하는 수를 얻는 알고리즘입니다.

## 함수 설명

### `euclidean_gcd(a: int, b: int) -> int`

반복문(Iteration)을 사용하여 두 정수의 최대공약수를 계산합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 첫 번째 정수
- `b` (`int`): 두 번째 정수

#### 알고리즘 (Algorithm)

1. `b`가 0이 될 때까지 다음을 반복합니다:
   - `a`를 `b`로 나눈 나머지를 구합니다.
   - `a`에는 이전의 `b` 값을, `b`에는 계산된 나머지를 대입합니다. (`a, b = b, a % b`)
2. `b`가 0이 되면, `a`가 최대공약수이므로 반환합니다.

### `euclidean_gcd_recursive(a: int, b: int) -> int`

재귀 호출(Recursion)을 사용하여 두 정수의 최대공약수를 계산합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 첫 번째 정수
- `b` (`int`): 두 번째 정수

#### 알고리즘 (Algorithm)

1. **기저 사례 (Base Case)**: `b`가 0이면 `a`를 반환합니다.
2. **재귀 단계 (Recursive Step)**: `b`가 0이 아니면 `euclidean_gcd_recursive(b, a % b)`를 호출합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 몇 가지 예제에 대한 GCD 계산 결과를 출력합니다.

```python
if __name__ == "__main__":
    main()
```
