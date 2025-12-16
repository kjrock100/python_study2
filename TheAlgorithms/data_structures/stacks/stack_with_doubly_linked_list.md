# `stack_with_doubly_linked_list.py` 코드 설명

이 문서는 `stack_with_doubly_linked_list.py` 스크립트에 구현된, 이중 연결 리스트(Doubly Linked List)를 이용한 스택(Stack) 자료 구조에 대해 설명합니다.

## 1. 스택(Stack)이란?

스택은 후입선출(Last-In, First-Out, LIFO) 원칙을 따르는 선형 자료 구조입니다. 즉, 가장 마지막에 추가된 요소가 가장 먼저 제거됩니다.

**주요 연산:**
-   **Push**: 스택의 맨 위에 요소를 추가합니다.
-   **Pop**: 스택의 맨 위에서 요소를 제거하고 반환합니다.

## 2. 이중 연결 리스트 기반 구현

이 코드는 스택을 이중 연결 리스트를 사용하여 구현합니다.

-   **`head` 포인터**: 스택의 맨 위(top)에 있는 노드를 가리킵니다.
-   **Push 연산**: 새로운 노드를 생성하여 리스트의 맨 앞에 추가하고, `head`를 이 새 노드로 갱신합니다.
-   **Pop 연산**: 현재 `head` 노드를 제거하고, `head`를 다음 노드로 갱신합니다.

이중 연결 리스트를 사용하면 `push`와 `pop` 연산 모두 O(1)의 시간 복잡도를 가집니다.

## 3. 클래스 및 메서드 설명

### `Node` 클래스
-   **역할**: 이중 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드를 가리키는 참조.
    -   `prev`: 이전 노드를 가리키는 참조.

### `Stack` 클래스

#### `__init__(self)`
-   **역할**: 빈 스택을 초기화하며, `head`를 `None`으로 설정합니다.

#### `push(self, data: T) -> None`
-   **역할**: 스택의 맨 위에 새로운 데이터를 추가합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  새로운 `Node`를 생성합니다.
    2.  스택이 비어있으면, `head`를 새 노드로 설정합니다.
    3.  그렇지 않으면, 새 노드의 `next`를 기존 `head`로, 기존 `head`의 `prev`를 새 노드로 연결한 후, `head`를 새 노드로 갱신합니다.

#### `pop(self) -> T | None`
-   **역할**: 스택의 맨 위에서 요소를 제거하고 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  스택이 비어있으면 `None`을 반환합니다.
    2.  `head` 노드의 데이터를 저장합니다.
    3.  `head` 포인터를 다음 노드로 이동시킵니다.
    4.  새로운 `head`가 존재하면, 그 `prev` 포인터를 `None`으로 설정하여 이전 노드와의 연결을 끊습니다.
    5.  저장해 둔 데이터를 반환합니다.

#### `top(self) -> T | None`
-   **역할**: 스택의 맨 위 요소를 삭제하지 않고 반환합니다.
-   **시간 복잡도**: O(1)

#### `__len__(self) -> int`
-   **역할**: 스택에 포함된 요소의 개수를 반환합니다.
-   **시간 복잡도**: O(N), 스택의 모든 노드를 순회하여 길이를 계산합니다.
    > **개선 제안**: 클래스에 `size` 속성을 추가하고 `push`/`pop` 시마다 값을 증감시키면 O(1)으로 개선할 수 있습니다.

#### `is_empty(self) -> bool`
-   **역할**: 스택이 비어있는지 확인합니다.
-   **시간 복잡도**: O(1)

#### `print_stack(self) -> None`
-   **역할**: 스택의 내용을 맨 위 요소부터 순서대로 출력합니다.

## 4. 사용 예제

`doctest`와 `if __name__ == "__main__"` 블록에 사용 예제가 포함되어 있습니다.

```python
# 빈 스택 생성
stack = Stack()

# 데이터 삽입 (push)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

# 현재 스택 상태 출력
stack.print_stack()
# 출력: stack elements are:
#       7->6->5->4->

# 맨 위 요소 확인
print("\nTop element is ", stack.top())
# 출력: Top element is  7

# 스택 크기 확인
print("Size of the stack is ", len(stack))
# 출력: Size of the stack is  4

# 데이터 추출 (pop)
stack.pop()
stack.pop()

# pop 이후 스택 상태
stack.print_stack()
# 출력: stack elements are:
#       5->4->

# 스택이 비어있는지 확인
print("\nstack is empty:", stack.is_empty())
# 출력: stack is empty: False
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/stacks/stack_with_doubly_linked_list.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.