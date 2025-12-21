# FP-GraphMiner 알고리즘 (Frequent Pattern Graph Miner)

이 문서는 `frequent_pattern_graph_miner.py` 파일에 구현된 **FP-GraphMiner 알고리즘**에 대해 설명합니다.

## 개요

FP-GraphMiner는 네트워크 그래프 집합에서 빈번하게 나타나는 부분 그래프(Frequent Subgraph)를 효율적으로 찾기 위한 알고리즘입니다. 여러 그래프의 정보를 **FP-Graph**라는 압축된 형태로 표현하여, 중복 계산을 줄이고 마이닝 속도를 높입니다.

## 주요 데이터 구조

- **`edge_array`**: 입력 데이터로, 여러 개의 그래프를 리스트 형태로 저장합니다. 각 그래프는 간선(Edge)들의 리스트로 표현됩니다. (예: `'ab-e1'`은 노드 a와 b 사이의 e1 타입 간선을 의미)
- **Bitcode (비트코드)**: 특정 간선이 어떤 그래프들에 존재하는지를 나타내는 비트열입니다. 예를 들어, 5개의 그래프 중 1, 2, 4번째 그래프에 간선이 존재하면 `11010`과 같이 표현됩니다.

## 주요 함수

### 전처리 및 초기화
- **`preprocess(edge_array)`**: 입력된 간선 문자열(예: `'ab-e1'`)을 파싱하여 처리하기 쉬운 형태로 변환합니다.
- **`get_distinct_edge(edge_array)`**: 모든 그래프에서 중복을 제거한 유일한 간선 목록을 추출합니다.

### 빈도 분석 및 그룹화
- **`get_bitcode(edge_array, distinct_edge)`**: 각 간선에 대한 비트코드를 생성합니다.
- **`get_frequency_table(edge_array)`**: 각 간선의 등장 빈도(Support)와 비트코드를 계산하여 빈도 테이블을 생성하고, 빈도가 높은 순으로 정렬합니다.
- **`get_nodes(frequency_table)`**: 동일한 비트코드를 가진 간선들을 묶어 노드(Node)로 정의합니다.
- **`get_cluster(nodes)`**: 비트코드의 가중치(1의 개수, 즉 지지도)가 같은 노드들을 묶어 클러스터(Cluster)를 형성합니다.

### FP-Graph 구축
- **`construct_graph(cluster, nodes)`**: 클러스터와 노드 정보를 바탕으로 FP-Graph를 구축합니다.
- **`create_edge(nodes, graph, cluster, c1)`**: 상위 클러스터와 하위 클러스터 간의 포함 관계(비트코드의 부분집합 관계)를 확인하여 FP-Graph 상의 간선을 연결합니다.

### 마이닝 (Mining)
- **`find_freq_subgraph_given_support(s, cluster, graph)`**: 주어진 지지도(Support) `s` 퍼센트 이상인 빈번한 부분 그래프를 찾습니다.
- **`myDFS(graph, start, end, path)`**: FP-Graph 상에서 깊이 우선 탐색(DFS)을 수행하여 연결된 패턴들을 찾습니다.
- **`freq_subgraphs_edge_list(paths)`**: 탐색된 경로를 바탕으로 최종적인 빈번 부분 그래프의 간선 리스트를 반환합니다.

## 실행 흐름

1. **전처리**: `preprocess`를 통해 데이터를 정제합니다.
2. **테이블 생성**: `get_frequency_table`로 간선별 빈도와 비트코드를 구합니다.
3. **구조화**: `get_nodes`, `get_cluster`를 통해 데이터를 계층적으로 구조화합니다.
4. **그래프 구축**: `construct_graph`로 마이닝을 위한 FP-Graph를 만듭니다.
5. **마이닝**: `find_freq_subgraph_given_support` 함수에 원하는 지지도(예: 60%)를 입력하여 조건을 만족하는 부분 그래프를 추출합니다.
6. **결과 출력**: `print_all`을 통해 노드, 지지도, 클러스터, 그래프 구조, 발견된 부분 그래프 등을 출력합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 예제 데이터(`edge_array`)를 사용하여 알고리즘을 실행하는 과정을 확인할 수 있습니다.

```python
# 예시: 지지도 60% 이상인 부분 그래프 찾기
find_freq_subgraph_given_support(60, cluster, graph)
```
