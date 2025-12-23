# Find Max (최대값 찾기) 알고리즘

이 문서는 `find_max.py` 파일에 구현된 **최대값 찾기** 알고리즘에 대한 설명입니다.

## 개요

주어진 숫자 리스트(정수 또는 실수)를 순회하며 가장 큰 값을 찾아 반환하는 간단한 선형 탐색 알고리즘입니다.

## 함수 설명

### `find_max(nums: list[int | float]) -> int | float`

리스트 내의 요소들을 비교하여 최대값을 반환합니다. 파이썬 내장 함수 `max()`와 유사한 기능을 수행합니다.

#### 매개변수 (Parameters)

- `nums` (`list[int | float]`): 숫자(정수 또는 실수)들이 담긴 리스트입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `nums`가 비어있을 경우 "find_max() arg is an empty sequence" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력 리스트가 비어있는지 확인합니다.
2. 리스트의 첫 번째 요소를 현재 최대값 변수 `max_num`으로 설정합니다.
3. 리스트의 모든 요소를 순회하며, 현재 요소 `x`가 `max_num`보다 크면 `max_num`을 `x`로 갱신합니다.
4. 순회가 끝나면 `max_num`을 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
```
