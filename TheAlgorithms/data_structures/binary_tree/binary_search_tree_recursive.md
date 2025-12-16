# `binary_search_tree_recursive.py` 코드 설명

이 문서는 `binary_search_tree_recursive.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 **이진 탐색 트리(Binary Search Tree, BST)** 자료구조와 관련 연산(삽입, 탐색, 삭제 등)을 **재귀적(recursive)** 방식으로 구현합니다.

## 목차
1.  이진 탐색 트리란?
2.  클래스 설명
    -   `Node`
    -   `BinarySearchTree`
3.  주요 메서드 설명
    -   `put(label)`
    -   `search(label)`
    -   `remove(label)`
    -   순회 메서드 (`inorder_traversal`, `preorder_traversal`)
4.  실행 방법
5.  코드 개선 제안

## 이진 탐색 트리란?

이진 탐색 트리는 다음과 같은 속성을 만족하는 이진 트리입니다.
-   모든 노드의 왼쪽 서브트리에 있는 값들은 현재 노드의 값보다 작습니다.
-   모든 노드의 오른쪽 서브트리에 있는 값들은 현재 노드의 값보다 큽니다.
-   왼쪽과 오른쪽 서브트리 또한 각각 이진 탐색 트리입니다.

이러한 속성 덕분에 평균적으로 **O(log n)**의 시간 복잡도로 데이터를 효율적으로 탐색, 삽입, 삭제할 수 있습니다.

## 클래스 설명

### `Node`

트리를 구성하는 각 노드를 나타내는 클래스입니다.
-   `label`: 노드에 저장되는 값.
-   `parent`: 부모 노드를 가리키는 포인터.
-   `left`, `right`: 왼쪽 및 오른쪽 자식 노드를 가리키는 포인터.

### `BinarySearchTree`

이진 탐색 트리 전체를 관리하는 메인 클래스입니다.
-   `root`: 트리의 루트 노드를 저장합니다.
-   `put(label)`: 트리에 새로운 노드를 삽입합니다.
-   `search(label)`: 트리에서 특정 값을 가진 노드를 찾습니다.
-   `remove(label)`: 트리에서 특정 값을 가진 노드를 삭제합니다.
-   `exists(label)`: 특정 값이 트리에 존재하는지 확인합니다.
-   `get_max_label()` / `get_min_label()`: 트리의 최댓값/최솟값을 찾습니다.
-   `inorder_traversal()` / `preorder_traversal()`: 트리를 순회합니다.

## 주요 메서드 설명

### `put(label: int)`

트리에 새로운 노드를 삽입합니다. 이 메서드는 내부적으로 재귀 헬퍼 함수인 `_put`을 호출합니다.

-   **`_put(node, label, parent)` 알고리즘**:
    1.  현재 `node`가 `None`이면, 새로운 `Node`를 생성하여 반환합니다. (재귀의 종료 조건)
    2.  `label`이 현재 노드의 값보다 작으면, 왼쪽 서브트리에 대해 `_put`을 재귀적으로 호출합니다.
    3.  `label`이 현재 노드의 값보다 크면, 오른쪽 서브트리에 대해 `_put`을 재귀적으로 호출합니다.
    4.  `label`이 현재 노드의 값과 같으면, 중복을 허용하지 않으므로 예외를 발생시킵니다.

### `search(label: int)`

트리에서 특정 `label`을 가진 노드를 찾습니다. 내부적으로 `_search`를 호출합니다.

-   **`_search(node, label)` 알고리즘**:
    1.  현재 `node`가 `None`이면, 값을 찾지 못한 것이므로 예외를 발생시킵니다.
    2.  `label`이 현재 노드의 값보다 작으면, 왼쪽 서브트리에서 재귀적으로 탐색합니다.
    3.  `label`이 현재 노드의 값보다 크면, 오른쪽 서브트리에서 재귀적으로 탐색합니다.
    4.  `label`이 현재 노드의 값과 같으면, 해당 노드를 반환합니다.

### `remove(label: int)`

트리에서 특정 `label`을 가진 노드를 삭제합니다.

-   **알고리즘**:
    1.  `search`를 이용해 삭제할 노드를 찾습니다.
    2.  삭제할 노드의 자식 수에 따라 경우를 나누어 처리합니다.
        -   **자식이 없거나 하나인 경우**: `_reassign_nodes`를 호출하여 부모 노드가 자식 노드를 직접 가리키도록 연결을 재설정합니다.
        -   **자식이 둘인 경우**:
            -   오른쪽 서브트리에서 가장 작은 값(`_get_lowest_node`)을 찾습니다.
            -   삭제할 노드의 `label`을 찾은 가장 작은 값으로 교체합니다.
            -   가장 작은 값을 가졌던 노드를 삭제합니다. (이 노드는 자식이 최대 하나이므로 간단히 삭제 가능)

### 순회 메서드 (`inorder_traversal`, `preorder_traversal`)

트리의 모든 노드를 방문하는 방법을 제공합니다.

-   **`inorder_traversal` (중위 순회)**: 왼쪽 서브트리 -> 현재 노드 -> 오른쪽 서브트리 순서로 방문합니다. BST에서 중위 순회를 하면 노드 값들이 정렬된 순서로 나옵니다.
-   **`preorder_traversal` (전위 순회)**: 현재 노드 -> 왼쪽 서브트리 -> 오른쪽 서브트리 순서로 방문합니다. 트리를 복사할 때 유용합니다.

## 실행 방법

스크립트를 직접 실행하면 `binary_search_tree_example` 함수가 호출되어 예제 트리를 생성하고, 다양한 메서드를 실행하여 그 결과를 출력합니다. 또한, `unittest`를 사용하여 클래스의 각 기능이 올바르게 동작하는지 테스트합니다.

```bash
python binary_search_tree_recursive.py
```

## 코드 개선 제안

1.  **`remove` 메서드의 복잡성**: `remove` 메서드, 특히 자식이 둘인 노드를 삭제하는 로직이 다소 복잡합니다. `_get_lowest_node` 함수가 노드를 찾는 동시에 트리 구조를 변경하는 두 가지 책임을 가지고 있어 이해하기 어렵습니다. 후임자(successor) 노드를 찾고, 그 값을 복사한 후, 후임자 노드를 재귀적으로 삭제하는 방식으로 로직을 분리하면 더 명확해집니다.

    ```python
    # remove 개선 제안 예시
    def remove(self, label: int):
        self.root = self._remove(self.root, label)

    def _remove(self, node: Node | None, label: int) -> Node | None:
        if node is None:
            raise Exception(f"Node with label {label} does not exist")
        
        if label < node.label:
            node.left = self._remove(node.left, label)
        elif label > node.label:
            node.right = self._remove(node.right, label)
        else: # 노드를 찾았을 때
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # 자식이 둘인 경우: 오른쪽 서브트리에서 가장 작은 노드를 찾음
            temp = self._get_min_node(node.right)
            node.label = temp.label
            node.right = self._remove(node.right, temp.label)
        return node
    ```

2.  **예외 처리**: `search`와 `remove`에서 노드가 없을 때 `Exception`을 발생시키는 것은 일반적이지 않습니다. `search`는 `None`을 반환하고, `remove`는 아무 작업도 하지 않거나 `KeyError`를 발생시키는 것이 더 일반적인 API 디자인입니다.

3.  **재귀 깊이 제한**: 재귀를 사용하는 구현은 파이썬의 재귀 깊이 제한(기본값 1000)에 도달할 수 있습니다. 매우 깊은 트리를 다룰 경우, `sys.setrecursionlimit()`을 사용하거나 반복(iterative) 방식으로 전환해야 할 수 있습니다. 이 스크립트는 `binary_search_tree.py`와 비교하여 재귀적 접근법을 보여주는 좋은 예시입니다.

4.  **테스트 방식**: `unittest`와 `doctest`를 모두 사용하여 코드를 테스트하는 것은 매우 좋은 습관입니다. 이는 코드의 신뢰성을 크게 높여줍니다.