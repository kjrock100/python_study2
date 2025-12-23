# Largest of Very Large Numbers (매우 큰 수의 대소 비교) 알고리즘

이 문서는 `largest_of_very_large_numbers.py` 파일에 구현된 **매우 큰 수의 대소 비교** 알고리즘에 대한 설명입니다.

## 개요

$x^y$ 형태의 두 수가 주어졌을 때, $x$와 $y$가 매우 크면 직접 계산하여 비교하는 것이 불가능하거나 비효율적입니다 (오버플로우 발생). 이 알고리즘은 로그(Logarithm)의 성질을 이용하여 직접 계산하지 않고도 두 수의 크기를 비교합니다.

수학적 원리는 다음과 같습니다. 로그 함수는 단조 증가 함수이므로 대소 관계가 유지됩니다.
$$ x^y > a^b \iff \log(x^y) > \log(a^b) \iff y \log(x) > b \log(a) $$

## 함수 설명

### `res(x, y)`

$x^y$의 크기를 비교하기 위한 대리 값($y \log_{10}(x)$)을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `x` (`int`): 밑 (Base)
- `y` (`int`): 지수 (Exponent)

#### 알고리즘 (Algorithm)

1. `x`와 `y`가 모두 0이 아닌 경우:
   - `math.log10(x)`를 사용하여 $y \times \log_{10}(x)$를 계산하고 반환합니다.
2. `x`가 0인 경우:
   - 0을 반환합니다. ($0^y = 0$)
3. `y`가 0인 경우:
   - 1을 반환합니다. ($x^0 = 1$)

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 두 개의 (밑, 지수) 쌍을 입력받아 더 큰 수를 출력합니다.

```python
# 실행 시 입력 예시
# Enter the base and the power separated by a comma: 10, 100
# Enter the base and the power separated by a comma: 9, 101
```

**출력 결과:**

```
Largest number is 10 ^ 100
```

**설명**: $100 \log_{10}(10) = 100$, $101 \log_{10}(9) \approx 101 \times 0.954 = 96.35$ 이므로 $10^{100}$이 더 큽니다.
