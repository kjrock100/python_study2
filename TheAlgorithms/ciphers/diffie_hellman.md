# `diffie_hellman.py` 코드 설명

이 문서는 `diffie_hellman.py` 파이썬 스크립트에 포함된 `DiffieHellman` 클래스를 설명합니다. 이 스크립트는 안전하지 않은 통신 채널에서 두 당사자가 비밀 키를 안전하게 공유할 수 있도록 하는 **디피-헬만 키 교환(Diffie-Hellman Key Exchange)** 프로토콜을 구현합니다.

## 목차
1.  디피-헬만 키 교환이란?
2.  `DiffieHellman` 클래스
    -   `__init__(group)`
    -   `get_private_key()`
    -   `generate_public_key()`
    -   `is_valid_public_key(key)`
    -   `generate_shared_key(other_key_str)`
    -   `is_valid_public_key_static(...)`
    -   `generate_shared_key_static(...)`
3.  실행 방법
4.  코드 개선 제안

## 디피-헬만 키 교환이란?

디피-헬만 키 교환은 암호학적 프로토콜로, 두 참여자(예: 앨리스와 밥)가 사전에 어떠한 비밀 정보도 공유하지 않은 상태에서 공개된 통신망을 통해 공통의 비밀 키를 생성할 수 있게 해줍니다.

**동작 원리**:
1.  **공개 매개변수 동의**: 두 참여자는 미리 약속된 매우 큰 소수 `p`(prime)와 생성자 `g`(generator)를 공유합니다. 이 스크립트에서는 RFC 3526에 정의된 표준 그룹들을 사용합니다.
2.  **개인키 생성**: 각 참여자는 자신만 아는 비밀 정수(개인키) `a`와 `b`를 각각 생성합니다.
3.  **공개키 생성 및 교환**:
    -   앨리스는 `A = g^a mod p`를 계산하여 밥에게 전송합니다.
    -   밥은 `B = g^b mod p`를 계산하여 앨리스에게 전송합니다.
4.  **공유 비밀키 생성**:
    -   앨리스는 밥에게 받은 `B`를 사용하여 `S = B^a mod p`를 계산합니다.
    -   밥은 앨리스에게 받은 `A`를 사용하여 `S = A^b mod p`를 계산합니다.
5.  **결과**: 수학적으로 `(g^b)^a mod p`와 `(g^a)^b mod p`는 동일하므로, 두 참여자는 같은 공유 비밀키 `S`를 갖게 됩니다. 이 키는 이후의 대칭키 암호화 통신에 사용될 수 있습니다.

## `DiffieHellman` 클래스

디피-헬만 키 교환 프로토콜의 한쪽 참여자를 나타내는 클래스입니다.

### `__init__(group: int = 14)`

클래스 인스턴스를 초기화합니다.
-   `group`: 사용할 디피-헬만 그룹 번호(기본값 14, 2048-bit). `primes` 딕셔너리에서 해당 그룹의 소수(`prime`)와 생성자(`generator`)를 가져옵니다.
-   `__private_key`: `os.urandom`을 사용하여 암호학적으로 안전한 32바이트 길이의 무작위 개인키를 생성합니다.

### `get_private_key() -> str`

생성된 개인키를 16진수 문자열 형태로 반환합니다.

### `generate_public_key() -> str`

자신의 개인키와 공개 매개변수(`g`, `p`)를 사용하여 공개키(`g^private_key mod p`)를 계산하고, 16진수 문자열로 반환합니다.

### `is_valid_public_key(key: int) -> bool`

상대방의 공개키가 NIST SP 800-56A 표준에 따라 유효한지 검증합니다. 이는 특정 공격(예: 소그룹 공격)을 방지하는 데 도움이 됩니다.

### `generate_shared_key(other_key_str: str) -> str`

상대방의 공개키(`other_key_str`)를 받아 공유 비밀키를 생성합니다.
-   **알고리즘**:
    1.  상대방의 공개키 유효성을 `is_valid_public_key`로 검증합니다.
    2.  `공유키 = (상대방 공개키)^private_key mod p` 공식을 사용하여 공유 비밀키를 계산합니다.
    3.  계산된 공유키(정수)를 문자열로 변환하고 `sha256` 해시 함수를 적용하여 최종적인 256비트 공유 비밀키를 생성합니다. 이는 공유키의 길이를 고정하고 편향을 제거하는 데 도움이 됩니다.

### `is_valid_public_key_static(...)` 와 `generate_shared_key_static(...)`

이들은 각각 `is_valid_public_key`와 `generate_shared_key`의 **정적 메서드(static method)** 버전입니다. 클래스 인스턴스를 생성하지 않고도 키 유효성 검증 및 공유키 생성을 수행할 수 있게 해줍니다. 모든 필요한 값(개인키, 공개키, 그룹 정보)을 인자로 직접 전달받아야 합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 클래스의 예제 코드가 실행되고, 키 교환 과정의 정확성이 자동으로 테스트됩니다.

```bash
python diffie_hellman.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **정적 메서드와 인스턴스 메서드의 중복**: `is_valid_public_key`와 `is_valid_public_key_static`처럼, 인스턴스 메서드와 정적 메서드가 거의 동일한 로직을 중복으로 가지고 있습니다. 정적 메서드를 기본 구현으로 두고, 인스턴스 메서드가 이 정적 메서드를 호출하도록 하여 코드 중복을 줄일 수 있습니다.

    ```python
    # 개선 제안 예시
    def is_valid_public_key(self, key: int) -> bool:
        return DiffieHellman.is_valid_public_key_static(key, self.prime)

    def generate_shared_key(self, other_key_str: str) -> str:
        private_key_hex = hex(self.__private_key)[2:]
        return DiffieHellman.generate_shared_key_static(
            private_key_hex, other_key_str, group=self.group_id # group_id를 __init__에 저장해야 함
        )
    ```

2.  **키 타입의 일관성**: `get_private_key`와 `generate_public_key`는 16진수 문자열을 반환하지만, `generate_shared_key`는 해시된 16진수 문자열을 반환합니다. 반환되는 키의 "형태"가 다르다는 점을 함수 이름이나 docstring에 더 명확하게 명시하면 좋습니다. (예: `generate_shared_secret_hash`)

3.  **개인키 길이**: 개인키를 `urandom(32)`로 생성하여 256비트로 고정하고 있습니다. 이는 충분히 안전하지만, 사용하는 그룹의 소수(`prime`) 크기에 맞춰 개인키의 크기를 조절하는 것이 더 일반적인 접근 방식입니다. (예: 소수의 비트 길이와 비슷한 길이의 개인키)

4.  **`primes` 딕셔너리 관리**: `primes` 딕셔너리는 매우 큰 상수로, 스크립트의 가독성을 저해할 수 있습니다. 이 데이터를 별도의 JSON 파일이나 설정 파일로 분리하여 로드하는 방식을 고려하면 코드가 더 깔끔해집니다.
