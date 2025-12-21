# 모든 구성 방법 찾기 (All Construct)

이 문서는 `all_construct.py` 파일에 구현된 **All Construct** 알고리즘에 대해 설명합니다. 이 알고리즘은 동적 계획법(Dynamic Programming)을 사용하여, 주어진 문자열 조각(substring)들을 조합해 목표 문자열(target)을 만들 수 있는 **모든 가능한 방법**을 찾아냅니다.

## 개요

주어진 단어 목록(`word_bank`)에 있는 단어들을 반복 사용하여 `target` 문자열을 구성할 수 있는 모든 조합을 2차원 리스트 형태로 반환합니다.

## 주요 함수: `all_construct(target, word_bank)`

### `all_construct(target: str, word_bank: list[str] | None = None) -> list[list[str]]`
- **목적**: `target` 문자열을 구성할 수 있는 모든 단어 조합을 반환합니다.
- **매개변수**:
  - `target`: 만들고자 하는 목표 문자열.
  - `word_bank`: 사용할 수 있는 단어(부분 문자열)들의 리스트.
- **반환값**: 가능한 모든 조합을 담은 리스트의 리스트. (예: `[['purp', 'le'], ['p', 'ur', 'p', 'le']]`)

### 알고리즘 동작 원리 (Tabulation)

1. **테이블 초기화**:
   - `target`의 길이 + 1 크기의 리스트 `table`을 생성합니다.
   - `table[i]`는 `target`의 처음 `i`글자까지를 구성할 수 있는 모든 방법(조합)을 저장합니다.
   - `table[0]`은 `[[]]`로 초기화합니다. (빈 문자열을 만드는 유일한 방법은 아무 단어도 선택하지 않는 것입니다.)

2. **반복 및 상태 전이**:
   - 인덱스 `i`를 0부터 `target`의 길이까지 순회합니다.
   - 만약 `table[i]`가 비어있지 않다면(즉, 현재 위치까지 도달 가능하다면):
     - `word_bank`의 모든 `word`에 대해 다음을 확인합니다.
     - `target`의 `i`번째 위치부터 시작하는 부분 문자열이 `word`와 일치하는지 검사합니다 (`target[i : i + len(word)] == word`).
     - 일치한다면, `table[i]`에 있는 모든 조합에 현재 `word`를 추가하여 `table[i + len(word)]`에 저장합니다.
     - *구현 상세*: 코드에서는 효율성을 위해 `[word] + way` 형태로 단어를 앞에 붙여 저장합니다. 이로 인해 조합이 역순으로 쌓이게 됩니다.

3. **결과 정리**:
   - 모든 반복이 끝난 후, `table[len(target)]`에는 목표 문자열을 만드는 모든 조합이 저장되어 있습니다.
   - 저장 과정에서 역순으로 쌓인 단어 순서를 바로잡기 위해 각 조합을 `reverse()` 합니다.

4. **반환**: 최종 조합 리스트를 반환합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 사용 예시를 확인할 수 있습니다:

```python
print(all_construct("hello", ["he", "l", "o"]))
# 출력: [['he', 'l', 'l', 'o']]

print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# 출력: [['purp', 'le'], ['p', 'ur', 'p', 'le']]
```
