# `lempel_ziv_decompress.py` 코드 설명

이 문서는 `lempel_ziv_decompress.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 `lempel_ziv.py`에 의해 **렘펠-지브-웰치(Lempel-Ziv-Welch, LZW)** 알고리즘으로 압축된 파일을 다시 원래의 데이터로 **복원(decompression)**하는 기능을 구현합니다.

## 목차
1.  LZW 압축 해제란?
2.  함수 설명
    -   `read_file_binary(file_path)`
    -   `decompress_data(data_bits)`
    -   `remove_prefix(data_bits)`
    -   `write_file_binary(file_path, to_write)`
    -   `compress(source_path, destination_path)`
3.  실행 방법
4.  코드 개선 제안

## LZW 압축 해제란?

LZW 압축 해제는 압축 과정에서 생성된 코드 시퀀스를 다시 원래의 데이터 스트림으로 변환하는 과정입니다. 압축과 동일한 방식으로 사전을 동적으로 구축하면서, 입력된 코드를 사전에 있는 문자열로 치환하여 원본 데이터를 복원합니다.

이 스크립트는 `lempel_ziv.py`와 쌍을 이루어 동작하도록 설계되었습니다.

## 함수 설명

### `read_file_binary(file_path: str) -> str`

지정된 파일을 바이너리 모드로 읽어, 그 내용을 '0'과 '1'로 이루어진 하나의 긴 비트 문자열로 변환하여 반환합니다.

### `decompress_data(data_bits: str) -> str`

주어진 비트 문자열을 LZW 알고리즘을 사용하여 압축 해제합니다.

-   **알고리즘**:
    1.  '0'과 '1'로 초기화된 사전을 생성합니다.
    2.  입력된 비트 문자열(`data_bits`)을 순회하면서, 사전에 존재하는 가장 긴 코드(`curr_string`)를 찾습니다.
    3.  해당 코드를 사전에 있는 원래의 문자열로 치환하여 결과에 추가합니다.
    4.  압축 과정과 동일한 규칙에 따라 사전을 업데이트합니다. (새로운 코드와 문자열을 사전에 추가)
    5.  모든 비트 문자열을 처리할 때까지 이 과정을 반복합니다.

> **주의**: 이 함수의 사전 업데이트 로직은 `lempel_ziv.py`의 압축 로직과 정확히 대칭되지 않아, 일부 데이터에 대해 올바르게 복원되지 않을 수 있습니다. (개선 제안 참조)

### `remove_prefix(data_bits: str) -> str`

압축된 데이터의 맨 앞에 추가된 원본 파일 크기 정보를 제거합니다. 이 크기 정보는 엘리어스 감마 코딩(Elias gamma coding) 방식으로 인코딩되어 있습니다.

-   **알고리즘**: '1'이 나올 때까지의 '0'의 개수를 세어, 접두사의 길이를 파악하고 해당 부분을 데이터에서 제거합니다.

### `write_file_binary(file_path: str, to_write: str) -> None`

복원된 비트 문자열을 바이너리 파일로 씁니다.

-   **알고리즘**:
    1.  비트 문자열을 8비트(1바이트) 단위로 나눕니다.
    2.  압축 시 추가된 패딩을 처리하기 위해, 마지막 바이트를 특별히 처리합니다. (이 부분에 논리적 오류가 있을 수 있습니다.)
    3.  각 8비트 덩어리를 정수로 변환하고, 이를 바이트로 변환하여 파일에 씁니다.

### `compress(source_path: str, destination_path: str) -> None`

전체 압축 해제 과정을 총괄하는 메인 함수입니다. (함수 이름이 `compress`로 잘못되어 있습니다.)

-   **동작**:
    1.  `read_file_binary`로 압축된 파일을 읽습니다.
    2.  `remove_prefix`로 파일 크기 정보를 제거합니다.
    3.  `decompress_data`로 데이터를 복원합니다.
    4.  `write_file_binary`로 복원된 데이터를 파일에 씁니다.

## 실행 방법

이 스크립트는 커맨드 라인에서 압축된 파일 경로와 복원할 파일 경로를 인자로 받아 실행합니다.

```bash
# lempel_ziv.py로 먼저 파일을 압축합니다.
python lempel_ziv.py original.txt compressed.lzw

# 압축된 파일을 복원합니다.
python lempel_ziv_decompress.py compressed.lzw decompressed.txt
```

## 코드 개선 제안

1.  **함수 이름 수정**: `compress`라는 함수 이름은 명백히 잘못되었습니다. `decompress`로 변경해야 코드의 역할을 정확히 나타낼 수 있습니다.

2.  **`decompress_data` 로직 수정**: 현재 `decompress_data`의 사전 업데이트 로직은 압축 로직과 정확히 일치하지 않습니다. 올바른 LZW 압축 해제 알고리즘은 "현재 코드"와 "이전 코드"를 사용하여 사전을 구축해야 합니다. 이 부분을 수정하지 않으면 많은 경우 복원이 실패합니다.

3.  **`write_file_binary` 버그 수정**: 이 함수는 마지막 바이트를 처리하는 로직에서 `result_byte_array[:-1]`를 사용하여 마지막 바이트를 항상 무시하고 있습니다. 이로 인해 파일의 마지막 부분이 손실됩니다. 압축 시 추가된 '1' 비트와 그 뒤의 '0' 패딩을 정확히 찾아 제거하는 로직으로 수정해야 합니다.

    ```diff
    --- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/compression/lempel_ziv_decompress.py
    +++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/compression/lempel_ziv_decompress.py
    @@ -81,13 +81,17 @@
     Writes given to_write string (should only consist of 0's and 1's) as bytes in the
     file
     """
-    byte_length = 8
+    # Find the end of the actual data before padding
+    try:
+        last_one_index = to_write.rindex("1")
+        to_write = to_write[:last_one_index]
+    except ValueError:
+        # No '1' found, might be an empty or all-zero string
+        pass
+
+    byte_length = 8
     try:
         with open(file_path, "wb") as opened_file:
             result_byte_array = [
@@ -95,16 +99,6 @@
                 for i in range(0, len(to_write), byte_length)
             ]
 
-            if len(result_byte_array[-1]) % byte_length == 0:
-                result_byte_array.append("10000000")
-            else:
-                result_byte_array[-1] += "1" + "0" * (
-                    byte_length - len(result_byte_array[-1]) - 1
-                )
-
-            for elem in result_byte_array[:-1]:
+            for elem in result_byte_array:
                 opened_file.write(int(elem, 2).to_bytes(1, byteorder="big"))
     except OSError:
         print("File not accessible")

    ```
    > **참고**: 위 diff는 `write_file_binary`의 패딩 처리 문제를 해결하기 위한 한 가지 접근 방식입니다. 더 견고한 방법은 압축 시 원본 비트 길이를 저장하고, 복원 시 그 길이만큼만 읽는 것입니다.

4.  **오류 처리**: `read_file_binary`와 `write_file_binary`에서 `sys.exit()`를 호출하는 대신, 예외를 발생시켜 호출하는 쪽에서 처리하도록 하면 모듈의 재사용성이 높아집니다.

