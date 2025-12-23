# Allocation Number (할당 번호) 알고리즘

이 문서는 `allocation_number.py` 파일에 구현된 **바이트 할당(Byte Allocation)** 알고리즘에 대한 설명입니다.

## 개요

이 알고리즘은 전체 바이트 수를 주어진 파티션 수로 나누어, 각 파티션이 담당할 바이트 범위를 계산합니다. 주로 멀티스레드 다운로드 환경에서 각 스레드에 다운로드할 데이터 범위를 할당할 때 유용하게 사용됩니다 (예: HTTP Range 헤더).

## 함수 설명

### `allocation_num(number_of_bytes: int, partitions: int) -> list[str]`

전체 바이트를 지정된 수의 파티션으로 나누어 각 파티션의 시작과 끝 범위를 문자열 리스트로 반환합니다.

#### 매개변수 (Parameters)

- `number_of_bytes` (`int`): 전체 바이트 수입니다.
- `partitions` (`int`): 나눌 파티션(구역)의 개수입니다.

#### 예외 처리 (Error Handling)

- **ValueError**: `partitions`가 0 이하인 경우 "partitions must be a positive number!" 에러가 발생합니다.
- **ValueError**: `partitions`가 `number_of_bytes`보다 큰 경우 "partitions can not > number_of_bytes!" 에러가 발생합니다.

#### 알고리즘 (Algorithm)

1. 입력값 유효성을 검사합니다 (파티션 수가 양수인지, 전체 바이트 수보다 작거나 같은지).
2. 파티션당 기본 바이트 수(`bytes_per_partition`)를 계산합니다 (`number_of_bytes // partitions`).
3. 파티션 수만큼 반복하며 각 구역의 범위를 계산합니다:
   - **시작 바이트**: `i * bytes_per_partition + 1`
   - **끝 바이트**: 마지막 파티션인 경우 `number_of_bytes`, 그 외에는 `(i + 1) * bytes_per_partition`
4. "시작-끝" 형태의 문자열을 리스트에 추가하여 반환합니다.

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    import doctest

    doctest.testmod()
```
