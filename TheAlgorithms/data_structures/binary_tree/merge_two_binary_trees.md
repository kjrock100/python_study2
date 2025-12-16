# `merge_two_binary_trees.py` 코드 설명

이 문서는 `merge_two_binary_trees.py` 스크립트에 구현된 두 이진 트리를 병합하는 기능에 대해 설명합니다.

## 1. 문제 설명

두 개의 이진 트리가 주어졌을 때, 이들을 병합하여 새로운 트리를 만드는 문제입니다. 병합 규칙은 다음과 같습니다.

-   두 트리의 노드가 같은 위치에서 겹치면, 두 노드의 값을 더하여 병합된 트리의 새로운 노드 값으로 합니다.
-   한쪽 트리에만 노드가 존재하고 다른 쪽에는 없다면, 존재하는 노드를 그대로 병합된 트리의 노드로 사용합니다.

## 2. `Node` 클래스

트리를 구성하는 기본 단위인 노드를 표현하는 클래스입니다.

```python
class Node:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None
```
-   `value`: 노드가 저장하는 정수 값입니다.
-   `left`: 왼쪽 자식 노드를 가리킵니다.
-   `right`: 오른쪽 자식 노드를 가리킵니다.

## 3. 함수 설명

### `merge_two_binary_trees(tree1: Node | None, tree2: Node | None) -> Node | None`

-   **역할**: 두 개의 이진 트리(`tree1`, `tree2`)를 병합하고, 병합된 트리의 루트 노드를 반환합니다.
-   **동작 원리 (재귀)**:
    1.  **기저 사례 (Base Case)**:
        -   `tree1`이 `None`이면, `tree2`를 그대로 반환합니다.
        -   `tree2`가 `None`이면, `tree1`을 그대로 반환합니다.
    2.  **재귀 단계 (Recursive Step)**:
        -   `tree1`과 `tree2`가 모두 존재하면, `tree1`의 노드 값에 `tree2`의 노드 값을 더하여 `tree1`의 값을 갱신합니다.
        -   `tree1`의 왼쪽 자식과 `tree2`의 왼쪽 자식을 재귀적으로 병합하여 그 결과를 `tree1`의 새로운 왼쪽 자식으로 설정합니다.
        -   `tree1`의 오른쪽 자식과 `tree2`의 오른쪽 자식을 재귀적으로 병합하여 그 결과를 `tree1`의 새로운 오른쪽 자식으로 설정합니다.
    3.  **반환**: 수정된 `tree1`을 반환합니다. 이 함수는 `tree1`을 직접 수정(in-place)하는 방식으로 동작합니다.

### `print_preorder(root: Node | None) -> None`

-   **역할**: 트리의 노드들을 전위 순회(Pre-order: 루트 → 왼쪽 → 오른쪽) 방식으로 방문하여 각 노드의 값을 출력합니다. 병합 결과를 확인하기 위한 헬퍼 함수입니다.

## 4. 사용 예제

스크립트의 `if __name__ == "__main__":` 블록은 두 개의 예제 트리를 생성하고 병합한 후, 각 트리의 내용과 병합된 트리의 내용을 출력하여 함수의 동작을 보여줍니다.

```python
if __name__ == "__main__":
    # 첫 번째 트리 생성
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)
    tree1.left.left = Node(4)

    # 두 번째 트리 생성
    tree2 = Node(2)
    tree2.left = Node(4)
    tree2.right = Node(6)
    tree2.left.right = Node(9)
    tree2.right.right = Node(5)

    print("Tree1 is: ")
    print_preorder(tree1)
    # 출력: 1, 2, 4, 3

    print("Tree2 is: ")
    print_preorder(tree2)
    # 출력: 2, 4, 9, 6, 5

    merged_tree = merge_two_binary_trees(tree1, tree2)
    print("Merged Tree is: ")
    print_preorder(merged_tree)
    # 출력: 3, 6, 4, 9, 9, 5
```