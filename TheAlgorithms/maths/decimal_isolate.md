# Decimal Isolate (소수점 분리) 알고리즘

이 문서는 `decimal_isolate.py` 파일에 구현된 **소수점 이하 부분 분리** 알고리즘에 대한 설명입니다.

## 개요

주어진 실수(float)에서 정수 부분을 제외한 소수점 이하 부분만을 추출하여 반환하는 기능을 제공합니다. 필요에 따라 특정 자릿수까지 반올림할 수도 있습니다.

## 함수 설명

### `decimal_isolate(number, digitAmount)`

숫자의 소수점 이하 부분을 분리하여 반환합니다.

#### 매개변수 (Parameters)

- `number`: 소수점 이하를 분리할 숫자 (실수 또는 정수).
- `digitAmount`: 반올림할 소수점 자릿수. 0보다 크면 해당 자릿수까지 반올림하고, 그렇지 않으면 전체 소수 부분을 반환합니다.

#### 알고리즘 (Algorithm)

1. 입력된 숫자 `number`에서 정수 부분 `int(number)`를 뺍니다. 이렇게 하면 소수점 이하 부분만 남게 됩니다.
2. `digitAmount`가 0보다 큰 경우:
   - `round()` 함수를 사용하여 계산된 소수점 이하 부분을 지정된 자릿수(`digitAmount`)까지 반올림하여 반환합니다.
3. `digitAmount`가 0 이하인 경우:
   - 계산된 소수점 이하 부분을 그대로 반환합니다.

#### 예시 (Examples)

- `decimal_isolate(1.53, 0)` -> `0.53`
- `decimal_isolate(35.345, 2)` -> `0.34`
- `decimal_isolate(-14.789, 3)` -> `-0.789`

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) 예제 값들에 대한 실행 결과를 출력합니다.

```python
if __name__ == "__main__":
    print(decimal_isolate(1.53, 0))
    # ...
```
