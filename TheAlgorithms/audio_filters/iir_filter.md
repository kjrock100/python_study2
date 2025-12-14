이 파이썬 코드는 오디오 신호 처리에 사용되는 N차 IIR(Infinite Impulse Response, 무한 임펄스 응답) 필터를 구현한 IIRFilter 클래스를 정의합니다.

## IIR 필터란?

IIR 필터는 디지털 필터의 한 종류로, 현재의 출력을 계산할 때 이전의 입력값들뿐만 아니라 이전의 출력값들도 다시 참조(피드백)하는 구조를 가집니다. 이 "피드백" 특성 때문에 임펄스(짧은 신호) 하나가 입력되어도 그 영향이 무한히 지속될 수 있어 "무한 임펄스 응답"이라는 이름이 붙었습니다.

이 필터의 동작은 아래와 같은 전달 함수(Transfer Function)와 차분 방정식(Difference Equation)으로 정의됩니다.

- 전달 함수 H(z): H(z) = (b₀ + b₁z⁻¹ + ... + bₖz⁻№) / (a₀ + a₁z⁻¹ + ... + aₖz⁻№)
- 차분 방정식 y[n]: y[n] = (1/a₀) * ( (b₀x[n] + b₁x[n-1] + ...) - (a₁y[n-1] + a₂y[n-2] + ...) )

여기서:

- x[n]은 현재 입력 샘플, x[n-k]는 k번째 이전 입력 샘플입니다.
- y[n]은 현재 출력 샘플, y[n-k]는 k번째 이전 출력 샘플입니다.
- a와 b는 필터의 특성(예: 저역 통과, 고역 통과)을 결정하는 **계수(coefficients)**입니다.

IIRFilter 클래스는 바로 이 차분 방정식을 코드로 구현한 것입니다.

## IIRFilter 클래스 분석

1. __init__(self, order: int) - 초기화 메서드
```python
 Show full code block 
    def __init__(self, order: int) -> None:
        self.order = order

        # a_{0} ... a_{k}
        self.a_coeffs = [1.0] + [0.0] * order
        # b_{0} ... b_{k}
        self.b_coeffs = [1.0] + [0.0] * order

        # x[n-1] ... x[n-k]
        self.input_history = [0.0] * self.order
        # y[n-1] ... y[n-k]
        self.output_history = [0.0] * self.order
```

- 필터 객체를 처음 생성할 때 호출됩니다.
- order: 필터의 차수(order)를 지정합니다. 차수가 높을수록 더 급격한 필터 특성을 만들 수 있지만 계산량이 늘어납니다.
- a_coeffs, b_coeffs: 필터 계수를 저장하는 리스트입니다. 처음에는 아무런 효과가 없는 기본값(a₀=1.0, b₀=1.0, 나머지는 0)으로 초기화됩니다.
- input_history, output_history: 차분 방정식을 계산하는 데 필요한 과거의 입/출력 값들을 저장하기 위한 "메모리" 또는 "버퍼"입니다. order 개수만큼 0으로 채워진 리스트로 생성됩니다.

2. set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) - 계수 설정 메서드

```python
    def set_coefficients(self, a_coeffs: list[float], b_coeffs: list[float]) -> None:
        # ... (입력값 검증) ...
        self.a_coeffs = a_coeffs
        self.b_coeffs = b_coeffs
```

- 필터의 실제 동작을 정의하는 a와 b 계수를 설정합니다.
- butterworth_filter.py와 같은 파일에서 계산된 계수들이 이 메서드를 통해 필터 객체에 적용됩니다.
- 입력받은 계수 리스트의 길이가 필터의 차수(order + 1)와 맞는지 검증하여 잘못된 설정으로 인한 오류를 방지합니다.
- Docstring의 예제처럼 scipy.signal.butter와 같은 과학 계산 라이브러리에서 생성된 계수와 쉽게 호환되도록 설계되었습니다.

3. process(self, sample: float) -> float - 필터 처리 메서드

```python
    def process(self, sample: float) -> float:
        result = 0.0

        # 1. 과거 입/출력 값들을 이용한 계산
        for i in range(1, self.order + 1):
            result += (
                self.b_coeffs[i] * self.input_history[i - 1]
                - self.a_coeffs[i] * self.output_history[i - 1]
            )

        # 2. 현재 입력값을 반영하고 a_0로 정규화
        result = (result + self.b_coeffs[0] * sample) / self.a_coeffs[0]

        # 3. 히스토리 업데이트 (과거 값들을 한 칸씩 뒤로 밀기)
        self.input_history[1:] = self.input_history[:-1]
        self.output_history[1:] = self.output_history[:-1]

        # 4. 현재 입/출력 값을 히스토리의 맨 앞에 저장
        self.input_history[0] = sample
        self.output_history[0] = result

        return result
```

- 이 클래스의 핵심으로, 실제 필터링 연산을 수행합니다.
- 오디오 스트림에서 한 번에 하나의 샘플(sample)을 입력받아 필터링된 샘플(result)을 반환합니다.
- 동작 순서:
    - for 루프를 통해 차분 방정식의 sum(bᵢ * x[n-i]) 와 sum(aᵢ * y[n-i]) 부분을 계산합니다. (i는 1부터 시작)
    - 현재 입력 샘플 x[n]에 대한 항(b₀ * x[n])을 더하고, 전체 결과를 a₀으로 나누어 최종 출력 y[n]을 구합니다.
    - 다음 샘플 계산을 위해 히스토리 버퍼를 업데이트합니다. 모든 값을 한 칸씩 뒤로 밀어 가장 오래된 값을 버립니다.
    - 방금 사용한 현재 입력(sample)과 방금 계산된 현재 출력(result)을 히스토리 버퍼의 맨 앞에 저장하여 "가장 최신" 과거 값으로 만듭니다.

## 요약

IRFilter 클래스는 특정 필터의 종류(저역 통과, 고역 통과 등)에 얽매이지 않는 범용적인 IIR 필터 구현체입니다. set_coefficients를 통해 어떤 종류의 필터 계수든 설정할 수 있으며, process 메서드를 호출하여 오디오 샘플을 실시간으로 처리할 수 있는 유연하고 재사용 가능한 구조를 가지고 있습니다.