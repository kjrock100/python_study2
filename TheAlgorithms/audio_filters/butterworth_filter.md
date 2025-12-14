
## butterworth_filter.py 코드 분석

이 파이썬 스크립트는 버터워스(Butterworth) 디자인에 기반한 2차 IIR(Infinite Impulse Response) 필터를 생성하는 함수들을 제공합니다. 이 코드는 디지털 오디오 이퀄라이저(EQ) 설계에 널리 사용되는 "Audio EQ Cookbook"의 공식을 기반으로 작성되었습니다.

생성된 각 필터는 audio_filters.iir_filter.py에 정의된 IIRFilter 클래스의 인스턴스로, 특정 주파수 특성을 갖도록 a와 b 계수가 설정된 상태로 반환됩니다.

## 주요 개념

- IIR 필터 (Infinite Impulse Response Filter): 출력을 계산할 때 이전의 입력값뿐만 아니라 이전의 출력값도 다시 참조(피드백)하는 디지털 필터입니다. a (피드백) 계수와 b (피드포워드) 계수에 의해 특성이 결정됩니다.
- Audio EQ Cookbook: 디지털 오디오 처리를 위한 다양한 필터의 계수를 계산하는 표준화된 공식을 제공하는 문서입니다. 이 스크립트의 모든 계산은 이 문서를 따릅니다.
- 공통 매개변수:
  - frequency: 필터의 기준 주파수(컷오프 또는 중심 주파수) (Hz).
  - samplerate: 오디오 샘플링 레이트 (Hz).
  - q_factor: 필터의 Q 팩터. 공진(resonance)이나 대역폭(bandwidth)을 조절하며, 기본값은 버터워스 필터의 특성을 나타내는 1/sqrt(2) 입니다.
  - gain_db: 피크 및 쉘프 필터에서 사용되는 데시벨(dB) 단위의 게인 값.

## 공통 계산 로직

대부분의 필터 생성 함수는 시작 부분에서 다음과 같은 중간 변수들을 계산합니다. 이는 "Audio EQ Cookbook"의 공식을 구현한 것입니다.

```python
w0 = tau * frequency / samplerate  # tau는 2 * pi
_sin = sin(w0)
_cos = cos(w0)
alpha = _sin / (2 * q_factor)
```

- w0: 정규화된 각주파수(normalized angular frequency)입니다.
- _sin,_cos: w0의 사인 및 코사인 값으로, 계수 계산에 반복적으로 사용됩니다.
- alpha: Q 팩터와 관련된 중간 변수로, 필터의 뾰족한 정도에 영향을 줍니다.

## 함수별 상세 설명

각 make_* 함수는 특정 종류의 2차 필터를 생성합니다.

1. make_lowpass(frequency, samplerate, q_factor)

지정된 frequency 이하의 주파수만 통과시키는 저역 통과 필터를 생성합니다.

```python
def make_lowpass(...):
    # ... (공통 계산) ...
    b0 = (1 - _cos) / 2
    b1 = 1 - _cos
    a0 = 1 + alpha
    a1 = -2 * _cos
    a2 = 1 - alpha

    filt = IIRFilter(2)
    # a0로 정규화된 계수를 설정합니다.
    filt.set_coefficients([a0, a1, a2], [b0, b1, b0])
    return filt
```

2. make_highpass(frequency, samplerate, q_factor)

지정된 frequency 이상의 주파수만 통과시키는 고역 통과 필터를 생성합니다.

```python
def make_highpass(...):
    # ... (공통 계산) ...
    b0 = (1 + _cos) / 2
    b1 = -1 - _cos
    # ... (이하 lowpass와 유사) ...
```

3. make_bandpass(frequency, samplerate, q_factor)

지정된 frequency 주변의 특정 대역폭만 통과시키는 대역 통과 필터를 생성합니다.

```python
def make_bandpass(...):
    # ... (공통 계산) ...
    b0 = _sin / 2
    b1 = 0
    b2 = -b0
    # ... (이하 lowpass와 유사) ...
```

4. make_allpass(frequency, samplerate, q_factor)

모든 주파수를 동일한 크기로 통과시키지만, 특정 주파수 대역의 위상(phase)을 변화시키는 전역 통과 필터를 생성합니다.

```python
def make_allpass(...):
    # ... (공통 계산) ...
    b0 = 1 - alpha
    b1 = -2 * _cos
    b2 = 1 + alpha
    
    # a와 b 계수가 서로 대칭적인 구조를 가집니다.
    filt = IIRFilter(2)
    filt.set_coefficients([b2, b1, b0], [b0, b1, b2])
    return filt
```

5. make_peak(frequency, samplerate, gain_db, q_factor)

지정된 frequency 주변의 주파수 대역을 gain_db만큼 증폭하거나 감쇠시키는 피크 필터를 생성합니다. (파라메트릭 EQ의 기본 요소)

```python
def make_peak(...):
    # ... (공통 계산) ...
    big_a = 10 ** (gain_db / 40) # dB를 선형적인 값으로 변환

    b0 = 1 + alpha * big_a
    b1 = -2 * _cos
    b2 = 1 - alpha * big_a
    a0 = 1 + alpha / big_a
    a1 = -2 * _cos
    a2 = 1 - alpha / big_a
    # ...
```

6. make_lowshelf(frequency, samplerate, gain_db, q_factor)

지정된 frequency 이하의 모든 주파수 대역을 gain_db만큼 증폭하거나 감쇠시키는 로우 쉘프 필터를 생성합니다. (오디오 믹서의 Bass 조절 기능)

```python
def make_lowshelf(...):
    # ... (공통 계산 및 big_a 계산) ...
    # Cookbook에 명시된 복잡한 중간 변수들
    pmc = (big_a + 1) - (big_a - 1) * _cos
    ppmc = (big_a + 1) + (big_a - 1) * _cos
    mpc = (big_a - 1) - (big_a + 1) * _cos
    pmpc = (big_a - 1) + (big_a + 1) * _cos
    aa2 = 2 * sqrt(big_a) * alpha

    # 위 변수들을 조합하여 최종 a, b 계수 계산
    b0 = big_a * (pmc + aa2)
    # ...
```

7. make_highshelf(frequency, samplerate, gain_db, q_factor)

지정된 frequency 이상의 모든 주파수 대역을 gain_db만큼 증폭하거나 감쇠시키는 하이 쉘프 필터를 생성합니다. (오디오 믹서의 Treble 조절 기능)

```python
def make_highshelf(...):
    # ... (lowshelf와 유사한 중간 변수 계산) ...
    # lowshelf와 다른 공식으로 최종 a, b 계수 계산
    b0 = big_a * (ppmc + aa2)
    # ...
```

## 코드의 장점

- 모듈성: 각 필터 타입이 별도의 함수로 명확하게 분리되어 있어 사용하기 쉽습니다.
- 재사용성: IIRFilter 클래스를 활용하여 필터의 상태(계수, 히스토리)를 객체로 관리하므로 재사용이 용이합니다.
- 표준 구현: "Audio EQ Cookbook"이라는 검증된 표준을 따르므로 신뢰할 수 있는 결과를 제공합니다.
- 자가 테스트: doctest를 통해 각 함수의 기본적인 동작을 검증하고 사용 예시를 보여줍니다.
