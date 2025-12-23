# Average (Mean) 알고리즘

이 문서는 `average_mean.py` 파일에 구현된 **산술 평균(Arithmetic Mean)** 계산 알고리즘에 대한 설명입니다.

## 개요

**산술 평균**은 데이터 집합의 모든 값을 더한 후, 값의 개수로 나눈 값입니다. 통계학에서 가장 일반적으로 사용되는 중심 경향성 측정 방법입니다.

## 함수 설명

### `mean(nums: list) -> float`

주어진 숫자 리스트의 산술 평균을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `nums` (`list`): 평균을 계산할 숫자(정수 또는 실수)들이 담긴 리스트입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `nums`가 비어있을 경우 "List is empty" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력 리스트가 비어있는지 확인합니다.
2. `sum()` 함수를 사용하여 리스트에 있는 모든 숫자의 합을 구합니다.
3. `len()` 함수를 사용하여 리스트의 요소 개수를 구합니다.
4. 계산된 합을 요소의 개수로 나누어 평균을 구하고 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
