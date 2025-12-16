# `treap.py` 코드 설명

이 문서는 `treap.py` 스크립트에 구현된 트립(Treap) 자료 구조에 대해 설명합니다.

## 1. 트립(Treap)이란?

트립은 트리(Tree)와 힙(Heap)의 속성을 결합한 이진 트리 자료 구조입니다. 각 노드는 값(value)과 우선순위(priority)를 가집니다.

-   **값(Value)**에 대해서는 **이진 탐색 트리(Binary Search Tree)**의 속성을 만족합니다.
    -   왼쪽 서브트리의 모든 값 < 현재 노드의 값 < 오른쪽 서브트리의 모든 값
-   **우선순위(Priority)**에 대해서는 **힙(Heap)**의 속성을 만족합니다.
    -   부모 노드의 우선순위 > 자식 노드의 우선순위 (Max-heap 기준, 이 구현에서는 우선순위가 높은 쪽이 부모가 됨)

우선순위는 보통 무작위로 할당되며, 이 무작위성 덕분에 트립은 높은 확률로 균형 잡힌 상태를 유지합니다. 따라서 삽입, 삭제, 검색 연산의 기대 시간 복잡도는 O(log N)입니다.

이 구현은 **`split`**과 **`merge`**라는 두 가지 강력한 연산을 기반으로 합니다.

## 2. `Node` 클래스

트립을 구성하는 각 노드를 표현하는 클래스입니다.

-   `__init__(self, value)`: 노드를 초기화합니다.
    -   `value`: 노드가 저장하는 값.
    -   `prior`: `random()` 함수를 통해 할당되는 무작위 우선순위.
    -   `left`, `right`: 왼쪽, 오른쪽 자식 노드에 대한 참조.

## 3. 핵심 함수 설명

### `split(root: Node | None, value: int) -> tuple[Node | None, Node | None]`
-   **역할**: 주어진 `value`를 기준으로 트리를 두 개로 분리합니다.
-   **반환**: `(left_tree, right_tree)` 튜플.
    -   `left_tree`: `value`보다 작은 값들을 가진 모든 노드.
    -   `right_tree`: `value`보다 크거나 같은 값들을 가진 모든 노드.
-   **동작**: 재귀적으로 동작하며, 현재 노드의 값과 `value`를 비교하여 분할 지점을 찾고 트리를 재구성합니다.

### `merge(left: Node | None, right: Node | None) -> Node | None`
-   **역할**: 두 개의 트립을 하나로 병합합니다. **(전제 조건: `left` 트리의 모든 값은 `right` 트리의 모든 값보다 작아야 합니다.)**
-   **동작**: 두 트리의 루트 노드 중 우선순위(`prior`)가 더 높은 노드를 새로운 루트로 삼고, 나머지 부분을 재귀적으로 병합합니다.

### `insert(root: Node | None, value: int) -> Node | None`
-   **역할**: 트리에 새로운 `value`를 삽입합니다.
-   **시간 복잡도**: O(log N)
-   **동작**:
    1.  `split`을 사용하여 `value`를 기준으로 트리를 `left`와 `right`로 분리합니다.
    2.  `value`를 가진 새로운 노드를 생성합니다.
    3.  `merge(left, new_node)`를 수행하고, 그 결과와 `right`를 다시 `merge`합니다.

### `erase(root: Node | None, value: int) -> Node | None`
-   **역할**: 트리에 있는 특정 `value`를 가진 모든 노드를 삭제합니다.
-   **시간 복잡도**: O(log N)
-   **동작**:
    1.  `split(root, value - 1)`을 호출하여 `value`보다 작은 노드들(`left`)과 크거나 같은 노드들(`right`)로 분리합니다.
    2.  `right` 트리에 대해 `split(right, value)`를 호출하여 `value`와 같은 노드들을 분리해내고 버립니다.
    3.  남은 `left` 트리와 `right` 트리를 다시 `merge`합니다.

## 4. 유틸리티 및 테스트 함수

### `inorder(root: Node | None)`
-   **역할**: 트리를 중위 순회하며 노드의 값을 출력합니다. 트리의 모든 값이 정렬된 순서로 출력됩니다.

### `interactTreap(root: Node | None, args: str)`
-   **역할**: 사용자 입력을 파싱하여 트립 연산을 수행합니다.
    -   `+value`: `value`를 삽입합니다.
    -   `-value`: `value`를 삭제합니다.

### `main()`
-   **역할**: 사용자로부터 명령어를 계속 입력받아 트립을 조작하고 결과를 출력하는 메인 루프입니다.

## 5. 사용 예제

스크립트를 실행하고 명령어를 입력하여 트립을 조작할 수 있습니다.

**실행:**
```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/treap.py
```

**입력 및 출력 예시:**
```
enter numbers to create a tree, + value to add value into treap, - value to erase all nodes with value. 'q' to quit.
+1 +3 +5 +2
{'5: 0.81159': ('3: 0.77335': ('1: 0.44988': (None, '2: 0.1652')), None), None)}
-3
{'5: 0.81159': ('1: 0.44988': (None, '2: 0.1652')), None)}
q
good by!
```

## 6. 테스트

코드에는 `doctest`가 포함되어 있어 각 함수의 정확성을 검증할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/treap.py
```

테스트가 성공하면 아무런 출력도 나타나지 않습니다.