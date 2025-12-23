# Double Factorial (Iterative) 알고리즘

이 문서는 `double_factorial_iterative.py` 파일에 구현된 **이중 팩토리얼(Double Factorial)** 계산 알고리즘(반복적 방법)에 대한 설명입니다.

## 개요

**이중 팩토리얼** $n!!$은 $n$과 기우성(홀수/짝수)이 같은 $n$ 이하의 모든 양의 정수의 곱을 의미합니다.

- $n$이 짝수일 때: $n!! = n \times (n-2) \times \cdots \times 2$
- $n$이 홀수일 때: $n!! = n \times (n-2) \times \cdots \times 1$
- $0!! = 1$로 정의됩니다.

## 함수 설명

### `double_factorial(num: int) -> int`

주어진 정수 `num`의 이중 팩토리얼 값을 반복문(iteration)을 사용하여 계산합니다.

#### 매개변수 (Parameters)

- `num` (`int`): 이중 팩토리얼을 계산할 정수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력값 `num`이 정수가 아닌 경우 "double_factorial() only accepts integral values" 에러가 발생합니다.
- **ValueError**: 입력값 `num`이 음수인 경우 "double_factorial() not defined for negative values" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

1. 입력값의 타입과 음수 여부를 검사합니다.
2. 결과값 변수 `value`를 1로 초기화합니다.
3. `num`부터 0보다 클 때까지 2씩 감소시키며 반복합니다 (`range(num, 0, -2)`).
4. 반복마다 현재 숫자 `i`를 `value`에 곱합니다.
5. 최종 계산된 `value`를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
