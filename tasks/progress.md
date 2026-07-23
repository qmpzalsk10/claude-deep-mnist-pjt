# Progress Log

## 2026-07-23
- Installed Python 3.11.9 via winget (Python.Python.3.11)
- Installed tensorflow, numpy, pillow via pip
- Created `train_model.py` — CNN trained on MNIST (5 epochs)
  - Test accuracy: 99.02%, test loss: 0.0299
  - Model saved to `mnist_cnn_model.keras`
- Created `draw_and_predict.py` — tkinter GUI, mouse-drawn canvas + prediction
  - Verified preprocessing pipeline with font-rendered digits (7/10, glyph-shape mismatch expected)
  - Verified preprocessing pipeline with real MNIST images resized through canvas format (27/30)
  - Launched GUI app for manual user testing (drawing with mouse)
- Created `web_version/` folder with its own `CLAUDE.md`
  - Copied `mnist_cnn_model.keras` into `web_version/`
  - Installed Flask
  - Created `web_version/app.py` (Flask server, /predict API reusing the same preprocessing logic)
  - Created `web_version/templates/index.html` (HTML5 canvas drawing UI, mouse + touch support)
  - Ran Flask dev server on http://127.0.0.1:5000, verified /predict via synthetic digit test (200 OK, correct prediction)
  - Opened the app in the default browser for manual testing
  - User confirmed manual drawing test in browser works correctly
