# Binomial Distribution (이항 분포) 알고리즘

이 문서는 `binomial_distribution.py` 파일에 구현된 **이항 분포(Binomial Distribution)** 확률 계산 알고리즘에 대한 설명입니다.

## 개요

**이항 분포**는 연속된 $n$번의 독립적 시행에서 각 시행이 확률 $p$를 가질 때, $k$번 성공할 확률을 나타내는 이산 확률 분포입니다.

공식은 다음과 같습니다:
$$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} $$
여기서 $\binom{n}{k}$는 이항 계수(Binomial Coefficient)로, $\frac{n!}{k!(n-k)!}$입니다.

## 함수 설명

### `binomial_distribution(successes: int, trials: int, prob: float) -> float`

주어진 시행 횟수와 성공 확률에 대해, 특정 횟수만큼 성공할 확률을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `successes` (`int`): 성공 횟수 ($k$)
- `trials` (`int`): 전체 시행 횟수 ($n$)
- `prob` (`float`): 각 시행에서의 성공 확률 ($p$)

#### 예외 처리 (Error Handling)

다음의 경우 `ValueError`가 발생합니다:

1. 성공 횟수가 시행 횟수보다 큰 경우 (`successes > trials`)
2. 시행 횟수나 성공 횟수가 음수인 경우
3. 시행 횟수나 성공 횟수가 정수가 아닌 경우
4. 확률 `prob`가 0과 1 사이가 아닌 경우 ($0 < p < 1$)

#### 알고리즘 (Algorithm)

1. 입력값의 유효성을 검사합니다.
2. 확률 부분을 계산합니다: $p^k \times (1-p)^{n-k}$
3. `math.factorial`을 사용하여 이항 계수를 계산합니다: $\frac{n!}{k!(n-k)!}$
4. 확률 부분과 이항 계수를 곱하여 최종 확률을 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 테스트 케이스를 검증하고, 예제 값을 사용하여 결과를 출력합니다.

```python
if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trails")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
```
