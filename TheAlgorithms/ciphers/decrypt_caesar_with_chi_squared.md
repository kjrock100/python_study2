# `decrypt_caesar_with_chi_squared.py` 코드 설명

이 문서는 `decrypt_caesar_with_chi_squared.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 **카이제곱 통계(Chi-squared statistic)**를 이용하여 **카이사르 암호(Caesar Cipher)**로 암호화된 텍스트를 자동으로 해독하는 기능을 구현합니다.

## 목차
1.  카이제곱 통계를 이용한 암호 해독이란?
2.  함수 설명
    -   `decrypt_caesar_with_chi_squared(...)`
3.  실행 방법
4.  코드 개선 제안

## 카이제곱 통계를 이용한 암호 해독이란?

카이사르 암호는 키의 경우의 수가 적어 전사 공격(brute-force)이 쉽습니다. 하지만 전사 공격은 모든 해독 결과를 사람이 직접 보고 의미 있는 문장을 찾아야 하는 단점이 있습니다.

**카이제곱 통계를 이용한 해독**은 이 과정을 자동화합니다. 모든 언어에는 고유한 문자 빈도(frequency)가 있습니다. 예를 들어, 영어에서는 'e'가 가장 자주 사용됩니다. 카이제곱 검정은 어떤 텍스트의 문자 빈도가 특정 언어(여기서는 영어)의 표준 문자 빈도와 얼마나 유사한지를 측정하는 통계적 방법입니다.

해독 과정은 다음과 같습니다.
1.  암호문을 가능한 모든 키(0~25)로 복호화합니다.
2.  각 복호화 결과에 대해 카이제곱 통계 값을 계산합니다. 이 값은 해당 텍스트의 문자 빈도가 영어의 표준 빈도와 얼마나 다른지를 나타냅니다.
3.  **카이제곱 통계 값이 가장 낮은** 복호화 결과가 통계적으로 가장 영어 문장과 유사하므로, 가장 가능성 있는 평문으로 간주합니다.

## 함수 설명

### `decrypt_caesar_with_chi_squared(ciphertext, cipher_alphabet=None, frequencies_dict=None, case_sensitive=False)`

카이사르 암호문을 카이제곱 통계를 사용하여 해독하고, 가장 가능성 있는 키와 평문을 반환합니다.

-   **인자**:
    -   `ciphertext`: 해독할 암호문.
    -   `cipher_alphabet` (선택): 사용할 알파벳 리스트. 기본값은 영어 소문자.
    -   `frequencies_dict` (선택): 사용할 언어의 문자 빈도 딕셔너리. 기본값은 영어 빈도.
    -   `case_sensitive` (선택): 대소문자를 구분할지 여부.

-   **알고리즘**:
    1.  **모든 키 시도**: `0`부터 알파벳 길이-1까지의 모든 `shift` 값(키)에 대해 루프를 실행합니다.
    2.  **복호화**: 각 `shift` 값으로 암호문을 복호화합니다.
    3.  **카이제곱 통계 계산**:
        -   복호화된 텍스트의 각 문자에 대해, 해당 문자의 실제 등장 횟수(`occurrences`)를 셉니다.
        -   영어의 표준 빈도를 바탕으로 해당 문자가 텍스트에 등장할 기대 횟수(`expected`)를 계산합니다.
        -   `((occurrences - expected)² / expected)` 공식을 사용하여 각 문자의 카이제곱 값을 계산하고 모두 더하여 해당 `shift`에 대한 총 카이제곱 통계 값을 구합니다.
    4.  **결과 저장**: 각 `shift` 값과 그에 해당하는 카이제곱 통계 값, 그리고 복호화된 텍스트를 딕셔너리에 저장합니다.
    5.  **최적의 키 선택**: 저장된 결과 중에서 카이제곱 통계 값이 가장 작은 `shift`를 "가장 가능성 있는 키"로 선택합니다.

-   **반환값**: `(키, 카이제곱 값, 평문)` 형태의 튜플.

## 실행 방법

스크립트를 직접 실행하면 내장된 `doctest`를 통해 함수의 예제 코드가 실행되고, 함수의 정확성이 자동으로 테스트됩니다.

```bash
python decrypt_caesar_with_chi_squared.py
```

별도의 출력이 없다면 모든 테스트가 성공적으로 통과한 것입니다.

## 코드 개선 제안

1.  **카이제곱 계산 로직 개선**: 현재 카이제곱 통계 값을 계산하는 내부 루프는 비효율적입니다. 텍스트의 모든 문자를 순회하며 매번 `count()`를 호출하고 있습니다. 텍스트의 문자 빈도를 한 번만 계산한 후, 이를 바탕으로 카이제곱 값을 계산하는 것이 훨씬 효율적입니다.

    ```python
    # 개선 제안 예시
    from collections import Counter

    # ... (복호화 이후)
    
    chi_squared_statistic = 0.0
    text_length = len([c for c in decrypted_with_shift if c.lower() in frequencies])
    
    if text_length == 0:
        # 알파벳 문자가 없는 경우, 무한대 값을 주어 선택되지 않도록 함
        chi_squared_statistic = float('inf')
    else:
        # 텍스트의 문자 빈도를 한 번에 계산
        observed_counts = Counter(decrypted_with_shift.lower())
        
        for letter, expected_freq in frequencies.items():
            observed_count = observed_counts.get(letter, 0)
            expected_count = text_length * expected_freq
            
            if expected_count == 0:
                continue # 0으로 나누는 것을 방지

            chi_squared_statistic += ((observed_count - expected_count) ** 2) / expected_count
    ```

2.  **함수 분리**: `decrypt_caesar_with_chi_squared` 함수는 복호화와 통계 계산이라는 두 가지 주요 작업을 수행합니다. 카이사르 복호화 로직을 별도의 헬퍼 함수로 분리하면 코드의 구조가 더 명확해지고 재사용성이 높아집니다. 이는 `caesar_cipher.py`의 `decrypt` 함수를 활용하는 좋은 기회가 될 수 있습니다.

3.  **`case_sensitive` 로직 단순화**: `case_sensitive` 플래그에 따라 `if/else` 블록으로 코드가 나뉘어 있어 중복이 발생합니다. 복호화된 텍스트를 처리하기 전에 `lower()`를 적용할지 여부만 결정하고, 이후의 통계 계산 로직은 하나로 통일할 수 있습니다.

4.  **정렬 키 함수**: `chi_squared_statistic_values_sorting_key` 함수는 `min` 함수의 `key` 인자에 직접 람다(lambda) 함수를 사용하여 더 간결하게 표현할 수 있습니다.

    ```python
    # 개선 제안 예시
    most_likely_cipher = min(
        chi_squared_statistic_values,
        key=lambda k: chi_squared_statistic_values[k][0]
    )
    ```
