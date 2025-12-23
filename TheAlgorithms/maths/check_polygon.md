# Check Polygon (다각형 성립 확인) 알고리즘

이 문서는 `check_polygon.py` 파일에 구현된 **다각형 성립 조건 확인** 알고리즘에 대한 설명입니다.

## 개요

주어진 변의 길이들을 가지고 2차원 유클리드 공간에서 닫힌 다각형을 만들 수 있는지 판별합니다. 이는 삼각형 부등식(Triangle Inequality)을 일반화한 원리를 사용합니다. 가장 긴 변의 길이가 나머지 변들의 길이의 합보다 작아야 다각형이 성립합니다.

## 함수 설명

### `check_polygon(nums: list[float]) -> bool`

주어진 변의 길이 리스트로 다각형을 구성할 수 있는지 여부를 반환합니다.

#### 매개변수 (Parameters)

- `nums` (`list[float]`): 다각형의 각 변의 길이를 담은 리스트입니다.

#### 예외 처리 (Error Handling)

1. **ValueError**: 리스트의 요소 개수가 2개 미만인 경우 발생합니다. (메시지: "Monogons and Digons are not polygons in the Euclidean space")
   - _참고_: 코드상으로는 요소가 2개인 경우 에러가 발생하지 않지만, 2개의 변으로는 닫힌 다각형을 만들 수 없으므로 논리적으로 항상 `False`가 반환됩니다.
2. **ValueError**: 변의 길이가 0 이하인 값이 포함된 경우 발생합니다. (메시지: "All values must be greater than 0")

#### 알고리즘 (Algorithm)

1. 입력 리스트의 유효성을 검사합니다 (길이 확인, 양수 확인).
2. 원본 리스트를 보존하기 위해 복사본(`copy_nums`)을 생성합니다.
3. 복사본을 오름차순으로 정렬합니다.
4. 가장 긴 변(`copy_nums[-1]`)이 나머지 변들의 합(`sum(copy_nums[:-1])`)보다 작은지 비교하여 결과를 반환합니다.
   - 공식: $\max(S) < \sum (S \setminus \{\max(S)\})$

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
