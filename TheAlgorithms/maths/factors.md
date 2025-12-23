# Factors (약수) 알고리즘

이 문서는 `factors.py` 파일에 구현된 **약수(Factors)** 구하기 알고리즘에 대한 설명입니다.

## 개요

**약수**는 어떤 정수를 나누어 떨어지게 하는 정수를 의미합니다. 예를 들어, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24입니다.

## 함수 설명

### `factors_of_a_number(num: int) -> list`

주어진 정수 `num`의 모든 양의 약수를 찾아 리스트로 반환합니다.

#### 매개변수 (Parameters)

- `num` (`int`): 약수를 구할 정수입니다.

#### 알고리즘 (Algorithm)

1. 1부터 `num`까지의 모든 정수 `i`에 대해 반복합니다.
2. `num`을 `i`로 나누었을 때 나머지가 0인지 확인합니다 (`num % i == 0`).
3. 나머지가 0이면 `i`는 `num`의 약수이므로 리스트에 포함시킵니다.
4. 최종적으로 생성된 리스트를 반환합니다.

_참고_: 입력값이 1 미만인 경우(음수 포함), `range(1, num + 1)`이 비어있게 되므로 빈 리스트를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 숫자를 입력받아 약수를 계산하고 출력합니다.

```python
if __name__ == "__main__":
    num = int(input("Enter a number to find its factors: "))
    factors = factors_of_a_number(num)
    print(f"{num} has {len(factors)} factors: {', '.join(str(f) for f in factors)}")
```
