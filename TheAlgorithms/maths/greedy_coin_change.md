# Greedy Coin Change (탐욕적 동전 거스름돈) 알고리즘

이 문서는 `greedy_coin_change.py` 파일에 구현된 **탐욕적 동전 거스름돈(Greedy Coin Change)** 알고리즘에 대한 설명입니다.

## 개요

**탐욕적 동전 거스름돈 알고리즘**은 거스름돈 문제(Change-making problem)를 해결하기 위해 탐욕적 방법(Greedy Method)을 사용하는 알고리즘입니다. 주어진 금액을 만들기 위해 가장 큰 액면가의 동전(또는 지폐)부터 최대한 많이 사용하는 방식으로 작동합니다.

이 방식은 대부분의 표준 화폐 시스템(예: 미국 달러, 유로, 인도 루피 등)에서는 최소 개수의 동전을 사용하는 최적해를 보장하지만, 임의의 액면가 조합에 대해서는 항상 최적해를 보장하지는 않습니다.

## 함수 설명

### `find_minimum_change(denominations: list[int], value: str) -> list[int]`

주어진 액면가 리스트와 목표 금액에 대해 최소 개수의 동전 구성을 찾아 반환합니다.

#### 매개변수 (Parameters)

- `denominations` (`list[int]`): 사용 가능한 동전/지폐의 액면가 리스트입니다. (오름차순 정렬되어 있다고 가정합니다.)
- `value` (`str`): 거슬러 주어야 할 목표 금액입니다. (문자열로 입력받아 내부에서 정수로 변환합니다.)

#### 알고리즘 (Algorithm)

1. 입력받은 `value`를 정수형 `total_value`로 변환합니다.
2. `denominations` 리스트를 역순으로 순회합니다 (가장 큰 액면가부터 확인).
3. 현재 액면가가 `total_value`보다 작거나 같은 동안 반복합니다:
   - `total_value`에서 해당 액면가를 뺍니다.
   - 결과 리스트 `answer`에 해당 액면가를 추가합니다.
4. 최종적으로 구성된 `answer` 리스트를 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자에게 액면가를 직접 입력할지 묻고, 금액을 입력받아 결과를 출력합니다.

### 기본 실행 (인도 루피 예시)

사용자가 액면가를 입력하지 않으면 기본적으로 인도 화폐 단위(`[1, 2, 5, 10, 20, 50, 100, 500, 2000]`)를 사용합니다.

```python
# 실행 예시
# Do you want to enter your denominations ? (yY/n): n
# Enter the change you want to make: 987
# Following is minimal change for 987 :
# 500 100 100 100 100 50 20 10 5 2
```

### 사용자 정의 실행

사용자가 직접 액면가를 설정할 수도 있습니다.

```python
# 실행 예시
# Do you want to enter your denominations ? (yY/n): y
# Enter number of denomination: 3
# Denomination 0: 1
# Denomination 1: 5
# Denomination 2: 10
# Enter the change you want to make in Indian Currency: 18
# Following is minimal change for 18 :
# 10 5 1 1 1
```
