# `excel_title_to_column.py` 코드 설명

이 문서는 `excel_title_to_column.py` 파이썬 스크립트에 포함된 `excel_title_to_column` 함수를 설명합니다. 이 스크립트는 엑셀(Excel) 시트의 열 제목(예: "A", "AB")을 해당하는 열 번호(1, 28)로 변환하는 기능을 구현합니다.

## 목차
1.  엑셀 열 제목 변환 원리
2.  함수 설명
    -   `excel_title_to_column(column_title)`
3.  실행 방법
4.  코드 개선 제안

## 엑셀 열 제목 변환 원리

엑셀의 열 제목은 26진법과 유사한 시스템을 사용합니다.

-   `A`부터 `Z`까지는 1부터 26에 해당합니다.
-   `Z` 다음에는 `AA`, `AB`, ... 와 같이 두 자리로 넘어갑니다.

이는 각 자리수가 26의 거듭제곱을 나타내는 26진법으로 생각할 수 있습니다.

예를 들어, "AB"는 다음과 같이 계산됩니다.
`(A의 값 * 26¹) + (B의 값 * 26⁰) = (1 * 26) + (2 * 1) = 28`

## 함수 설명

### `excel_title_to_column(column_title: str) -> int`

엑셀 열 제목 문자열을 입력받아 해당하는 열 번호를 반환합니다.

-   **알고리즘**:
    1.  **유효성 검사**: `assert` 문을 사용하여 입력 문자열이 모두 대문자인지 확인합니다.
    2.  **변환**:
        -   문자열을 오른쪽부터 왼쪽으로 순회합니다. (`index`가 `len-1`에서 `0`으로 감소)
        -   각 문자에 대해, `ord(문자) - 64`를 사용하여 1부터 26까지의 값을 구합니다. (A=1, B=2, ...)
        -   이 값에 `26`의 거듭제곱(`power`)을 곱하여 해당 자리의 값을 계산합니다.
        -   계산된 값을 `answer`에 더하고, `power`를 1 증가시킵니다.
    3.  **결과 반환**: 최종적으로 계산된 열 번호를 반환합니다.

```python
>>> excel_title_to_column("A")
1
>>> excel_title_to_column("AB")
28
```

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수에 포함된 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python excel_title_to_column.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **'매직 넘버' 제거**: 코드에 사용된 숫자 `64`는 '매직 넘버'로, 그 의미를 즉시 파악하기 어렵습니다. `ord('A') - 1` 과 같이 계산하여 사용하면 코드의 가독성이 크게 향상됩니다.

2.  **알고리즘 단순화**: `while` 루프와 인덱스를 사용하는 대신, `for` 루프와 문자열을 직접 순회하는 방식으로 더 간결하게 작성할 수 있습니다. 이는 호너의 방법(Horner's method)과 유사한 방식으로, 왼쪽부터 순회하며 누적 값을 계산합니다.

    ```python
    # 개선 제안 예시
    def excel_title_to_column_simple(column_title: str) -> int:
        """
        A simpler implementation to convert an Excel column title to its number.
        """
        answer = 0
        offset = ord('A') - 1
        for char in column_title:
            answer = answer * 26 + (ord(char) - offset)
        return answer
    ```

3.  **입력 유효성 검사 방식**: `assert` 문은 주로 디버깅 목적으로 사용되며, `-O` 옵션으로 파이썬을 실행하면 비활성화될 수 있습니다. 사용자 입력과 같이 예측 불가능한 데이터를 처리할 때는 `if` 문과 `raise ValueError`를 사용하여 입력이 유효한지(예: 알파벳 대문자로만 구성되었는지) 검사하는 것이 더 안정적입니다.