# `red_black_tree.py` 코드 설명

이 문서는 `red_black_tree.py` 스크립트에 구현된 레드-블랙 트리(Red-Black Tree)에 대해 설명합니다.

## 1. 레드-블랙 트리란?

레드-블랙 트리는 자가 균형 이진 탐색 트리(Self-Balancing Binary Search Tree)의 한 종류입니다. 일반적인 이진 탐색 트리는 데이터가 편향되게 삽입될 경우 성능이 저하될 수 있지만, 레드-블랙 트리는 삽입, 삭제 시 특정 규칙에 따라 스스로 구조를 재조정하여 트리의 균형을 유지합니다. 이로 인해 검색, 삽입, 삭제 연산에 대해 최악의 경우에도 O(log n)의 시간 복잡도를 보장합니다.

### 5가지 핵심 속성

레드-블랙 트리의 모든 노드는 다음 5가지 속성을 만족해야 합니다.

1.  모든 노드는 **레드(Red)** 또는 **블랙(Black)** 색상을 가집니다.
2.  루트 노드는 항상 **블랙**입니다.
3.  모든 리프 노드(NIL, 코드에서는 `None`)는 **블랙**입니다.
4.  **레드** 노드의 자식은 반드시 **블랙**입니다. (즉, 레드 노드가 연속으로 나타날 수 없습니다.)
5.  임의의 노드에서부터 그 자손인 리프 노드에 이르는 모든 경로에는 동일한 개수의 **블랙** 노드가 존재합니다. (이를 '블랙 높이'라고 합니다.)

## 2. `RedBlackTree` 클래스 구조

이 구현에서는 `RedBlackTree` 클래스가 트리 자체이자 동시에 트리를 구성하는 각 노드를 나타냅니다.

-   `__init__(...)`: 노드를 초기화합니다.
    -   `label`: 노드가 저장하는 값.
    -   `color`: 노드의 색상 (0: 블랙, 1: 레드).
    -   `parent`: 부모 노드.
    -   `left`, `right`: 왼쪽, 오른쪽 자식 노드.

## 3. 주요 메서드 설명

### 3.1. 핵심 균형 조정 메서드

-   `rotate_left()` / `rotate_right()`: 트리의 균형을 맞추기 위한 핵심 연산입니다. 특정 노드를 축으로 서브트리를 회전시켜 구조를 변경합니다. O(1) 시간에 동작합니다.

### 3.2. 삽입 (Insertion)

-   `insert(label)`: 새로운 값을 트리에 삽입합니다.
    1.  일반적인 이진 탐색 트리처럼 적절한 위치를 찾아 노드를 삽입합니다. 새로운 노드는 항상 **레드**로 삽입됩니다.
    2.  새 노드 삽입으로 인해 레드-블랙 트리의 속성(특히 4, 5번)이 위반될 수 있습니다.
    3.  `_insert_repair()`를 호출하여 위반된 속성을 바로잡습니다.

-   `_insert_repair()`: 삽입 후 발생할 수 있는 속성 위반을 해결합니다. 부모, 삼촌(uncle) 노드의 색상에 따라 재색칠(recoloring) 또는 회전(rotation)을 수행하여 트리의 균형을 복원합니다.

### 3.3. 삭제 (Deletion)

-   `remove(label)`: 특정 값을 가진 노드를 트리에서 삭제합니다.
    1.  삭제할 노드를 찾습니다.
    2.  자식의 수에 따라 삭제 방식을 결정합니다. (자식이 2개인 경우, 후계자(successor) 또는 선임자(predecessor)와 값을 교체한 후 삭제)
    3.  노드 삭제로 인해 레드-블랙 트리의 속성이 위반될 수 있습니다.
    4.  `_remove_repair()`를 호출하여 위반된 속성을 바로잡습니다.

-   `_remove_repair()`: 삭제 후 발생할 수 있는 속성 위반을 해결합니다. 형제(sibling) 노드와 그 자식들의 색상에 따라 복잡한 재색칠 및 회전 과정을 거쳐 트리의 균형을 복원합니다.

### 3.4. 검색 및 순회 (Search & Traversal)

-   `search(label)`: 특정 값을 가진 노드를 O(log n) 시간에 검색합니다.
-   `floor(label)`, `ceil(label)`: 주어진 값보다 작거나 같은 가장 큰 값, 또는 크거나 같은 가장 작은 값을 찾습니다.
-   `get_max()`, `get_min()`: 트리 내의 최댓값과 최솟값을 찾습니다.
-   `inorder_traverse()`, `preorder_traverse()`, `postorder_traverse()`: 중위, 전위, 후위 순회를 위한 제너레이터(generator)를 제공합니다.

### 3.5. 속성 검증 메서드

-   `check_color_properties()`: 현재 트리가 레드-블랙 트리의 5가지 속성을 모두 만족하는지 검사합니다. 디버깅 및 테스트 목적으로 사용됩니다.

### 3.6. 헬퍼 속성

-   `grandparent`: 현재 노드의 조부모 노드를 반환합니다.
-   `sibling`: 현재 노드의 형제 노드를 반환합니다.
-   `is_left()`, `is_right()`: 현재 노드가 부모의 왼쪽/오른쪽 자식인지 확인합니다.

## 4. 사용 예제

```python
# 빈 레드-블랙 트리 생성 (루트는 블랙)
rbt = RedBlackTree(label=10, color=0)

# 여러 값 삽입 (메서드 체이닝 가능)
rbt.insert(5).insert(15).insert(3).insert(7).insert(12).insert(18)

# 중위 순회로 정렬된 결과 확인
print(f"In-order traversal: {list(rbt.inorder_traverse())}")
# 출력: In-order traversal: [3, 5, 7, 10, 12, 15, 18]

# 트리 구조와 색상 확인
print(rbt)
# 출력 (예시, 실제 구조는 다를 수 있음):
# {'10 blk': ({'5 blk': ('3 red', '7 red')}, {'15 blk': ('12 red', '18 red')})}

# 값 검색
if 12 in rbt:
    print("12 is in the tree.")

# 값 삭제
rbt.remove(7)
print(f"After removing 7: {list(rbt.inorder_traverse())}")
# 출력: After removing 7: [3, 5, 10, 12, 15, 18]

# 속성 검증
if rbt.check_color_properties():
    print("The tree maintains Red-Black properties.")
```

## 5. 테스트

스크립트에는 `pytests()`와 `main()` 함수를 통해 다양한 기능(회전, 삽입, 삭제, 검색 등)을 검증하는 종합적인 테스트 코드가 포함되어 있습니다. 터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/red_black_tree.py
```

모든 테스트가 통과하면 각 기능이 "works!"라는 메시지와 함께 출력됩니다.