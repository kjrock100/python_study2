# `print_reverse.py` 코드 설명

이 문서는 `print_reverse.py` 스크립트에 구현된, 단일 연결 리스트(Singly Linked List)의 요소들을 역순으로 출력하는 기능에 대해 설명합니다.

## 1. 개요

이 스크립트는 두 가지 주요 기능을 제공합니다.
1.  파이썬 리스트와 같은 시퀀스로부터 단일 연결 리스트를 생성합니다.
2.  생성된 연결 리스트의 요소들을 재귀(Recursion)를 이용하여 역순으로 출력합니다.

## 2. 클래스 및 함수 설명

### `Node` 클래스

-   **역할**: 연결 리스트를 구성하는 각 요소를 표현합니다.
-   **속성**:
    -   `data`: 노드가 저장하는 실제 데이터.
    -   `next`: 다음 노드를 가리키는 참조.
-   `__repr__(self)`: 노드와 그 뒤에 연결된 모든 노드의 데이터를 `->`로 연결하여 시각적인 문자열 표현을 반환합니다.

### `make_linked_list(elements_list: list)` 함수

-   **역할**: 주어진 리스트(`elements_list`)의 요소들로 단일 연결 리스트를 생성하고, 그 리스트의 헤드(head) 노드를 반환합니다.
-   **동작**:
    1.  리스트의 첫 번째 요소로 헤드 노드를 만듭니다.
    2.  리스트의 나머지 요소들을 순회하며 새로운 노드를 생성하고, 이전 노드의 `next` 포인터에 연결합니다.

### `print_reverse(head_node: Node) -> None` 함수

-   **역할**: 주어진 연결 리스트의 요소들을 역순으로 화면에 출력합니다.
-   **핵심 로직 (재귀)**:
    1.  **기저 사례 (Base Case)**: `head_node`가 `None`이면(리스트의 끝에 도달하면) 함수를 종료합니다.
    2.  **재귀 단계 (Recursive Step)**:
        -   `print_reverse(head_node.next)`를 호출하여 리스트의 나머지 부분에 대해 재귀적으로 함수를 실행합니다.
        -   재귀 호출이 모두 끝나고 반환되면(즉, 가장 마지막 노드부터), `print(head_node.data)`를 실행하여 현재 노드의 데이터를 출력합니다.
    -   이러한 "호출 후 출력" 방식 때문에, 함수 호출 스택(Call Stack)에 쌓였던 작업들이 역순으로 실행되면서 리스트의 요소들이 뒤에서부터 출력됩니다.

## 3. 사용 예제

`main()` 함수는 이 스크립트의 사용법을 보여줍니다.

```python
def main():
    # doctest 실행
    from doctest import testmod
    testmod()

    # 리스트로부터 연결 리스트 생성
    linked_list = make_linked_list([14, 52, 14, 12, 43])

    # 원본 연결 리스트 출력
    print("Linked List:")
    print(linked_list)
    # 출력:
    # Linked List:
    # 14->52->14->12->43

    # 역순으로 출력
    print("Elements in Reverse:")
    print_reverse(linked_list)
    # 출력:
    # Elements in Reverse:
    # 43
    # 12
    # 14
    # 52
    # 14
```

## 4. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/linked_list/print_reverse.py
```

테스트가 모두 통과하면 `main()` 함수의 출력 결과만 화면에 나타납니다.