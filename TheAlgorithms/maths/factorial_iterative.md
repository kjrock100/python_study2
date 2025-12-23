# Factorial (Iterative) 알고리즘

이 문서는 `factorial_iterative.py` 파일에 구현된 **팩토리얼(Factorial)** 계산 알고리즘(반복적 방법)에 대한 설명입니다.

## 개요

**팩토리얼** $n!$은 1부터 $n$까지의 모든 양의 정수의 곱을 의미합니다. $0! = 1$로 정의됩니다.
$$ n! = n \times (n-1) \times \cdots \times 2 \times 1 $$

## 함수 설명

### `factorial(number: int) -> int`

주어진 정수 `number`의 팩토리얼 값을 반복문(iteration)을 사용하여 계산합니다.

#### 매개변수 (Parameters)

- `number` (`int`): 팩토리얼을 계산할 0 이상의 정수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력값 `number`가 정수가 아닌 경우 "factorial() only accepts integral values" 에러가 발생합니다.
- **ValueError**: 입력값 `number`가 음수인 경우 "factorial() not defined for negative values" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

1. 입력값이 정수인지, 음수인지 확인하여 유효하지 않으면 에러를 발생시킵니다.
2. 결과값 변수 `value`를 1로 초기화합니다.
3. 1부터 `number`까지 반복하며 `value`에 현재 숫자 `i`를 곱합니다.
4. 최종 계산된 `value`를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증하고, 사용자 입력을 받아 팩토리얼을 계산합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    n = int(input("Enter a positive integer: ").strip() or 0)
    print(f"factorial{n} is {factorial(n)}")
```
