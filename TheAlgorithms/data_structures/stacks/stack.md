# `stack.py` 코드 설명

이 문서는 `stack.py` 스크립트에 구현된, 파이썬 리스트를 이용한 기본적인 스택(Stack) 자료 구조에 대해 설명합니다.

## 1. 스택(Stack)이란?

스택은 후입선출(Last-In, First-Out, LIFO) 원칙을 따르는 선형 자료 구조입니다. 즉, 가장 마지막에 추가된 요소가 가장 먼저 제거됩니다. 접시를 쌓는 것에 비유할 수 있습니다.

**주요 연산:**
-   **Push**: 스택의 맨 위에 요소를 추가합니다.
-   **Pop**: 스택의 맨 위에서 요소를 제거하고 반환합니다.
-   **Peek (또는 Top)**: 스택의 맨 위 요소를 제거하지 않고 확인합니다.

## 2. 구현 특징

-   **리스트 기반**: 파이썬의 내장 리스트(`list`)를 사용하여 스택을 구현합니다.
-   **고정 용량**: 생성 시 `limit`을 지정하여 스택의 최대 크기를 제한할 수 있습니다.
-   **사용자 정의 예외**: 스택이 가득 찼을 때(`StackOverflowError`) 또는 비어있을 때(`StackUnderflowError`) 발생하는 사용자 정의 예외를 정의하여 오류 상황을 명확하게 처리합니다.

## 3. 클래스 및 메서드 설명

### `Stack` 클래스

#### `__init__(self, limit: int = 10)`
-   **역할**: 스택을 초기화합니다.
-   **매개변수**:
    -   `limit`: 스택의 최대 용량 (기본값: 10).
-   **속성**:
    -   `stack`: 실제 데이터가 저장되는 리스트.
    -   `limit`: 최대 용량.

#### `push(self, data: T) -> None`
-   **역할**: 스택의 맨 위에 새로운 데이터를 추가합니다.
-   **시간 복잡도**: O(1) (분할 상환 분석)
-   **동작**:
    1.  스택이 가득 찼는지(`len(self.stack) >= self.limit`) 확인하고, 가득 찼으면 `StackOverflowError`를 발생시킵니다.
    2.  리스트의 `append` 메서드를 사용하여 데이터를 추가합니다.

#### `pop(self) -> T`
-   **역할**: 스택의 맨 위에서 요소를 제거하고 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**:
    1.  스택이 비어있는지 확인하고, 비어있으면 `StackUnderflowError`를 발생시킵니다.
    2.  리스트의 `pop` 메서드를 사용하여 마지막 요소를 제거하고 반환합니다.

#### `peek(self) -> T`
-   **역할**: 스택의 맨 위 요소를 삭제하지 않고 반환합니다.
-   **시간 복잡도**: O(1)
-   **동작**: 스택이 비어있으면 `StackUnderflowError`를, 아니면 `self.stack[-1]`을 반환합니다.

#### 유틸리티 메서드

-   `is_empty(self) -> bool`: 스택이 비어있는지 확인합니다. (O(1))
-   `is_full(self) -> bool`: 스택이 가득 찼는지 확인합니다. (O(1))
-   `size(self) -> int`: 스택의 현재 크기를 반환합니다. (O(1))

#### Dunder (Special) 메서드

-   `__bool__(self)`: 스택에 요소가 있는지 여부를 불리언 값으로 반환합니다. `if stack:` 구문에서 사용됩니다.
-   `__str__(self)`: 스택의 리스트 표현을 문자열로 반환합니다. `print(stack)` 구문에서 사용됩니다.
-   `__contains__(self, item: T)`: 특정 `item`이 스택에 포함되어 있는지 확인합니다. `item in stack` 구문을 지원합니다. (O(N))

## 4. 사용 예제

`test_stack()` 함수는 이 클래스의 사용법을 잘 보여줍니다.

```python
# 용량이 10인 스택 생성
stack = Stack(10)

# 스택이 비었는지 확인
assert stack.is_empty() is True

# 0부터 9까지 데이터 삽입
for i in range(10):
    stack.push(i)

# 스택이 가득 찼는지 확인
assert stack.is_full() is True

# 스택 오버플로우 예외 테스트
try:
    stack.push(100)
except StackOverflowError:
    print("Stack overflow occurred as expected.")

# 맨 위 요소 확인 및 추출
print(f"Top element: {stack.peek()}")  # 출력: Top element: 9
print(f"Popped element: {stack.pop()}") # 출력: Popped element: 9

print(f"New top element: {stack.peek()}") # 출력: New top element: 8
print(f"Stack size: {stack.size()}")    # 출력: Stack size: 9
```

## 5. 테스트 실행

스크립트를 직접 실행하면 `test_stack()` 함수가 호출되어 스택의 모든 기능이 올바르게 동작하는지 `assert` 문을 통해 검증합니다.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/stacks/stack.py
```

모든 `assert` 문을 통과하면 아무런 출력 없이 정상적으로 종료됩니다.

또한, `doctest`가 포함되어 있어 각 메서드의 독스트링에 있는 예제를 검증할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/stacks/stack.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.