# Extended Euclidean Algorithm (확장 유클리드 알고리즘)

이 문서는 `extended_euclidean_algorithm.py` 파일에 구현된 **확장 유클리드 알고리즘(Extended Euclidean Algorithm)**에 대한 설명입니다.

## 개요

**확장 유클리드 알고리즘**은 두 정수 $a, b$의 최대공약수(GCD)를 구할 뿐만 아니라, 베주 항등식(Bézout's identity)을 만족하는 정수해 $x, y$를 찾는 알고리즘입니다.

$$ ax + by = \gcd(a, b) $$

이 알고리즘은 모듈러 연산의 역원(Modular Inverse)을 구하거나 RSA 암호화 등에서 중요하게 사용됩니다.

## 함수 설명

### `extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int]`

주어진 두 정수 `a`와 `b`에 대해 $ax + by = \gcd(a, b)$를 만족하는 계수 $x, y$를 찾아 튜플 형태로 반환합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 첫 번째 정수
- `b` (`int`): 두 번째 정수

#### 반환값 (Returns)

- `tuple[int, int]`: 베주 항등식을 만족하는 계수 `(x, y)`

#### 알고리즘 (Algorithm)

이 구현은 재귀가 아닌 반복문(Iteration)을 사용하여 유클리드 호제법의 과정을 역추적하는 방식과 유사하게 계수를 갱신합니다.

1. **초기화**:

   - 나머지: `old_remainder = a`, `remainder = b`
   - $a$의 계수: `old_coeff_a = 1`, `coeff_a = 0`
   - $b$의 계수: `old_coeff_b = 0`, `coeff_b = 1`

2. **반복**: `remainder`가 0이 될 때까지 다음을 수행합니다.

   - 몫(`quotient`)을 계산합니다: `old_remainder // remainder`
   - 나머지를 갱신합니다: `old_remainder - quotient * remainder`
   - 계수들을 갱신합니다: `old_coeff - quotient * coeff`

3. **부호 보정**: 입력값 `a` 또는 `b`가 음수인 경우, 계산된 계수의 부호를 적절히 조정합니다.

4. **결과 반환**: 최종적으로 갱신된 `old_coeff_a`와 `old_coeff_b`를 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 커맨드 라인 인자(`sys.argv`)로 두 정수를 받아 결과를 출력합니다.

```bash
python extended_euclidean_algorithm.py 240 46
```

**출력 결과:** `(-9, 47)`
($240 \times (-9) + 46 \times 47 = -2160 + 2162 = 2 = \gcd(240, 46)$)
