# CLAUDE.md — web_version

> 이 폴더는 상위 프로젝트(`claude-deep-mnist-pjt`)의 **웹 버전**입니다.
> 상위 폴더의 `CLAUDE.md` 규칙(보안 규칙, 위험 작업 확인, 작업 원칙 등)을 그대로 따릅니다.

---

## 폴더 목적

손글씨 숫자 인식 프로그램의 데스크톱(tkinter) 버전을 브라우저에서 사용할 수 있도록
Flask 웹 서버로 다시 구현한 버전입니다.

- 브라우저 캔버스에 마우스로 숫자를 그림
- 그린 이미지를 서버(`/predict`)로 전송
- 서버는 상위 폴더에서 학습된 `mnist_cnn_model.keras` 모델로 예측 후 결과를 반환

---

## 구조

```
web_version/
├── CLAUDE.md          # 이 파일
├── app.py             # Flask 서버 (모델 로드 + /predict API)
├── mnist_cnn_model.keras  # 학습된 모델 (상위 폴더에서 복사)
└── templates/
    └── index.html     # 캔버스 드로잉 UI + JavaScript
```

---

## 코드 작성 규칙

- 모든 코드 주석은 **영어**로 작성 (상위 CLAUDE.md 지침).
- 모델을 다시 학습시키지 않음 — 상위 폴더의 `train_model.py`로 만든
  `mnist_cnn_model.keras`를 그대로 재사용.
- 서버 실행: `python app.py` → `http://127.0.0.1:5000` 접속.

---

## 참고

- 데스크톱 버전 원본: `../train_model.py`, `../draw_and_predict.py`
- 모델 입력 형식: 28x28 grayscale, 0~1 정규화, 흰색 숫자/검은 배경 (MNIST 포맷)
