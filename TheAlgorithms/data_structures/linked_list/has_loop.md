# `has_loop.py` 코드 설명

이 문서는 `has_loop.py` 스크립트에 구현된, 단일 연결 리스트(Singly Linked List)에서 루프(Loop) 또는 사이클(Cycle)의 존재 여부를 감지하는 기능에 대해 설명합니다.

## 1. 문제 설명: 연결 리스트의 루프 감지

연결 리스트에서 루프는 리스트의 마지막 노드가 `None`을 가리키는 대신, 리스트 내의 이전 노드 중 하나를 가리킬 때 발생합니다. 이로 인해 리스트를 순회할 때 무한 루프에 빠질 수 있습니다.

이 스크립트의 목적은 주어진 연결 리스트에 이러한 루프가 존재하는지 효율적으로 확인하는 것입니다.

## 2. 클래스 및 예외 설명

### `ContainsLoopError` 클래스
-   **역할**: 연결 리스트 순회 중 루프가 감지되었을 때 발생하는 사용자 정의 예외입니다.

### `Node` 클래스
-   **역할**: 연결 리스트를 구성하는 각 요소를 표현하는 클래스입니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next_node`: 다음 노드를 가리키는 참조.
-   **`__iter__(self)` 메서드**:
    -   **역할**: 노드부터 시작하여 연결 리스트를 순회하는 이터레이터(iterator)를 제공합니다.
    -   **루프 감지 로직**: 순회 중 이미 방문했던 노드를 다시 만나면 `ContainsLoopError` 예외를 발생시켜 루프의 존재를 알립니다. 이를 위해 `visited` 리스트에 방문한 노드 객체를 저장합니다.
    -   **시간 복잡도**: O(N) (최악의 경우 모든 노드를 방문)
    -   **공간 복잡도**: O(N) (방문한 노드를 저장하기 위한 `visited` 리스트)

## 3. `has_loop` 속성

### `has_loop(self) -> bool` (property)
-   **역할**: 현재 노드부터 시작하는 연결 리스트에 루프가 있는지 여부를 `True` 또는 `False`로 반환합니다.
-   **동작**:
    1.  `try-except` 블록을 사용하여 `self.__iter__()`를 호출하고 `list()`로 모든 노드를 순회하려고 시도합니다.
    2.  만약 `__iter__` 메서드에서 `ContainsLoopError`가 발생하면, 이는 루프가 존재한다는 의미이므로 `True`를 반환합니다.
    3.  `ContainsLoopError`가 발생하지 않고 순회가 성공적으로 완료되면, 루프가 없다는 의미이므로 `False`를 반환합니다.

## 4. 사용 예제

스크립트의 `if __name__ == "__main__":` 블록은 `has_loop` 속성의 사용법을 보여줍니다.

```python
if __name__ == "__main__":
    # 루프가 없는 연결 리스트 생성
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_loop)  # 출력: False

    # 루프가 있는 연결 리스트 생성 (4 -> 2)
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_loop)  # 출력: True

    # 데이터 값은 같지만 노드 객체는 다른 경우 (루프 아님)
    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)  # 새로운 Node(5) 객체
    root_node.next_node.next_node.next_node = Node(6) # 새로운 Node(6) 객체
    print(root_node.has_loop)  # 출력: False

    # 단일 노드 리스트 (루프 아님)
    root_node = Node(1)
    print(root_node.has_loop)  # 출력: False
```

## 5. 루프 감지 알고리즘에 대한 고려사항

현재 `__iter__` 메서드에서 사용하는 루프 감지 방식은 `visited` 리스트를 사용하여 이미 방문한 노드 객체를 추적합니다.

-   **장점**: 구현이 직관적입니다.
-   **단점**: `visited` 리스트에 모든 노드를 저장해야 하므로 O(N)의 추가 공간 복잡도를 필요로 합니다.

더 효율적인 루프 감지 알고리즘으로는 **플로이드의 사이클 감지 알고리즘(Floyd's Cycle-Finding Algorithm)**, 일명 **토끼와 거북이(Tortoise and Hare) 알고리즘**이 있습니다. 이 알고리즘은 두 개의 포인터(하나는 한 칸씩, 다른 하나는 두 칸씩 이동)를 사용하여 O(N) 시간 복잡도와 O(1) 공간 복잡도로 루프를 감지할 수 있습니다.

## 6. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/has_loop.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.