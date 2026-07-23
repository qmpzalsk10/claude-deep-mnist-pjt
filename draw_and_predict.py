"""Tkinter GUI app: draw a digit with the mouse and predict it using the trained MNIST CNN model."""

import tkinter as tk
from tkinter import messagebox

import numpy as np
from PIL import Image, ImageDraw, ImageOps
from tensorflow import keras

MODEL_PATH = "mnist_cnn_model.keras"
CANVAS_SIZE = 280  # 10x the MNIST image size, for easier mouse drawing
BRUSH_WIDTH = 16

model = keras.models.load_model(MODEL_PATH)


def preprocess_image(image):
    """Convert a white-background/black-stroke PIL image into a normalized
    28x28 array in the format the MNIST model expects (white digit on black)."""

    # MNIST digits are white strokes on a black background, so invert colors
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


class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognizer")

        # Canvas for mouse drawing (white background, black strokes)
        self.canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white", cursor="cross")
        self.canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Offscreen image that mirrors what is drawn on the canvas
        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), color=255)
        self.draw = ImageDraw.Draw(self.image)

        self.last_x, self.last_y = None, None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_last_position)

        self.result_label = tk.Label(root, text="Draw a digit (0-9)", font=("Arial", 20))
        self.result_label.grid(row=1, column=0, columnspan=3, pady=5)

        tk.Button(root, text="Predict", command=self.predict, width=10).grid(row=2, column=0, pady=10)
        tk.Button(root, text="Clear", command=self.clear, width=10).grid(row=2, column=1, pady=10)
        tk.Button(root, text="Quit", command=root.destroy, width=10).grid(row=2, column=2, pady=10)

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x is not None:
            self.canvas.create_line(
                self.last_x, self.last_y, x, y,
                width=BRUSH_WIDTH, fill="black", capstyle=tk.ROUND, smooth=True,
            )
            self.draw.line([self.last_x, self.last_y, x, y], fill=0, width=BRUSH_WIDTH)
        self.last_x, self.last_y = x, y

    def reset_last_position(self, _event):
        self.last_x, self.last_y = None, None

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), color=255)
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="Draw a digit (0-9)")

    def predict(self):
        array = preprocess_image(self.image)
        if array is None:
            messagebox.showinfo("No input", "Please draw a digit first.")
            return

        predictions = model.predict(array, verbose=0)[0]
        digit = int(np.argmax(predictions))
        confidence = float(predictions[digit]) * 100
        self.result_label.config(text=f"Prediction: {digit}  ({confidence:.1f}%)")


if __name__ == "__main__":
    root = tk.Tk()
    DigitRecognizerApp(root)
    root.mainloop()
