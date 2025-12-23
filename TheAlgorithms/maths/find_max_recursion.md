# Find Max Recursion (최대값 찾기 - 재귀) 알고리즘

이 문서는 `find_max_recursion.py` 파일에 구현된 **분할 정복(Divide and Conquer)** 방식을 이용한 최대값 찾기 알고리즘에 대한 설명입니다.

## 개요

주어진 숫자 리스트에서 재귀적인 분할 정복 방법을 사용하여 최대값을 찾아 반환합니다. 리스트를 절반으로 나누어 각각의 최대값을 구하고, 그 중 더 큰 값을 선택하는 과정을 반복합니다.

## 함수 설명

### `find_max(nums: list[int | float], left: int, right: int) -> int | float`

리스트의 특정 범위(`left`부터 `right`까지) 내에서 최대값을 찾아 반환합니다.

#### 매개변수 (Parameters)

- `nums` (`list[int | float]`): 숫자(정수 또는 실수)들이 담긴 리스트입니다.
- `left` (`int`): 검색을 시작할 인덱스입니다.
- `right` (`int`): 검색을 종료할 인덱스입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `nums`가 비어있을 경우 "find_max() arg is an empty sequence" 메시지와 함께 에러를 발생시킵니다.
- **IndexError**: `left`나 `right` 인덱스가 리스트 범위를 벗어날 경우 "list index out of range" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 입력 리스트가 비어있는지 확인합니다.
2. 인덱스 범위가 유효한지 확인합니다.
3. **기저 사례 (Base Case)**: `left`와 `right`가 같으면, 해당 인덱스의 값(`nums[left]`)을 반환합니다. (요소가 하나인 경우)
4. **재귀 단계 (Recursive Step)**:
   - 중간 인덱스 `mid`를 계산합니다 (`(left + right) // 2`).
   - 왼쪽 부분(`left` ~ `mid`)에 대해 `find_max`를 재귀 호출하여 `left_max`를 구합니다.
   - 오른쪽 부분(`mid + 1` ~ `right`)에 대해 `find_max`를 재귀 호출하여 `right_max`를 구합니다.
   - `left_max`와 `right_max` 중 더 큰 값을 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
```
