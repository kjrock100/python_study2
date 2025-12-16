# `skip_list.py` 코드 설명

이 문서는 `skip_list.py` 스크립트에 구현된 스킵 리스트(Skip List) 자료 구조에 대해 설명합니다.

## 1. 스킵 리스트(Skip List)란?

스킵 리스트는 정렬된 데이터를 저장하는 확률적(probabilistic) 자료 구조로, 균형 이진 탐색 트리(Balanced Binary Search Tree)의 대안으로 사용될 수 있습니다. 여러 레벨의 연결 리스트를 사용하여 구현되며, 각 노드는 무작위로 결정된 수의 레벨에 포함됩니다.

**주요 특징:**
-   **확률적 균형**: 노드가 어떤 레벨에 포함될지 무작위로 결정되므로, 트리가 균형을 유지할 확률이 높습니다.
-   **빠른 연산**: 평균적으로 검색, 삽입, 삭제 연산에 대해 O(log N)의 시간 복잡도를 가집니다. 최악의 경우 O(N)이 될 수도 있지만, 그 확률은 매우 낮습니다.
-   **간단한 구현**: 균형 이진 탐색 트리(예: 레드-블랙 트리, AVL 트리)에 비해 구현이 상대적으로 간단합니다.
-   **공간 복잡도**: O(N log N) (평균적으로)

## 2. 클래스 구조

### `Node` 클래스

스킵 리스트를 구성하는 각 요소를 표현하는 클래스입니다.

-   `__init__(self, key: KT | str = "root", value: VT | None = None)`: 노드를 초기화합니다.
    -   `key`: 노드의 키 값. 스킵 리스트는 이 키 값을 기준으로 정렬됩니다. "root"는 헤드 노드를 위한 특별한 키입니다.
    -   `value`: 키와 연결된 실제 데이터 값.
    -   `forward: list[Node[KT, VT]]`: 다음 노드를 가리키는 참조들의 리스트. `forward[i]`는 `i` 레벨에서의 다음 노드를 가리킵니다.
-   `__repr__(self) -> str`: 노드의 키와 값을 문자열로 표현합니다.
-   `@property level`: 노드가 포함된 레벨의 개수를 반환합니다 (`forward` 리스트의 길이).

### `SkipList` 클래스

스킵 리스트 전체를 관리하고, 삽입, 삭제, 검색 등의 연산을 제공하는 메인 클래스입니다.

-   `__init__(self, p: float = 0.5, max_level: int = 16)`: 스킵 리스트를 초기화합니다.
    -   `head: Node[KT, VT]`: 스킵 리스트의 시작을 나타내는 더미 헤드 노드.
    -   `level`: 현재 스킵 리스트의 최고 레벨.
    -   `p`: 노드가 다음 레벨로 올라갈 확률 (기본값 0.5).
    -   `max_level`: 스킵 리스트가 가질 수 있는 최대 레벨.

## 3. 주요 메서드 설명

### `__str__(self) -> str`
-   **역할**: 스킵 리스트의 시각적인 문자열 표현을 반환합니다.
-   **동작**: 각 레벨의 노드들을 연결하여 리스트의 구조를 보여줍니다.

### `__iter__(self)`
-   **역할**: 스킵 리스트의 모든 키를 오름차순으로 순회하는 이터레이터(iterator)를 반환합니다.
-   **동작**: 가장 낮은 레벨(level 0)을 따라 이동하며 각 노드의 키를 `yield`합니다.

### `random_level(self) -> int`
-   **역할**: 새로운 노드가 가질 레벨을 확률 `p`에 따라 무작위로 결정합니다.
-   **동작**: `random()` 함수를 사용하여 0과 1 사이의 난수를 생성하고, 이 값이 `p`보다 작을 때마다 레벨을 1씩 증가시킵니다. `max_level`을 초과하지 않습니다.

### `_locate_node(self, key) -> tuple[Node[KT, VT] | None, list[Node[KT, VT]]]`
-   **역할**: 주어진 `key`를 찾거나, `key`가 삽입될 위치를 찾기 위한 헬퍼 메서드입니다.
-   **반환**:
    -   `Node[KT, VT] | None`: `key`를 가진 노드가 존재하면 해당 노드, 없으면 `None`.
    -   `list[Node[KT, VT]]`: `update_vector`. 각 레벨에서 `key`를 가진 노드(또는 `key`가 삽입될 노드) 바로 앞에 있는 노드들의 리스트. 이 리스트는 삽입/삭제 시 포인터를 업데이트하는 데 사용됩니다.
-   **동작**: 최고 레벨부터 시작하여 `key`보다 작은 값을 가진 노드를 따라 이동합니다. 각 레벨에서 `key`보다 작은 마지막 노드를 `update_vector`에 저장합니다.

### `delete(self, key: KT)`
-   **역할**: 스킵 리스트에서 특정 `key`를 가진 노드를 삭제합니다.
-   **동작**:
    1.  `_locate_node`를 호출하여 삭제할 노드와 `update_vector`를 얻습니다.
    2.  노드가 존재하면, `update_vector`에 저장된 노드들의 `forward` 포인터를 조정하여 삭제할 노드를 건너뛰도록 합니다.
    3.  삭제 후 최고 레벨이 비어있게 되면 `self.level`을 감소시킵니다.

### `insert(self, key: KT, value: VT)`
-   **역할**: 스킵 리스트에 새로운 `key`와 `value` 쌍을 삽입합니다. `key`가 이미 존재하면 `value`를 업데이트합니다.
-   **동작**:
    1.  `_locate_node`를 호출하여 `key`의 위치를 찾습니다.
    2.  `key`가 이미 존재하면 해당 노드의 `value`를 업데이트합니다.
    3.  `key`가 없으면:
        -   `random_level`을 호출하여 새 노드의 레벨을 결정합니다.
        -   새 노드의 레벨이 현재 스킵 리스트의 최고 레벨보다 높으면, `head` 노드의 `forward` 리스트를 확장하고 `update_vector`를 업데이트합니다.
        -   새로운 `Node`를 생성하고, `update_vector`를 사용하여 각 레벨에서 새 노드를 삽입할 위치에 `forward` 포인터를 연결합니다.

### `find(self, key: VT) -> VT | None`
-   **역할**: 주어진 `key`와 연결된 `value`를 찾아 반환합니다. `key`가 없으면 `None`을 반환합니다.
-   **동작**: `_locate_node`를 호출하여 `key`를 가진 노드를 찾고, 그 노드의 `value`를 반환합니다.

## 4. 사용 예제

스크립트의 `main()` 함수와 `pytests()` 함수에 다양한 사용 예제가 포함되어 있습니다.

```python
skip_list = SkipList()

# 삽입
skip_list.insert(2, "Two")
skip_list.insert(1, "One")
skip_list.insert(3, "Three")

# 순회 (정렬된 키 반환)
print(list(skip_list))
# 출력: [1, 2, 3]

# 검색
print(skip_list.find(2))
# 출력: 'Two'

# 기존 키 업데이트
skip_list.insert(2, "Updated Two")
print(skip_list.find(2))
# 출력: 'Updated Two'

# 삭제
skip_list.delete(2)
print(list(skip_list))
# 출력: [1, 3]
print(skip_list.find(2))
# 출력: None

# 시각적 표현
print(skip_list)
# 출력 (예시, 레벨은 무작위):
# SkipList(level=...)
# [root]--...
# [1]--1...
# [3]--3...
# None    *...
```

## 5. 테스트

스크립트에는 `doctest`와 `pytests()` 함수를 통해 코드의 정확성을 검증하는 테스트 코드가 포함되어 있습니다. `pytests()`는 스킵 리스트의 확률적 특성 때문에 여러 번 반복하여 테스트를 수행합니다.

터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/skip_list.py
```

`doctest`는 각 메서드의 독스트링에 포함된 예제를 검증하며, `pytests()`는 다양한 삽입, 삭제, 검색 시나리오를 테스트합니다.

```python
def pytests():
    for i in range(100):
        # Repeat test 100 times due to the probabilistic nature of skip list
        # random values == random bugs
        test_insert()
        test_insert_overrides_existing_value()

        test_searching_empty_list_returns_none()
        test_search()

        test_deleting_item_from_empty_list_do_nothing()
        test_deleted_items_are_not_founded_by_find_method()
        test_delete_removes_only_given_key()
        test_delete_doesnt_leave_dead_nodes()

        test_iter_always_yields_sorted_values()
```

모든 테스트가 통과하면 `main()` 함수의 출력 결과만 화면에 나타납니다.