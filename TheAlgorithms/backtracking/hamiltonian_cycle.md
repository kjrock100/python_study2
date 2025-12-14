
## 코드 분석

이 파이썬 스크립트는 주어진 그래프에서 **해밀턴 순환(Hamiltonian Cycle)**을 찾는 알고리즘을 구현한 것입니다. 해밀턴 순환이란 그래프의 모든 정점(node)을 정확히 한 번씩만 방문하고 시작점으로 다시 돌아오는 경로를 의미합니다.

이 문제는 대표적인 NP-완전 문제로, 모든 경우의 수를 탐색해야 할 수 있습니다. 코드는 이 문제를 해결하기 위해 **백트래킹(Backtracking)**이라는 재귀적 탐색 기법을 사용합니다.

## hamiltonian_cycle 함수 (메인 진입점)

```python
def hamilton_cycle(graph: list[list[int]], start_index: int = 0) -> list[int]:
    # ... (docstring 생략) ...
    # 1. 경로 리스트 초기화
    path = [-1] * (len(graph) + 1)
    # 2. 시작점과 끝점 설정
    path[0] = path[-1] = start_index
    # 3. 재귀 함수 호출 및 결과 반환
    return path if util_hamilton_cycle(graph, path, 1) else []
```

- 역할: 해밀턴 순환 탐색을 시작하고, 최종 결과를 반환하는 메인 함수입니다.
- 동작:
    1. path 리스트를 -1로 초기화합니다. 크기를 그래프 크기 + 1로 만드는 이유는 [시작, v1, v2, ..., 끝(시작과 동일)] 과 같이 전체 순환 경로를 저장하기 위함입니다. -1은 아직 방문하지 않은 정점을 의미합니다.
    2. path 리스트의 맨 앞과 맨 뒤를 start_index로 설정하여 경로의 시작과 끝이 같아야 한다는 순환 조건을 명시합니다.
    3. 핵심 로직을 담은 util_hamilton_cycle 함수를 호출합니다.
        - path의 두 번째 원소(인덱스 1)부터 채우기 시작하므로 curr_ind를 1로 설정하여 넘겨줍니다.
        - util_hamilton_cycle이 True를 반환하면 해밀턴 순환을 찾은 것이므로 완성된 path를 반환하고, False를 반환하면 빈 리스트 []를 반환합니다.

## util_hamilton_cycle 함수 (핵심 로직)

```python
def util_hamilton_cycle(graph: list[list[int]], path: list[int], curr_ind: int) -> bool:
    # ... (docstring 생략) ...
    # 1. 재귀 종료 조건 (Base Case)
    if curr_ind == len(graph):
        # 마지막 정점에서 시작 정점으로 돌아갈 수 있는지 확인
        return graph[path[curr_ind - 1]][path[0]] == 1

    # 2. 재귀 호출 (Recursive Step)
    for next_vertex in range(0, len(graph)):
        if valid_connection(graph, next_vertex, curr_ind, path):
            # 선택 (Choose)
            path[curr_ind] = next_vertex
            # 탐색 (Explore)
            if util_hamilton_cycle(graph, path, curr_ind + 1):
                return True
            # 선택 취소 (Unchoose / Backtrack)
            path[curr_ind] = -1
    return False
```

- 역할: 백트래킹을 통해 가능한 모든 경로를 재귀적으로 탐색하여 해밀턴 순환을 찾는 핵심 함수입니다.
- 동작 원리:
    1. 재귀 종료 조건: curr_ind가 그래프의 정점 수와 같아지면, 모든 정점을 방문하여 경로(path)를 완성했다는 의미입니다.
        - 이때, 마지막으로 방문한 정점(path[curr_ind - 1])에서 시작 정점(path[0])으로 돌아가는 길이 있는지 확인합니다. 길이 있다면 완전한 순환이므로 True를 반환합니다.
    2. 재귀 호출: for 루프를 돌며 다음에 방문할 정점을 탐색합니다.
        - valid_connection 함수를 호출하여 현재 정점에서 next_vertex로 이동하는 것이 유효한지 검사합니다.
        - 선택 (Choose): 이동이 유효하면, path의 현재 위치에 next_vertex를 추가합니다.
        - 탐색 (Explore): util_hamilton_cycle을 다시 호출하여 다음 경로를 찾으러 더 깊이 들어갑니다. (curr_ind + 1)
            - 만약 이 재귀 호출이 True를 반환했다면, 해답을 찾은 것이므로 더 이상 탐색하지 않고 즉시 True를 반환합니다.
        - 선택 취소 (Unchoose / Backtrack): 깊이 들어간 탐색이 실패했다면(재귀 호출이 False를 반환했다면), 방금 추가했던 next_vertex를 다시 -1로 되돌립니다. 이것이 바로 백트래킹입니다. 현재 선택을 취소하고 for 루프의 다음 후보 정점으로 새로운 탐색을 시작합니다.
    3. for 루프가 모두 끝났는데도 True를 반환하지 못했다면, 현재 상태에서는 해답을 찾을 수 없다는 의미이므로 False를 반환합니다.

## valid_connection 함수 (유효성 검사)

```python
def valid_connection(
    graph: list[list[int]], next_ver: int, curr_ind: int, path: list[int]
) -> bool:
    # 1. 현재 정점과 다음 정점 사이에 간선이 있는지 확인
    if graph[path[curr_ind - 1]][next_ver] == 0:
        return False

    # 2. 다음 정점이 이미 경로에 포함되어 있는지 확인
    return not any(vertex == next_ver for vertex in path)
```

- 역할: 특정 정점을 경로에 추가할 수 있는지 두 가지 조건을 확인합니다.
- 동작:
    1. 연결 확인: 현재 경로의 마지막 정점(path[curr_ind - 1])에서 다음 후보 정점(next_ver)으로 가는 간선이 그래프에 존재하는지 확인합니다. graph는 인접 행렬이므로 graph[u][v] == 1이면 간선이 존재합니다.
    2. 방문 여부 확인: 다음 후보 정점(next_ver)이 path 리스트에 이미 포함되어 있는지 확인합니다. 해밀턴 순환은 각 정점을 한 번만 방문해야 하므로, 이미 방문한 정점은 다시 선택할 수 없습니다.
    3. 두 조건을 모두 만족해야만 True를 반환합니다.

이 세 함수가 유기적으로 작동하여, 백트래킹을 통해 가능한 모든 경로를 탐색하고 해밀턴 순환이 존재하면 그 경로를, 존재하지 않으면 빈 리스트를 반환하게 됩니다.
