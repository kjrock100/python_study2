# Average Absolute Deviation (평균 절대 편차) 알고리즘

이 문서는 `average_absolute_deviation.py` 파일에 구현된 **평균 절대 편차(Average Absolute Deviation)** 계산 알고리즘에 대한 설명입니다.

## 개요

**평균 절대 편차**는 데이터 값들이 평균으로부터 얼마나 떨어져 있는지를 나타내는 산포도의 일종입니다. 각 데이터 값과 평균의 차이(편차)의 절대값들의 평균을 구하여 계산합니다.

## 함수 설명

### `average_absolute_deviation(nums: list[int]) -> float`

주어진 숫자 리스트의 평균 절대 편차를 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `nums` (`list[int]`): 정수(또는 실수)들이 담긴 리스트입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `nums`가 비어있을 경우 "List is empty" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력 리스트가 비어있는지 확인합니다.
2. 리스트의 산술 평균(mean)을 계산합니다. (`sum(nums) / len(nums)`)
3. 각 요소와 평균의 차이의 절대값을 모두 더합니다. (`sum(abs(x - average) for x in nums)`)
4. 합계를 요소의 개수로 나누어 평균 절대 편차를 구하고 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
