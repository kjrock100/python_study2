# Absolute Max (절대값 최대값) 알고리즘

이 문서는 `abs_max.py` 파일에 구현된 **절대값 최대값 찾기** 알고리즘에 대한 설명입니다.

## 개요

주어진 정수 리스트에서 절대값이 가장 큰 수를 찾아 반환하는 기능을 제공합니다. 두 가지 구현 방식(`abs_max`, `abs_max_sort`)이 포함되어 있습니다.

## 함수 설명

### `abs_max(x: list[int]) -> int`

리스트를 순회하며 절대값이 가장 큰 요소를 찾습니다.

#### 매개변수 (Parameters)

- `x` (`list[int]`): 정수들이 담긴 리스트입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `x`가 비어있을 경우 "abs_max() arg is an empty sequence" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 리스트가 비어있는지 확인합니다.
2. 첫 번째 요소를 현재 최대값 변수 `j`로 설정합니다.
3. 리스트의 모든 요소를 순회하며, 현재 요소 `i`의 절대값이 `j`의 절대값보다 크면 `j`를 `i`로 갱신합니다.
4. 최종적으로 `j`를 반환합니다.

### `abs_max_sort(x: list[int]) -> int`

파이썬의 내장 정렬 기능을 사용하여 절대값이 가장 큰 요소를 찾습니다.

#### 매개변수 (Parameters)

- `x` (`list[int]`): 정수들이 담긴 리스트입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `x`가 비어있을 경우 "abs_max_sort() arg is an empty sequence" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 리스트가 비어있는지 확인합니다.
2. `sorted()` 함수를 사용하여 리스트를 정렬합니다. 이때 `key=abs`를 사용하여 절대값을 기준으로 오름차순 정렬합니다.
3. 정렬된 리스트의 마지막 요소(`[-1]`)를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증하고, `main()` 함수를 호출하여 간단한 단언문(assert) 테스트를 수행합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
```
