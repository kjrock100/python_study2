# `hash_table_with_linked_list.py` 코드 설명

이 문서는 `hash_table_with_linked_list.py` 스크립트에 구현된, 분리 연결법(Separate Chaining)을 사용하는 해시 테이블에 대해 설명합니다.

## 1. 분리 연결법(Separate Chaining)이란?

분리 연결법은 해시 테이블에서 발생하는 충돌(Collision)을 해결하는 고전적인 방법 중 하나입니다. 충돌이란 서로 다른 두 개 이상의 키가 동일한 해시 값(테이블 인덱스)을 갖게 되는 상황을 말합니다.

이 방법은 해시 테이블의 각 슬롯(버킷)을 연결 리스트(Linked List)로 만듭니다. 동일한 인덱스로 해싱되는 모든 데이터는 해당 인덱스의 연결 리스트에 차례로 저장됩니다. 이 코드에서는 파이썬의 `collections.deque`를 연결 리스트처럼 사용합니다.

**장점**:
-   개방 주소법(Open Addressing)과 달리 테이블이 가득 차도 계속해서 데이터를 추가할 수 있습니다.
-   데이터 삭제가 간단합니다.

## 2. 클래스 및 메서드 설명

### `HashTableWithLinkedList(HashTable)` 클래스

이 클래스는 `HashTable` 부모 클래스를 상속받아, 충돌 해결 전략으로 분리 연결법을 구현합니다.

#### `__init__(self, *args, **kwargs)`
-   **역할**: 부모 클래스인 `HashTable`의 생성자를 호출하여 해시 테이블을 초기화합니다.

#### `_set_value(self, key, data)`
-   **역할**: 주어진 `key`(해시된 인덱스)에 `data`를 저장합니다.
-   **동작**:
    1.  `self.values[key]` 슬롯이 비어있으면(`None`), 새로운 `deque`를 생성하여 할당합니다.
    2.  해당 `deque`의 맨 앞에 `data`를 추가합니다 (`appendleft`).

#### `balanced_factor(self)`
-   **역할**: 해시 테이블의 균형 인자(또는 부하율과 관련된 지표)를 계산합니다.
-   **동작**: 각 슬롯(연결 리스트)의 "남은 공간"을 기준으로 전체적인 부하를 계산하는 독자적인 공식을 사용합니다. 이 값이 클수록 테이블이 더 비어있음을 의미합니다.

#### `_collision_resolution(self, key, data=None)`
-   **역할**: `HashTable`의 충돌 해결 로직을 오버라이드(override)합니다. 이 메서드는 분리 연결법을 사용할지, 아니면 다른 방법을 사용할지 결정하는 역할을 합니다.
-   **동작**:
    1.  현재 `key`에 해당하는 연결 리스트의 길이가 설정된 `charge_factor`보다 작거나, 또는 전체 테이블에 아직 빈 슬롯(`None`)이 하나라도 있는 경우, `key`를 그대로 반환합니다. 이는 "현재 `key`의 연결 리스트에 데이터를 추가하라"는 의미입니다.
    2.  만약 위 조건이 모두 거짓이면(즉, 해당 연결 리스트가 꽉 찼고, 테이블의 다른 슬롯도 모두 사용 중인 경우), 부모 클래스의 `_collision_resolution` 메서드를 호출하여 다른 충돌 해결책(예: 재해싱)을 시도합니다.

## 3. 사용 예제

이 클래스는 `HashTable`의 `insert` 메서드 내부에서 충돌이 발생했을 때 호출됩니다.

```python
# (가상 코드)
# from .hash_table import HashTable
# from .hash_table_with_linked_list import HashTableWithLinkedList

# HashTable이 내부적으로 HashTableWithLinkedList의 로직을 사용한다고 가정

# hash_table = HashTable(size=10)
# hash_table.insert("apple", 10)
# hash_table.insert("banana", 20)

# 만약 "apple"과 "banana"가 같은 인덱스 3으로 해싱된다면:
# 1. hash_table.insert("apple", 10) -> values[3] = deque([10])
# 2. hash_table.insert("banana", 20) -> 충돌 발생
# 3. _collision_resolution(3) 호출 -> 3을 반환
# 4. _set_value(3, 20) 호출 -> values[3] = deque([20, 10])
```

결과적으로 `values[3]`에는 `[20, 10]`을 담고 있는 `deque`가 저장됩니다.