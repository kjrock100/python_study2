# Binomial Coefficient (이항 계수) 알고리즘

이 문서는 `binomial_coefficient.py` 파일에 구현된 **이항 계수(Binomial Coefficient)** 계산 알고리즘에 대한 설명입니다.

## 개요

**이항 계수** $\binom{n}{r}$은 $n$개의 서로 다른 원소에서 $r$개를 선택하는 경우의 수를 의미합니다. 이 알고리즘은 **파스칼의 삼각형(Pascal's Triangle)** 원리를 이용하여 이항 계수를 효율적으로 계산합니다.

## 함수 설명

### `binomial_coefficient(n, r)`

파스칼의 삼각형 성질을 이용하여 $\binom{n}{r}$ 값을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 전체 원소의 개수 ($n \ge r$)
- `r` (`int`): 선택할 원소의 개수 ($r \ge 0$)

#### 알고리즘 (Algorithm)

이 구현은 동적 계획법(Dynamic Programming)을 사용하여 공간 복잡도를 $O(r)$로 최적화했습니다.

1. 크기가 `r + 1`인 리스트 `C`를 0으로 초기화합니다.
2. $\binom{n}{0} = 1$이므로 `C[0]`을 1로 설정합니다.
3. 1부터 `n`까지 반복하며 다음을 수행합니다:
   - `j`를 `min(i, r)`부터 1까지 감소시키며 반복합니다.
   - `C[j] = C[j] + C[j-1]`을 수행합니다.
   - 이는 파스칼의 항등식 $\binom{n}{k} = \binom{n-1}{k} + \binom{n-1}{k-1}$을 이용한 것입니다.
4. 최종적으로 `C[r]`을 반환합니다.

## 실행 예시

파일을 직접 실행하면, $n=10, r=5$일 때의 이항 계수를 계산하여 출력합니다.

```python
print(binomial_coefficient(n=10, r=5))
# 출력: 252
```
