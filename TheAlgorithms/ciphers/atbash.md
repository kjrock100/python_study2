# `atbash.py` 코드 설명

이 문서는 `atbash.py` 파이썬 스크립트에 포함된 함수들을 설명합니다. 이 스크립트는 가장 간단한 형태의 치환 암호 중 하나인 **아트바시(Atbash) 암호**를 구현합니다.

## 목차
1.  아트바시 암호란?
2.  함수 설명
    -   `atbash_slow(sequence)`
    -   `atbash(sequence)`
    -   `benchmark()`
3.  실행 방법
4.  코드 개선 제안

## 아트바시 암호란?

아트바시 암호는 알파벳의 순서를 완전히 뒤집어 문자를 치환하는 방식입니다.

-   첫 번째 문자인 `A`는 마지막 문자인 `Z`로, 두 번째 문자인 `B`는 끝에서 두 번째 문자인 `Y`로 치환됩니다.
-   이러한 규칙이 대문자와 소문자에 각각 적용됩니다.
-   암호화와 복호화 과정이 동일하다는 특징이 있습니다.

## 함수 설명

### `atbash_slow(sequence: str) -> str`

ASCII 코드 값을 직접 계산하여 아트바시 암호화를 수행하는 첫 번째 구현 방식입니다.

-   **알고리즘**:
    1.  입력된 문자열(`sequence`)의 각 문자를 순회합니다.
    2.  `ord()` 함수로 문자의 ASCII 코드 값을 얻습니다.
    3.  ASCII 값의 범위를 확인하여 문자가 대문자인지(`65`~`90`), 소문자인지(`97`~`122`) 판별합니다.
    4.  **대문자**: `155`에서 현재 문자의 ASCII 값을 빼서 변환될 문자의 ASCII 값을 계산합니다. (`155 = ord('A') + ord('Z')`)
    5.  **소문자**: `219`에서 현재 문자의 ASCII 값을 빼서 변환될 문자의 ASCII 값을 계산합니다. (`219 = ord('a') + ord('z')`)
    6.  `chr()` 함수를 사용하여 계산된 ASCII 값을 다시 문자로 변환합니다.
    7.  알파벳이 아닌 문자는 그대로 둡니다.

### `atbash(sequence: str) -> str`

파이썬의 내장 모듈과 문자열 기능을 활용하여 더 간결하고 읽기 쉽게 구현한 방식입니다.

-   **알고리즘**:
    1.  `string.ascii_letters`를 사용하여 원본 알파벳 문자열(`'abc...xyzABC...XYZ'`)을 만듭니다.
    2.  문자열 슬라이싱(`[::-1]`)을 이용해 원본 알파벳을 뒤집은 문자열(`'zyx...cbaZYX...CBA'`)을 만듭니다.
    3.  리스트 컴프리헨션을 사용하여 입력 문자열의 각 문자를 순회합니다.
    4.  문자가 원본 알파벳에 포함되어 있으면, `index()` 메서드로 해당 문자의 위치를 찾고, 그 위치를 이용해 뒤집힌 알파벳 문자열에서 치환될 문자를 가져옵니다.
    5.  알파벳이 아닌 문자는 그대로 유지합니다.
    6.  `"".join()`을 사용하여 변환된 문자 리스트를 최종 문자열로 합칩니다.

이 방식은 `atbash_slow`에 비해 "매직 넘버"(155, 219 등)를 사용하지 않아 코드가 더 명확하고 유지보수가 쉽습니다.

### `benchmark()`

`atbash_slow`와 `atbash` 두 함수의 실행 성능을 비교하고 측정합니다.

-   **동작**: `timeit` 모듈을 사용하여 각 함수가 `string.printable`(출력 가능한 모든 ASCII 문자)을 암호화하는 데 걸리는 시간을 측정하고 결과를 출력합니다. 일반적으로 `atbash` 함수가 더 빠른 성능을 보입니다.

## 실행 방법

스크립트를 직접 실행하면 몇 가지 예제에 대한 암호화 결과를 보여주고, 이어서 두 함수의 성능 벤치마크 결과를 출력합니다.

```bash
python atbash.py
```

**실행 결과 예시:**
```
ABCDEFGH encrypted in atbash: ZYXWVUTS
123GGjj encrypted in atbash: 123TTqq
testStringtest encrypted in atbash: gvhgHgirmtgvhg
with space encrypted in atbash: drgs hkzxv
Running performance benchmarks...
> atbash_slow() 20.0... seconds
>      atbash() 11.5... seconds
```

## 코드 개선 제안

1.  **`atbash_slow`의 가독성 향상**: `atbash_slow` 함수에 사용된 `155`, `219`와 같은 "매직 넘버"는 코드의 의도를 파악하기 어렵게 만듭니다. 이 숫자들을 `ord('A') + ord('Z')`와 같이 계산 과정으로 대체하면 가독성이 크게 향상됩니다.

    ```python
    # 개선 제안 예시
    UPPER_OFFSET = ord('A') + ord('Z')  # 155
    LOWER_OFFSET = ord('a') + ord('z')  # 219

    if 'A' <= i <= 'Z':
        output += chr(UPPER_OFFSET - extract)
    elif 'a' <= i <= 'z':
        output += chr(LOWER_OFFSET - extract)
    ```

2.  **`atbash`의 효율성 개선**: `atbash` 함수는 `letters.index(c)`를 루프마다 호출합니다. 이는 문자열이 길어질수록 비효율적일 수 있습니다. `str.maketrans()`와 `str.translate()`를 사용하면 한 번의 테이블 생성으로 매우 빠른 변환이 가능합니다.

    ```python
    # 개선 제안 예시
    import string

    def atbash_fast(sequence: str) -> str:
        alphabets = string.ascii_lowercase + string.ascii_uppercase
        reversed_alphabets = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
        translation_table = str.maketrans(alphabets, reversed_alphabets)
        return sequence.translate(translation_table)
    ```
    이 `atbash_fast` 함수는 일반적으로 `atbash` 함수보다 훨씬 빠릅니다.

