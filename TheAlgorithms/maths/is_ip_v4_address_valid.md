# Is IP v4 Address Valid (IPv4 주소 유효성 검사)

이 문서는 `is_ip_v4_address_valid.py` 파일에 구현된 **IPv4 주소 유효성 검사** 알고리즘에 대한 설명입니다.

## 개요

주어진 문자열이 유효한 IPv4 주소 형식을 따르는지 판별합니다. IPv4 주소는 `A.B.C.D` 형태의 4개의 옥텟(octet)으로 구성됩니다.

> **참고**: 일반적인 IPv4 주소의 범위는 0~255이지만, 이 코드의 구현에서는 **0~254** 범위의 숫자만을 유효한 것으로 간주하고 있습니다. (예: 255가 포함된 주소는 유효하지 않다고 판단함)

## 함수 설명

### `is_ip_v4_address_valid(ip_v4_address: str) -> bool`

입력된 문자열이 유효한 IPv4 주소인지 확인하여 불리언(Boolean) 값을 반환합니다.

#### 매개변수 (Parameters)

- `ip_v4_address` (`str`): 검사할 IP 주소 문자열입니다.

#### 반환값 (Returns)

- `True`: 유효한 IPv4 주소인 경우.
- `False`: 유효하지 않은 경우.

#### 알고리즘 (Algorithm)

1. 입력 문자열을 점(`.`)을 기준으로 분리합니다 (`split(".")`).
2. 분리된 각 부분 중 숫자로만 구성된(`isdigit()`) 항목들을 정수(`int`)로 변환하여 리스트 `octets`를 생성합니다.
   - 이 과정에서 음수 부호가 있거나 숫자가 아닌 문자가 포함된 부분은 제외됩니다.
3. 다음 두 가지 조건을 모두 만족하는지 확인합니다:
   - `octets` 리스트의 길이가 정확히 4개여야 합니다.
   - 리스트의 모든 숫자가 0 이상 254 이하의 범위에 있어야 합니다.

## 실행 예시

파일을 직접 실행하면(`if __name__ == "__main__":`), 사용자로부터 IP 주소를 입력받아 유효성 여부를 출력합니다.

```python
if __name__ == "__main__":
    ip = input().strip()
    valid_or_invalid = "valid" if is_ip_v4_address_valid(ip) else "invalid"
    print(f"{ip} is a {valid_or_invalid} IP v4 address.")
```

**입력/출력 예시:**

- 입력: `192.168.0.23` -> 출력: `192.168.0.23 is a valid IP v4 address.`
- 입력: `192.255.15.8` -> 출력: `192.255.15.8 is a invalid IP v4 address.` (255 포함으로 인해)
