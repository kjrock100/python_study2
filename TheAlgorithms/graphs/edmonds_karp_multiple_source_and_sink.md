# 다중 소스 및 싱크 최대 유량 (Multiple Source and Sink Max Flow)

이 문서는 `edmonds_karp_multiple_source_and_sink.py` 파일에 구현된 **다중 소스 및 싱크를 지원하는 네트워크 유량 알고리즘**에 대해 설명합니다.

파일 이름에는 Edmonds-Karp가 포함되어 있지만, 실제 구현된 알고리즘은 **Push-Relabel 알고리즘**을 사용하고 있습니다.

## 개요

이 코드는 여러 개의 소스(Source)와 여러 개의 싱크(Sink)가 있는 그래프에서 최대 유량(Maximum Flow)을 계산하는 프레임워크를 제공합니다. 다중 소스/싱크 문제는 가상의 **슈퍼 소스(Super Source)**와 **슈퍼 싱크(Super Sink)**를 도입하여 단일 소스/싱크 문제로 변환하여 해결합니다.

## 주요 클래스

### `FlowNetwork`

- **목적**: 유량 네트워크를 초기화하고 관리합니다.
- **주요 메서드**:
  - `_normalizeGraph(sources, sinks)`:
    - 입력받은 소스가 여러 개이거나 싱크가 여러 개일 경우, 가상의 정점(슈퍼 소스, 슈퍼 싱크)을 생성합니다.
    - 슈퍼 소스에서 각 원래 소스로 무한대(또는 매우 큰 값) 용량의 간선을 연결합니다.
    - 각 원래 싱크에서 슈퍼 싱크로 무한대 용량의 간선을 연결합니다.
    - 이를 통해 표준적인 단일 소스-단일 싱크 알고리즘을 적용할 수 있게 합니다.
  - `findMaximumFlow()`: 설정된 알고리즘을 실행하여 최대 유량을 반환합니다.
  - `setMaximumFlowAlgorithm(Algorithm)`: 사용할 최대 유량 알고리즘 클래스를 설정합니다.

### `PushRelabelExecutor`

- **목적**: **Push-Relabel 알고리즘**을 사용하여 최대 유량을 계산합니다.
- **상속**: `MaximumFlowAlgorithmExecutor`를 상속받습니다.
- **알고리즘 동작**:
  - **초기화 (`_algorithm`)**:
    - 소스에서 나가는 간선에 대해 포화 유량(Preflow)을 흘려보냅니다.
    - 소스의 높이(Height)를 정점의 개수로 설정합니다.
  - **반복**:
    - 초과 유량(Excess)이 있는 정점을 선택하여 `processVertex`를 수행합니다.
    - **Push (밀기)**: 인접한 정점 중 높이가 낮은 정점으로 유량을 보냅니다.
    - **Relabel (재지정)**: 유량을 보낼 수 없는 경우, 현재 정점의 높이를 증가시킵니다.
    - 이 과정을 더 이상 초과 유량이 있는 정점이 없을 때까지 반복합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 실행 예시를 확인할 수 있습니다.

```python
entrances = [0]
exits = [3]
graph = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

# 네트워크 준비
flowNetwork = FlowNetwork(graph, entrances, exits)
# 알고리즘 설정 (Push-Relabel 사용)
flowNetwork.setMaximumFlowAlgorithm(PushRelabelExecutor)
# 계산
maximumFlow = flowNetwork.findMaximumFlow()

print(f"maximum flow is {maximumFlow}")
```

## 참고 사항

- 이 코드는 인접 행렬(Adjacency Matrix) 방식을 사용하여 그래프를 표현합니다.
- `FlowNetworkAlgorithmExecutor` 구조를 통해 다른 알고리즘(예: Edmonds-Karp, Dinic)도 쉽게 추가하여 확장할 수 있도록 설계되어 있습니다.
