# Factorial (Recursive) 알고리즘

이 문서는 `factorial_recursive.py` 파일에 구현된 **팩토리얼(Factorial)** 계산 알고리즘(재귀적 방법)에 대한 설명입니다.

## 개요

**팩토리얼** $n!$은 1부터 $n$까지의 모든 양의 정수의 곱을 의미합니다. $0! = 1$로 정의됩니다.
$$ n! = n \times (n-1) \times \cdots \times 2 \times 1 $$

이 구현은 **재귀(Recursion)**를 사용하여 계산합니다.

## 함수 설명

### `factorial(n: int) -> int`

주어진 정수 `n`의 팩토리얼 값을 재귀 호출을 사용하여 계산합니다.

#### 매개변수 (Parameters)

- `n` (`int`): 팩토리얼을 계산할 0 이상의 정수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력값 `n`이 정수가 아닌 경우 "factorial() only accepts integral values" 에러가 발생합니다.
- **ValueError**: 입력값 `n`이 음수인 경우 "factorial() not defined for negative values" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

1. 입력값의 타입과 음수 여부를 검사합니다.
2. **기저 사례 (Base Case)**: `n`이 0 또는 1이면 1을 반환합니다.
3. **재귀 단계 (Recursive Step)**: `n`이 1보다 크면 `n * factorial(n - 1)`을 호출하여 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
