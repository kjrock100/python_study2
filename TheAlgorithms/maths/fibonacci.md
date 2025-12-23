# Fibonacci Sequence Algorithms

이 문서는 `fibonacci.py` 파일에 구현된 **피보나치 수열(Fibonacci Sequence)** 계산 알고리즘들에 대한 설명입니다.

## 개요

**피보나치 수열**은 각 숫자가 바로 앞의 두 숫자의 합이 되는 수열입니다. 일반적으로 0과 1로 시작합니다.
$$ F*0 = 0, F_1 = 1 $$
$$ F_n = F*{n-1} + F\_{n-2} $$

이 파일은 반복(Iteration), 재귀(Recursion), 메모이제이션(Memoization), 그리고 비네의 공식(Binet's Formula)을 사용한 4가지 구현 방식을 제공하며, 각 방식의 성능을 비교합니다.

## 함수 설명

### `fib_iterative(n: int) -> list[int]`

반복문을 사용하여 0번째부터 n번째까지의 피보나치 수열을 리스트로 반환합니다.

- **알고리즘**: 리스트 `[0, 1]`로 시작하여, 마지막 두 요소의 합을 리스트에 추가하는 과정을 `n-1`번 반복합니다.
- **특징**: 직관적이며 효율적입니다.

### `fib_recursive(n: int) -> list[int]`

재귀 호출을 사용하여 피보나치 수열을 계산합니다.

- **알고리즘**: $F_n$을 구하기 위해 $F_{n-1}$과 $F_{n-2}$를 재귀적으로 호출합니다. 이 함수는 0부터 `n`까지 각 항에 대해 재귀 함수를 별도로 호출하여 리스트를 구성합니다.
- **단점**: 중복 계산이 매우 많아 `n`이 커질수록 실행 시간이 기하급수적으로 증가합니다.

### `fib_memoization(n: int) -> list[int]`

메모이제이션(Memoization) 기법을 적용한 재귀 방식입니다.

- **알고리즘**: 이미 계산된 피보나치 수를 딕셔너리(`cache`)에 저장해 두고, 필요할 때 다시 계산하지 않고 저장된 값을 사용합니다.
- **장점**: 재귀의 간결함을 유지하면서도 반복적 방식만큼 빠릅니다.

### `fib_binet(n: int) -> list[int]`

비네의 공식(Binet's Formula)을 사용하여 근사값을 계산합니다.

- **공식**: $F_n = \frac{\phi^n - (1-\phi)^n}{\sqrt{5}}$, 여기서 $\phi = \frac{1 + \sqrt{5}}{2}$ (황금비)
- **제약 사항**:
  - 부동소수점 연산을 사용하므로 `n`이 커지면(약 71 이상) 정밀도 오차가 발생하여 정확한 정수값을 얻지 못할 수 있습니다.
  - 파이썬의 `float` 타입 한계로 인해 `n >= 1475`일 때 오버플로우가 발생합니다.

### `time_func(func, *args, **kwargs)`

함수의 실행 시간을 측정하여 출력하는 헬퍼 함수입니다.

## 실행 및 벤치마크

파일을 직접 실행하면(`if __name__ == "__main__":`), `n=20`일 때 각 함수의 실행 시간을 측정하여 출력합니다.

```python
if __name__ == "__main__":
    num = 20
    time_func(fib_iterative, num)
    time_func(fib_recursive, num)
    time_func(fib_memoization, num)
    time_func(fib_binet, num)
```

**참고**: `fib_recursive`는 `n`이 커지면 매우 느려지므로, 벤치마크 시 작은 `n` 값을 사용하는 것이 좋습니다.
