# `basic_binary_tree.py` 코드 설명

이 문서는 `basic_binary_tree.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 기본적인 **이진 트리(Binary Tree)** 자료구조와 관련 유틸리티 함수들을 구현합니다.

## 목차
1.  이진 트리란?
2.  클래스 설명
    -   `Node`
3.  함수 설명
    -   `display(tree)`
    -   `depth_of_tree(tree)`
    -   `is_full_binary_tree(tree)`
4.  실행 방법
5.  코드 개선 제안

## 이진 트리란?

이진 트리는 각 노드가 최대 두 개의 자식 노드(왼쪽 자식, 오른쪽 자식)를 갖는 트리 자료구조입니다. 이 스크립트는 이러한 노드들을 연결하여 트리를 구성하고, 트리의 속성을 분석하는 함수들을 제공합니다.

## 클래스 설명

### `Node`

이진 트리를 구성하는 각 노드를 나타내는 클래스입니다.

-   `data`: 노드에 저장되는 값.
-   `left`: 왼쪽 자식 노드를 가리키는 포인터.
-   `right`: 오른쪽 자식 노드를 가리키는 포인터.

## 함수 설명

### `display(tree: Node | None) -> None`

주어진 트리를 **중위 순회(In-order Traversal)** 방식으로 순회하며 각 노드의 값을 출력합니다.

-   **알고리즘**:
    1.  왼쪽 서브트리를 재귀적으로 방문합니다.
    2.  현재 노드의 값을 출력합니다.
    3.  오른쪽 서브트리를 재귀적으로 방문합니다.

### `depth_of_tree(tree: Node | None) -> int`

이진 트리의 깊이(또는 높이)를 계산합니다.

-   **알고리즘**:
    1.  **종료 조건**: 트리가 비어있으면(None), 깊이는 0입니다.
    2.  **재귀 단계**: 왼쪽 서브트리의 깊이와 오른쪽 서브트리의 깊이를 각각 재귀적으로 계산합니다.
    3.  두 깊이 중 더 큰 값에 1(현재 노드)을 더하여 반환합니다.

### `is_full_binary_tree(tree: Node) -> bool`

주어진 트리가 **정 이진 트리(Full Binary Tree)**인지 확인합니다.

-   **정 이진 트리란?**: 모든 노드가 0개 또는 2개의 자식 노드를 갖는 트리입니다.
-   **알고리즘**:
    1.  **종료 조건**: 트리가 비어있으면, 정 이진 트리로 간주합니다.
    2.  **검사**: 현재 노드의 자식이 하나만 있거나(왼쪽만 있거나 오른쪽만 있음) 하면, 정 이진 트리가 아니므로 `False`를 반환합니다.
    3.  **재귀 단계**: 현재 노드가 0개 또는 2개의 자식을 갖는다면, 왼쪽과 오른쪽 서브트리에 대해 재귀적으로 함수를 호출하여 두 서브트리 모두 정 이진 트리인지 확인합니다.

## 실행 방법

스크립트를 직접 실행하면 `main` 함수가 호출되어 예제 트리를 생성하고, `is_full_binary_tree`, `depth_of_tree`, `display` 함수를 차례로 실행하여 결과를 출력합니다.

```bash
python basic_binary_tree.py
```

**실행 결과:**
```
False
5
Tree is: 
4
2
6
5
1
8
9
7
3
```

## 코드 개선 제안

1.  **클래스 기반 설계**: 현재 노드 클래스와 트리 연산 함수들이 분리되어 있습니다. 이들을 `BinaryTree`라는 클래스로 묶고, `display`, `depth_of_tree` 등을 그 클래스의 메서드로 만들면 코드의 캡슐화가 향상되고 객체 지향적인 설계가 됩니다.

    ```python
    # 개선 제안 예시
    class BinaryTree:
        def __init__(self, root: Node | None = None):
            self.root = root

        def display(self):
            self._display_recursive(self.root)

        def _display_recursive(self, node):
            # ...

        def get_depth(self):
            return self._depth_of_tree_recursive(self.root)
        
        # ...
    ```

2.  **`display` 함수의 유연성**: 현재 `display` 함수는 중위 순회만 지원하며 결과를 항상 `print`합니다. `binary_tree_traversals.py`처럼, 다양한 순회 방식(전위, 후위, 레벨 순서)을 구현하고, 결과를 리스트로 반환하도록 하면 함수의 재사용성이 높아집니다.

3.  **`doctest` 활용**: `main` 함수에서 테스트하는 대신, 각 함수에 `doctest`를 추가하면 코드의 문서화와 테스트를 동시에 수행할 수 있어 유지보수가 더 편리해집니다. (현재 코드에는 이미 `doctest`가 잘 작성되어 있습니다.)