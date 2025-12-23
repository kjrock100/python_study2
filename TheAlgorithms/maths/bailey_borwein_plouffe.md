# Bailey-Borwein-Plouffe (BBP) 알고리즘

이 문서는 `bailey_borwein_plouffe.py` 파일에 구현된 **베일리-보웬-플루프(BBP) 공식**을 이용한 파이(π)의 특정 자릿수 계산 알고리즘에 대한 설명입니다.

## 개요

**BBP 공식**은 파이(π)의 16진수 표현에서, 앞선 자릿수들을 계산하지 않고도 n번째 자릿수를 직접 계산할 수 있게 해주는 유명한 자릿수 추출 알고리즘입니다.

이 알고리즘은 다음 공식을 기반으로 합니다:
$$ \pi = \sum\_{k=0}^{\infty} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right) $$

## 함수 설명

### `bailey_borwein_plouffe(digit_position: int, precision: int = 1000) -> str`

BBP 공식을 사용하여 파이(π)의 16진수 표현에서 `digit_position`에 해당하는 자릿수를 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `digit_position` (`int`): 추출하고자 하는 자릿수의 위치입니다 (소수점 바로 다음이 1번째). 양의 정수여야 합니다.
- `precision` (`int`): 계산의 정확도를 높이기 위해 사용되는 추가 항의 개수입니다. 값이 클수록 정확도가 높아지지만 실행 시간이 길어집니다. (기본값: 1000)

#### 예외 처리 (Error Handling)

- **ValueError**: `digit_position`이 양의 정수가 아니거나, `precision`이 음이 아닌 정수가 아닐 경우 발생합니다.

#### 알고리즘 (Algorithm)

1. 입력값의 유효성을 검사합니다.
2. BBP 공식의 각 항($\frac{4}{8k+1}$, $\frac{2}{8k+4}$ 등)에 대해 `_subsum` 헬퍼 함수를 호출하여 합계를 계산합니다.
3. 계산된 합계(`sum_result`)는 $(16^{n-1})\pi$의 근사값이며, 이 값의 소수 부분은 파이의 n번째 16진수 자릿수로 시작합니다.
4. `sum_result % 1`을 통해 소수 부분만 추출합니다.
5. 소수 부분에 16을 곱하여 원하는 자릿수를 정수 부분으로 만듭니다.
6. 이 정수 값을 16진수 문자열로 변환하여 반환합니다.

### `_subsum(digit_pos_to_extract: int, denominator_addend: int, precision: int) -> float`

BBP 공식의 각 시그마(Σ) 부분을 계산하는 내부 헬퍼 함수입니다.

#### 매개변수 (Parameters)

- `digit_pos_to_extract` (`int`): 추출할 자릿수 위치입니다.
- `denominator_addend` (`int`): 분모의 `8k + j`에서 `j`에 해당하는 값 (1, 4, 5, 6)입니다.
- `precision` (`int`): 계산의 정확도를 위한 추가 항의 개수입니다.

#### 알고리즘 (Algorithm)

1. 합계 변수 `sum`을 0.0으로 초기화합니다.
2. `0`부터 `digit_pos_to_extract + precision`까지 반복하며 각 항을 계산하여 `sum`에 더합니다.
3. 각 항의 분자는 $16^{n-1-k}$입니다.
   - `k < n-1`인 경우, 메모리 문제를 피하고 계산 속도를 높이기 위해 모듈러 거듭제곱(`pow(base, exp, mod)`)을 사용하여 계산합니다. 이는 정수 부분에만 영향을 미치고 우리가 원하는 소수 부분에는 영향을 주지 않습니다.
   - `k >= n-1`인 경우, 일반 거듭제곱을 사용합니다.
4. 계산된 합계를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

예시로, `range(1, 11)`에 대해 함수를 실행하면 파이의 소수점 이하 10자리 16진수 표현인 `243f6a8885`를 얻을 수 있습니다.
