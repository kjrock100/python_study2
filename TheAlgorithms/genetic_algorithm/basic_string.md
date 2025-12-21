# 기본 문자열 유전 알고리즘 (Basic String Genetic Algorithm)

이 문서는 `basic_string.py` 파일에 구현된 **기본 문자열 유전 알고리즘**에 대해 설명합니다. 이 알고리즘은 무작위 문자열 집단에서 시작하여, 유전 알고리즘의 4단계(평가, 선택, 교차, 돌연변이)를 거쳐 목표 문자열(Target String)로 진화시키는 과정을 보여줍니다.

## 개요

유전 알고리즘(Genetic Algorithm)은 생물학적 진화 과정을 모방한 최적화 알고리즘입니다. 이 코드는 특정 문자열을 목표로 설정하고, 무작위로 생성된 문자열들이 세대를 거듭하며 목표 문자열과 얼마나 비슷해지는지 시뮬레이션합니다.

## 주요 상수 (Hyperparameters)

- `N_POPULATION`: 각 세대의 개체군 크기 (기본값: 200).
- `N_SELECTED`: 다음 세대를 위해 선택되는 상위 개체의 수 (기본값: 50).
- `MUTATION_PROBABILITY`: 유전자가 돌연변이를 일으킬 확률 (기본값: 0.4).

## 주요 함수: `basic`

### `basic(target: str, genes: list[str], debug: bool = True) -> tuple[int, int, str]`

- **목적**: 유전 알고리즘을 실행하여 `target` 문자열을 찾습니다.
- **매개변수**:
  - `target`: 목표 문자열.
  - `genes`: 사용할 수 있는 문자들의 리스트 (유전자 풀).
  - `debug`: 진행 상황 출력 여부.
- **반환값**: `(세대 수, 총 개체 수, 찾은 문자열)` 튜플.

### 알고리즘 동작 과정

1. **유효성 검사**: `target` 문자열의 모든 문자가 `genes` 리스트에 포함되어 있는지 확인합니다.
2. **초기화**: `N_POPULATION`만큼의 무작위 문자열을 생성하여 초기 개체군(`population`)을 형성합니다.
3. **진화 루프 (While True)**:
   - **평가 (Evaluation)**: 각 개체의 적합도(Fitness)를 계산합니다. 적합도는 목표 문자열과 일치하는 문자의 개수입니다.
   - **종료 조건**: 목표 문자열과 완벽하게 일치하는 개체가 있으면 결과를 반환합니다.
   - **정렬**: 적합도가 높은 순서대로 개체들을 정렬합니다.
   - **세대 교체**: 기존 개체군 중 일부를 유지하고 나머지는 제거합니다.
   - **선택 및 번식**: 상위 `N_SELECTED`개의 개체를 부모로 선택하여 자손을 생성합니다.
     - **교차 (Crossover)**: 두 부모 문자열을 섞어 자식을 만듭니다.
     - **돌연변이 (Mutation)**: 일정 확률로 자식의 문자를 변경합니다.

## 내부 헬퍼 함수

- `evaluate(item)`: 문자열이 목표 문자열과 얼마나 유사한지 점수를 매깁니다.
- `select(parent_1)`: 선택된 부모(`parent_1`)와 또 다른 상위권 부모를 교차시켜 자손을 생성합니다.
- `crossover(parent_1, parent_2)`: 두 부모 문자열을 임의의 지점에서 잘라 이어 붙입니다.
- `mutate(child)`: 자식 문자열의 특정 문자를 무작위로 변경합니다.

## 사용법

`if __name__ == "__main__":` 블록에서 실행 예시를 확인할 수 있습니다.

```python
target_str = "This is a genetic algorithm..."
genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ...")
basic(target_str, genes_list)
```
