# `lempel_ziv.py` 코드 설명

이 문서는 `lempel_ziv.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 **렘펠-지브-웰치(Lempel-Ziv-Welch, LZW)** 알고리즘을 사용하여 파일을 압축하는 기능을 구현합니다.

## 목차
1.  LZW 압축이란?
2.  함수 설명
    -   `read_file_binary(file_path)`
    -   `add_key_to_lexicon(...)`
    -   `compress_data(data_bits)`
    -   `add_file_length(source_path, compressed)`
    -   `write_file_binary(file_path, to_write)`
    -   `compress(source_path, destination_path)`
3.  실행 방법
4.  코드 개선 제안

## LZW 압축이란?

LZW는 무손실 데이터 압축 알고리즘으로, 텍스트에서 반복되는 시퀀스를 찾아 이를 코드로 대체하는 방식으로 동작합니다.

**압축 과정**:
1.  **사전(Lexicon/Dictionary) 초기화**: 가능한 모든 단일 문자(이 스크립트에서는 '0'과 '1')로 사전을 초기화합니다.
2.  **데이터 스캔**: 입력 데이터 스트림을 순차적으로 읽으면서, 현재까지 읽은 시퀀스가 사전에 있는지 확인합니다.
3.  **최장 일치 찾기**: 사전에 있는 가장 긴 시퀀스를 찾습니다.
4.  **코드 출력 및 사전 업데이트**:
    -   찾은 가장 긴 시퀀스에 해당하는 코드를 출력합니다.
    -   "가장 긴 시퀀스 + 다음 문자"로 구성된 새로운 시퀀스를 사전에 추가하고 새로운 코드를 할당합니다.
5.  이 과정을 데이터 끝까지 반복합니다.

이 스크립트는 바이너리 데이터(0과 1)에 대해 이 알고리즘을 적용합니다.

## 함수 설명

### `read_file_binary(file_path: str) -> str`

지정된 파일을 바이너리 모드로 읽어, 그 내용을 '0'과 '1'로 이루어진 하나의 긴 비트 문자열로 변환하여 반환합니다.

### `add_key_to_lexicon(lexicon, curr_string, index, last_match_id)`

LZW 압축 과정에서 사전에 새로운 항목을 추가합니다.

-   **알고리즘**:
    -   기존에 일치했던 문자열(`curr_string`)을 사전에서 제거합니다.
    -   `curr_string + "0"`과 `curr_string + "1"`을 새로운 키로 사전에 추가하고, 각각에 새로운 코드를 할당합니다.
    -   사전의 크기가 2의 거듭제곱이 될 때마다, 기존 코드들 앞에 '0'을 추가하여 코드 길이를 1비트씩 늘립니다.

### `compress_data(data_bits: str) -> str`

주어진 비트 문자열을 LZW 알고리즘을 사용하여 압축합니다.

-   **알고리즘**:
    1.  '0'과 '1'로 사전을 초기화합니다.
    2.  입력 비트 문자열(`data_bits`)을 순회하면서, 사전에 있는 가장 긴 시퀀스(`curr_string`)를 찾습니다.
    3.  해당 시퀀스의 코드를 결과 문자열에 추가합니다.
    4.  `add_key_to_lexicon`을 호출하여 사전을 업데이트합니다.
    5.  모든 비트를 처리할 때까지 이 과정을 반복합니다.

### `add_file_length(source_path: str, compressed: str) -> str`

압축된 데이터의 맨 앞에 원본 파일의 크기 정보를 **엘리어스 감마 코딩(Elias gamma coding)** 방식으로 인코딩하여 추가합니다. 이는 압축 해제 시 원본 파일의 정확한 크기를 복원하는 데 사용됩니다.

### `write_file_binary(file_path: str, to_write: str) -> None`

압축된 비트 문자열을 바이너리 파일로 씁니다.

-   **알고리즘**:
    1.  비트 문자열을 8비트(1바이트) 단위로 나눕니다.
    2.  마지막 바이트가 8비트를 채우지 못할 경우, '1' 비트와 필요한 만큼의 '0' 비트를 추가하여 패딩(padding)합니다.
    3.  각 8비트 덩어리를 정수로 변환하고, 이를 바이트로 변환하여 파일에 씁니다.

### `compress(source_path: str, destination_path: str) -> None`

전체 압축 과정을 총괄하는 메인 함수입니다.

-   **동작**:
    1.  `read_file_binary`로 원본 파일을 읽습니다.
    2.  `compress_data`로 데이터를 압축합니다.
    3.  `add_file_length`로 파일 크기 정보를 추가합니다.
    4.  `write_file_binary`로 압축된 데이터를 파일에 씁니다.

## 실행 방법

이 스크립트는 커맨드 라인에서 원본 파일 경로와 압축할 파일 경로를 인자로 받아 실행합니다.

```bash
python lempel_ziv.py original.txt compressed.lzw
```

## 코드 개선 제안

1.  **`add_key_to_lexicon`의 비효율성**: 이 함수는 `lexicon.pop()`을 사용하고, 사전 크기가 2의 거듭제곱이 될 때마다 전체 사전을 순회하며 값을 수정합니다. 이는 매우 비효율적입니다. LZW의 표준 구현에서는 사전을 이렇게 수정하지 않습니다. 사전은 계속 커지기만 하며, 코드 길이는 필요할 때 동적으로 결정됩니다. 이 함수를 제거하고 `compress_data` 내에서 사전을 직접 관리하는 것이 더 효율적입니다.

2.  **`compress_data`의 비효율성**: `while curr_string != "" and curr_string not in lexicon: curr_string += "0"` 부분은 압축되지 않은 나머지 비트들을 처리하기 위한 것으로 보이지만, 이는 데이터 손실을 유발할 수 있으며 올바른 LZW 처리 방식이 아닙니다. 압축 루프가 끝난 후 남은 `curr_string`이 있다면, 그에 해당하는 코드를 결과에 추가해야 합니다.

3.  **오류 처리**: `read_file_binary`와 `write_file_binary`에서 `sys.exit()`를 호출하는 대신, 예외(Exception)를 발생시켜 호출하는 쪽(예: `compress` 함수)에서 `try...except` 블록으로 처리하도록 하면 모듈의 재사용성이 높아집니다.

4.  **쌍을 이루는 복원 스크립트**: 이 스크립트는 `lempel_ziv_decompress.py`와 쌍을 이룹니다. 두 스크립트의 사전 관리 로직이 정확히 대칭을 이루어야 올바르게 동작합니다. 현재 구현은 복잡하고 비표준적인 사전 관리 방식으로 인해, 일부 데이터에 대해 압축-복원 과정이 실패할 가능성이 높습니다. 더 간단하고 표준적인 LZW 알고리즘으로 재작성하는 것을 강력히 권장합니다.