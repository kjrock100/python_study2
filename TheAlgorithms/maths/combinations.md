# Combinations (조합) 알고리즘

이 문서는 `combinations.py` 파일에 구현된 **조합(Combinations)** 계산 알고리즘에 대한 설명입니다.

## 개요

**조합**은 서로 다른 $n$개의 원소 중에서 순서에 상관없이 $k$개를 선택하는 경우의 수를 의미합니다. 수학적으로 $\binom{n}{k}$ 또는 $_nC_k$로 표기합니다.

공식은 다음과 같습니다:
$$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $$

## 함수 설명

### `combinations(n: int, k: int) -> int`

주어진 $n$과 $k$에 대해 조합의 수 $\binom{n}{k}$를 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 전체 원소의 개수입니다. ($n \ge k$)
- `k` (`int`): 선택할 원소의 개수입니다. ($k \ge 0$)

#### 예외 처리 (Error Handling)

- **ValueError**: `n < k`이거나 `k < 0`인 경우 "Please enter positive integers for n and k where n >= k" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력값 `n`과 `k`의 유효성을 검사합니다.
2. `math.factorial` 함수를 사용하여 팩토리얼을 계산합니다.
3. 조합 공식 $\frac{n!}{k!(n-k)!}$을 적용하여 결과를 계산하고 정수형으로 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 다음 예제들에 대한 계산 결과를 출력합니다.

1. 52장의 카드 덱에서 5장의 카드를 뽑는 경우의 수
2. 40명의 학생을 4명씩 그룹으로 나누는 경우의 수
3. 10개의 F1 팀 중 상위 3팀이 선정되는 경우의 수

```python
print(combinations(52, 5))  # 2598960
print(combinations(40, 4))  # 91390
print(combinations(10, 3))  # 120
```
