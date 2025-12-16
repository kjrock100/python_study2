# `balanced_parentheses.py` 코드 설명

이 문서는 `balanced_parentheses.py` 스크립트에 구현된, 괄호 문자열의 균형을 확인하는 알고리즘에 대해 설명합니다.

## 1. 문제 설명: 균형 잡힌 괄호

균형 잡힌 괄호 문자열은 다음 규칙을 만족하는 문자열을 의미합니다.

1.  모든 여는 괄호 `(`, `[`, `{`는 반드시 짝이 맞는 닫는 괄호 `)`, `]`, `}`를 가져야 합니다.
2.  괄호의 쌍은 올바른 순서로 닫혀야 합니다. 예를 들어, `[(])`는 짝은 맞지만 순서가 틀렸으므로 균형 잡히지 않은 문자열입니다.

이 스크립트의 목적은 주어진 문자열이 이러한 규칙을 만족하는지 확인하는 것입니다.

## 2. 핵심 알고리즘: 스택(Stack) 활용

이 코드는 **스택(Stack)** 자료 구조를 사용하여 괄호의 균형을 효율적으로 검사합니다. 스택은 후입선출(Last-In, First-Out, LIFO) 특성을 가지며, 이 문제에 매우 적합합니다.

**동작 원리:**
1.  빈 스택을 생성합니다.
2.  입력 문자열을 처음부터 끝까지 한 글자씩 순회합니다.
3.  **여는 괄호 (`(`, `[`, `{`)를 만나면**: 스택에 `push`합니다.
4.  **닫는 괄호 (`)`, `]`, `}`)를 만나면**:
    -   만약 스택이 비어있다면, 짝이 맞는 여는 괄호가 없다는 의미이므로 즉시 `False`를 반환합니다.
    -   스택에서 가장 최근에 추가된 여는 괄호를 `pop`합니다.
    -   `pop`한 여는 괄호가 현재의 닫는 괄호와 짝이 맞지 않으면, `False`를 반환합니다.
5.  **괄호가 아닌 다른 문자**는 무시합니다.
6.  문자열 순회가 끝난 후, **스택이 비어있으면** 모든 괄호의 짝이 맞았다는 의미이므로 `True`를 반환합니다. 만약 스택에 여는 괄호가 남아있다면, 짝이 맞지 않는 것이므로 `False`를 반환합니다.

## 3. 함수 설명

### `balanced_parentheses(parentheses: str) -> bool`

-   **역할**: 주어진 문자열 `parentheses`가 균형 잡힌 괄호를 가지고 있는지 여부를 `True` 또는 `False`로 반환합니다.
-   **매개변수**:
    -   `parentheses`: 검사할 괄호 문자열.
-   **시간 복잡도**: O(N), 여기서 N은 문자열의 길이입니다. 문자열을 한 번만 순회합니다.
-   **공간 복잡도**: O(N), 최악의 경우(모든 문자가 여는 괄호일 때) 스택에 모든 괄호를 저장해야 합니다.

## 4. 사용 예제

`doctest`와 `if __name__ == "__main__"` 블록에 다양한 사용 예제가 포함되어 있습니다.

```python
# doctest 예제
>>> balanced_parentheses("([]{})")
True
>>> balanced_parentheses("[()]{}{[()()]()}")
True
>>> balanced_parentheses("[(])")
False
>>> balanced_parentheses("1+2*3-4") # 괄호가 아닌 문자는 무시됨
True

# main 블록 예제
examples = ["((()))", "((())", "(()))"]
for example in examples:
    not_str = "" if balanced_parentheses(example) else "not "
    print(f"{example} is {not_str}balanced")

# 출력:
# ((())) is balanced
# ((()) is not balanced
# (())) is not balanced
```

## 5. 테스트 실행

파일에 포함된 `doctest`를 실행하여 코드의 정확성을 검증할 수 있습니다. 터미널에서 다음 명령어를 실행하세요.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/stacks/balanced_parentheses.py
```

테스트가 모두 통과하면 아무런 출력도 나타나지 않습니다.