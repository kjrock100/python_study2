# Largest Subarray Sum (최대 부분 배열 합) 알고리즘

이 문서는 `largest_subarray_sum.py` 파일에 구현된 **최대 부분 배열 합(Largest Subarray Sum)**을 구하는 알고리즘에 대한 설명입니다.

## 개요

이 알고리즘은 **카데인 알고리즘(Kadane's Algorithm)**을 사용하여 1차원 숫자 배열에서 연속된 부분 배열의 합 중 가장 큰 값을 $O(n)$ 시간 복잡도로 찾아냅니다. 음수가 포함된 배열에서도 올바르게 동작하도록 구현되어 있습니다.

## 함수 설명

### `max_sub_array_sum(a: list, size: int = 0)`

주어진 리스트 `a`에서 가장 큰 연속 부분 배열의 합을 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `a` (`list`): 정수들이 담긴 리스트입니다.
- `size` (`int`): 리스트의 크기입니다. (기본값: 0, 0이면 `len(a)`를 사용합니다.)

#### 알고리즘 (Algorithm)

1. `max_so_far`를 시스템에서 표현 가능한 가장 작은 정수(`-maxsize - 1`)로 초기화합니다. 이는 배열의 모든 원소가 음수일 경우를 대비하기 위함입니다.
2. `max_ending_here`를 0으로 초기화합니다.
3. 리스트의 각 요소 `a[i]`에 대해 순회하며 다음을 수행합니다:
   - `max_ending_here`에 `a[i]`를 더합니다.
   - 만약 `max_so_far`가 `max_ending_here`보다 작다면, `max_so_far`를 `max_ending_here`로 갱신합니다.
   - 만약 `max_ending_here`가 0보다 작다면, 0으로 초기화합니다. (음수 합은 이후의 합을 감소시키므로 버립니다.)
4. 최종적으로 `max_so_far`를 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 예제 배열에 대한 최대 부분 배열 합을 출력합니다.

```python
if __name__ == "__main__":
    a = [-13, -3, -25, -20, 1, -16, -23, -12, -5, -22, -15, -4, -7]
    print(("Maximum contiguous sum is", max_sub_array_sum(a, len(a))))
```

**출력 결과:**

```
('Maximum contiguous sum is', 1)
```

(이 예제에서 양수는 `1` 하나뿐이므로, 최대 합은 `1`이 됩니다.)
