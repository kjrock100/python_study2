# 카탈란 수 (Catalan Numbers)

이 문서는 `catalan_numbers.py` 파일에 구현된 **카탈란 수(Catalan Numbers)** 생성 알고리즘에 대해 설명합니다. 카탈란 수는 조합론의 다양한 계산 문제에서 등장하는 수열입니다.

## 개요

카탈란 수는 다음과 같은 점화식을 만족하는 수열입니다:
- $C_0 = 1$
- $C_{n+1} = \sum_{i=0}^{n} C_i C_{n-i}$

이 코드는 위 점화식을 바탕으로 **동적 계획법(Dynamic Programming)**을 사용하여 0부터 $n$까지의 카탈란 수를 계산합니다.

## 주요 함수: `catalan_numbers`

### `catalan_numbers(upper_limit: int) -> list[int]`
- **목적**: 0부터 `upper_limit`까지의 카탈란 수열을 리스트로 반환합니다.
- **매개변수**:
  - `upper_limit`: 생성할 수열의 마지막 인덱스 ($n$). 0 이상의 정수여야 합니다.
- **반환값**: 카탈란 수들이 담긴 정수 리스트.
- **예외 처리**: 입력값이 음수일 경우 `ValueError`를 발생시킵니다.

### 알고리즘 동작 원리

1. **초기화**:
   - 크기가 `upper_limit + 1`인 리스트 `catalan_list`를 0으로 초기화합니다.
   - 기저 사례(Base Case)를 설정합니다: `catalan_list[0] = 1`.
   - `upper_limit`가 0보다 크다면 `catalan_list[1] = 1`로 설정합니다.

2. **점화식 적용 (Recurrence)**:
   - 인덱스 `i`를 2부터 `upper_limit`까지 반복합니다.
   - 각 `i`에 대해 내부 루프 `j`를 0부터 `i-1`까지 반복하며 다음 값을 누적합니다:
     - `catalan_list[i] += catalan_list[j] * catalan_list[i - j - 1]`
   - 이는 $C_i = \sum_{j=0}^{i-1} C_j C_{i-1-j}$ 공식을 코드로 구현한 것입니다.

## 카탈란 수의 응용

코드의 주석(Docstring)에 언급된 카탈란 수의 대표적인 응용 사례는 다음과 같습니다:
- 길이가 $2n$인 디크 단어(Dyck words)의 개수.
- $n$쌍의 괄호로 만들 수 있는 올바른 괄호 문자열의 개수 (예: `()()`, `(())`).
- $n+1$개의 요소를 괄호로 묶는 모든 방법의 수.
- $n+1$개의 리프 노드(Leaf)를 가진 포화 이진 트리(Full Binary Tree)의 개수.

## 사용법

`if __name__ == "__main__":` 블록을 통해 스크립트를 직접 실행할 수 있습니다.
1. 프로그램을 실행하면 상한값(`upper_limit`)을 입력받습니다.
2. 입력된 값까지의 카탈란 수열을 출력합니다.
3. `-1`을 입력하면 프로그램이 종료됩니다.

```python
# 예시
catalan_numbers(5)
# 결과: [1, 1, 2, 5, 14, 42]
```