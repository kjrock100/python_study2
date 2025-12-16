# `number_of_possible_binary_trees.py` 코드 설명

이 문서는 `number_of_possible_binary_trees.py` 스크립트에 구현된, 주어진 노드 개수로 만들 수 있는 이진 트리와 이진 탐색 트리의 개수를 계산하는 알고리즘에 대해 설명합니다.

## 1. 개요

이 스크립트는 주어진 노드 개수(n)에 대해 만들 수 있는 서로 다른 **이진 트리(Binary Tree)**와 **이진 탐색 트리(Binary Search Tree)**의 총개수를 계산합니다.

-   **이진 탐색 트리(BST)의 개수**: 카탈란 수(Catalan Number)를 이용하여 구합니다.
-   **이진 트리(BT)의 개수**: `(n번째 카탈란 수) * n!` 공식을 사용합니다.

## 2. 핵심 개념

### 카탈란 수 (Catalan Number)

카탈란 수는 조합론에서 자주 등장하는 수열로, 다양한 문제의 경우의 수를 세는 데 사용됩니다. 특히, **n개의 노드로 만들 수 있는 서로 다른 구조의 이진 탐색 트리의 개수**는 n번째 카탈란 수와 같습니다.

이 코드에서는 이항 계수(Binomial Coefficient)를 이용한 다음 공식을 사용하여 O(n) 시간 복잡도로 카탈란 수를 계산합니다.

> **C_n = (1 / (n + 1)) * C(2n, n)**

여기서 `C(2n, n)`은 "2n개 중에서 n개를 뽑는 조합"을 의미합니다.

### 이진 트리의 개수

n개의 노드로 만들 수 있는 이진 트리의 총개수는 이진 탐색 트리의 개수와 관련이 있습니다.

-   먼저, n개의 노드로 만들 수 있는 **트리의 구조**는 n번째 카탈란 수만큼 존재합니다.
-   각각의 고유한 트리 구조에 대해, n개의 서로 다른 값을 노드에 배치하는 경우의 수는 **n! (n 팩토리얼)**입니다.

따라서, 총 이진 트리의 개수는 다음 공식으로 계산됩니다.

> **(n번째 카탈란 수) * n!**

## 3. 함수 설명

### `binomial_coefficient(n: int, k: int) -> int`

-   **역할**: 이항 계수 "n choose k" (C(n, k))를 계산합니다.
-   **동작**: `C(n, k) = n! / (k! * (n-k)!)` 공식을 O(k) 시간에 효율적으로 계산합니다. `k > n-k`일 경우 `k = n-k`로 바꾸어 계산량을 줄이는 최적화가 포함되어 있습니다.

### `catalan_number(node_count: int) -> int`

-   **역할**: `node_count`에 해당하는 카탈란 수를 반환합니다. 이는 주어진 노드 개수로 만들 수 있는 이진 탐색 트리의 총개수와 같습니다.
-   **동작**: `binomial_coefficient` 함수를 호출하여 `C(2n, n) / (n + 1)`을 계산합니다.

### `factorial(n: int) -> int`

-   **역할**: 주어진 정수 `n`의 팩토리얼(n!)을 계산합니다.
-   **동작**: 1부터 n까지의 모든 정수를 곱하는 반복문을 사용합니다.

### `binary_tree_count(node_count: int) -> int`

-   **역할**: `node_count`개의 노드로 만들 수 있는 이진 트리의 총개수를 반환합니다.
-   **동작**: `catalan_number(n) * factorial(n)` 공식을 그대로 구현합니다.

## 4. 사용 예제

스크립트를 직접 실행하면 사용자로부터 노드의 개수를 입력받아 결과를 출력합니다.

**실행:**
```bash
python /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/number_of_possible_binary_trees.py
```

**입력:**
```
Enter the number of nodes: 5
```

**출력:**
```
Given 5 nodes, there are 5040 binary trees and 42 binary search trees.
```

## 5. 테스트

코드에는 `doctest`가 포함되어 있어 각 함수의 정확성을 검증할 수 있습니다.

```bash
python -m doctest /home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/binary_tree/number_of_possible_binary_trees.py
```