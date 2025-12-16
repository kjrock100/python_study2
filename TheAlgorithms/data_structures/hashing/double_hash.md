# `double_hash.py` 코드 설명

이 문서는 `double_hash.py` 스크립트에 구현된 이중 해싱(Double Hashing)을 이용한 개방 주소법(Open Addressing) 해시 테이블에 대해 설명합니다.

## 1. 이중 해싱(Double Hashing)이란?

이중 해싱은 해시 테이블에서 충돌(Collision)이 발생했을 때, 다음 위치를 찾기 위한 방법 중 하나입니다. 개방 주소법의 일종으로, 두 개의 서로 다른 해시 함수를 사용합니다.

-   **첫 번째 해시 함수 (`h1`)**: 키의 초기 위치를 결정합니다.
-   **두 번째 해시 함수 (`h2`)**: 충돌 발생 시 이동할 다음 위치의 간격(step)을 결정합니다.

i번째 시도에서의 위치는 일반적으로 다음 공식을 따릅니다.
> **`index = (h1(key) + i * h2(key)) % table_size`**

이 방식은 선형 탐사(Linear Probing)나 제곱 탐사(Quadratic Probing)에서 발생하는 특정 패턴의 클러스터링 문제를 완화하는 데 효과적입니다.

## 2. 클래스 및 메서드 설명

### `DoubleHash(HashTable)` 클래스

이 클래스는 `HashTable` 부모 클래스를 상속받아, 충돌 해결 전략으로 이중 해싱을 구현합니다.

#### `__init__(self, *args, **kwargs)`
-   **역할**: 부모 클래스인 `HashTable`의 생성자를 호출하여 해시 테이블을 초기화합니다.

#### `__hash_function_2(self, value, data)`
-   **역할**: 두 번째 해시 함수(`h2`)의 역할을 수행합니다. 충돌 시 이동할 간격을 계산합니다.
-   **동작**:
    1.  `value % self.size_table` 보다 큰 소수(`next_prime_gt`)를 찾습니다.
    2.  `next_prime_gt - (data % next_prime_gt)`를 반환하여 0이 아닌 양의 정수 간격을 보장하려 시도합니다.

#### `__hash_double_function(self, key, data, increment)`
-   **역할**: `i * h2(key)` 부분에 해당하는 값을 계산합니다.
-   **매개변수**:
    -   `key`, `data`: 해싱에 사용될 값.
    -   `increment`: 충돌 횟수 (`i`).
-   **동작**: `(increment * __hash_function_2(key, data)) % self.size_table`을 계산하여 테이블 크기 내의 오프셋을 반환합니다.

#### `_collision_resolution(self, key, data=None)`
-   **역할**: `HashTable`의 충돌 해결 로직을 오버라이드(override)합니다. 이중 해싱을 사용하여 `key`를 삽입할 빈 공간을 찾습니다.
-   **동작**:
    1.  첫 번째 해시 함수(`self.hash_function`)를 사용하여 초기 위치 `new_key`를 계산합니다.
    2.  해당 위치가 비어있지 않으면, `__hash_double_function`을 사용하여 다음 위치를 계산하는 과정을 반복합니다.
    3.  `balanced_factor`가 임계값(`lim_charge`)을 넘으면, 재해싱이 필요하다고 판단하여 `None`을 반환하고 탐색을 중단합니다.
    4.  빈 슬롯을 찾으면 해당 인덱스를 반환합니다.

> **구현상의 주의점**:
> 현재 `_collision_resolution` 메서드의 충돌 시 다음 위치 계산 로직은 `new_key = self.__hash_double_function(...)`으로 되어 있습니다.
> 표준적인 이중 해싱 공식은 `(h1(key) + i * h2(key)) % M` 이지만, 이 코드에서는 `h1(key)` 부분이 누락되어 `i * h2(key) % M` 만으로 다음 위치를 계산하고 있습니다. 이는 의도된 동작이 아닐 수 있으며, 해시 성능에 영향을 줄 수 있습니다. 올바른 구현은 `new_key = (self.hash_function(data) + self.__hash_double_function(key, data, i)) % self.size_table` 형태가 되어야 합니다.

## 3. 사용 예제

이 클래스는 직접 실행되기보다는 `HashTable` 클래스에 의해 내부적으로 사용됩니다. `HashTable`의 `insert` 메서드가 호출될 때, 만약 충돌이 발생하면 이 클래스에 정의된 `_collision_resolution` 메서드가 실행됩니다.

```python
# (가상 코드)
# from .hash_table import HashTable
# from .double_hash import DoubleHash

# DoubleHash를 충돌 해결 전략으로 사용하는 해시 테이블 생성
# 실제로는 HashTable이 내부적으로 이 클래스를 사용하도록 설계되어야 함

# hash_table = DoubleHash(size=10)
# hash_table.insert("apple", 10)
# hash_table.insert("banana", 20) # "apple"과 충돌 발생 시
                                # _collision_resolution이 호출됨
```