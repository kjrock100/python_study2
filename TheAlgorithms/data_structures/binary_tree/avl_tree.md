# `avl_tree.py` 코드 설명

이 문서는 `avl_tree.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 노드의 삽입 및 삭제 시 자동으로 균형을 유지하는 **자가 균형 이진 탐색 트리(Self-balancing Binary Search Tree)**인 **AVL 트리**를 구현합니다.

## 목차
1.  AVL 트리란?
2.  클래스 설명
    -   `my_queue`
    -   `my_node`
    -   `AVLtree`
3.  주요 함수 설명 (트리 연산)
    -   `right_rotation(node)` / `left_rotation(node)`
    -   `lr_rotation(node)` / `rl_rotation(node)`
    -   `insert_node(node, data)`
    -   `del_node(root, data)`
4.  실행 방법
5.  코드 개선 제안

## AVL 트리란?

AVL 트리는 모든 노드에서 **왼쪽 서브트리의 높이와 오른쪽 서브트리의 높이 차이가 1 이하**라는 균형 조건(balance factor)을 만족하는 이진 탐색 트리입니다. 이 조건을 유지하기 위해, 노드를 삽입하거나 삭제할 때 트리가 불균형 상태가 되면 **회전(Rotation)** 연산을 통해 스스로 균형을 맞춥니다.

이러한 특성 덕분에 AVL 트리는 탐색, 삽입, 삭제 연산에 대해 최악의 경우에도 **O(log n)**의 시간 복잡도를 보장합니다.

## 클래스 설명

### `my_queue`

트리의 레벨 순회(level-order traversal)를 위해 사용되는 간단한 큐(Queue) 자료구조입니다.

### `my_node`

AVL 트리를 구성하는 각 노드를 나타내는 클래스입니다.
-   `data`: 노드에 저장되는 값.
-   `left`, `right`: 왼쪽 및 오른쪽 자식 노드를 가리키는 포인터.
-   `height`: 현재 노드를 루트로 하는 서브트리의 높이.

### `AVLtree`

AVL 트리 전체를 관리하는 메인 클래스입니다.
-   `root`: 트리의 루트 노드를 저장합니다.
-   `insert(data)`: 트리에 새로운 노드를 삽입합니다.
-   `del_node(data)`: 트리에서 특정 값을 가진 노드를 삭제합니다.
-   `get_height()`: 트리의 전체 높이를 반환합니다.
-   `__str__()`: 트리를 레벨 순회하여 시각적으로 표현한 문자열을 반환합니다.

## 주요 함수 설명 (트리 연산)

### `right_rotation(node)` / `left_rotation(node)`

트리의 균형을 맞추기 위한 가장 기본적인 단일 회전 연산입니다.
-   `right_rotation`: 특정 노드를 기준으로 서브트리를 오른쪽으로 회전시킵니다.
-   `left_rotation`: 특정 노드를 기준으로 서브트리를 왼쪽으로 회전시킵니다.

### `lr_rotation(node)` / `rl_rotation(node)`

단일 회전으로 균형을 맞출 수 없는 경우 사용되는 이중 회전 연산입니다.
-   `lr_rotation` (Left-Right Rotation): 왼쪽 자식 노드를 먼저 왼쪽으로 회전시킨 후, 현재 노드를 오른쪽으로 회전시킵니다.
-   `rl_rotation` (Right-Left Rotation): 오른쪽 자식 노드를 먼저 오른쪽으로 회전시킨 후, 현재 노드를 왼쪽으로 회전시킵니다.

### `insert_node(node, data)`

트리에 새로운 노드를 재귀적으로 삽입하고, 필요한 경우 회전 연산을 수행하여 균형을 맞춥니다.

-   **알고리즘**:
    1.  이진 탐색 트리의 규칙에 따라 삽입할 위치를 찾아 노드를 추가합니다.
    2.  재귀적으로 부모 노드로 돌아오면서, 각 노드의 높이를 업데이트합니다.
    3.  균형 인수(왼쪽 높이 - 오른쪽 높이)가 2 또는 -2가 되어 불균형이 감지되면, 적절한 회전(`right_rotation`, `lr_rotation` 등)을 수행하여 균형을 복원합니다.

### `del_node(root, data)`

트리에서 특정 값을 가진 노드를 재귀적으로 삭제하고, 필요한 경우 회전 연산을 수행하여 균형을 맞춥니다.

-   **알고리즘**:
    1.  삭제할 노드를 찾습니다.
    2.  삭제할 노드의 자식 수에 따라 경우를 나누어 처리합니다.
        -   자식이 없거나 하나인 경우: 해당 노드를 제거하고 자식을 부모에 연결합니다.
        -   자식이 둘인 경우: 왼쪽 서브트리에서 가장 큰 값(또는 오른쪽 서브트리에서 가장 작은 값)을 찾아 현재 노드의 값과 교체한 후, 그 값을 가진 노드를 재귀적으로 삭제합니다.
    3.  `insert_node`와 마찬가지로, 재귀적으로 돌아오면서 높이를 업데이트하고 불균형이 발생하면 회전을 통해 균형을 맞춥니다.

## 실행 방법

스크립트를 직접 실행하면 `doctest`를 통해 클래스와 함수의 정확성을 테스트한 후, 0부터 9까지의 숫자를 무작위 순서로 삽입하고 다시 삭제하는 과정을 시각적으로 보여줍니다.

```bash
python avl_tree.py
```

**실행 결과 예시:**
```
insert:3
 3
*************************************
insert:8
  3
 *  8
*************************************
insert:9
right rotation node: 8
  8
 3  9
*************************************
...
```

## 코드 개선 제안

1.  **클래스 구조 통합**: 현재 `my_node` 클래스와 `AVLtree` 클래스, 그리고 전역 함수들(`insert_node`, `del_node` 등)로 기능이 분산되어 있습니다. `my_node`를 `AVLtree` 클래스 내의 내부 클래스로 만들고, `insert_node`와 같은 함수들을 `AVLtree`의 메서드로 통합하면 코드의 캡슐화가 향상되고 구조가 더 명확해집니다.

    ```python
    # 개선 제안 예시
    class AVLTree:
        class Node:
            # ... Node 클래스 구현 ...

        def __init__(self):
            self.root = None

        def insert(self, data):
            self.root = self._insert(self.root, data)

        def _insert(self, node, data):
            # ... 재귀적 삽입 및 회전 로직 ...
            return balanced_node
    ```

2.  **네이밍 컨벤션**: `my_queue`, `my_node`, `AVLtree`와 같이 클래스 이름의 대소문자 사용이 일관되지 않습니다. 파이썬에서는 클래스 이름에 파스칼 케이스(PascalCase)를 사용하는 것이 표준(PEP 8)이므로, `MyQueue`, `MyNode`, `AVLTree`로 변경하는 것이 좋습니다.

3.  **`my_queue` 클래스**: `collections.deque`는 고도로 최적화된 양방향 큐를 제공합니다. 직접 구현한 `my_queue` 대신 `collections.deque`를 사용하면 코드가 더 간결해지고 성능도 향상됩니다.

4.  **`del_node`의 복잡성**: `del_node` 함수는 여러 경우를 처리해야 하므로 로직이 복잡합니다. 각 경우(자식이 0개, 1개, 2개)에 대한 처리 로직을 별도의 헬퍼 메서드로 분리하면 가독성을 높일 수 있습니다.

5.  **`print` 문 제거**: `right_rotation`, `left_rotation`, `insert`, `del_node` 함수 내에 포함된 `print` 문은 디버깅에는 유용하지만, 라이브러리로서의 재사용성을 떨어뜨립니다. 로깅(logging) 모듈을 사용하거나, 이 `print` 문들을 제거하는 것이 좋습니다.