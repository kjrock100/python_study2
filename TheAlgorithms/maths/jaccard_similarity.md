# Jaccard Similarity (자카드 유사도) 알고리즘

이 문서는 `jaccard_similarity.py` 파일에 구현된 **자카드 유사도(Jaccard Similarity)** 계산 알고리즘에 대한 설명입니다.

## 개요

**자카드 유사도**는 두 집합 사이의 유사성을 측정하는 지표입니다. 두 집합의 교집합의 크기를 합집합의 크기로 나눈 값으로 정의됩니다.

$$ J(A, B) = \frac{|A \cap B|}{|A \cup B|} $$

값은 0과 1 사이이며, 1에 가까울수록 두 집합이 유사함을 의미합니다.

## 함수 설명

### `jaccard_similariy(setA, setB, alternativeUnion=False)`

두 집합(또는 리스트, 튜플) 간의 자카드 유사도를 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `setA` (`set` | `list` | `tuple`): 첫 번째 집합 또는 리스트.
- `setB` (`set` | `list` | `tuple`): 두 번째 집합 또는 리스트.
- `alternativeUnion` (`bool`): `True`일 경우, 합집합의 크기 대신 두 집합의 원소 개수의 합($|A| + |B|$)을 분모로 사용합니다. (기본값: `False`)

#### 반환값 (Returns)

- `float`: 계산된 자카드 유사도 값.

#### 알고리즘 (Algorithm)

1. 입력이 `set` 타입인 경우:
   - 파이썬의 `set` 메서드인 `intersection()`과 `union()`을 사용하여 교집합과 합집합의 크기를 구합니다.
2. 입력이 `list` 또는 `tuple`인 경우:
   - 리스트 컴프리헨션을 사용하여 교집합과 합집합을 직접 계산합니다.
3. `alternativeUnion`이 `True`인 경우:
   - 분모를 합집합의 크기 대신 `len(setA) + len(setB)`로 계산합니다. 이는 자기 자신과의 유사도가 0.5가 되는 특징이 있습니다.
4. 최종적으로 `교집합 크기 / 합집합 크기`를 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 예제 집합에 대한 유사도를 출력합니다.

```python
if __name__ == "__main__":
    setA = {"a", "b", "c", "d", "e"}
    setB = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similariy(setA, setB))
    # 출력: 0.375
```
