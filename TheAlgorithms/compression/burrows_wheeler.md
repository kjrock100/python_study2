# `burrows_wheeler.py` 코드 설명

이 문서는 `burrows_wheeler.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 텍스트 압축 알고리즘의 효율을 높이기 위한 전처리 단계로 사용되는 **버로스-휠러 변환(Burrows-Wheeler Transform, BWT)**과 그 역변환을 구현합니다.

## 목차
1.  버로스-휠러 변환이란?
2.  함수 설명
    -   `all_rotations(s)`
    -   `bwt_transform(s)`
    -   `reverse_bwt(bwt_string, idx_original_string)`
3.  실행 방법
4.  코드 개선 제안

## 버로스-휠러 변환이란?

버로스-휠러 변환은 문자열을 재배열하여 동일한 문자들이 연속적으로 나타나도록 만드는 알고리즘입니다. 이렇게 변환된 문자열은 런-렝스 인코딩(Run-Length Encoding)과 같은 다른 압축 기법에 더 효율적으로 압축될 수 있습니다.

**변환 과정**:
1.  원본 문자열의 모든 순환(rotation)된 형태를 만듭니다.
2.  이 순환된 문자열들을 사전순으로 정렬합니다.
3.  정렬된 각 문자열의 마지막 글자들을 순서대로 이어 붙여 BWT 문자열을 만듭니다.
4.  정렬된 목록에서 원본 문자열이 몇 번째에 위치했는지를 인덱스로 함께 저장합니다.

이 변환의 가장 중요한 특징은 **가역적(reversible)**이라는 것입니다. 즉, BWT 문자열과 원본 문자열의 인덱스만 있으면 원래의 문자열로 완벽하게 복원할 수 있습니다.

## 함수 설명

### `all_rotations(s: str) -> list[str]`

주어진 문자열의 모든 순환된 형태를 생성하여 리스트로 반환합니다.

-   **알고리즘**: 문자열 슬라이싱을 사용하여 `s[i:] + s[:i]` 형태로 문자열을 회전시키고, 이를 모든 `i`에 대해 반복합니다.

```python
>>> all_rotations("BANANA")
['BANANA', 'ANANAB', 'NANABA', 'ANABAN', 'NABANA', 'ABANAN']
```

### `bwt_transform(s: str) -> BWTTransformDict`

주어진 문자열에 대해 버로스-휠러 변환을 수행합니다.

-   **알고리즘**:
    1.  `all_rotations`를 호출하여 모든 순환된 문자열을 얻습니다.
    2.  이 리스트를 사전순으로 정렬합니다.
    3.  정렬된 리스트의 각 문자열에서 마지막 문자를 추출하여 `bwt_string`을 만듭니다.
    4.  정렬된 리스트에서 원본 문자열 `s`의 위치를 찾아 `idx_original_string`으로 저장합니다.
-   **반환값**: `{'bwt_string': ..., 'idx_original_string': ...}` 형태의 딕셔너리.

```python
>>> bwt_transform("^BANANA")
{'bwt_string': 'BNN^AAA', 'idx_original_string': 6}
```

### `reverse_bwt(bwt_string: str, idx_original_string: int) -> str`

BWT로 변환된 문자열을 원래의 문자열로 **역변환(복원)**합니다.

-   **알고리즘**:
    1.  BWT 문자열(`bwt_string`)을 첫 번째 열로, 이 열을 정렬한 것을 마지막 열로 하는 테이블을 반복적으로 재구성합니다.
    2.  `len(bwt_string)` 만큼 이 과정을 반복하면, 정렬된 순환 문자열 목록이 복원됩니다.
    3.  복원된 목록에서 `idx_original_string`에 해당하는 문자열이 바로 원본 문자열입니다.

## 실행 방법

스크립트를 직접 실행하면 사용자로부터 문자열을 입력받아 BWT 변환과 역변환 과정을 시연합니다.

```bash
python burrows_wheeler.py
```

**실행 예시:**
```
Provide a string that I will generate its BWT transform: BANANA
Burrows Wheeler transform for string 'BANANA' results in 'ANNB.AA'
Reversing Burrows Wheeler transform for entry 'ANNB.AA' we get original string 'BANANA'
```

## 코드 개선 제안

1.  **`reverse_bwt` 함수의 효율성**: 현재 `reverse_bwt` 함수는 `len(bwt_string)` 만큼의 루프를 돌면서 매번 문자열을 합치고 정렬하는 과정을 반복합니다. 이는 매우 비효율적입니다(시간 복잡도 O(N² * logN)). BWT 역변환은 **LF-mapping (Last-to-First Mapping)** 속성을 이용하여 O(N) 또는 O(N * logN) 시간 복잡도로 훨씬 효율적으로 구현할 수 있습니다.

    ```python
    # LF-mapping을 이용한 개선 제안 예시
    def reverse_bwt_fast(bwt_string: str, idx: int) -> str:
        n = len(bwt_string)
        first_col = sorted(bwt_string)
        
        # 각 문자의 등장 횟수를 기록하여 LF-mapping 테이블 생성
        last_to_first_map = []
        counts = {}
        for char in bwt_string:
            count = counts.get(char, 0)
            last_to_first_map.append((char, count))
            counts[char] = count + 1
            
        sorted_counts = {}
        lf_map = [-1] * n
        for i, (char, count) in enumerate(last_to_first_map):
            # first_col에서 (char, count)에 해당하는 위치를 찾음
            pos = first_col.index(char) + sorted_counts.get(char, 0)
            lf_map[pos] = i
            sorted_counts[char] = sorted_counts.get(char, 0) + 1

        # LF-mapping을 따라가며 원본 문자열 복원
        original_string = ""
        current_idx = idx
        for _ in range(n):
            original_string = bwt_string[current_idx] + original_string
            current_idx = lf_map.index(current_idx)
            
        return original_string
    ```
    > **참고**: 위 코드는 개념적인 예시이며, 실제 구현은 더 최적화될 수 있습니다.

2.  **입력 유효성 검사**: `reverse_bwt` 함수에서 `idx_original_string`을 `int()`로 변환하는 부분은 `float` 값(예: 11.4)도 허용합니다. 이는 의도된 동작일 수 있으나, 정수 인덱스가 기대된다면 더 엄격한 타입 검사를 추가하는 것이 좋습니다.

3.  **타입 힌트**: `BWTTransformDict`와 같은 `TypedDict`를 사용하여 반환 타입을 명시한 것은 매우 좋은 습관입니다. 코드의 명확성과 안정성을 높여줍니다.