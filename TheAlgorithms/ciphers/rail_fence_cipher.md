# `rail_fence_cipher.py` 코드 설명

이 문서는 `rail_fence_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 문자의 위치를 재배열하는 간단한 형태의 전치 암호(transposition cipher)인 **레일 펜스 암호(Rail Fence Cipher)**를 구현합니다.

## 목차
1.  레일 펜스 암호란?
2.  함수 설명
    -   `encrypt(input_string, key)`
    -   `decrypt(input_string, key)`
    -   `bruteforce(input_string)`
3.  실행 방법
4.  코드 개선 제안

## 레일 펜스 암호란?

레일 펜스 암호는 평문을 여러 줄(rail)에 걸쳐 지그재그(zigzag) 형태로 쓴 다음, 각 줄을 순서대로 읽어 암호문을 만드는 방식입니다. 여기서 사용되는 줄의 개수가 **키(key)**가 됩니다.

**암호화 예시 (키 = 3):**
1.  평문 "WE ARE DISCOVERED"를 3줄에 걸쳐 지그재그로 씁니다.
    ```
    W . . . E . . . C . . . V . . . D
    . E . R . D . S . O . E . E . E .
    . . A . . . I . . . R . . . R . .
    ```
2.  각 줄을 순서대로 읽어 암호문을 만듭니다.
    -   첫 번째 줄: `WECVD`
    -   두 번째 줄: `ERDSOEE`
    -   세 번째 줄: `AIRR`
    -   최종 암호문: `WECVDERDSOEEAIRR`

복호화는 이 과정의 역순으로, 암호문의 길이를 바탕으로 각 줄에 몇 개의 문자가 들어갈지 계산한 후, 다시 지그재그 형태로 읽어 평문을 복원합니다.

## 함수 설명

### `encrypt(input_string: str, key: int) -> str`

주어진 문자열을 레일 펜스 암호로 **암호화**합니다.

-   **알고리즘**:
    1.  `key` 개수만큼의 빈 리스트를 가진 `temp_grid`를 생성합니다.
    2.  입력 문자열의 각 문자를 순회하면서, 지그재그 패턴에 따라 현재 문자가 위치할 행(rail)의 인덱스를 계산합니다.
    3.  계산된 인덱스에 해당하는 행에 문자를 추가합니다.
    4.  모든 문자를 배치한 후, 각 행의 문자들을 순서대로 이어 붙여 최종 암호문을 생성합니다.

### `decrypt(input_string: str, key: int) -> str`

레일 펜스 암호로 암호화된 문자열을 **복호화**합니다.

-   **알고리즘**:
    1.  먼저, 암호문 없이 평문의 길이와 키를 사용하여 각 행에 몇 개의 문자가 들어갈지 계산하여 격자(grid)의 "틀"을 만듭니다.
    2.  암호문을 순서대로 읽으면서, 이 틀에 따라 각 행을 채워 넣습니다.
    3.  문자가 모두 채워진 격자를 다시 지그재그 형태로 읽으면서 원래의 평문을 복원합니다.

### `bruteforce(input_string: str) -> dict[int, str]`

암호문을 가능한 모든 키로 복호화하여 **전사 공격(Brute-Force Attack)**을 수행합니다.

-   **역할**: 키를 모를 때, 1부터 암호문 길이-1까지의 모든 키를 시도하여 복호화된 모든 결과를 딕셔너리 형태로 반환합니다. 사용자는 이 결과들 중에서 의미 있는 문장을 찾아 원래의 평문과 키를 유추할 수 있습니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python rail_fence_cipher.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **지그재그 인덱스 계산 로직**: `encrypt`와 `decrypt` 함수에서 지그재그 패턴의 인덱스를 계산하는 로직이 중복됩니다. 이 로직을 별도의 헬퍼 함수(예: `get_zigzag_indices(length, key)`)로 분리하면 코드 중복을 줄이고 가독성을 높일 수 있습니다.

    ```python
    # 개선 제안 예시
    def get_zigzag_indices(length: int, key: int) -> list[int]:
        lowest = key - 1
        if lowest == 0:
            return [0] * length
        
        indices = []
        for i in range(length):
            num = i % (lowest * 2)
            num = min(num, lowest * 2 - num)
            indices.append(num)
        return indices
    ```

2.  **`decrypt` 함수의 복잡성**: `decrypt` 함수의 로직, 특히 격자의 틀을 만들고 채우는 과정이 다소 복잡합니다. 암호화 시 각 문자가 최종적으로 어느 위치로 이동하는지를 계산하여, 복호화 시에는 그 역연산을 수행하는 방식으로 접근하면 로직을 더 단순화할 수 있습니다.

3.  **`bruteforce` 함수의 범위**: 현재 `bruteforce`는 `range(1, len(input_string))`까지 모든 키를 시도합니다. 키가 `len(input_string) // 2`를 넘어가면 패턴이 단순해지거나 의미가 없어지므로, 탐색 범위를 줄여 효율성을 높일 수 있습니다. 하지만 현재 방식도 작은 텍스트에서는 문제가 되지 않습니다.

4.  **사용자 인터페이스 추가**: `if __name__ == "__main__"` 블록에 `input()` 함수를 사용하여 사용자로부터 메시지와 키, 모드를 직접 입력받아 암호화를 시연하는 기능을 추가하면 스크립트의 활용도가 높아집니다.