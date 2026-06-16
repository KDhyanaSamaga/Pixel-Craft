# PixelCraft — Desktop Photo Editor

> ⚠️ **Built for fun & learning only** — This project was made to explore GUI development with Tkinter and image processing with OpenCV. Not intended for production use.

---

## What is PixelCraft?

PixelCraft is a lightweight desktop photo editing application built entirely in Python. It provides a simple, intuitive interface where users can open an image, apply common editing operations, preview the result in real time, and save the output — all without leaving the app.

The goal was straightforward: learn how a GUI framework (Tkinter) can collect user inputs and pass them to an image processing library (OpenCV) to produce a result. No cloud, no browser, just a clean desktop app.

---

## Tech Stack

| Technology | Role |
|---|---|
| **Python 3.x** | Core language |
| **Tkinter** | GUI — windows, buttons, sliders, menus |
| **OpenCV (`opencv-python`)** | Image processing engine |
| **Pillow (PIL)** | Displaying OpenCV images inside Tkinter |

### Installation

```bash
pip install opencv-python pillow
```

> Tkinter ships with Python by default and requires no separate installation.

---

## Features

PixelCraft focuses on the following photo editing operations:

### Transforms
- **Rotate** — Rotate image by a custom angle (0–360°) using a slider
- **Flip** — Flip horizontally or vertically with a button click
- **Crop** — Select a region by entering X, Y, Width, and Height values
- **Resize** — Scale the image to a custom width and height

### Adjustments
- **Brightness** — Increase or decrease brightness using a slider
- **Contrast** — Adjust image contrast via a slider

### Filters
- **Grayscale** — Convert the image to black and white
- **Blur** — Apply a Gaussian blur effect
- **Edge Detection** — Detect and highlight edges using Canny

### File Operations
- **Open Image** — Load any image from your local files
- **Save Image** — Export the edited image to disk
- **Reset** — Revert to the original image at any point

---

## How It Works

The app follows a simple input → process → display loop:

```
User moves a slider / clicks a button
           ↓
Tkinter captures the value
           ↓
Value is passed to an OpenCV function
           ↓
OpenCV processes the image frame
           ↓
Pillow converts it for Tkinter display
           ↓
Updated preview shown in the GUI
```

Example — Brightness slider at value `+50`:
```python
result = cv2.convertScaleAbs(image, alpha=1.0, beta=50)
```

Example — Rotation at `45°`:
```python
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))
```

---

## Project Structure

```
photo_editor/
│
├── main.py               # Entry point — launches the application
├── ui.py                 # Tkinter GUI — windows, buttons, sliders, layout
├── image_processor.py    # All OpenCV functions (rotate, crop, blur, etc.)
│
├── assets/               # App icons or any static assets
│
└── images/               # Sample images for testing
```

### File Responsibilities

**`main.py`**
- Initializes the Tkinter root window
- Wires the UI and processor together
- Starts the main event loop

**`ui.py`**
- Defines all GUI components (buttons, sliders, input boxes, image canvas)
- Captures user inputs and calls the corresponding processor functions
- Updates the image preview after each operation

**`image_processor.py`**
- Contains all OpenCV logic as standalone functions
- Each function accepts an image and the required parameters, returns the processed image
- Completely decoupled from the GUI layer

---

## Running the App

```bash
python main.py
```

---

## Packaging as an Executable

To share the app with someone who doesn't have Python installed:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

This produces a single `.exe` (Windows) or binary (Mac/Linux) inside the `dist/` folder that anyone can run directly.

---

## Limitations

- No multi-layer or non-destructive editing (single image, sequential operations)
- No audio or video support — photo editing only
- No undo history (reset returns to original, but no step-by-step undo)
- No web deployment — desktop only

---

## Purpose

This project was built purely for **fun and learning**. The main goals were:

- Understand how GUI frameworks work in Python
- Learn how to integrate OpenCV into a real application
- Practice separating UI logic from processing logic (clean architecture)
- Get comfortable with packaging Python apps for distribution

If you're also learning Python GUI or OpenCV, feel free to fork this and experiment!

---

## License

This project has no formal license — it's a personal learning project. Use it however you like.
