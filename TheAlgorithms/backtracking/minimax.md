## 코드 분석: minimax.py

이 파이썬 스크립트는 미니맥스(Minimax) 알고리즘을 구현한 것입니다. 미니맥스는 틱택토나 체스와 같은 2인용 게임에서, 상대방이 항상 최선의 수를 둔다고 가정할 때 자신에게 가장 유리한 수를 찾는 데 사용되는 의사결정 알고리즘입니다.

이 코드는 게임의 마지막 상태(leaf node)들의 점수(scores)가 주어졌을 때, 루트 노드에서 어떤 값을 얻을 수 있는지를 재귀적으로 계산합니다.

## minimax 함수 (핵심 로직)

```python
import math

def minimax(
    depth: int, node_index: int, is_max: bool, scores: list[int], height: float
) -> int:
    """
    >>> import math
    >>> scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    65
    # ... (doctest 생략)
    """

    # 1. 입력값 검증
    if depth < 0:
        raise ValueError("Depth cannot be less than 0")
    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    # 2. 재귀 종료 조건 (Base Case)
    if depth == height:
        return scores[node_index]

    # 3. 재귀 호출 (Recursive Step)
    if is_max:
        # Maximizer의 차례: 자식 노드들의 결과 중 최댓값을 선택
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )
    else: # is_max가 False일 때
        # Minimizer의 차례: 자식 노드들의 결과 중 최솟값을 선택
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height),
        )
```

### 동작 원리

이 함수는 게임 트리(Game Tree)를 탐색하며 각 노드의 값을 결정합니다.

1. 입력값 검증: depth가 음수이거나 scores 리스트가 비어있는 비정상적인 경우를 확인하고 오류를 발생시킵니다.

2. 재귀 종료 조건 (Base Case):
    - if depth == height:: 현재 깊이(depth)가 게임 트리의 최대 높이(height)에 도달했다는 것은, 게임의 끝(leaf node)에 도달했음을 의미합니다.
    - return scores[node_index]: 이 경우, 더 이상 탐색하지 않고 해당 노드의 점수를 scores 리스트에서 찾아 반환합니다.

3. 재귀 호출 (Recursive Step):
    - if is_max: (Maximizer의 차례): 현재 차례가 점수를 최대화하려는 플레이어(Maximizer)일 경우, 다음 두 자식 노드를 재귀적으로 탐색한 후 그 결과 중 **더 큰 값(max)**을 자신의 값으로 선택합니다.
    - else: (Minimizer의 차례): 현재 차례가 점수를 최소화하려는 플레이어(Minimizer)일 경우, 다음 두 자식 노드를 재귀적으로 탐색한 후 그 결과 중 **더 작은 값(min)**을 자신의 값으로 선택합니다.
    - node_index * 2와 node_index * 2 + 1: 이 코드는 게임 트리가 완전 이진 트리(complete binary tree)라고 가정하고, 현재 노드의 자식 노드 인덱스를 계산하여 다음 탐색을 진행합니다.

### main 함수 및 실행 블록

```python
def main() -> None:
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    # 트리의 높이를 계산합니다. (scores 개수가 8개이므로 높이는 3)
    height = math.log(len(scores), 2)
    print("Optimal value : ", end="")
    # minimax 알고리즘 실행
    print(minimax(0, 0, True, scores, height))


if __name__ == "__main__":
    import doctest

    doctest.testmod() # 코드의 예제가 올바르게 동작하는지 테스트
    main()
```

- main 함수는 minimax 알고리즘을 실행하는 예시입니다.
- scores 리스트는 게임이 끝났을 때 얻을 수 있는 8가지 경우의 점수를 나타냅니다.
- height = math.log(len(scores), 2)는 점수 리스트의 길이를 바탕으로 게임 트리의 높이를 계산합니다. (log₂8 = 3)
- minimax(0, 0, True, scores, height)를 호출하여, 깊이 0, 인덱스 0에서 Maximizer로 시작했을 때 얻을 수 있는 최적의 점수를 계산하고 출력합니다.

## 코드 개선 제안

현재 코드는 미니맥스 알고리즘을 잘 구현하고 있지만, 가독성과 명확성을 위해 몇 가지 개선을 할 수 있습니다.

1. height 매개변수 제거: height는 scores 리스트의 길이로부터 항상 계산될 수 있으므로, minimax 함수에 계속 전달할 필요가 없습니다. 함수 내부에서 len(scores)를 직접 사용하도록 변경하면 함수 호출이 더 간결해집니다.
2. 변수명 개선: is_max는 is_maximizing_player와 같이 역할을 더 명확히 드러내는 이름으로 변경하면 가독성이 향상됩니다.
3. main 함수 분리: main 함수는 예제 실행을 위한 것이므로, if __name__ == "__main__" 블록 안으로 완전히 옮겨서 스크립트의 구조를 더 명확하게 할 수 있습니다.

아래는 위 제안들을 반영한 수정 코드입니다.

```
minimax.py
-20
+16
 Show full code block 


def minimax(
    depth: int, node_index: int, is_max: bool, scores: list[int], height: float
    depth: int, node_index: int, is_maximizing_player: bool, scores: list[int]
) -> int:
    """
    >>> import math
    >>> scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    >>> minimax(0, 0, True, scores)
    65
    >>> minimax(-1, 0, True, scores, height)
    >>> minimax(-1, 0, True, scores)
    Traceback (most recent call last):
        ...
    ValueError: Depth cannot be less than 0
    >>> minimax(0, 0, True, [], 2)
    >>> minimax(0, 0, True, [])
    Traceback (most recent call last):
        ...
    ValueError: Scores cannot be empty
    >>> scores = [3, 5, 2, 9, 12, 5, 23, 23]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    >>> minimax(0, 0, True, scores)
    12
    """

    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    height = math.log(len(scores), 2)
    if depth == height:
        return scores[node_index]

    if is_max:
    if is_maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
            minimax(depth + 1, node_index * 2, False, scores),
            minimax(depth + 1, node_index * 2 + 1, False, scores),
        )

    return min(
        minimax(depth + 1, node_index * 2, True, scores, height),
        minimax(depth + 1, node_index * 2 + 1, True, scores, height),
        minimax(depth + 1, node_index * 2, True, scores),
        minimax(depth + 1, node_index * 2 + 1, True, scores),
    )


def main() -> None:
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)
    print("Optimal value : ", end="")
    print(minimax(0, 0, True, scores, height))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

    # Example usage:
    scores_example = [90, 23, 6, 33, 21, 65, 123, 34423]
    optimal_value = minimax(0, 0, True, scores_example)
    print(f"Optimal value : {optimal_value}")
```