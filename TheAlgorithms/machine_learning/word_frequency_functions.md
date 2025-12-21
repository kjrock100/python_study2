# 단어 빈도 함수 (Word Frequency Functions)

이 문서는 `word_frequency_functions.py` 파일에 구현된 **단어 빈도(Word Frequency)** 관련 알고리즘에 대해 설명합니다.

## 개요

TF-IDF(Term Frequency - Inverse Document Frequency)와 같은 알고리즘은 정보 검색(Information Retrieval) 및 텍스트 마이닝(Text Mining) 분야에서 단어의 가중치를 계산하는 데 널리 사용됩니다. 이 코드는 텍스트 데이터에서 단어의 중요도를 평가하기 위한 기본적인 함수들을 제공합니다.

## 주요 함수

### 1. 용어 빈도 (Term Frequency, TF)
`term_frequency(term: str, document: str) -> int`

- **목적**: 특정 문서(`document`) 내에서 주어진 단어(`term`)가 몇 번 등장하는지 계산합니다.
- **동작**:
  - 문서에서 구두점과 줄바꿈 문자를 제거합니다.
  - 공백을 기준으로 문서를 토큰화(Tokenization)합니다.
  - 대소문자를 구분하지 않고 단어의 등장 횟수를 셉니다.

### 2. 문서 빈도 (Document Frequency, DF)
`document_frequency(term: str, corpus: str) -> tuple[int, int]`

- **목적**: 전체 문서 집합(`corpus`) 중에서 주어진 단어(`term`)가 포함된 문서의 개수를 계산합니다.
- **매개변수**:
  - `corpus`: 여러 문서가 줄바꿈(`\n`)으로 구분된 문자열.
- **반환값**: `(단어가 포함된 문서 수, 전체 문서 수)` 튜플.

### 3. 역문서 빈도 (Inverse Document Frequency, IDF)
`inverse_document_frequency(df: int, N: int, smoothing=False) -> float`

- **목적**: 단어의 일반적인 중요도를 계산합니다. 특정 단어가 많은 문서에 등장할수록(즉, 흔한 단어일수록) IDF 값은 낮아집니다.
- **수식**:
  - 기본: $\log_{10}(\frac{N}{df})$
  - 스무딩(Smoothing) 적용 시: $1 + \log_{10}(\frac{N}{1 + df})$
- **매개변수**:
  - `df`: 문서 빈도 (Document Frequency).
  - `N`: 전체 문서의 수.
  - `smoothing`: 0으로 나누는 오류를 방지하고 값을 조정하기 위한 스무딩 적용 여부.

### 4. TF-IDF
`tf_idf(tf: int, idf: int) -> float`

- **목적**: TF와 IDF를 결합하여 특정 문서 내에서 단어의 독창성(Originality) 또는 중요도를 계산합니다.
- **수식**: $TF \times IDF$
- **의미**: 특정 문서에는 자주 등장하지만(High TF), 전체 문서 집합에서는 드물게 등장하는(High IDF) 단어일수록 높은 값을 가집니다.

## 사용 예시

```python
document = "To be, or not to be"
corpus = "This is the first document.\nThis is the second document."

# TF 계산
tf = term_frequency("to", document) # 결과: 2

# DF 계산
df, N = document_frequency("document", corpus) # 결과: (2, 2)

# IDF 계산
idf = inverse_document_frequency(df, N) # 결과: 0.0 (log10(1) = 0)

# TF-IDF 계산
score = tf_idf(tf, idf) # 결과: 0.0
```

## 요구 사항
- `string`: 구두점 제거를 위해 사용.
- `math`: 로그 계산(`log10`)을 위해 사용.
