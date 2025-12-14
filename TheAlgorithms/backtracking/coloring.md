
이 코드는 그래프 이론의 고전적인 문제 중 하나인 **"그래프 색칠 문제(Graph Coloring Problem)"**를 해결하는 알고리즘을 구현한 것입니다. 이 문제는 주어진 그래프에서 인접한 정점(vertex)들이 서로 다른 색을 갖도록 하면서, 최대 m개의 색을 사용해 모든 정점을 칠할 수 있는 방법을 찾는 것입니다. 이 코드는 **백트래킹(Backtracking)**이라는 재귀적 탐색 기법을 사용합니다.

코드는 크게 세 개의 함수로 구성되어 있습니다. 각 함수의 역할과 동작 방식을 순서대로 살펴보겠습니다.

## color 함수 (메인 진입점)

```python
def color(graph: list[list[int]], max_colors: int) -> list[int]:
    """
    Wrapper function to call subroutine called util_color
    which will either return True or False.
    If True is returned colored_vertices list is filled with correct colorings
    ...
    """
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices

    return []
```

- 역할: 그래프 색칠을 시작하고 최종 결과를 반환하는 메인 함수입니다.
- 동작:
    1. colored_vertices = [-1] * len(graph): 각 정점의 색을 저장할 리스트를 만듭니다. 처음에는 아무 색도 칠해져 있지 않다는 의미로 모든 값을 -1로 초기화합니다.
    2. util_color(graph, max_colors, colored_vertices, 0): 실제 색칠을 수행하는 재귀 함수 util_color를 호출합니다.
        - graph: 색칠할 그래프 (인접 행렬)
        - max_colors: 사용할 수 있는 최대 색의 수
        - colored_vertices: 색칠 결과를 저장할 리스트
        - 0: 0번 정점부터 색칠을 시작하겠다는 의미의 시작 인덱스
    3. util_color 함수가 True를 반환하면, colored_vertices 리스트에 유효한 색칠 방법이 저장된 것이므로 이 리스트를 반환합니다.
    4. 만약 False를 반환하면, 주어진 max_colors로는 그래프를 칠할 수 없다는 뜻이므로 빈 리스트 []를 반환합니다.

## util_color 함수 (핵심 백트래킹 로직)

```python
def util_color(
    graph: list[list[int]], max_colors: int, colored_vertices: list[int], index: int
) -> bool:
    # ... (주석 생략)

    # Base Case (재귀 종료 조건)
    if index == len(graph):
        return True

    # Recursive Step (재귀 호출)
    for i in range(max_colors):
        if valid_coloring(graph[index], colored_vertices, i):
            # Color current vertex (선택)
            colored_vertices[index] = i
            # Validate coloring (탐색)
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            # Backtrack (선택 취소)
            colored_vertices[index] = -1
    return False
```

- 역할: 백트래킹을 통해 가능한 모든 색칠 조합을 재귀적으로 탐색하는 핵심 함수입니다.
- 동작 원리 (Choose, Explore, Unchoose 패턴):
    1. 재귀 종료 조건 (Base Case): if index == len(graph):
        - index는 현재 색칠하려는 정점의 번호입니다. 이 값이 그래프의 전체 정점 수와 같아지면, 모든 정점을 성공적으로 칠했다는 의미이므로 True를 반환합니다.
    2. 재귀 단계 (Recursive Step): for i in range(max_colors):
        - 현재 index번 정점에 칠할 수 있는 모든 색(0부터 max_colors-1까지)을 하나씩 시도해봅니다.
        - 유효성 검사: if valid_coloring(...)
            - i번 색을 index번 정점에 칠해도 되는지(valid_coloring 함수로) 확인합니다. 즉, 인접한 정점 중에 같은 색이 있는지 검사합니다.
        - 선택 (Choose): colored_vertices[index] = i
            - 유효하다면, index번 정점에 i번 색을 칠합니다.
        - 탐색 (Explore): if util_color(..., index + 1):
            - 현재 상태를 그대로 두고, 다음 정점(index + 1)을 칠하기 위해 재귀 호출을 합니다. 만약 이 재귀 호출이 결국 True를 반환한다면, 해답을 찾은 것이므로 현재 함수도 True를 반환하며 재귀를 종료합니다.
        - 선택 취소 (Unchoose / Backtrack): colored_vertices[index] = -1
            - 위 탐색(Explore)이 실패했다면(즉, i번 색을 칠했더니 다음 단계에서 해답을 찾을 수 없었다면), index번 정점의 색을 다시 -1(칠하지 않은 상태)로 되돌려 놓습니다. 이것이 바로 백트래킹입니다. 이 과정을 통해 for 루프의 다음 색을 시도할 수 있습니다.
    3. for 루프가 모두 끝날 때까지 True를 반환하지 못했다면, 현재 index번 정점에는 칠할 수 있는 색이 없다는 뜻이므로 False를 반환합니다.

## valid_coloring 함수 (유효성 검사)

```python
def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color: int
) -> bool:
    # ... (주석 생략)
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )
```

- 역할: 특정 정점에 특정 색을 칠하는 것이 유효한지(규칙에 맞는지) 검사합니다.
- 동작:
  - neighbours: 현재 정점의 인접 정보를 담은 리스트입니다. (인접 행렬의 한 행)
  - colored_vertices: 현재까지 칠해진 색상 정보 리스트입니다.
  - color: 현재 칠하려고 시도하는 색입니다.
  - any(...) 구문은 neighbours 리스트를 순회하며 다음 조건을 만족하는 경우가 하나라도 있는지 확인합니다.
    - neighbour == 1: i번 정점이 현재 정점과 인접해 있고,
    - colored_vertices[i] == color: 그 i번 정점의 색이 지금 칠하려는 color와 같은 경우
  - not any(...): 만약 위 조건을 만족하는 인접 정점이 하나도 없다면 any()는 False를 반환하고, not을 통해 최종적으로 True(유효함)가 반환됩니다. 반대로, 같은 색을 가진 인접 정점이 하나라도 있다면 any()가 True가 되고, 최종적으로 False(유효하지 않음)가 반환됩니다.

## 코드 개선 제안

현재 코드는 잘 작동하지만, 가독성과 명확성을 위해 valid_coloring 함수를 좀 더 풀어쓸 수 있습니다.

```python
def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color_to_check: int
) -> bool:
    """
    주어진 색상이 인접 정점의 색상과 충돌하지 않는지 확인합니다.
    """
    for vertex_index, is_neighbour in enumerate(neighbours):
        # is_neighbour가 1이면 vertex_index는 이웃입니다.
        if is_neighbour == 1:
            # 이웃의 색상이 확인하려는 색상과 같은지 봅니다.
            if colored_vertices[vertex_index] == color_to_check:
                # 같은 색을 가진 이웃이 있으므로 유효하지 않습니다.
                return False
    # 모든 이웃을 확인했지만 충돌이 없었으므로 유효합니다.
    return True
```

위와 같이 for 루프를 사용하여 명시적으로 작성하면 any() 구문에 익숙하지 않은 사람도 로직을 더 쉽게 이해할 수 있습니다. 기능적으로는 원래 코드와 동일합니다.
