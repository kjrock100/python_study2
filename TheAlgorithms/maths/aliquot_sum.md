# Aliquot Sum (알리코 합) 알고리즘

이 문서는 `aliquot_sum.py` 파일에 구현된 **알리코 합(Aliquot Sum)** 계산 알고리즘에 대한 설명입니다.

## 개요

**알리코 합(Aliquot Sum)**은 어떤 자연수 `n`의 진약수(proper divisor, 자기 자신을 제외한 약수)들의 합을 의미합니다.
예를 들어, 15의 약수는 1, 3, 5, 15이고, 진약수는 1, 3, 5이므로 알리코 합은 1 + 3 + 5 = 9가 됩니다.

## 함수 설명

### `aliquot_sum(input_num: int) -> int`

주어진 정수의 알리코 합을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `input_num` (`int`): 알리코 합을 구할 양의 정수입니다.

#### 예외 처리 (Error Handling)

1. **ValueError**: 입력값 `input_num`이 정수(`int`)가 아닌 경우 "Input must be an integer" 메시지와 함께 에러를 발생시킵니다.
2. **ValueError**: 입력값 `input_num`이 양수가 아닌 경우(0 이하) "Input must be positive" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력값의 타입과 범위를 검증합니다.
2. 1부터 `input_num // 2`까지의 숫자를 순회합니다. (자기 자신을 제외한 약수는 절반을 넘을 수 없기 때문입니다.)
3. `input_num`을 나누어 떨어뜨리는 수(약수)들을 모두 더합니다.
4. 합계 결과를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
