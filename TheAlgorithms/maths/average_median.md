# Average Median (중앙값) 알고리즘

이 문서는 `average_median.py` 파일에 구현된 **중앙값(Median)** 계산 알고리즘에 대한 설명입니다.

## 개요

**중앙값**은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 데이터 집합의 대표값 중 하나로, 이상치(outlier)의 영향을 덜 받는다는 특징이 있습니다.

## 함수 설명

### `median(nums: list) -> int | float`

주어진 숫자 리스트의 중앙값을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `nums` (`list`): 숫자(정수 또는 실수)들이 담긴 리스트입니다.

#### 알고리즘 (Algorithm)

1. 입력된 리스트 `nums`를 `sorted()` 함수를 사용하여 오름차순으로 정렬합니다.
2. 리스트의 길이를 구하고, 비트 연산(`>> 1`)을 사용하여 중간 인덱스(`mid_index`)를 계산합니다. (이는 2로 나눈 몫을 구하는 것과 같습니다.)
3. 리스트의 길이가 짝수인 경우:
   - 중간에 위치한 두 값(`sorted_list[mid_index]`와 `sorted_list[mid_index - 1]`)의 평균을 계산하여 반환합니다.
4. 리스트의 길이가 홀수인 경우:
   - 정가운데 위치한 값(`sorted_list[mid_index]`)을 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
