# Krishnamurthy Number (크리슈나무르티 수) 알고리즘

이 문서는 `krishnamurthy_number.py` 파일에 구현된 **크리슈나무르티 수(Krishnamurthy Number)** 판별 알고리즘에 대한 설명입니다.

## 개요

**크리슈나무르티 수**는 각 자릿수의 팩토리얼 합이 원래의 수와 같은 수를 말합니다. **피터슨 수(Peterson Number)** 또는 **강한 수(Strong Number)**라고도 불립니다.

예를 들어, 145는 다음과 같이 계산되므로 크리슈나무르티 수입니다.
$$ 1! + 4! + 5! = 1 + 24 + 120 = 145 $$

## 함수 설명

### `factorial(digit: int) -> int`

주어진 한 자리 숫자(digit)의 팩토리얼을 재귀적으로 계산하여 반환합니다.

#### 매개변수 (Parameters)

- `digit` (`int`): 팩토리얼을 계산할 정수 (주로 0-9 사이의 값).

#### 알고리즘 (Algorithm)

1. `digit`이 0 또는 1이면 1을 반환합니다.
2. 그렇지 않으면 `digit * factorial(digit - 1)`을 반환합니다.

### `krishnamurthy(number: int) -> bool`

주어진 숫자가 크리슈나무르티 수인지 판별하여 불리언 값을 반환합니다.

#### 매개변수 (Parameters)

- `number` (`int`): 판별할 양의 정수.

#### 알고리즘 (Algorithm)

1. 각 자릿수의 팩토리얼 합을 저장할 변수 `factSum`을 0으로 초기화합니다.
2. 입력된 `number`의 복사본 `duplicate`를 생성합니다.
3. `duplicate`가 0보다 큰 동안 다음을 반복합니다:
   - `divmod(duplicate, 10)`을 사용하여 마지막 자릿수(`digit`)와 나머지 부분(`duplicate`)을 분리합니다.
   - `digit`의 팩토리얼을 계산하여 `factSum`에 더합니다.
4. 계산된 `factSum`이 원래의 `number`와 같은지 비교하여 결과를 반환합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 숫자를 입력받아 크리슈나무르티 수 여부를 출력합니다.

```python
if __name__ == "__main__":
    print("Program to check whether a number is a Krisnamurthy Number or not.")
    number = int(input("Enter number: ").strip())
    print(f"{number} is {'' if krishnamurthy(number) else 'not '}a Krishnamurthy Number.")
```
