# `beaufort_cipher.py` 코드 설명

이 문서는 `beaufort_cipher.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 비즈네르 암호(Vigenère cipher)와 유사한 다중 문자 치환 암호인 **보퍼트 암호(Beaufort Cipher)**의 한 변형을 구현합니다.

## 목차
1.  보퍼트 암호란?
2.  함수 설명
    -   `generate_key(message, key)`
    -   `cipher_text(message, key_new)`
    -   `original_text(cipher_text, key_new)`
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 보퍼트 암호란?

보퍼트 암호는 키워드를 사용하는 다중 문자 치환 암호입니다. 표준 보퍼트 암호의 암호화 공식은 `암호문(C) ≡ (키(K) - 평문(P)) (mod 26)` 이며, 암호화와 복호화 과정이 동일한 특징(reciprocal cipher)을 가집니다.

하지만 이 스크립트에서 구현된 방식은 `암호문(C) ≡ (평문(P) - 키(K)) (mod 26)` 공식을 사용합니다. 이는 **비즈네르 암호의 복호화 공식**과 동일하며, "보퍼트-비즈네르 암호"라고도 불리는 변형입니다.

## 함수 설명

### `generate_key(message: str, key: str) -> str`

평문(`message`)의 길이에 맞게 키(`key`)를 반복하여 새로운 키 문자열을 생성합니다.

-   **역할**: 다중 문자 치환에 필요한 길이의 키 스트림을 만듭니다.
-   **알고리즘**: 원본 키를 평문의 길이와 같아질 때까지 순환적으로 이어 붙입니다.

```python
>>> generate_key("THE GERMAN ATTACK", "SECRET")
'SECRETSECRETSECRE'
```

### `cipher_text(message: str, key_new: str) -> str`

주어진 메시지를 보퍼트 암호 변형 방식으로 **암호화**합니다.

-   **알고리즘**:
    1.  평문과 생성된 키를 한 글자씩 순회합니다.
    2.  각 문자의 알파벳 순서(A=0, B=1, ...)를 숫자로 변환합니다.
    3.  `새로운 인덱스 = (평문 인덱스 - 키 인덱스) % 26` 공식을 적용합니다.
    4.  계산된 인덱스를 다시 알파벳 문자로 변환하여 암호문에 추가합니다.
    5.  공백은 그대로 유지됩니다.

### `original_text(cipher_text: str, key_new: str) -> str`

암호화된 텍스트를 원래의 평문으로 **복호화**합니다.

-   **알고리즘**:
    1.  암호문과 생성된 키를 한 글자씩 순회합니다.
    2.  `새로운 인덱스 = (암호문 인덱스 + 키 인덱스) % 26` 공식을 적용하여 평문 인덱스를 복원합니다.
    3.  계산된 인덱스를 다시 알파벳 문자로 변환하여 평문에 추가합니다.
    4.  `+ 26` 부분은 불필요하지만 결과에 영향을 주지는 않습니다.

### `main()`

미리 정의된 메시지와 키를 사용하여 암호화 및 복호화 과정을 시연하고 결과를 출력합니다.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 각 함수의 정확성을 테스트한 후, `main` 함수가 실행되어 암호화/복호화 예제를 보여줍니다.

```bash
python beaufort_cipher.py
```

**실행 결과:**
```
Encrypted Text = BDC PAYUWL JPAIYI
Original Text = THE GERMAN ATTACK
```

## 코드 개선 제안

1.  **`generate_key` 함수 단순화**: 현재 `generate_key` 함수의 `while` 루프는 복잡합니다. `itertools.cycle`이나 모듈러 연산(`%`)을 사용하면 더 간결하고 효율적으로 구현할 수 있습니다.

    ```python
    # 개선 제안 예시
    from itertools import cycle

    def generate_key_simple(message: str, key: str) -> str:
        key_cycle = cycle(key)
        return "".join(next(key_cycle) for _ in range(len(message)))
    ```

2.  **암호화/복호화 로직 통합**: 암호화와 복호화 함수는 매우 유사합니다. 연산자(더하기/빼기)를 인자로 받는 단일 함수로 통합하여 코드 중복을 줄일 수 있습니다.

3.  **전역 변수 지양**: `dict1`과 `dict2`는 전역 변수로 선언되어 있습니다. 이들을 클래스 멤버로 캡슐화하거나, 함수 내에서 지역적으로 생성하여 사용하는 것이 코드의 명확성과 재사용성을 높입니다.

4.  **알고리즘 명확화**: 스크립트의 주석이나 docstring에 이 구현이 표준 보퍼트 암호가 아닌, `C ≡ (P - K) (mod 26)` 공식을 사용하는 변형임을 명시하면 사용자의 혼동을 줄일 수 있습니다.
