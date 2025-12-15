# `polybius.py` 코드 설명

이 문서는 `polybius.py` 파이썬 스크립트에 포함된 `PolybiusCipher` 클래스를 설명합니다. 이 스크립트는 각 문자를 2차원 격자(grid)의 좌표로 변환하는 **폴리비오스 암호(Polybius Cipher)**를 구현합니다.

## 목차
1.  폴리비오스 암호란?
2.  `PolybiusCipher` 클래스
    -   `__init__()`
    -   `letter_to_numbers(letter)`
    -   `numbers_to_letter(index1, index2)`
    -   `encode(message)`
    -   `decode(message)`
3.  실행 방법
4.  코드 개선 제안

## 폴리비오스 암호란?

폴리비오스 암호는 2차원 격자(보통 5x5 크기)를 사용하여 각 문자를 두 개의 숫자로 이루어진 좌표로 치환하는 방식입니다.

1.  **암호판 생성**: 5x5 격자에 알파벳을 채웁니다. 26개의 알파벳을 모두 담기 위해 보통 'I'와 'J'를 같은 칸에 둡니다.
2.  **암호화**: 평문의 각 문자를 암호판에서 찾아 해당하는 행(row)과 열(column) 번호로 변환합니다. 예를 들어, 'A'는 '11', 'B'는 '12'로 변환될 수 있습니다.
3.  **복호화**: 두 자리 숫자 쌍을 다시 암호판의 좌표로 사용하여 원래의 문자로 복원합니다.

이 암호 자체는 보안성이 매우 낮지만, 비피드(Bifid) 암호와 같은 다른 복잡한 암호의 구성 요소로 사용됩니다.

> **참고**: 이 스크립트는 `numpy` 라이브러리를 사용하여 암호판을 관리합니다.

## `PolybiusCipher` 클래스

폴리비오스 암호화 및 복호화 기능을 캡슐화한 클래스입니다.

### `__init__()`

클래스 인스턴스를 초기화합니다. 5x5 크기의 폴리비오스 암호판을 `numpy` 배열로 생성하여 `self.SQUARE`에 저장합니다. 'j'는 'i'와 동일하게 취급되므로 암호판에 포함되지 않습니다.

### `letter_to_numbers(letter: str) -> np.ndarray`

주어진 문자에 해당하는 폴리비오스 암호판의 좌표(1-based 인덱스)를 `numpy` 배열로 반환합니다.

-   **알고리즘**: `np.where()`를 사용하여 암호판에서 문자의 위치를 찾고, 인덱스에 1을 더하여 반환합니다.

### `numbers_to_letter(index1: int, index2: int) -> str`

주어진 좌표(1-based 인덱스)에 해당하는 문자를 암호판에서 찾아 반환합니다.

### `encode(message: str) -> str`

주어진 메시지를 폴리비오스 암호로 **인코딩(암호화)**합니다.

-   **알고리즘**:
    1.  메시지를 소문자로 변환하고, 'j'를 'i'로 바꿉니다.
    2.  메시지의 각 문자를 순회하며, 문자가 공백이 아니면 `letter_to_numbers`를 이용해 좌표로 변환하고, 두 숫자를 문자열로 이어 붙여 결과에 추가합니다.
    3.  공백은 그대로 유지합니다.

```python
>>> PolybiusCipher().encode("test message")
'44154344 32154343112215'
```

### `decode(message: str) -> str`

암호화된 메시지를 원래의 평문으로 **디코딩(복호화)**합니다.

-   **알고리즘**:
    1.  입력된 메시지에서 공백을 임시로 두 개의 공백으로 바꿉니다. (이는 숫자 쌍과 공백을 구분하기 위한 트릭입니다.)
    2.  메시지를 두 글자씩 순회합니다.
    3.  두 글자가 모두 숫자이면, 이를 좌표로 사용하여 `numbers_to_letter`로 문자를 복원합니다.
    4.  두 글자가 공백이면, 하나의 공백으로 복원합니다.

## 실행 방법

이 스크립트는 직접 실행할 수 있는 `main` 블록이 없지만, `doctest`를 포함하고 있어 테스트를 통해 함수의 정확성을 검증할 수 있습니다.

```bash
python -m doctest -v polybius.py
```

## 코드 개선 제안

1.  **`numpy` 의존성 제거**: 이 알고리즘은 `numpy` 없이 표준 파이썬 딕셔너리로 더 간단하고 효율적으로 구현할 수 있습니다. `numpy`는 강력하지만, 이 작업에는 불필요한 외부 의존성입니다. 문자와 좌표를 미리 딕셔너리에 저장해두면 조회가 훨씬 빠릅니다.

    ```python
    # 개선 제안 예시
    class PolybiusCipherSimple:
        def __init__(self):
            square_str = "abcdefghiklmnopqrstuvwxyz"
            self.letter_to_coords = {ch: f"{(i//5)+1}{(i%5)+1}" for i, ch in enumerate(square_str)}
            self.coords_to_letter = {v: k for k, v in self.letter_to_coords.items()}
        
        def encode(self, message: str) -> str:
            # ... (딕셔너리 조회로 재작성)
    ```

2.  **효율적인 문자열 처리**: `encode`와 `decode` 함수에서 `encoded_message = encoded_message + ...`와 같이 루프 안에서 문자열을 반복적으로 더하는 것은 비효율적입니다. 문자 조각들을 리스트에 추가한 후, 마지막에 `"".join()`을 사용하여 한 번에 합치는 것이 훨씬 빠릅니다.

3.  **`decode` 함수 로직 단순화**: `decode` 함수의 공백 처리 로직(`message.replace(" ", "  ")`)은 다소 복잡하고 직관적이지 않습니다. 먼저 메시지를 공백 기준으로 나눈 후, 각 숫자 덩어리를 처리하는 방식이 더 명확합니다.

    ```python
    # decode 개선 제안 예시
    def decode(self, message: str) -> str:
        decoded_words = []
        for word in message.split(' '):
            if not word: continue
            # 숫자 덩어리를 두 글자씩 쪼개서 리스트로 만듦
            chunks = [word[i:i+2] for i in range(0, len(word), 2)]
            # 각 chunk를 디코딩하고 합침
            decoded_words.append("".join(self.coords_to_letter[chunk] for chunk in chunks))
        return " ".join(decoded_words)
    ```

4.  **사용자 정의 암호판**: 현재 암호판은 하드코딩되어 있습니다. `bifid.py`처럼, 클래스 생성자에서 키워드를 인자로 받아 사용자 정의 암호판을 생성하는 기능을 추가하면 암호의 유연성과 (약간의) 보안성을 높일 수 있습니다.