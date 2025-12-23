# Karatsuba Algorithm (카라추바 알고리즘)

이 문서는 `karatsuba.py` 파일에 구현된 **카라추바 알고리즘(Karatsuba Algorithm)**에 대한 설명입니다.

## 개요

**카라추바 알고리즘**은 두 개의 큰 정수를 곱하는 빠른 곱셈 알고리즘입니다. 분할 정복(Divide and Conquer) 방법을 사용하여 일반적인 $O(n^2)$ 곱셈보다 빠른 $O(n^{\log_2 3}) \approx O(n^{1.585})$의 시간 복잡도를 가집니다.

## 함수 설명

### `karatsuba(a, b)`

두 정수 `a`와 `b`의 곱을 카라추바 알고리즘을 사용하여 계산합니다.

#### 매개변수 (Parameters)

- `a` (`int`): 곱할 첫 번째 정수.
- `b` (`int`): 곱할 두 번째 정수.

#### 알고리즘 (Algorithm)

1. **기저 사례 (Base Case)**: `a` 또는 `b`가 한 자리 숫자일 경우(코드에서는 `len(str(n)) == 1`), 일반 곱셈(`a * b`)을 수행하여 반환합니다.
2. **분할 (Split)**:
   - 두 수 중 더 긴 자릿수를 기준으로 절반(`m2`)을 구합니다.
   - `divmod`를 사용하여 각 수를 두 부분으로 나눕니다.
     - $a = a_1 \times 10^{m2} + a_2$
     - $b = b_1 \times 10^{m2} + b_2$
3. **재귀 호출 (Recursive Step)**:
   - $z = a_1 \times b_1$ (`karatsuba(a1, b1)`)
   - $x = a_2 \times b_2$ (`karatsuba(a2, b2)`)
   - $y = (a_1 + a_2) \times (b_1 + b_2)$ (`karatsuba(a1 + a2, b1 + b2)`)
4. **결합 (Combine)**:
   - 다음 공식을 사용하여 최종 결과를 계산합니다.
     $$ \text{Result} = z \times 10^{2 \cdot m2} + (y - z - x) \times 10^{m2} + x $$

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 예제 숫자에 대한 곱셈 결과를 출력합니다.

```python
if __name__ == "__main__":
    main()
```

**출력 결과:**

```
363200407
```

(15463 \* 23489 = 363200407)
