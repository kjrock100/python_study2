# 코드는 bisection 함수를 사용하여 주어진 구간에서 함수의 근을 찾는 방법을 구현한 것입니다

bisection(function, a, b) 함수:

목표: 함수 function이 구간 [a, b]에서 0이 되는 지점(근)을 찾습니다.

원리: 중간값 정리(Bolzano's theorem)에 기반합니다. 구간의 양 끝점에서 함수의 부호가 다르면 그 사이에 반드시 근이 존재한다는 아이디어를 활용합니다.

매개변수:

function: 근을 찾고자 하는 함수입니다. float를 입력받아 float를 반환하는 Callable 타입이어야 합니다.
a: 구간의 시작점입니다.
b: 구간의 끝점입니다.
동작 방식:

초기 확인:
function(a) 또는 function(b)가 0이면, a 또는 b가 근이므로 바로 반환합니다.
function(a) *function(b) > 0이면, a와 b 모두 양수이거나 음수이므로 이 구간에선 근을 찾을 수 없다고 판단하고 ValueError를 발생시킵니다.
반복적인 구간 분할:
구간 [a, b]의 중간점 mid를 계산합니다.
abs(start - mid) > 10**-7 조건을 만족하는 동안 (즉, 원하는 정밀도에 도달할 때까지) 다음을 반복합니다.
function(mid)가 0이면, mid가 근이므로 반환합니다.
function(mid)* function(start) < 0이면, start와 mid 사이에 근이 있으므로 end를 mid로 업데이트합니다.
그렇지 않으면, mid와 end 사이에 근이 있으므로 start를 mid로 업데이트합니다.
mid를 다시 계산합니다.
결과 반환:
반복문이 종료되면, mid는 근의 근사값이 됩니다. mid를 반환합니다.
오류 처리:

주어진 구간에서 근을 찾을 수 없는 경우 ValueError를 발생시킵니다.
정밀도:

while abs(start - mid) > 10**-7:에서 10의 -7승 오차 내에서 근을 찾습니다.
Docstring 예제:

함수의 사용법을 보여주는 doctest 예제가 포함되어 있습니다.
f(x) 함수:

예제 함수로, x**3 - 2 * x - 5를 계산합니다.
if __name__ == "__main__": 블록:

스크립트가 직접 실행될 때만 실행되는 코드입니다.
bisection(f, 1, 1000)을 호출하여 f(x) 함수의 근을 구간 [1, 1000]에서 찾고 결과를 출력합니다.
doctest.testmod()를 호출하여 doctest 예제를 실행하고, 코드의 정확성을 검증합니다.

# Callable 에 대해서 설명해줘

Callable은 Python의 typing 모듈에서 제공하는 타입 힌트 중 하나입니다. 함수 또는 메서드의 타입을 표현하는 데 사용됩니다. Callable[[Arg1, Arg2, ...], ReturnType] 형태로 사용하며, Arg1, Arg2 등은 인수의 타입, ReturnType은 반환 타입을 나타냅니다.

예를 들어, 다음과 같은 함수가 있다고 가정해 보겠습니다.

```python
def add(x: int, y: int) -> int:
    return x + y
```

이 함수의 타입을 Callable을 사용하여 표현하면 다음과 같습니다.

```python
from typing import Callable

add_type: Callable[[int, int], int]
```

Callable은 함수의 인자와 반환 값에 대한 타입 정보를 명시적으로 제공함으로써, 코드의 가독성을 높이고 타입 검사기의 오류 검출 능력을 향상시키는 데 기여합니다.

# doctest

doctest는 파이썬 모듈의 docstring 내에 포함된 예제 코드를 실행하고, 그 결과를 실제 실행 결과와 비교하여 코드가 예상대로 작동하는지 자동으로 검증하는 테스트 프레임워크입니다.

doctest의 작동 방식:

docstring에서 예제 추출: doctest는 모듈, 클래스, 함수 등의 docstring을 검색하여 >>>로 시작하는 파이썬 코드를 예제로 인식합니다.
코드 실행 및 결과 캡처: 추출된 예제 코드를 실행하고, 그 결과를 캡처합니다.
결과 비교: 캡처된 실행 결과를 docstring에 명시된 예상 결과와 비교합니다.
성공/실패 판정: 실행 결과와 예상 결과가 일치하면 테스트가 성공한 것으로, 그렇지 않으면 실패한 것으로 판정합니다.
예제:

```python
 Show full code block 
def add(a, b):
    """
    두 수를 더하는 함수입니다.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

위 예제에서 doctest는 add(2, 3)과 add(-1, 1)을 실행하고, 각각의 결과가 docstring에 명시된 5와 0과 일치하는지 확인합니다.

doctest 사용의 장점:

간편한 테스트 작성: 별도의 테스트 파일 없이, docstring 내에 예제를 포함하는 방식으로 테스트를 작성할 수 있습니다.
코드와 문서의 통합: 테스트 코드가 문서의 일부로 포함되므로, 코드 변경 시 문서도 함께 업데이트되는 효과가 있습니다.
코드의 가독성 향상: 예제를 통해 코드의 사용법을 명확하게 보여주므로, 코드의 가독성을 높일 수 있습니다.
