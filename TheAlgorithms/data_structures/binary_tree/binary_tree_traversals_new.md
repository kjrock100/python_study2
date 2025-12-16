# `binary_tree_traversals.py` 코드 설명

이 문서는 `binary_tree_traversals.py` 스크립트에 구현된 다양한 이진 트리 순회(Tree Traversal) 알고리즘에 대해 설명합니다.

## 1. 이진 트리 순회란?

트리 순회는 트리의 각 노드를 체계적으로 한 번씩 방문하는 과정입니다. 어떤 순서로 노드를 방문하느냐에 따라 여러 종류의 순회 방법이 있으며, 각각 다른 목적에 사용됩니다.

이 스크립트는 다음과 같은 순회 방법을 구현합니다.
-   **깊이 우선 탐색 (DFS)**: Pre-order, In-order, Post-order
-   **너비 우선 탐색 (BFS)**: Level-order
-   **기타**: Zigzag

## 2. `Node` 클래스

트리를 구성하는 기본 단위인 노드를 표현하기 위해 파이썬의 `dataclass`를 사용합니다.

```python
@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None
```
-   `data`: 노드가 저장하는 값입니다.
-   `left`: 왼쪽 자식 노드를 가리킵니다.
-   `right`: 오른쪽 자식 노드를 가리킵니다.

## 3. 순회 함수 설명

모든 예제는 아래와 같은 트리를 기준으로 설명합니다.

```
      1
     / \
    2   3
   / \
  4   5
```

### 3.1. 깊이 우선 탐색 (Depth-First Search, DFS)

#### `preorder(root: Node | None) -> list[int]`
-   **순서**: 루트(Root) → 왼쪽(Left) → 오른쪽(Right)
-   **설명**: 현재 노드를 먼저 처리한 후, 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 방문합니다.
-   **결과**: `[1, 2, 4, 5, 3]`

#### `inorder(root: Node | None) -> list[int]`
-   **순서**: 왼쪽(Left) → 루트(Root) → 오른쪽(Right)
-   **설명**: 왼쪽 서브트리를 모두 방문한 후 현재 노드를 처리하고, 마지막으로 오른쪽 서브트리를 방문합니다. 이진 탐색 트리(BST)에서 이 순회를 사용하면 노드 값이 오름차순으로 정렬됩니다.
-   **결과**: `[4, 2, 5, 1, 3]`

#### `postorder(root: Node | None) -> list[int]`
-   **순서**: 왼쪽(Left) → 오른쪽(Right) → 루트(Root)
-   **설명**: 왼쪽과 오른쪽 서브트리를 모두 방문한 후, 마지막으로 현재 노드를 처리합니다. 자식 노드를 먼저 삭제해야 하는 경우 등에 사용됩니다.
-   **결과**: `[4, 5, 2, 3, 1]`

### 3.2. 너비 우선 탐색 (Breadth-First Search, BFS)

#### `level_order(root: Node | None) -> Sequence[Node | None]`
-   **순서**: 위에서 아래로, 같은 레벨에서는 왼쪽에서 오른쪽으로.
-   **설명**: 큐(`deque`)를 사용하여 트리의 루트부터 시작해 각 레벨의 모든 노드를 순서대로 방문합니다.
-   **결과**: `[1, 2, 3, 4, 5]`

### 3.3. 기타 순회

#### `zigzag(root: Node | None) -> Sequence[Node | None] | list[Any]`
-   **순서**: 레벨별로 순회하되, 한 레벨은 왼쪽에서 오른쪽으로, 다음 레벨은 오른쪽에서 왼쪽으로 번갈아 가며 방문합니다.
-   **설명**: 내부적으로 `height`, `get_nodes_from_left_to_right`, `get_nodes_from_right_to_left` 함수를 사용하여 구현됩니다.
-   **결과**: `[[1], [3, 2], [4, 5]]`

## 4. 헬퍼 함수

#### `height(root: Node | None) -> int`
-   **역할**: 트리의 높이를 계산합니다. 루트만 있는 경우 높이는 1입니다.

#### `get_nodes_from_left_to_right(root: Node | None, level: int)`
-   **역할**: 특정 레벨(`level`)에 있는 노드들을 왼쪽에서 오른쪽 순서로 가져옵니다.

#### `get_nodes_from_right_to_left(root: Node | None, level: int)`
-   **역할**: 특정 레벨(`level`)에 있는 노드들을 오른쪽에서 왼쪽 순서로 가져옵니다.

## 5. 사용법 및 테스트

스크립트는 `main()` 함수를 통해 모든 순회 방식의 결과를 출력하여 기능을 시연합니다.

또한, `doctest`가 포함되어 있어 코드의 정확성을 쉽게 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하여 테스트를 진행할 수 있습니다.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/binary_tree_traversals.py
```

테스트가 성공적으로 완료되면, 각 순회 방식의 결과가 콘솔에 출력됩니다.