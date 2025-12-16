# `from_sequence.py` 코드 설명

이 문서는 `from_sequence.py` 스크립트에 구현된, 시퀀스(리스트 또는 튜플)로부터 단일 연결 리스트를 생성하는 기능에 대해 설명합니다.

## 1. 개요

이 스크립트의 주된 목적은 파이썬의 리스트나 튜플과 같은 시퀀스 데이터를 입력받아, 이를 기반으로 새로운 단일 연결 리스트(Singly Linked List)를 구축하고 그 문자열 표현을 출력하는 것입니다.

## 2. 클래스 및 함수 설명

### `Node` 클래스

연결 리스트를 구성하는 각 요소를 표현하는 클래스입니다.

-   `__init__(self, data=None)`: 노드를 초기화합니다.
    -   `data`: 노드가 저장하는 실제 데이터. 기본값은 `None`입니다.
    -   `next`: 다음 노드를 가리키는 참조. 초기값은 `None`입니다.
-   `__repr__(self)`: 노드와 그 뒤에 연결된 모든 노드의 시각적인 문자열 표현을 반환합니다.
    -   **예시**: `<1> ---> <3> ---> <5> ---> <END>`

### `make_linked_list(elements_list)` 함수

-   **역할**: 주어진 시퀀스(`elements_list`)의 요소들로 단일 연결 리스트를 생성하고, 그 리스트의 헤드(head) 노드를 반환합니다.
-   **매개변수**:
    -   `elements_list`: 연결 리스트를 만들고자 하는 요소들의 시퀀스 (예: `[1, 2, 3]`, `(a, b, c)`).
-   **동작 과정**:
    1.  **빈 리스트 처리**: `elements_list`가 비어있으면 `Exception`을 발생시킵니다.
    2.  **헤드 노드 생성**: `elements_list`의 첫 번째 요소를 사용하여 `head` 노드를 생성합니다. `current` 포인터도 `head`를 가리키도록 초기화합니다.
    3.  **나머지 노드 연결**: `elements_list`의 두 번째 요소부터 마지막 요소까지 반복합니다.
        -   각 요소에 대해 새로운 `Node`를 생성합니다.
        -   `current.next`를 새로 생성된 노드로 설정하여 연결합니다.
        -   `current`를 새로 생성된 노드로 이동시킵니다.
    4.  **반환**: 최종적으로 생성된 연결 리스트의 `head` 노드를 반환합니다.

## 3. 사용 예제

스크립트의 `if __name__ == "__main__":` 블록은 `make_linked_list` 함수의 사용법을 보여줍니다.

```python
# 예제 데이터 리스트
list_data = [1, 3, 5, 32, 44, 12, 43]
print(f"List: {list_data}")
# 출력: List: [1, 3, 5, 32, 44, 12, 43]

print("Creating Linked List from List.")
# 출력: Creating Linked List from List.

# make_linked_list 함수를 호출하여 연결 리스트 생성
linked_list = make_linked_list(list_data)

print("Linked List:")
# 출력: Linked List:

# 생성된 연결 리스트 출력 (Node.__repr__ 메서드 사용)
print(linked_list)
# 출력: <1> ---> <3> ---> <5> ---> <32> ---> <44> ---> <12> ---> <43> ---> <END>
```

## 4. 테스트

이 스크립트에는 별도의 `doctest`나 `unittest`가 포함되어 있지 않지만, `if __name__ == "__main__":` 블록의 예제 코드를 통해 기본적인 동작을 확인할 수 있습니다.