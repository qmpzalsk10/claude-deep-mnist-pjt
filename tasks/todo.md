# Todo — 웹 버전 손글씨 숫자 인식 프로그램

- [x] 1. winget으로 Python 3.11 설치
- [x] 2. tensorflow, numpy, pillow 설치
- [x] 3. `train_model.py` 작성 및 학습 → `mnist_cnn_model.keras` 저장 (정확도 99.02%)
- [x] 4. `draw_and_predict.py` (tkinter GUI 데스크톱 버전) 작성 및 실행 확인
- [x] 5. `web_version` 폴더 생성 + `web_version/CLAUDE.md` 작성
- [x] 6. Flask 설치
- [x] 7. `web_version/app.py` 작성 — 학습된 모델(mnist_cnn_model.keras) 로드, `/predict` API 제공
- [x] 8. `web_version/templates/index.html` 작성 — 브라우저 캔버스에 마우스로 그리기 + 예측 버튼
- [x] 9. Flask 서버 실행 후 브라우저로 접속해서 직접 그려보고 인식 확인 (API 테스트 완료, 브라우저 오픈)
