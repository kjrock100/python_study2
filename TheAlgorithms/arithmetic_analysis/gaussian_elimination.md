# gaussian_elimination.py 코드에 대해 자세히 설명해 드리겠습니다

이 코드는 선형 연립방정식의 해를 구하는 **가우스 소거법(Gaussian Elimination)**을 Python과 numpy 라이브러리를 사용하여 구현한 것입니다.

코드는 크게 두 개의 함수, gaussian_elimination과 retroactive_resolution으로 구성되어 있습니다.

## 전체적인 흐름

gaussian_elimination 함수는 계수 행렬(coefficients)과 상수 벡터(vector)를 입력받아 첨가 행렬(augmented matrix)을 만듭니다.
이 첨가 행렬을 전방 소거법(Forward Elimination)을 통해 상삼각행렬(Upper Triangular Matrix) 형태로 변환합니다.
변환된 상삼각행렬과 상수 벡터를 retroactive_resolution 함수에 넘겨줍니다.
retroactive_resolution 함수는 후방 대입법(Back Substitution)을 사용하여 최종 해를 계산하고 반환합니다.

## gaussian_elimination 함수 분석

이 함수는 가우스 소거법의 핵심인 전방 소거(Forward Elimination) 과정을 수행합니다.

```python
def gaussian_elimination(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    This function performs Gaussian elimination method

    Examples:
        1x1 - 4x2 - 2x3 = -2        1x1 + 2x2 = 5
        5x1 + 2x2 - 2x3 = -3        5x1 + 2x2 = 5
        1x1 - 1x2 + 0x3 = 4
    >>> gaussian_elimination([[1, -4, -2], [5, 2, -2], [1, -1, 0]], [[-2], [-3], [4]])
    array([[ 2.3 ],
           [-1.7 ],
           [ 5.55]])
    # ... (doctest 예제 생략)
    """
    # 1. 계수 행렬이 정사각 행렬인지 확인
    rows, columns = np.shape(coefficients)
    if rows != columns:
        # 정사각 행렬이 아니면 빈 배열을 반환합니다.
        # 오류를 발생시키는 것이 더 명확할 수 있습니다.
        return np.array((), dtype=float)

    # 2. 계수 행렬과 상수 벡터를 합쳐 첨가 행렬 생성
    augmented_mat: NDArray[float64] = np.concatenate((coefficients, vector), axis=1)
    augmented_mat = augmented_mat.astype("float64")

    # 3. 행렬을 상삼각행렬로 변환 (전방 소거)
    for row in range(rows - 1):
        pivot = augmented_mat[row, row] # 기준이 되는 대각 원소 (피벗)
        for col in range(row + 1, columns):
            # 피벗 아래의 원소들을 0으로 만들기 위한 비율 계산
            factor = augmented_mat[col, row] / pivot
            # 해당 행 전체에 연산 적용
            augmented_mat[col, :] -= factor * augmented_mat[row, :]

    # 4. 상삼각행렬을 이용해 후방 대입법으로 해 구하기
    x = retroactive_resolution(
        augmented_mat[:, 0:columns], augmented_mat[:, columns : columns + 1]
    )

    return x
```

## 동작 방식

1. 입력값 검증: 선형 연립방정식을 풀기 위해 계수 행렬(coefficients)이 n x n 형태의 정사각 행렬이어야 합니다. np.shape으로 행과 열의 크기를 구해 같은지 확인합니다.
2. 첨가 행렬 생성: np.concatenate를 사용하여 계수 행렬과 상수 벡터(vector)를 합쳐 하나의 행렬로 만듭니다. 예를 들어, Ax = b에서 [A|b] 형태의 행렬을 만듭니다.

3. 전방 소거 (Forward Elimination):

- 바깥쪽 for 루프는 기준 행(pivot row)을 선택합니다.
- pivot은 현재 기준 행의 대각선에 위치한 요소입니다.
- 안쪽 for 루프는 기준 행 아래의 모든 행을 순회합니다.
- factor는 아래 행의 첫 번째 요소를 pivot으로 나눈 값입니다. 이 factor를 기준 행에 곱한 뒤 아래 행에서 빼주면, 아래 행의 첫 번째 요소가 0이 됩니다.
- 이 과정을 모든 행에 대해 반복하면, 행렬의 주대각선 아래 모든 요소가 0이 되는 상삼각행렬이 만들어집니다.

4. 후방 대입 호출: 만들어진 상삼각행렬과 변환된 상수 벡터를 retroactive_resolution 함수에 전달하여 최종 해를 구합니다.

## retroactive_resolution 함수 분석

이 함수는 상삼각행렬 형태의 연립방정식을 **후방 대입법(Back Substitution)**으로 풉니다.

```python
def retroactive_resolution(
    coefficients: NDArray[float64], vector: NDArray[float64]
) -> NDArray[float64]:
    """
    This function performs a retroactive linear system resolution
        for triangular matrix
    # ... (doctest 예제 생략)
    """

    rows, columns = np.shape(coefficients)

    # 1. 해를 저장할 벡터를 0으로 초기화
    x: NDArray[float64] = np.zeros((rows, 1), dtype=float)
    
    # 2. 마지막 행부터 첫 번째 행까지 역순으로 반복
    for row in reversed(range(rows)):
        sum = 0
        # 3. 이미 계산된 변수들의 값을 이용해 합계를 구함
        for col in range(row + 1, columns):
            sum += coefficients[row, col] * x[col]

        # 4. 현재 행의 변수 값을 계산
        x[row, 0] = (vector[row] - sum) / coefficients[row, row]

    return x
```

## 동작 방식

상삼각행렬은 마지막 방정식에 변수가 하나만 존재하므로 해를 바로 구할 수 있습니다.

예시: 0x₁ + 0x₂ + 5x₃ = 15 => x₃ = 15 / 5 = 3

이렇게 구한 x₃ 값을 그 바로 윗줄 방정식에 대입하면 x₂를 구할 수 있고, 이 과정을 반복하면 모든 변수의 해를 찾을 수 있습니다.

1. 해 벡터 초기화: x라는 이름의 결과 벡터를 0으로 채웁니다.
2. 역순 반복: reversed(range(rows))를 사용하여 마지막 행부터 첫 행까지 거꾸로 순회합니다.
3. 합계 계산: 현재 행(row)에서, 이미 값이 구해진 변수들(x[col])과 그 계수(coefficients[row, col])의 곱을 모두 더합니다. 4An. 변수 값 계산: (상수 - 합계) / 대각선 계수 공식을 통해 현재 행에 해당하는 변수 x[row]의 값을 계산합니다.
4. 결과 반환: 모든 변수의 값이 계산된 x 벡터를 반환합니다.

## 코드 개선 제안

gaussian_elimination 함수에서 정사각 행렬이 아닐 경우, 빈 배열을 반환하는 대신 ValueError를 발생시키는 것이 더 명확하고 파이썬스러운 방식입니다.

```
gaussian_elimination.py
-1
+3
    # coefficients must to be a square matrix so we need to check first
    rows, columns = np.shape(coefficients)
    if rows != columns:
        return np.array((), dtype=float)
        raise ValueError(
            f"Coefficient matrix must be square. Got {rows}x{columns} matrix."
        )

    # augmented matrix
    augmented_mat: NDArray[float64] = np.concatenate((coefficients, vector), axis=1)
```

Use code with care. Learn more
이렇게 수정하면 함수 사용자가 잘못된 입력을 주었을 때 즉시 문제를 인지할 수 있습니다.
