# Binary Search Tree (이진 탐색 트리)

이 문서는 `binary_search_tree.py` 파일에 구현된 이진 탐색 트리에 대한 설명을 제공합니다.

## 1. 이진 탐색 트리란?

이진 탐색 트리(Binary Search Tree, BST)는 다음과 같은 속성을 가진 노드 기반의 이진 트리 자료 구조입니다.

-   각 노드의 왼쪽 서브트리에는 해당 노드의 값보다 작은 값들만 포함됩니다.
-   각 노드의 오른쪽 서브트리에는 해당 노드의 값보다 큰 값들만 포함됩니다.
-   왼쪽과 오른쪽 서브트리 또한 각각 이진 탐색 트리입니다.
-   일반적으로 중복된 값은 허용되지 않지만, 이 구현에서는 중복 시 오른쪽에 배치됩니다.

이러한 속성 덕분에 균형이 잘 잡힌 트리의 경우, 평균적으로 O(log n) 시간 복잡도로 항목을 검색, 추가, 삭제할 수 있습니다.

## 2. 파일 구조

이 파이썬 파일은 두 개의 클래스와 여러 함수로 구성됩니다.

-   `Node`: 트리의 각 노드를 나타내는 클래스입니다.
-   `BinarySearchTree`: 이진 탐색 트리 자체를 나타내며, 노드를 추가, 검색, 삭제하는 등의 메서드를 포함합니다.
-   `postorder`: 후위 순회를 위한 독립적인 함수입니다.
-   `binary_search_tree`: doctest와 예제 코드를 포함하는 함수입니다.

## 3. 클래스 및 메서드 설명

### 3.1. `Node` 클래스

트리의 기본 구성 요소인 노드를 정의합니다.

-   `__init__(self, value, parent)`: 노드를 초기화합니다.
    -   `value`: 노드가 저장하는 값입니다.
    -   `parent`: 부모 노드를 가리킵니다. 노드 삭제 시 재연결을 용이하게 합니다.
    -   `left`: 왼쪽 자식 노드를 가리킵니다.
    -   `right`: 오른쪽 자식 노드를 가리킵니다.
-   `__repr__(self)`: `pprint`를 사용하여 트리의 구조를 시각적으로 보기 좋게 표현합니다.

### 3.2. `BinarySearchTree` 클래스

이진 탐색 트리의 전체적인 동작을 관리합니다.

-   `__init__(self, root=None)`: 트리를 초기화하며, `root` 노드를 설정할 수 있습니다.
-   `__str__(self)`: 트리를 문자열로 표현합니다. `Node`의 `__repr__`를 호출하여 전체 트리를 출력합니다.
-   `insert(self, *values)`: 하나 이상의 값을 받아 트리에 삽입합니다. 내부적으로 `__insert` 메서드를 호출합니다.
-   `search(self, value)`: 주어진 `value`를 가진 노드를 찾아 반환합니다. 값이 없으면 `None`을 반환하고, 트리가 비어있으면 `IndexError`를 발생시킵니다.
-   `remove(self, value)`: 주어진 `value`를 가진 노드를 삭제합니다. 삭제할 노드의 자식 수에 따라 세 가지 경우를 처리합니다.
    1.  **자식이 없는 경우**: 해당 노드를 그냥 삭제합니다.
    2.  **자식이 하나인 경우**: 해당 노드를 자식 노드로 교체합니다.
    3.  **자식이 둘인 경우**: 왼쪽 서브트리에서 가장 큰 값(In-order Predecessor)을 찾아 현재 노드의 값과 교체한 후, 해당 노드를 삭제합니다.
-   `get_max(self, node=None)`: 특정 서브트리(기본값은 전체 트리)에서 가장 큰 값을 가진 노드를 반환합니다.
-   `get_min(self, node=None)`: 특정 서브트리(기본값은 전체 트리)에서 가장 작은 값을 가진 노드를 반환합니다.
-   `traversal_tree(self, traversal_function=None)`: 트리를 순회합니다. 순회 함수를 인자로 받을 수 있으며, 기본적으로는 전위 순회(`preorder_traverse`)를 수행합니다.
-   `preorder_traverse(self, node)`: 전위 순회(루트 -> 왼쪽 -> 오른쪽)를 수행하는 제너레이터입니다.
-   `inorder(self, arr: list, node: Node)`: 중위 순회(왼쪽 -> 루트 -> 오른쪽)를 수행하고 결과를 리스트 `arr`에 저장합니다.
-   `find_kth_smallest(self, k: int, node: Node)`: 트리에서 k번째로 작은 원소를 찾습니다. 중위 순회 결과가 오름차순 정렬된다는 속성을 이용합니다.

#### 내부 헬퍼 메서드

-   `__reassign_nodes(self, node, new_children)`: 노드 삭제 시 부모와 자식 노드 간의 연결을 재설정합니다.
-   `is_right(self, node)`: 해당 노드가 부모의 오른쪽 자식인지 확인합니다.
-   `__insert(self, value)`: 단일 값을 트리에 삽입하는 내부 로직입니다.

### 3.3. 독립 함수

-   `postorder(curr_node)`: 후위 순회(왼쪽 -> 오른쪽 -> 루트)를 수행하고 노드 리스트를 반환합니다.

## 4. 사용 예제

```python
# 이진 탐색 트리 생성 및 값 삽입
t = BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)

# 트리 구조 출력 (pprint 형식)
print(t)
# {8: ({3: ({1: None},
#           {6: ({4: None},
#                {7: None})})},
#      {10: (None,
#            {14: ({13: None},
#                  None)})})}

# 값 검색
if t.search(6) is not None:
    print("값 6이 트리에 존재합니다.")
else:
    print("값 6이 트리에 존재하지 않습니다.")

# 최대/최소값 찾기
print("최대값: ", t.get_max().value)
print("최소값: ", t.get_min().value)

# 전위 순회
print("전위 순회:", " ".join(repr(i.value) for i in t.traversal_tree()))

# 후위 순회
print("후위 순회:", " ".join(repr(i.value) for i in t.traversal_tree(postorder)))

# k번째 작은 값 찾기
k = 3
print(f"{k}번째 작은 값: {t.find_kth_smallest(k, t.root)}")

# 값 삭제
t.remove(3)
print("3을 삭제한 후 트리 구조:")
print(t)
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/binary_search_tree.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.