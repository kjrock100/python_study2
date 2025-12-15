# `xor_cipher.py` 코드 설명

이 문서는 `xor_cipher.py` 파이썬 스크립트에 포함된 `XORCipher` 클래스를 설명합니다. 이 스크립트는 비트 연산자인 **XOR(배타적 논리합)**을 이용하는 간단한 스트림 암호인 **XOR 암호(XOR Cipher)**를 구현합니다.

## 목차
1.  XOR 암호란?
2.  `XORCipher` 클래스
    -   `__init__(key)`
    -   `encrypt(content, key)`
    -   `decrypt(content, key)`
    -   `encrypt_string(content, key)`
    -   `decrypt_string(content, key)`
    -   `encrypt_file(file, key)`
    -   `decrypt_file(file, key)`
3.  실행 방법
4.  코드 개선 제안

## XOR 암호란?

XOR 암호는 평문의 각 비트를 키의 해당 비트와 XOR 연산하여 암호문을 만드는 방식입니다. XOR 연산은 같은 값을 입력하면 0, 다른 값을 입력하면 1을 반환하는 특징이 있습니다.

`A XOR B = C`

XOR 암호의 가장 중요한 특징은 **상호적(reciprocal)**이라는 점입니다. 암호문에 동일한 키를 사용하여 다시 XOR 연산을 수행하면 원래의 평문으로 돌아옵니다.

`C XOR B = A`

이 때문에 암호화와 복호화에 동일한 알고리즘을 사용할 수 있습니다.

## `XORCipher` 클래스

XOR 암호화 및 복호화 기능을 캡슐화한 클래스입니다.

### `__init__(key: int = 0)`

클래스 인스턴스를 초기화합니다. 사용자가 키를 제공하지 않으면 기본값으로 `0`을 사용합니다.

### `encrypt(content: str, key: int) -> list[str]`

문자열을 암호화하여 문자 리스트를 반환합니다.

-   **알고리즘**:
    1.  입력된 문자열(`content`)의 각 문자의 ASCII 값에 `key`를 XOR 연산합니다.
    2.  결과 ASCII 값을 다시 문자로 변환하여 리스트에 추가합니다.

### `decrypt(content: list[str], key: int) -> list[str]`

암호화된 문자 리스트를 복호화합니다.

-   **알고리즘**: XOR 암호의 특성상, 이 함수의 내부 로직은 `encrypt`와 동일합니다.

### `encrypt_string(content: str, key: int = 0) -> str`

문자열을 암호화하여 하나의 문자열로 반환합니다. `encrypt`와 유사하지만, 반환 타입이 다릅니다.

### `decrypt_string(content: str, key: int = 0) -> str`

암호화된 문자열을 복호화합니다. `encrypt_string`과 동일한 로직을 사용합니다.

### `encrypt_file(file: str, key: int = 0) -> bool`

지정된 파일을 읽어 암호화하고, 그 결과를 `encrypt.out` 파일에 저장합니다.

-   **동작**: 파일의 각 줄을 `encrypt_string` 함수를 사용하여 암호화하고 새로운 파일에 씁니다.

### `decrypt_file(file: str, key: int = 0) -> bool`

암호화된 파일을 읽어 복호화하고, 그 결과를 `decrypt.out` 파일에 저장합니다.

## 실행 방법

스크립트 파일 하단의 주석 처리된 테스트 코드를 해제하여 실행할 수 있습니다.

1.  `xor_cipher.py` 파일의 맨 아래쪽 테스트 코드를 주석 해제합니다.
2.  필요하다면, `encrypt_file` 테스트를 위해 `test.txt` 파일을 생성합니다.
3.  스크립트를 실행합니다.
    ```bash
    python xor_cipher.py
    ```

## 코드 개선 제안

1.  **코드 중복 제거**: `encrypt`와 `decrypt`, `encrypt_string`과 `decrypt_string` 함수는 내부 로직이 완전히 동일합니다. 이는 XOR 암호의 특징 때문입니다. 이들을 하나의 범용 함수(예: `process_data`)로 통합하고, `encrypt`와 `decrypt`는 이 범용 함수를 호출하는 별칭(alias)으로 만들면 코드 중복을 크게 줄일 수 있습니다.

    ```python
    # 개선 제안 예시
    def process_string(self, content: str, key: int = 0) -> str:
        # ... (XOR 로직 구현) ...
        return ans

    def encrypt_string(self, content: str, key: int = 0) -> str:
        return self.process_string(content, key)

    def decrypt_string(self, content: str, key: int = 0) -> str:
        return self.process_string(content, key)
    ```

2.  **키 처리 로직**: `key %= 255` 또는 `while key > 255: key -= 255`와 같이 키를 255로 제한하는 로직이 반복됩니다. 키는 어떤 정수든 될 수 있으며, `ord(ch) ^ key` 연산은 키의 크기에 상관없이 올바르게 동작합니다. 이 키 제한 로직은 불필요하며, 제거하는 것이 더 일반적이고 올바른 구현입니다.

3.  **입력 타입**: `decrypt` 함수는 `list[str]`를 입력으로 받지만, 다른 함수들은 `str`을 받습니다. 입력 타입을 일관성 있게 `str`으로 통일하는 것이 좋습니다.

4.  **파일 처리**: `encrypt_file`과 `decrypt_file`의 출력 파일 이름이 "encrypt.out", "decrypt.out"으로 하드코딩되어 있습니다. 출력 파일 이름을 함수의 인자로 받아 사용자가 지정할 수 있도록 하면 유연성이 향상됩니다.

5.  **정적 메서드**: 이 클래스는 상태(`self.__key`)를 가지지만, 모든 메서드가 `key`를 인자로 다시 받습니다. 만약 클래스 인스턴스에 저장된 키를 사용하도록 설계한다면, 메서드에서 `key` 인자를 선택적으로 만들고, 제공되지 않을 경우 `self.__key`를 사용하도록 수정할 수 있습니다. 만약 상태가 필요 없다면, 이 함수들을 클래스 밖으로 빼내어 모듈 수준의 함수로 만드는 것도 좋은 방법입니다.