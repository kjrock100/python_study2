# `hash_table.py` 코드 설명

이 문서는 `hash_table.py` 스크립트에 구현된 기본 해시 테이블(Hash Table)에 대해 설명합니다. 이 클래스는 다른 해싱 전략을 구현하기 위한 부모 클래스로서의 역할을 합니다.

## 1. 해시 테이블(Hash Table)이란?

해시 테이블은 키(Key)를 값(Value)에 매핑할 수 있는 자료 구조로, 평균적으로 O(1)의 시간 복잡도로 데이터의 삽입, 삭제, 검색을 수행할 수 있습니다.

이 구현은 **개방 주소법(Open Addressing)**을 기본 충돌 해결 전략으로 사용하며, 구체적으로는 **선형 탐사(Linear Probing)** 방식을 따릅니다.

## 2. 클래스 및 메서드 설명

### `HashTable` 클래스

#### `__init__(self, size_table, charge_factor=None, lim_charge=None)`
-   **역할**: 해시 테이블을 초기화합니다.
-   **매개변수**:
    -   `size_table`: 해시 테이블의 초기 크기.
    -   `lim_charge`: 재해싱(Rehashing)을 트리거하는 부하율(Load Factor)의 임계값 (기본값 0.75).
    -   `charge_factor`: 부하율 계산에 사용되는 계수 (기본값 1).
-   **속성**:
    -   `values`: 실제 데이터가 저장되는 리스트.
    -   `_keys`: 키와 데이터를 매핑하여 저장하는 딕셔너리.

#### `hash_function(self, key)`
-   **역할**: 간단한 모듈러(modulo) 연산을 사용하여 주어진 `key`에 대한 해시 값을 (테이블 인덱스) 계산합니다.

#### `insert_data(self, data)`
-   **역할**: 데이터를 해시 테이블에 삽입하는 메인 메서드입니다.
-   **동작**:
    1.  데이터의 해시 값(`key`)을 계산합니다.
    2.  해당 `key`의 슬롯이 비어있으면, `_set_value`를 호출하여 데이터를 저장합니다.
    3.  이미 같은 데이터가 있으면, 아무것도 하지 않습니다.
    4.  다른 데이터가 있어 충돌이 발생하면, `_collision_resolution`을 호출하여 빈 슬롯을 찾습니다.
    5.  만약 빈 슬롯을 찾지 못하면(테이블이 너무 꽉 차서), `rehashing`을 수행한 후 다시 데이터 삽입을 시도합니다.

#### `_collision_resolution(self, key, data=None)`
-   **역할**: 충돌 발생 시 다음 위치를 찾는 기본 전략인 **선형 탐사(Linear Probing)**를 구현합니다.
-   **동작**: 현재 위치에서 1씩 증가시키면서 빈 슬롯(`None`)을 찾습니다. 테이블에 빈 슬롯이 없으면 `None`을 반환하여 재해싱이 필요함을 알립니다.

#### `rehashing(self)`
-   **역할**: 테이블이 너무 꽉 찼을 때 테이블의 크기를 늘리고 모든 데이터를 다시 삽입합니다.
-   **동작**:
    1.  현재 테이블 크기보다 큰 다음 소수(prime number)를 새로운 크기로 설정합니다.
    2.  `values`와 `_keys`를 비웁니다.
    3.  기존에 저장되어 있던 모든 데이터를 새로운 크기의 테이블에 다시 삽입합니다.

#### `balanced_factor(self)`
-   **역할**: 현재 해시 테이블의 부하율(Load Factor)을 계산합니다.
-   **공식**: `(사용 중인 슬롯 수) / (전체 테이블 크기 * charge_factor)`

#### `_set_value(self, key, data)`
-   **역할**: `values` 리스트와 `_keys` 딕셔너리에 데이터를 설정하는 헬퍼 메서드입니다.

## 3. 상속을 통한 확장성

이 `HashTable` 클래스는 다양한 충돌 해결 전략을 구현하기 위한 기반(base class)으로 설계되었습니다.

-   `_collision_resolution(self, key, data=None)`
-   `_set_value(self, key, data)`
-   `balanced_factor(self)`

위와 같은 메서드들을 자식 클래스에서 오버라이드(override)함으로써, **이중 해싱(`DoubleHash`)**이나 **분리 연결법(`HashTableWithLinkedList`)**과 같은 다른 해싱 기법을 쉽게 구현할 수 있습니다.

## 4. 사용 예제

```python
# 10개의 슬롯을 가진 해시 테이블 생성
ht = HashTable(10)

# 데이터 삽입
ht.insert_data(1)
ht.insert_data(11)  # 1과 충돌 발생
ht.insert_data(21)  # 1, 11과 충돌 발생

# 내부 상태 확인
# 1은 인덱스 1에 저장됨
# 11은 충돌 후 선형 탐사에 의해 인덱스 2에 저장됨
# 21은 충돌 후 선형 탐사에 의해 인덱스 3에 저장됨
print(ht.values)
# 출력: [None, 1, 11, 21, None, None, None, None, None, None]

print(ht.keys())
# 출력: {1: 1, 2: 11, 3: 21}

# 부하율 확인
print(ht.balanced_factor())
# 출력: 0.3
```