# `stock_span_problem.py` 코드 설명

이 문서는 `stock_span_problem.py` 스크립트에 구현된, 주식 스팬 문제(Stock Span Problem)를 해결하는 알고리즘에 대해 설명합니다.

## 1. 주식 스팬 문제(Stock Span Problem)란?

주식 스팬 문제는 n일간의 주식 가격 정보가 주어졌을 때, 각 날짜에 대한 스팬(span)을 계산하는 문제입니다.

특정 날짜 `i`의 스팬 `S[i]`는, 오늘을 포함하여 **연속적으로** 오늘 주가보다 작거나 같았던 날들의 최대 일수를 의미합니다.

**예시:**
-   주가: `[100, 80, 60, 70, 60, 75, 85]`
-   스팬: `[1, 1, 1, 2, 1, 4, 6]`
    -   85의 스팬은 6입니다. (85, 75, 60, 70, 60, 80은 모두 85보다 작거나 같고, 100에서 끊깁니다.)
    -   75의 스팬은 4입니다. (75, 60, 70, 60은 모두 75보다 작거나 같고, 80에서 끊깁니다.)

## 2. 핵심 알고리즘: 스택(Stack) 활용

이 문제를 효율적으로 해결하기 위해 **스택(Stack)** 자료 구조를 사용합니다. 이 알고리즘은 배열을 한 번만 순회하므로 O(N)의 시간 복잡도를 가집니다.

**동작 원리:**
1.  빈 스택을 생성합니다. 이 스택에는 주가의 **인덱스**가 저장됩니다.
2.  배열을 왼쪽에서 오른쪽으로 (0일부터 n-1일까지) 순회합니다.
3.  **현재 주가(`price[i]`)**가 **스택의 맨 위(top)에 있는 인덱스에 해당하는 주가**보다 크거나 같으면, 스택에서 계속 `pop`합니다.
    -   이는 현재 주가보다 낮은 이전의 봉우리들은 더 이상 스팬 계산에 영향을 주지 못하므로 제거하는 과정입니다.
4.  `pop` 과정이 끝난 후:
    -   스택이 비어있다면, 현재 주가가 지금까지 중 가장 높다는 의미입니다. 따라서 스팬은 `i + 1`이 됩니다.
    -   스택이 비어있지 않다면, 스택의 맨 위에는 현재 주가보다 큰 첫 번째 봉우리의 인덱스가 남아있게 됩니다. 따라서 스팬은 `현재 인덱스 - 스택 top 인덱스`가 됩니다.
5.  현재 인덱스 `i`를 스택에 `push`합니다.

## 3. 코드 분석 및 버그 수정

### `calculateSpan(price, S)` 함수

-   **역할**: 주어진 주가 리스트 `price`를 기반으로 각 날짜의 스팬을 계산하여 리스트 `S`에 저장합니다.
-   **시간 복잡도**: O(N) - 각 원소는 스택에 최대 한 번씩 `push`되고 `pop`됩니다.
-   **공간 복잡도**: O(N) - 최악의 경우 스택에 모든 인덱스가 저장될 수 있습니다.

### 코드의 버그

원본 코드에는 스택의 맨 위 원소를 참조하는 부분에 버그가 있습니다. 파이썬 리스트를 스택으로 사용할 때, 맨 위 원소는 `st[-1]`로 접근해야 하지만, 코드에서는 `st[0]`으로 잘못 접근하고 있습니다.

-   **원본 코드 (버그 있음)**:
    ```python
    while len(st) > 0 and price[st[0]] <= price[i]:
        st.pop()
    S[i] = i + 1 if len(st) <= 0 else (i - st[0])
    ```
-   **수정된 코드 (올바른 로직)**:
    ```python
    while st and price[st[-1]] <= price[i]:
        st.pop()
    S[i] = i + 1 if not st else (i - st[-1])
    ```

아래는 버그가 수정된 전체 코드입니다.

```diff
--- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/stacks/stock_span_problem.py
+++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/data_structures/stacks/stock_span_problem.py
@@ -9,24 +9,24 @@
 
 def calculateSpan(price, S):
 
-    n = len(price)
     # Create a stack and push index of fist element to it
-    st = []
-    st.append(0)
+    stack = []
+    # Span value of first element is always 1
+    S[0] = 1
+    stack.append(0)
 
-    # Span value of first element is always 1
-    S[0] = 1
-
     # Calculate span values for rest of the elements
-    for i in range(1, n):
+    for i in range(1, len(price)):
 
         # Pop elements from stack while stack is not
         # empty and top of stack is smaller than price[i]
-        while len(st) > 0 and price[st[0]] <= price[i]:
-            st.pop()
+        while stack and price[stack[-1]] <= price[i]:
+            stack.pop()
 
         # If stack becomes empty, then price[i] is greater
         # than all elements on left of it, i.e. price[0],
         # price[1], ..price[i-1]. Else the price[i]  is
         # greater than elements after top of stack
-        S[i] = i + 1 if len(st) <= 0 else (i - st[0])
+        S[i] = i + 1 if not stack else (i - stack[-1])
 
         # Push this element to stack
-        st.append(i)
+        stack.append(i)
 
 
 # A utility function to print elements of array

```

## 4. 사용 예제

```python
# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price) + 1)]

# Fill the span values in array S[]
calculateSpan(price, S)

# Print the calculated span values
printArray(S, len(price))
# 수정된 코드로 실행 시 올바른 출력: 1 1 2 4 5 1
```

## 5. 테스트

이 스크립트에는 별도의 `doctest`나 `unittest`가 포함되어 있지 않지만, `if __name__ == "__main__":` 블록의 예제 코드를 통해 기본적인 동작을 확인할 수 있습니다.