# Entropy (엔트로피) 알고리즘

이 문서는 `entropy.py` 파일에 구현된 **정보 엔트로피(Information Entropy)** 계산 알고리즘에 대한 설명입니다.

## 개요

주어진 텍스트 데이터에 대해 섀넌 엔트로피(Shannon entropy)를 계산합니다. 텍스트 내의 문자 출현 빈도를 분석하여 정보의 불확실성 정도를 측정합니다.

## 함수 설명

### `calculate_prob(text: str) -> None`

주어진 텍스트에 대해 다음 세 가지 엔트로피 값을 계산하고 출력합니다.

1. **1차 엔트로피 (First-order Entropy)**: 단일 문자의 출현 확률에 기반한 엔트로피 ($H(X)$).
2. **2차 엔트로피 (Second-order Entropy)**: 두 문자 쌍(Bigram)의 출현 확률에 기반한 엔트로피 ($H(XY)$).
3. **조건부 엔트로피 근사값**: 2차 엔트로피와 1차 엔트로피의 차이 ($H(XY) - H(X)$). 이는 이전 문자가 주어졌을 때 다음 문자의 불확실성($H(X_n | X_{n-1})$)을 나타냅니다.

#### 매개변수 (Parameters)

- `text` (`str`): 분석할 입력 문자열입니다.

#### 알고리즘 (Algorithm)

섀넌의 엔트로피 공식을 사용합니다:
$$ H(X) = - \sum\_{i} P(x_i) \log_2 P(x_i) $$

1. `analyze_text` 함수를 통해 문자 및 문자 쌍의 빈도수를 구합니다.
2. 전체 합계로 나누어 각 항목의 확률($P$)을 계산합니다.
3. 공식에 대입하여 엔트로피를 합산합니다.
4. 결과를 소수점 첫째 자리까지 반올림하여 출력합니다.

### `analyze_text(text: str) -> tuple[dict, dict]`

텍스트를 분석하여 문자와 문자 쌍의 빈도수를 계산하는 헬퍼 함수입니다.

#### 매개변수 (Parameters)

- `text` (`str`): 분석할 입력 문자열입니다.

#### 반환값 (Returns)

- `tuple[dict, dict]`:
  1. 단일 문자 빈도수 딕셔너리 (`Counter`)
  2. 두 문자 쌍(Bigram) 빈도수 딕셔너리 (`Counter`)

## 테스트 및 실행

파일을 직접 실행하면(`if __name__ == "__main__":`) `doctest` 모듈을 통해 독스트링(docstring)에 작성된 테스트 케이스를 검증합니다.

```python
if __name__ == "__main__":
    main()
```
