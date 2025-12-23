# Absolute Min (절대값 최소값) 알고리즘

이 문서는 `abs_min.py` 파일에 구현된 **절대값 최소값 찾기** 알고리즘에 대한 설명입니다.

## 개요

주어진 정수 리스트에서 절대값이 가장 작은 수를 찾아 반환하는 기능을 제공합니다.

## 함수 설명

### `abs_min(x: list[int]) -> int`

리스트를 순회하며 절대값이 가장 작은 요소를 찾습니다.

#### 매개변수 (Parameters)

- `x` (`list[int]`): 정수들이 담긴 리스트입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: 입력 리스트 `x`가 비어있을 경우 "abs_min() arg is an empty sequence" 메시지와 함께 에러를 발생시킵니다.

#### 알고리즘 (Algorithm)

1. 리스트가 비어있는지 확인합니다.
2. 첫 번째 요소를 현재 최소값 변수 `j`로 설정합니다.
3. 리스트의 모든 요소를 순회하며, 현재 요소 `i`의 절대값이 `j`의 절대값보다 작으면 `j`를 `i`로 갱신합니다.
   - 절대값 계산은 `abs_val` 함수(같은 패키지의 `abs` 모듈에서 가져옴)를 사용합니다.
4. 최종적으로 `j`를 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증하고, `main()` 함수를 호출하여 예제 리스트에 대한 실행 결과를 출력합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
```
