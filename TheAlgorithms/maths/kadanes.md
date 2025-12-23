# Kadane's Algorithm (카데인 알고리즘)

이 문서는 `kadanes.py` 파일에 구현된 **카데인 알고리즘(Kadane's Algorithm)**에 대한 설명입니다.

## 개요

**카데인 알고리즘**은 **최대 부분 배열 합 문제(Maximum Subarray Problem)**를 해결하기 위한 동적 계획법(Dynamic Programming) 기반의 알고리즘입니다. 주어진 수열에서 연속된 부분 배열의 합 중 가장 큰 값을 $O(n)$ 시간 복잡도로 찾아냅니다.

## 함수 설명

### `negative_exist(arr: list) -> int`

리스트의 모든 요소가 음수인지 확인하고, 그렇다면 그중 최댓값을 반환하는 헬퍼 함수입니다.

#### 매개변수 (Parameters)

- `arr` (`list`): 정수 리스트입니다.

#### 알고리즘 (Algorithm)

1. 리스트가 비어있으면 `[0]`으로 취급합니다.
2. 리스트를 순회하며 0 이상의 수가 있는지 확인합니다.
   - 0 이상의 수가 하나라도 있으면 `0`을 반환합니다. (카데인 알고리즘의 일반 로직을 적용하기 위함)
3. 모든 수가 음수라면, 그중 가장 큰 값(0에 가장 가까운 음수)을 반환합니다.

### `kadanes(arr: list) -> int`

카데인 알고리즘을 사용하여 최대 부분 배열 합을 계산합니다.

#### 매개변수 (Parameters)

- `arr` (`list`): 정수 리스트입니다.

#### 알고리즘 (Algorithm)

1. 먼저 `negative_exist(arr)`를 호출합니다.
   - 반환값이 음수라면, 모든 요소가 음수라는 뜻이므로 그 값(최대값)을 바로 반환합니다.
2. 그렇지 않다면(적어도 하나의 양수가 있거나 0이 반환된 경우), 일반적인 카데인 알고리즘을 수행합니다.
   - `max_sum` (전체 최대 합)과 `max_till_element` (현재 위치까지의 부분 합)를 0으로 초기화합니다.
   - 리스트를 순회하며 `max_till_element`에 현재 값을 더합니다.
   - `max_sum`보다 `max_till_element`가 크면 `max_sum`을 갱신합니다.
   - `max_till_element`가 0보다 작아지면 0으로 초기화합니다. (음수가 되면 부분 합을 이어가는 것이 손해이므로 버립니다.)
3. 최종적으로 `max_sum`을 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 공백으로 구분된 정수들을 입력받아 최대 부분 배열 합을 출력합니다.

```python
if __name__ == "__main__":
    try:
        print("Enter integer values sepatated by spaces")
        arr = [int(x) for x in input().split()]
        print(f"Maximum subarray sum of {arr} is {kadanes(arr)}")
    except ValueError:
        print("Please enter integer values.")
```

**입력/출력 예시:**

- 입력: `-2 -3 4 -1 -2 1 5 -3`
- 출력: `Maximum subarray sum of [-2, -3, 4, -1, -2, 1, 5, -3] is 7` (부분 배열 `[4, -1, -2, 1, 5]`의 합)
