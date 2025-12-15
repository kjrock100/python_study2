# `transposition_cipher_encrypt_decrypt_file.py` 코드 설명

이 문서는 `transposition_cipher_encrypt_decrypt_file.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 **전치 암호(Transposition Cipher)**를 사용하여 텍스트 파일을 암호화하고 복호화하는 기능을 제공하는 커맨드 라인 도구입니다.

> **참고**: 이 스크립트는 암호화 및 복호화 로직을 위해 `transposition_cipher.py` 파일에 의존합니다.

## 목차
1.  스크립트의 역할
2.  함수 설명
    -   `main()`
3.  실행 방법
4.  코드 개선 제안

## 스크립트의 역할

이 스크립트는 `transposition_cipher.py`에 구현된 암호화 및 복호화 함수를 사용하여, 실제 파일에 대한 암호화 작업을 수행합니다. 사용자는 키(key)와 모드(암호화/복호화)를 지정하여 한 파일을 다른 파일로 변환할 수 있습니다.

-   **암호화**: `Prehistoric Men.txt` 파일의 내용을 읽어 암호화한 후, `Output.txt` 파일에 저장합니다.
-   **복호화**: `Output.txt` 파일의 내용을 읽어 복호화한 후, 다시 `Output.txt` 파일에 덮어씁니다.

또한, 작업에 소요된 시간을 측정하여 보여줍니다.

## 함수 설명

### `main()`

스크립트의 전체 실행 로직을 담고 있는 메인 함수입니다.

-   **알고리즘**:
    1.  **파일 이름 및 사용자 입력**:
        -   입력 파일(`inputFile`)과 출력 파일(`outputFile`) 이름을 하드코딩으로 정의합니다.
        -   사용자로부터 암호화 키(정수)와 모드('e' 또는 'd')를 입력받습니다.
    2.  **파일 존재 여부 확인**:
        -   입력 파일이 존재하는지 확인하고, 없으면 프로그램을 종료합니다.
        -   출력 파일이 이미 존재하면, 덮어쓸지 여부를 사용자에게 확인받습니다.
    3.  **시간 측정 시작**: `time.time()`으로 작업 시작 시간을 기록합니다.
    4.  **모드에 따른 작업 수행**:
        -   **암호화 모드 (`e`)**: `inputFile`의 내용을 읽어 `transposition_cipher.encryptMessage()`를 호출하여 암호화합니다.
        -   **복호화 모드 (`d`)**: `outputFile`의 내용을 읽어 `transposition_cipher.decryptMessage()`를 호출하여 복호화합니다.
    5.  **결과 저장**: 암호화 또는 복호화된 결과를 `outputFile`에 씁니다.
    6.  **시간 측정 종료**: 총 소요 시간을 계산하고 화면에 출력합니다.

## 실행 방법

스크립트를 직접 실행하면 사용자 입력을 받아 파일 암호화/복호화를 수행합니다.

1.  **준비**: 스크립트와 같은 디렉터리에 `Prehistoric Men.txt`라는 이름의 텍스트 파일을 준비합니다.
2.  **실행**:
    ```bash
    python transposition_cipher_encrypt_decrypt_file.py
    ```
3.  **입력**: 터미널의 안내에 따라 키와 모드(e/d)를 입력합니다.

**실행 예시:**
```
Enter key: 8
Encrypt/Decrypt [e/d]: e
Overwrite Output.txt? [y/n]
> y
Done ( 0.01 seconds )
```

## 코드 개선 제안

1.  **복호화 소스 파일 버그 수정**: 현재 복호화 모드(`d`)는 암호화된 파일이 아닌, 출력 파일(`outputFile`)을 다시 읽어 복호화를 시도합니다. 이는 논리적 오류입니다. 암호화된 내용을 담고 있는 파일을 입력 소스로 사용해야 합니다. 예를 들어, 암호화 시 `Output.txt`에 썼다면, 복호화 시에는 이 파일을 읽어야 합니다. 현재 코드는 암호화 후 바로 복호화하면 `Output.txt`를 읽으므로 동작하지만, 별도로 복호화만 실행할 때는 의도와 다르게 동작할 수 있습니다.

    ```diff
    --- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/ciphers/transposition_cipher_encrypt_decrypt_file.py
    +++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/ciphers/transposition_cipher_encrypt_decrypt_file.py
    @@ -25,7 +25,7 @@
             content = f.read()
         translated = transCipher.encryptMessage(key, content)
     elif mode.lower().startswith("d"):
-        with open(outputFile) as f:
+        with open(inputFile) as f: # Or specify the encrypted file
             content = f.read()
         translated = transCipher.decryptMessage(key, content)
 
     with open(outputFile, "w") as outputObj:

    ```

2.  **하드코딩된 파일 이름 제거**: `inputFile`과 `outputFile` 이름이 코드에 고정되어 있어 유연성이 떨어집니다. `sys.argv`나 `argparse` 모듈을 사용하여 사용자가 커맨드 라인에서 직접 입력 및 출력 파일 경로를 지정하도록 만들면 스크립트의 활용도가 크게 향상됩니다.

3.  **사용자 입력 유효성 검사**: 사용자가 키로 숫자가 아닌 값을 입력하거나, 모드로 'e' 또는 'd'가 아닌 값을 입력했을 때 발생하는 오류를 `try-except` 블록으로 처리하면 프로그램의 안정성을 높일 수 있습니다.

4.  **모듈 임포트 스타일**: `from . import transposition_cipher as transCipher`는 상대 경로 임포트로, 패키지 내부에서 실행될 때 올바르게 동작합니다. 만약 단독 스크립트로 실행하려면 `import transposition_cipher as transCipher`와 같이 절대 경로 임포트를 사용해야 할 수 있습니다. 코드의 사용 환경을 명확히 하는 것이 좋습니다.