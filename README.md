# 손글씨 숫자 인식 (MNIST CNN)

MNIST 데이터셋으로 학습한 CNN 모델을 이용해 손으로 쓴 숫자(0~9)를 인식하는 프로젝트입니다.
데스크톱(tkinter) 버전과 웹(Flask) 버전, 두 가지로 실행할 수 있습니다.

## 구성

```
.
├── train_model.py           # MNIST로 CNN 모델 학습 → mnist_cnn_model.keras 저장
├── draw_and_predict.py      # 데스크톱 GUI (tkinter) — 마우스로 그리고 예측
├── mnist_cnn_model.keras    # 학습된 모델
├── web_version/
│   ├── app.py                # Flask 서버 — /predict API
│   ├── templates/index.html  # 브라우저 캔버스 드로잉 UI
│   ├── mnist_cnn_model.keras  # 학습된 모델 (복사본)
│   └── CLAUDE.md
└── tasks/                   # 작업 계획/기록 (todo.md, progress.md)
```

## 설치

```bash
pip install tensorflow numpy pillow flask
```

## 모델 학습

```bash
python train_model.py
```

MNIST 데이터를 다운로드해 CNN을 학습하고, 학습이 끝나면 `mnist_cnn_model.keras` 파일로 저장합니다.
(테스트 정확도 약 99%)

## 실행 — 데스크톱 버전

```bash
python draw_and_predict.py
```

창이 열리면 마우스로 숫자를 그리고 **Predict** 버튼을 누르면 예측 결과가 표시됩니다.
**Clear**로 캔버스를 지울 수 있습니다.

## 실행 — 웹 버전

```bash
cd web_version
python app.py
```

브라우저에서 `http://127.0.0.1:5000` 접속 후, 캔버스에 숫자를 그리고 **Predict**를 누르면
서버가 예측 결과를 반환합니다.

## 참고

- 모델 입력 형식: 28x28 grayscale, 0~1 정규화, MNIST 포맷(흰 숫자/검은 배경)에 맞춰 전처리
- 실제 마우스로 그린 손글씨는 MNIST 원본 데이터와 스타일이 달라 인식률이 학습/평가 정확도(99%)보다
  낮게 느껴질 수 있습니다. 개선 작업은 `tasks/progress.md`에서 계속 기록합니다.
