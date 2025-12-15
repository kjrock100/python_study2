# `cnn_classification.py` 코드 설명

이 문서는 `cnn_classification.py` 파이썬 스크립트를 설명합니다. 이 스크립트는 `TensorFlow`와 `Keras` 라이브러리를 사용하여, 흉부 X-ray 이미지에서 결핵(Tuberculosis) 유무를 판별하는 **합성곱 신경망(Convolutional Neural Network, CNN)** 모델을 구축, 훈련, 그리고 평가하는 과정을 구현합니다.

## 목차
1.  CNN이란?
2.  스크립트의 전체 흐름
3.  코드 단계별 설명
    -   Part 1: CNN 모델 구축
    -   Part 2: 이미지 데이터 준비 및 모델 훈련
    -   Part 3: 새로운 이미지로 예측
4.  실행 방법
5.  코드 개선 제안

## CNN이란?

CNN은 이미지 인식 및 분류 작업에 특히 효과적인 딥러닝 모델입니다. 인간의 시각 처리 시스템을 모방하여, 이미지의 지역적인 특징(선, 모서리, 질감 등)을 추출하고 이를 조합하여 더 복잡한 패턴을 학습합니다.

**주요 구성 요소**:
-   **합성곱 계층 (Convolutional Layer)**: 필터(커널)를 사용하여 이미지의 특징 맵(feature map)을 생성합니다.
-   **풀링 계층 (Pooling Layer)**: 특징 맵의 크기를 줄여 계산량을 감소시키고, 주요 특징을 강조합니다. (예: Max Pooling)
-   **완전 연결 계층 (Fully Connected Layer)**: 추출된 특징들을 바탕으로 최종적인 분류를 수행합니다.

## 스크립트의 전체 흐름

1.  **모델 정의**: `Keras`의 `Sequential` API를 사용하여 CNN 모델의 구조(합성곱, 풀링, 완전 연결 계층)를 정의합니다.
2.  **데이터 준비**: 훈련용(training set)과 테스트용(test set) 이미지들을 디렉터리에서 불러와, 모델 훈련에 적합한 형태로 전처리하고 증강(augmentation)합니다.
3.  **모델 훈련**: 준비된 이미지 데이터로 CNN 모델을 훈련시키고, 훈련된 모델을 `cnn.h5` 파일로 저장합니다.
4.  **예측**: 훈련된 모델을 사용하여 새로운 단일 이미지에 대해 결핵 유무를 예측합니다.

## 코드 단계별 설명

### Part 1: CNN 모델 구축

`tensorflow.keras.models.Sequential`을 사용하여 모델의 각 계층을 순차적으로 쌓습니다.

1.  **`Conv2D` (합성곱 계층)**: 32개의 3x3 필터를 사용하여 입력 이미지(64x64x3)에서 특징을 추출합니다. 활성화 함수로는 `relu`를 사용합니다.
2.  **`MaxPooling2D` (최대 풀링 계층)**: 2x2 크기의 풀링 윈도우를 사용하여 특징 맵의 크기를 절반으로 줄입니다.
3.  **두 번째 합성곱 + 풀링 계층**: 더 깊은 수준의 특징을 학습하기 위해 합성곱과 풀링 계층을 한 번 더 추가합니다.
4.  **`Flatten` (평탄화 계층)**: 다차원의 특징 맵을 1차원 벡터로 변환하여 완전 연결 계층에 입력할 수 있도록 준비합니다.
5.  **`Dense` (완전 연결 계층)**:
    -   첫 번째 `Dense` 계층은 128개의 뉴런을 가지며, 추출된 특징들을 조합합니다.
    -   두 번째 `Dense` 계층은 1개의 뉴런과 `sigmoid` 활성화 함수를 사용하여, 최종적으로 이미지가 특정 클래스(여기서는 '결핵')에 속할 확률(0~1)을 출력합니다.
6.  **`compile`**: 모델의 학습 방식을 설정합니다.
    -   `optimizer='adam'`: 경사 하강법 최적화 알고리즘.
    -   `loss='binary_crossentropy'`: 이진 분류 문제에 사용되는 손실 함수.
    -   `metrics=['accuracy']`: 훈련 및 테스트 과정에서 모델의 성능을 평가할 지표로 '정확도'를 사용합니다.

### Part 2: 이미지 데이터 준비 및 모델 훈련

1.  **`ImageDataGenerator`**:
    -   `train_datagen`: 훈련용 이미지에 대해 데이터 증강(augmentation)을 수행합니다. 이미지의 크기를 조절하고, 기울이거나, 확대/축소하고, 좌우 반전을 적용하여 모델이 더 다양한 데이터에 대해 학습하도록 돕습니다. (과적합 방지)
    -   `test_datagen`: 테스트용 이미지에 대해서는 픽셀 값만 0~1 사이로 정규화합니다.
2.  **`flow_from_directory`**: 지정된 디렉터리에서 이미지를 불러옵니다.
    -   디렉터리 구조(`dataset/training_set/Normal`, `dataset/training_set/Tuberculosis`)를 기반으로 자동으로 라벨을 생성합니다.
    -   이미지를 `target_size=(64, 64)`로 리사이즈하고, `batch_size=32` 단위로 묶어 모델에 공급합니다.
3.  **`fit_generator`**: 생성된 데이터 제너레이터를 사용하여 모델을 훈련시킵니다.
    -   `epochs=30`: 전체 훈련 데이터셋을 30번 반복하여 학습합니다.

### Part 3: 새로운 이미지로 예측

1.  예측할 단일 이미지를 불러와 모델의 입력 크기(64x64)에 맞게 리사이즈합니다.
2.  이미지를 `numpy` 배열로 변환하고, 모델이 처리할 수 있는 4차원 텐서(배치 크기 포함)로 차원을 확장합니다.
3.  `classifier.predict()`를 호출하여 예측을 수행합니다.
4.  결과 확률값(0 또는 1에 가까운 값)에 따라 "Normal" 또는 "Abnormality detected"로 최종 예측 결과를 결정합니다.

## 실행 방법

1.  **필요한 라이브러리 설치**:
    ```bash
    pip install tensorflow numpy
    ```
2.  **데이터셋 준비**:
    -   링크에서 데이터셋을 다운로드합니다.
    -   스크립트와 같은 디렉터리에 `dataset` 폴더를 만들고, 그 안에 `training_set`과 `test_set` 폴더를 생성합니다.
    -   각 세트 폴더 안에 `Normal`과 `Tuberculosis` 하위 폴더를 만들고, 해당하는 이미지를 분류하여 넣습니다.
    -   예측을 위한 `dataset/single_prediction/image.png` 파일을 준비합니다.
3.  **스크립트 실행**:
    ```bash
    python cnn_classification.py
    ```

## 코드 개선 제안

1.  **`fit_generator` 대신 `fit` 사용**: `fit_generator`는 TensorFlow 2.1.0부터 구식(deprecated)이 되었으며, `fit` 메서드가 제너레이터를 직접 지원합니다. `fit`을 사용하도록 코드를 업데이트하는 것이 좋습니다.

    ```diff
    --- a/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/computer_vision/cnn_classification.py
    +++ b/home/kjrock/work2/study/kjrock100/python_study2/TheAlgorithms/computer_vision/cnn_classification.py
    @@ -58,9 +58,7 @@
         "dataset/test_set", target_size=(64, 64), batch_size=32, class_mode="binary"
     )
 
-    classifier.fit_generator(
-        training_set, steps_per_epoch=5, epochs=30, validation_data=test_set
-    )
+    classifier.fit(training_set, epochs=30, validation_data=test_set)
 
     classifier.save("cnn.h5")
 

    ```
    > **참고**: `steps_per_epoch` 인자는 `fit` 메서드에서 자동으로 계산되므로 일반적으로 생략할 수 있습니다.

2.  **예측 결과 처리 로직**: `if result[0][0] == 0:`과 `if result[0][0] == 1:` 부분은 예측값이 정확히 0 또는 1이 아닐 경우 아무런 예측도 하지 않는 버그가 있습니다. `sigmoid` 함수의 출력은 0과 1 사이의 확률값이므로, 임계값(예: 0.5)을 기준으로 판단해야 합니다.

    ```python
    # 개선 제안 예시
    if result[0][0] < 0.5:
        prediction = "Normal"
    else:
        prediction = "Abnormality detected"
    print(f"Prediction: {prediction} (Probability: {result[0][0]:.4f})")
    ```

3.  **하드코딩된 경로 및 파라미터**: 데이터셋 경로, 이미지 크기, 배치 크기, 에포크 수 등이 코드에 하드코딩되어 있습니다. `argparse` 모듈을 사용하여 이들을 커맨드 라인 인자로 받도록 수정하면, 다른 데이터셋이나 설정으로 실험하기가 훨씬 용이해집니다.

4.  **모델 로드 주석**: `load_model` 관련 코드가 주석 처리되어 있습니다. 이 부분을 활성화하고, 훈련된 모델이 이미 존재할 경우 훈련을 건너뛰고 바로 예측을 수행하는 로직을 추가하면 시간을 절약할 수 있습니다.