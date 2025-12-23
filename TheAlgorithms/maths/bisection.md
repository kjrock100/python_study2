# Bisection Method (이분법) 알고리즘

이 문서는 `bisection.py` 파일에 구현된 **이분법(Bisection Method)** 알고리즘에 대한 설명입니다.

## 개요

**이분법**은 연속 함수 $f(x)$에 대해 $f(a)$와 $f(b)$의 부호가 서로 다른 구간 $[a, b]$가 주어졌을 때, 그 구간을 반복적으로 반으로 나누어 근(root)을 찾는 수치해석 방법입니다. 중간값 정리(Bolzano's theorem)를 기반으로 합니다.

## 함수 설명

### `equation(x: float) -> float`

근을 찾고자 하는 대상 함수 $f(x)$를 정의합니다.
이 코드에서는 $f(x) = 10 - x^2$로 정의되어 있습니다.

### `bisection(a: float, b: float) -> float`

주어진 구간 $[a, b]$에서 `equation` 함수의 근을 찾아 반환합니다.

#### 매개변수 (Parameters)

- `a` (`float`): 구간의 시작점입니다.
- `b` (`float`): 구간의 끝점입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: `equation(a) * equation(b) >= 0`인 경우 "Wrong space!" 에러가 발생합니다. 즉, 두 지점의 함수값 부호가 같으면 구간 내에 근이 존재한다는 보장이 없으므로 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 구간의 양 끝점 $a, b$에서의 함수값 부호가 서로 다른지 확인합니다.
2. 구간의 길이 $(b - a)$가 허용 오차(여기서는 0.01)보다 작아질 때까지 다음을 반복합니다:
   - 중간 지점 $c = \frac{a + b}{2}$를 계산합니다.
   - 만약 $f(c) == 0$이면 정확한 근을 찾은 것이므로 반복을 중단합니다.
   - $f(c)$와 $f(a)$의 부호가 다르면 ($f(c) \times f(a) < 0$), 근은 $[a, c]$ 구간에 존재하므로 $b$를 $c$로 업데이트합니다.
   - 그렇지 않으면 근은 $[c, b]$ 구간에 존재하므로 $a$를 $c$로 업데이트합니다.
3. 최종적으로 계산된 중간 지점 $c$를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 테스트 케이스를 검증하고, 예제 구간에 대한 실행 결과를 출력합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(bisection(-2, 5))
    print(bisection(0, 6))
```
