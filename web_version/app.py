"""Flask web server for the handwritten digit recognizer.

Serves the drawing page and a /predict endpoint that runs the trained
MNIST CNN model on an image sent from the browser canvas.
"""

import base64
import io

import numpy as np
from flask import Flask, jsonify, render_template, request
from PIL import Image, ImageOps
from tensorflow import keras

MODEL_PATH = "mnist_cnn_model.keras"

app = Flask(__name__)
model = keras.models.load_model(MODEL_PATH)


def preprocess_image(image):
    """Convert a white-background/black-stroke PIL image into a normalized
    28x28 array in the format the MNIST model expects (white digit on black)."""

    # The browser canvas sends white background with black strokes,
    # but MNIST digits are white strokes on a black background, so invert colors
    inverted = ImageOps.invert(image)

    # Crop to the bounding box of the drawn strokes to center the digit
    bbox = inverted.getbbox()
    if bbox is None:
        return None

    cropped = inverted.crop(bbox)

    # Pad around the digit so it does not touch the image edges, like real MNIST samples
    padding = 20
    padded_size = max(cropped.size) + padding * 2
    padded = Image.new("L", (padded_size, padded_size), color=0)
    paste_x = (padded_size - cropped.width) // 2
    paste_y = (padded_size - cropped.height) // 2
    padded.paste(cropped, (paste_x, paste_y))

    # Resize down to the 28x28 input size expected by the model
    resized = padded.resize((28, 28), Image.LANCZOS)

    array = np.array(resized).astype("float32") / 255.0
    return array.reshape(1, 28, 28, 1)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "image" not in data:
        return jsonify({"error": "No image data provided"}), 400

    # The data URL looks like "data:image/png;base64,<...>"
    header, encoded = data["image"].split(",", 1)
    image_bytes = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(image_bytes)).convert("L")

    array = preprocess_image(image)
    if array is None:
        return jsonify({"error": "Empty canvas"}), 400

    predictions = model.predict(array, verbose=0)[0]
    digit = int(np.argmax(predictions))
    confidence = float(predictions[digit]) * 100

    return jsonify({"digit": digit, "confidence": round(confidence, 1)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
