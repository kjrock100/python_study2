# `quine_mc_cluskey.py` 코드 설명

이 문서는 `quine_mc_cluskey.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 디지털 논리 회로의 **부울 함수(Boolean function)를 최소화**하기 위한 **퀸-매클러스키(Quine-McCluskey) 알고리즘**을 구현합니다.

## 목차
1.  퀸-매클러스키 알고리즘이란?
2.  알고리즘 단계
3.  함수 설명
    -   `decimal_to_binary()`
    -   `compare_string()`
    -   `check()`
    -   `is_for_table()`
    -   `prime_implicant_chart()`
    -   `selection()`
    -   `main()`
4.  실행 방법
5.  코드 개선 제안

## 퀸-매클러스키 알고리즘이란?

카르노 맵(Karnaugh map)과 같이 부울 함수를 간소화하는 데 사용되는 표(tabular) 방식의 알고리즘입니다. 변수의 개수가 많아져도 컴퓨터를 통해 체계적으로 최소화된 논리식을 찾을 수 있다는 장점이 있습니다.

## 알고리즘 단계

이 스크립트는 퀸-매클러스키 알고리즘의 두 가지 주요 단계를 구현합니다.

1.  **주항(Prime Implicants) 찾기**: 모든 민텀(minterm)을 포함하는 간소화된 항들의 집합을 찾습니다.
2.  **필수 주항(Essential Prime Implicants) 선택**: 주항들 중에서 최소한의 개수로 모든 민텀을 포함하는 집합을 선택하여 최종 논리식을 구성합니다.

## 함수 설명

### `decimal_to_binary(no_of_variable, minterms)`

사용자가 입력한 10진수 민텀 리스트를 2진수 문자열 리스트로 변환합니다.

-   **역할**: 알고리즘의 첫 단계로, 모든 민텀을 2진수 형태로 표현합니다.
-   **반환값**: `list[str]` 타입의 2진수 문자열 리스트.

### `compare_string(string1, string2)`

두 개의 2진수 문자열을 비교하여 한 비트만 다른지 확인합니다.

-   **역할**: 퀸-매클러스키 1단계에서 인접한 항을 찾아 결합하는 데 사용됩니다.
-   **로직**:
    -   두 문자열이 정확히 한 비트만 다르면, 다른 비트 위치를 `_` (don't care)로 바꾼 문자열을 반환합니다. (예: `'0010'`, `'0110'` -> `'0_10'`)
    -   두 비트 이상 다르거나 같으면 `'X'`를 반환하여 결합할 수 없음을 알립니다.

### `check(binary)`

2진수 민텀 리스트로부터 모든 **주항(Prime Implicants)** 을 찾습니다.

-   **알고리즘**: 퀸-매클러스키 1단계의 핵심입니다.
    1.  `compare_string`을 이용해 리스트 내의 모든 항 쌍을 비교하여 결합 가능한 항들을 찾습니다.
    2.  결합된 항들은 다음 단계의 입력이 되고, 어떤 항과도 결합되지 않은 항들은 "주항"으로 따로 저장됩니다.
    3.  더 이상 새로운 항이 결합되지 않을 때까지 이 과정을 반복합니다.
-   **반환값**: `list[str]` 타입의 주항 리스트.

### `is_for_table(string1, string2, count)`

주항(`string1`)이 특정 민텀(`string2`)을 포함(cover)하는지 확인합니다.

-   **역할**: 주항 차트(Prime Implicant Chart)를 생성할 때 사용됩니다.
-   **로직**: 주항의 `_`를 제외한 나머지 비트들이 민텀의 해당 비트와 일치하는지 검사합니다.

### `prime_implicant_chart(prime_implicants, binary)`

주항과 원래 민텀 간의 포함 관계를 나타내는 **주항 차트**를 생성합니다.

-   **역할**: 퀸-매클러스키 2단계의 준비 과정입니다.
-   **구조**: 행은 주항, 열은 민텀을 나타내는 2차원 리스트입니다. `chart[i][j]`가 `1`이면 `i`번째 주항이 `j`번째 민텀을 포함한다는 의미입니다.

### `selection(chart, prime_implicants)`

주항 차트를 분석하여 모든 민텀을 포함하는 최소한의 주항 집합, 즉 **필수 주항(Essential Prime Implicants)** 을 선택합니다.

-   **알고리즘**: 퀸-매클러스키 2단계의 핵심입니다.
    1.  **필수 주항 찾기**: 특정 민텀을 유일하게 포함하는 주항을 찾아 결과에 추가합니다.
    2.  **나머지 민텀 처리 (Greedy 접근)**: 필수 주항으로 처리된 민텀들을 제외하고, 남은 민텀들을 가장 많이 포함하는 주항을 순서대로 선택하여 모든 민텀이 포함될 때까지 반복합니다.
-   **반환값**: `list[str]` 타입의 최종 선택된 주항 리스트.

### `main()`

사용자로부터 변수의 개수와 민텀을 입력받아 전체 퀸-매클러스키 알고리즘을 실행하고, 최종 결과를 출력합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자 입력을 받아 부울 함수 최소화를 수행합니다.

```bash
python quine_mc_cluskey.py
```

실행 후, 변수의 개수와 공백으로 구분된 민텀들을 입력합니다.

```
Enter the no. of variables
4
Enter the decimal representation of Minterms 'Spaces Separated'
0 1 2 5 6 7 8 9 10 14
```

## 코드 개선 제안

1.  **타입 힌트 및 변수명 개선**:
    -   `minterms`를 `float`으로 받는 것은 의도와 다를 수 있습니다. `int`로 변경하는 것이 명확합니다.
    -   `check1`, `temp`, `rem` 등 모호한 변수명을 `is_combined`, `next_terms`, `selected_row_index` 와 같이 의미가 명확한 이름으로 변경하면 가독성이 크게 향상됩니다.

2.  **알고리즘 로직 명확화**:
    -   `compare_string` 함수는 두 비트 이상 다를 때와 완전히 같을 때 모두 `'X'`를 반환하는데, 이는 혼동을 줄 수 있습니다. 목적에 맞게 로직을 분리하거나 주석을 추가하는 것이 좋습니다.
    -   `selection` 함수의 두 번째 `while` 루프는 복잡한 로직을 수행합니다. 이를 "필수 주항 선택"과 "나머지 민텀 처리" 단계로 나누어 별도의 함수로 분리하면 코드를 이해하고 유지보수하기가 더 쉬워집니다.

3.  **데이터 구조 활용**:
    -   `check` 함수에서 `list(set(temp))`를 사용하여 중복을 제거하는 것은 효율적입니다. 이처럼 적절한 데이터 구조(set, dict)를 활용하면 코드를 더 간결하고 빠르게 만들 수 있습니다.

4.  **Docstring 및 주석 보강**:
    -   현재 `doctest`는 간단한 케이스만 다루고 있습니다. 실제 알고리즘의 동작을 보여주는 더 복잡한 예제를 추가하면 함수의 동작을 이해하는 데 큰 도움이 됩니다.
    -   각 함수의 역할과 알고리즘의 특정 단계와의 연관성을 주석으로 명시하면 좋습니다.

아래는 `compare_string` 함수의 가독성을 개선한 예시입니다.

```python
# 개선 제안 예시
def find_combinable_term(term1: str, term2: str) -> str | None:
    """
    Compares two binary terms. If they differ by exactly one bit,
    returns the combined term with a '_' (don't care).
    Otherwise, returns None.

    >>> find_combinable_term('0010', '0110')
    '0_10'
    >>> find_combinable_term('0010', '1010')
    '_010'
    >>> find_combinable_term('0010', '0011') # More than one difference
    None
    >>> find_combinable_term('0010', '0010') # No difference
    None
    """
    diff_index = -1
    diff_count = 0
    for i in range(len(term1)):
        if term1[i] != term2[i]:
            diff_count += 1
            diff_index = i

    if diff_count == 1:
        term_list = list(term1)
        term_list[diff_index] = "_"
        return "".join(term_list)

    return None
```