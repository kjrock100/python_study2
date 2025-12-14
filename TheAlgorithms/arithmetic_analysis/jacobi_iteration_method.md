
jacobi_iteration_method.py 코드에 대해 자세히 설명해 드리겠습니다.

이 코드는 선형 연립방정식의 근사 해를 구하는 **야코비 반복법(Jacobi Iteration Method)**을 구현한 것입니다.

## 전체적인 흐름

야코비 반복법은 Ax = b 형태의 연립방정식에서 해 x를 반복적으로 계산하여 근사값을 찾아가는 알고리즘입니다. 특정 조건(주대각선이 지배적인 행렬)에서만 수렴이 보장됩니다.

1. jacobi_iteration_method 함수:

    - 계수 행렬(A), 상수 행렬(b), 초기 추정값(x₀), 반복 횟수를 입력받습니다.
    - 입력된 행렬들이 야코비 방법을 적용하기에 적합한 형태인지 검증합니다.
    - 계수 행렬이 강 대각 지배(strictly diagonally dominant) 조건을 만족하는지 strictly_diagonally_dominant 함수를 통해 확인합니다.
    - 주어진 반복 횟수만큼 야코비 반복법 공식을 적용하여 해를 계산합니다.
    - 최종적으로 계산된 해를 반환합니다.

2. strictly_diagonally_dominant 함수:

    - 입력된 행렬이 강 대각 지배 행렬인지 검사합니다.
    - 강 대각 지배 행렬은 야코비 방법의 수렴을 보장하는 중요한 조건입니다.
    - 조건을 만족하지 않으면 ValueError를 발생시킵니다.

## 함수별 상세 분석

### 1.jacobi_iteration_method 함수

이 함수는 야코비 반복법의 핵심 로직을 수행합니다.

```python
def jacobi_iteration_method(
    coefficient_matrix: NDArray[float64],
    constant_matrix: NDArray[float64],
    init_val: list[int],
    iterations: int,
) -> list[float]:
    # ... (docstring 생략) ...

    # 1. 입력값 검증
    rows1, cols1 = coefficient_matrix.shape
    rows2, cols2 = constant_matrix.shape

    if rows1 != cols1:
        raise ValueError(...)
    if cols2 != 1:
        raise ValueError(...)
    if rows1 != rows2:
        raise ValueError(...)
    if len(init_val) != rows1:
        raise ValueError(...)
    if iterations <= 0:
        raise ValueError("Iterations must be at least 1")

    # 2. 첨가 행렬 생성 및 대각 지배 확인
    table: NDArray[float64] = np.concatenate(
        (coefficient_matrix, constant_matrix), axis=1
    )
    rows, cols = table.shape
    strictly_diagonally_dominant(table)

    # 3. 야코비 반복 계산
    for i in range(iterations):
        new_val = []
        for row in range(rows):
            temp = 0
            for col in range(cols):
                if col == row:
                    denom = table[row][col]  # 대각 원소 a_ii
                elif col == cols - 1:
                    val = table[row][col]    # 상수 b_i
                else:
                    # a_ij * x_j (j != i) 부분
                    temp += (-1) * table[row][col] * init_val[col]
            # x_i = (b_i - sum(a_ij * x_j)) / a_ii
            temp = (temp + val) / denom
            new_val.append(temp)
        init_val = new_val # 다음 반복을 위해 해 업데이트

    return [float(i) for i in new_val]
```

#### 동작 방식

1. 입력값 검증:

    - 계수 행렬(coefficient_matrix)은 n x n 정사각 행렬이어야 합니다.
    - 상수 행렬(constant_matrix)은 n x 1 열벡터여야 합니다.
    - 초기 추정값(init_val)의 개수는 방정식의 개수(n)와 같아야 합니다.
    - 반복 횟수(iterations)는 1 이상이어야 합니다.
    - 조건에 맞지 않으면 명확한 오류 메시지와 함께 ValueError를 발생시킵니다.

2. 준비 단계:

    - np.concatenate를 사용하여 계수 행렬과 상수 행렬을 합쳐 [A|b] 형태의 첨가 행렬(table)을 만듭니다.
    - strictly_diagonally_dominant 함수를 호출하여 행렬 A가 야코비 방법의 수렴 조건을 만족하는지 확인합니다.

3. 야코비 반복 계산:

    - 이중 for 루프를 통해 야코비 공식을 구현합니다.
    - 바깥 루프는 주어진 iterations 횟수만큼 전체 계산을 반복합니다.
    - 안쪽 루프는 각 방정식(행)에 대해 새로운 해 x_i를 계산합니다.
    - 야코비 방법의 핵심 공식은 다음과 같습니다. x_i^(k+1) = (1 / a_ii) *(b_i - Σ(a_ij* x_j^k)) (여기서 j ≠ i, k는 반복 횟수)
    - 코드에서는 이 공식을 약간 다르게 계산하지만 결과는 동일합니다.
        - temp 변수에 - Σ(a_ij * x_j^k) 부분을 먼저 계산합니다.
        - 이후 (temp + b_i) / a_ii 를 통해 x_i의 새 값을 구합니다.
    - 한 번의 반복이 끝나면, 새로 계산된 해 new_val을 다음 반복에서 사용할 init_val로 업데이트합니다.
  
### 2. strictly_diagonally_dominant 함수
이 함수는 행렬이 강 대각 지배(strictly diagonally dominant) 행렬인지 확인합니다.

강 대각 지배 조건: 행렬의 각 행에서, 대각선 상에 있는 원소의 절댓값이 그 행의 다른 모든 원소들의 절댓값의 합보다 커야 합니다. |a_ii| > Σ|a_ij| (여기서 j ≠ i)

```python
def strictly_diagonally_dominant(table: NDArray[float64]) -> bool:
    # ... (docstring 생략) ...
    rows, cols = table.shape
    is_diagonally_dominant = True
    for i in range(0, rows):
        sum = 0
        for j in range(0, cols - 1):
            if i == j:
                continue
            else:
                sum += table[i][j] # 버그: 절댓값을 취해야 합니다.

        if table[i][i] <= sum: # 버그: 절댓값을 취해야 합니다.
            raise ValueError("Coefficient matrix is not strictly diagonally dominant")
    return is_diagonally_dominant
```

## 문제점 및 개선 제안

현재 strictly_diagonally_dominant 함수에는 심각한 버그가 있습니다. 강 대각 지배 조건은 절댓값을 기준으로 비교해야 하지만, 현재 코드는 절댓값을 사용하지 않고 있습니다. 이로 인해 음수 값이 포함된 경우 조건을 잘못 판단할 수 있습니다.

아래와 같이 수정하여 이 버그를 해결해야 합니다.

```
jacobi_iteration_method.py
-2
+2
            if i == j:
                continue
            else:
                sum += table[i][j]
                sum += abs(table[i][j])

        if table[i][i] <= sum:
        if abs(table[i][i]) <= sum:
            raise ValueError("Coefficient matrix is not strictly diagonally dominant")

    return is_diagonally_dominant
```

## 변경 사항 설명

1. sum += abs(table[i][j]): 행의 다른 원소들을 더할 때 abs()를 사용하여 절댓값의 합을 구하도록 수정했습니다.
2. if abs(table[i][i]) <= sum:: 대각 원소 또한 abs()를 사용하여 절댓값으로 비교하도록 수정했습니다.

이렇게 수정하면 야코비 방법의 수렴 조건을 정확하게 검사할 수 있습니다.

## if __name__ == "__main__" 블록

이 부분은 스크립트가 직접 실행될 때 doctest를 실행합니다. doctest는 함수의 독스트링(docstring)에 포함된 예제 코드(>>>로 시작하는 부분)를 자동으로 실행하고, 그 결과가 예상과 일치하는지 확인하여 코드의 정확성을 검증하는 유용한 도구입니다.
