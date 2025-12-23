# Hardy-Ramanujan Theorem Algorithm

이 문서는 `hardy_ramanujanalgo.py` 파일에 구현된 **하디-라마누잔 정리(Hardy-Ramanujan Theorem)**와 관련된 알고리즘에 대한 설명입니다.

## 개요

**하디-라마누잔 정리**는 자연수 $n$의 서로 다른 소인수의 개수 $\omega(n)$가 대략 $\ln(\ln(n))$이 된다는 정리입니다.
이 코드는 주어진 수 $n$에 대해 실제 **서로 다른 소인수의 개수(Distinct Prime Factors Count)**를 계산하는 함수를 구현하고, 이를 $\ln(\ln(n))$ 값과 비교하는 예제를 포함하고 있습니다.

## 함수 설명

### `exactPrimeFactorCount(n)`

주어진 정수 `n`의 서로 다른 소인수의 개수를 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 소인수의 개수를 구할 양의 정수입니다.

#### 알고리즘 (Algorithm)

1. 소인수 개수를 저장할 변수 `count`를 0으로 초기화합니다.
2. **2의 배수 처리**: `n`이 2로 나누어 떨어지면 `count`를 1 증가시키고, `n`이 2로 나누어 떨어지지 않을 때까지 계속 2로 나눕니다.
3. **홀수 소인수 처리**: 3부터 $\sqrt{n}$까지 2씩 증가시키며(`i`) 반복합니다.
   - `n`이 `i`로 나누어 떨어지면 `count`를 1 증가시킵니다.
   - `n`이 `i`로 나누어 떨어지지 않을 때까지 계속 `i`로 나눕니다. (중복 소인수 제거)
4. **남은 소수 처리**: 반복문 종료 후 `n`이 2보다 크다면, 남은 `n`은 소수이므로 `count`를 1 증가시킵니다.
5. 최종 `count`를 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 숫자 `51242183`에 대해 서로 다른 소인수의 개수와 $\ln(\ln(n))$ 값을 계산하여 출력합니다.

```python
if __name__ == "__main__":
    n = 51242183
    print(f"The number of distinct prime factors is/are {exactPrimeFactorCount(n)}")
    print(f"The value of log(log(n)) is {math.log(math.log(n)):.4f}")
```

**출력 결과:**

```
The number of distinct prime factors is/are 3
The value of log(log(n)) is 2.8765
```
