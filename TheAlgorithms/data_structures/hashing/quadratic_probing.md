# `quadratic_probing.py` 코드 설명

이 문서는 `quadratic_probing.py` 스크립트에 구현된 제곱 탐사(Quadratic Probing)를 이용한 개방 주소법(Open Addressing) 해시 테이블에 대해 설명합니다.

## 1. 제곱 탐사(Quadratic Probing)란?

제곱 탐사는 해시 테이블에서 충돌(Collision)이 발생했을 때, 다음 위치를 찾기 위한 방법 중 하나입니다. 선형 탐사(Linear Probing)가 충돌 지점에서 1, 2, 3, ... 칸씩 순차적으로 이동하는 것과 달리, 제곱 탐사는 1², 2², 3², ... (즉, 1, 4, 9, ...) 칸씩 이동하여 다음 위치를 탐색합니다.

i번째 시도에서의 위치는 일반적으로 다음 공식을 따릅니다.
> **`index = (h(key) + i^2) % table_size`**

이 방식은 선형 탐사에서 발생하는 **기본 클러스터링(Primary Clustering)** 문제(데이터가 한 곳에 길게 뭉치는 현상)를 완화하는 데 효과적입니다.

## 2. 클래스 및 메서드 설명

### `QuadraticProbing(HashTable)` 클래스

이 클래스는 `HashTable` 부모 클래스를 상속받아, 충돌 해결 전략으로 제곱 탐사를 구현합니다.

#### `__init__(self, *args, **kwargs)`
-   **역할**: 부모 클래스인 `HashTable`의 생성자를 호출하여 해시 테이블을 초기화합니다.

#### `_collision_resolution(self, key, data=None)`
-   **역할**: `HashTable`의 충돌 해결 로직을 오버라이드(override)합니다. 제곱 탐사를 사용하여 `key`를 삽입할 빈 공간을 찾습니다.
-   **매개변수**:
    -   `key`: 충돌이 발생한 초기 해시 인덱스.
    -   `data`: 삽입하려는 원본 데이터 (이 구현에서는 사용되지 않음).
-   **동작**:
    1.  탐사 횟수를 나타내는 `i`를 1로 초기화합니다.
    2.  `new_key = (key + i*i) % self.size_table` 공식을 사용하여 다음 탐사 위치를 계산합니다.
    3.  해당 위치(`new_key`)가 비어있지 않으면, `i`를 1씩 증가시키며 빈 슬롯을 찾을 때까지 이 과정을 반복합니다.
    4.  탐사 도중 테이블의 부하율(`balanced_factor`)이 임계값(`lim_charge`)을 넘으면, 재해싱이 필요하다고 판단하여 `None`을 반환하고 탐색을 중단합니다.
    5.  빈 슬롯을 찾으면 해당 인덱스를 반환합니다.

## 3. 사용 예제

이 클래스는 `HashTable`의 `insert_data` 메서드 내부에서 충돌이 발생했을 때 호출됩니다.

```python
# (가상 코드)
# from .hash_table import HashTable
# from .quadratic_probing import QuadraticProbing

# HashTable이 내부적으로 QuadraticProbing의 로직을 사용한다고 가정

# ht = HashTable(size=10)
# ht.insert_data(1)  # hash(1) = 1. values[1]에 저장
# ht.insert_data(11) # hash(11) = 1. 충돌 발생!

# _collision_resolution(1) 호출:
# i = 1, new_key = (1 + 1*1) % 10 = 2. values[2]가 비어있으므로 2 반환.
# 11은 values[2]에 저장됨.

# ht.insert_data(21) # hash(21) = 1. 충돌 발생!
# _collision_resolution(1) 호출:
# i = 1, new_key = (1 + 1*1) % 10 = 2. values[2]는 11이므로 다시 탐사.
# i = 2, new_key = (1 + 2*2) % 10 = 5. values[5]가 비어있으므로 5 반환.
# 21은 values[5]에 저장됨.
```

## 4. 한계점

-   **이차 클러스터링(Secondary Clustering)**: 서로 다른 키가 동일한 초기 해시 값을 가질 경우, 그 이후의 탐사 순서가 모두 동일해지는 문제가 발생할 수 있습니다.
-   **테이블 크기**: 제곱 탐사가 테이블의 모든 슬롯을 방문하도록 보장하려면, 테이블 크기는 특정 형태의 소수(prime number)여야 하고 부하율이 0.5를 넘지 않아야 하는 등의 조건이 필요합니다. 이 구현의 부모 클래스인 `HashTable`은 재해싱 시 소수를 사용하므로 이 문제를 일부 완화합니다.