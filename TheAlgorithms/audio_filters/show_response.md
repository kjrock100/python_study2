
## show_response.py 코드 분석

이 파이썬 스크립트는 주어진 오디오 필터의 특성을 시각화하는 두 가지 주요 함수, show_frequency_response와 show_phase_response를 제공합니다. matplotlib과 numpy 라이브러리를 사용하여 필터가 각 주파수 대역에 어떻게 반응하는지를 그래프로 보여줍니다.

이 코드는 특정 필터 구현에 종속되지 않고, process 메서드를 가진 어떤 필터 객체든 분석할 수 있도록 Protocol을 사용하여 유연하게 설계되었습니다.

## 주요 구성 요소 상세 설명

1. FilterType(Protocol)

```python
 Show full code block 
class FilterType(Protocol):
    def process(self, sample: float) -> float:
        """
        Calculate y[n]

        >>> issubclass(FilterType, Protocol)
        True
        """
        return 0.0
```

- 역할: 필터 객체가 가져야 할 구조(인터페이스)를 정의합니다.
- 설명: typing.Protocol을 사용하여, 시각화 함수에 전달될 filter 객체는 반드시 process(self, sample: float) -> float라는 메서드를 가지고 있어야 함을 명시합니다. 이는 IIRFilter 클래스처럼 특정 클래스에 의존하지 않고, 오리 타이핑(duck typing)을 정적으로 지원하여 코드의 유연성과 재사용성을 높여줍니다.

1. get_bounds 함수

```python
def get_bounds(
    fft_results: np.ndarray, samplerate: int
) -> tuple[int | float, int | float]:
    # ...
```

- 역할: 주파수 응답 그래프의 Y축(Gain) 범위를 적절하게 설정하기 위한 최소/최대값을 계산합니다.
- 동작:
     1. FFT 결과(fft_results)에서 유효한 주파수 범위(DC 성분인 0Hz와 Nyquist 주파수 이상은 제외)의 최소/최대 dB 값을 찾습니다.
     2. 찾은 최소값은 -20dB보다 작지 않게, 최대값은 20dB보다 크지 않게 조정합니다.
     3. 이를 통해 그래프가 너무 과도하게 확대/축소되지 않고 항상 일정한 범위 내에서 보기 좋게 표시되도록 합니다.

1. show_frequency_response 함수

```python
def show_frequency_response(filter: FilterType, samplerate: int) -> None:
    # ...
```

- 역할: 필터의 주파수 응답(Frequency Response), 즉 각 주파수에 대한 게인(Gain) 변화를 그래프로 보여줍니다.
- 동작 원리 (임펄스 응답 측정):
     1. 임펄스 신호 생성: [1, 0, 0, ...] 형태의 임펄스(impulse) 신호를 만듭니다. 임펄스 신호는 이론적으로 모든 주파수 성분을 동일한 크기로 포함하고 있습니다.
     2. 임펄스 응답 계산: 이 임펄스 신호를 필터의 process 메서드에 통과시켜 나오는 결과, 즉 **임펄스 응답(Impulse Response)**을 얻습니다.
     3. FFT 수행: 임펄스 응답을 푸리에 변환(FFT)하면 필터의 주파수 응답을 얻을 수 있습니다. 더 부드러운 그래프를 위해 제로 패딩(zero-padding)을 추가한 후 np.fft.fft를 수행합니다.
     4. dB 변환: FFT 결과(복소수)의 크기를 계산하고, 이를 데시벨(dB) 단위로 변환(20 * np.log10(...))합니다.
     5. 그래프 출력:
         - X축은 주파수(Hz)를 로그 스케일로 표시하여 사람이 소리를 인지하는 방식과 유사하게 보여줍니다.
         - Y축은 get_bounds 함수로 구한 범위 내에서 게인(dB)을 표시합니다.
         - plt.plot()과 plt.show()를 통해 계산된 주파수 응답 그래프를 화면에 출력합니다.

1. show_phase_response 함수

```python
def show_phase_response(filter: FilterType, samplerate: int) -> None:
    # ...
```

- 역할: 필터의 위상 응답(Phase Response), 즉 각 주파수 성분이 필터를 통과할 때 위상(phase)이 얼마나 변하는지를 그래프로 보여줍니다.
- 동작 원리:
     1. 주파수 응답을 계산하는 과정과 동일하게 임펄스 응답을 구하고 FFT를 수행합니다.
     2. 위상 계산: FFT 결과(복소수)에서 np.angle 함수를 사용하여 각 주파수 성분의 위상(라디안 단위)을 추출합니다.
     3. 위상 펼치기(Unwrap): 위상 값은 보통 -π에서 +π 사이에서 갑자기 점프하는 현상이 발생합니다. np.unwrap 함수는 이 점프를 제거하여 위상이 연속적으로 부드럽게 변하는 것처럼 보여줍니다.
     4. 그래프 출력:
         - X축은 주파수(Hz)를 로그 스케일로 표시합니다.
         - Y축은 위상 변화(라디안)를 표시합니다.
         - 계산된 위상 응답 그래프를 화면에 출력합니다.

## 코드의 장점

- 모듈성 및 재사용성: Protocol을 사용하여 필터의 구체적인 구현과 시각화 코드를 분리했습니다. process 메서드만 있다면 어떤 필터 객체든 이 함수들로 분석할 수 있습니다.
- 표준 시각화: 오디오 분석에서 표준적으로 사용되는 로그 스케일의 주파수 축과 dB 단위의 게인을 사용하여 전문적인 분석 결과를 제공합니다.
- 가독성: 각 함수의 역할이 명확하고, numpy와 matplotlib을 효율적으로 사용하여 코드가 간결합니다.

이 코드는 디지털 오디오 필터를 설계하고 그 특성을 확인할 때 매우 유용한 도구입니다.
