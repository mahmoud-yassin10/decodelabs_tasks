# Project 4: Advanced OCR Text Recognition Pipeline

## Overview

This project is an advanced **Optical Character Recognition (OCR) pipeline** built using Python, OpenCV, NumPy, and Tesseract OCR for the **DecodeLabs Artificial Intelligence Internship**.

The system reads an image containing printed text, applies multiple image-preprocessing techniques, extracts machine-readable text, calculates word-level confidence scores, filters low-confidence detections, draws bounding boxes around validated words, and saves detailed reports.

The pipeline goes beyond the basic project requirements by automatically testing multiple preprocessing strategies and Tesseract Page Segmentation Modes before selecting the strongest OCR configuration.

---

## Project Goal

The goal of this project is to build a functional text-recognition pipeline capable of:

- Loading raw image input
- Applying image preprocessing
- Extracting readable text from an image
- Measuring OCR confidence scores
- Filtering low-confidence detections
- Drawing bounding boxes around validated words
- Comparing multiple OCR configurations
- Selecting the strongest result automatically
- Saving visual outputs and reports

---

## Key Features

- Tesseract OCR integration
- OpenCV image processing
- Automatic Tesseract executable discovery
- Grayscale conversion
- Gaussian blur
- Automatic deskewing
- Otsu thresholding
- Adaptive thresholding
- Multiple preprocessing modes
- Multiple Tesseract Page Segmentation Modes
- Automatic OCR configuration comparison
- Automatic best-result selection
- Word-level confidence scores
- Minimum 80% confidence filtering
- Bounding boxes around validated words
- Annotated image output
- Raw extracted text output
- Confidence-filtered validated text output
- OCR confidence CSV report
- OCR mode-comparison CSV report
- OCR summary report

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Tesseract OCR
- pytesseract
- CSV
- pathlib
- Git
- GitHub

---

## Folder Structure

```text
project-4-ocr-text-recognition/
│
├── ocr_pipeline.py
├── requirements.txt
├── README.md
│
├── sample-input/
│   └── sample_document.png
│
└── generated-output/
    ├── 01_original.png
    ├── 02_grayscale.png
    ├── 03_blurred.png
    ├── 04_deskewed.png
    ├── 05_otsu_threshold.png
    ├── 06_adaptive_threshold.png
    ├── 07_annotated_output.png
    ├── extracted_text.txt
    ├── validated_text.txt
    ├── ocr_confidence_report.csv
    ├── ocr_mode_comparison.csv
    └── ocr_summary.txt
```

---

## Installation

### 1. Install Python Packages

Run:

```bash
pip install pytesseract opencv-python numpy
```

On Windows, if needed:

```bash
py -m pip install pytesseract opencv-python numpy
```

### 2. Install Tesseract OCR

Tesseract OCR must be installed separately because `pytesseract` is only a Python wrapper.

The default Windows installation path is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The Python script automatically checks:

1. Whether `tesseract` is available through the system PATH
2. Whether Tesseract exists in the default Windows installation folder

---

## Input Image

Place the test image inside:

```text
sample-input/
```

Rename it:

```text
sample_document.png
```

A clear image containing printed English text is recommended.

---

## How to Run

From the repository root folder, run:

```bash
python project-4-ocr-text-recognition/ocr_pipeline.py
```

On Windows, if `python` does not work:

```bash
py project-4-ocr-text-recognition/ocr_pipeline.py
```

---

## OCR Workflow

```text
Input Image
→ Load Image
→ Deskew Image
→ Convert to Grayscale
→ Apply Gaussian Blur
→ Apply Thresholding
→ Run OCR Configurations
→ Compare Results
→ Select Best Configuration
→ Filter by Confidence
→ Draw Bounding Boxes
→ Save Reports
```

---

## Preprocessing Modes

The pipeline generates and tests five image versions:

```text
original_deskewed
grayscale
blurred
otsu_threshold
adaptive_threshold
```

### 1. Original Deskewed Image

The original image is corrected for rotation before OCR.

### 2. Grayscale Image

Color information is removed to simplify visual analysis.

```text
RGB Image
→ Grayscale Intensity Matrix
```

### 3. Blurred Image

Gaussian blur reduces minor artifacts and noise.

```text
Grayscale Image
→ Smoothed Image
```

### 4. Otsu Threshold Image

Otsu thresholding automatically calculates a global cutoff value and converts pixels into black or white values.

```text
Grayscale Pixel
→ Black or White Pixel
```

### 5. Adaptive Threshold Image

Adaptive thresholding calculates local thresholds for different areas of the image. This can help when lighting is uneven.

---

## Deskewing

The pipeline detects text rotation and corrects tilted images before OCR.

Example:

```text
Tilted Text
→ Detected Rotation Angle
→ Corrected Horizontal Text
```

In the tested sample, the detected deskew angle was:

```text
-0.63 degrees
```

---

## Tesseract Page Segmentation Modes

The pipeline tests four Tesseract Page Segmentation Modes:

| PSM Mode | Description                  |
| -------- | ---------------------------- |
| `3`      | Automatic page segmentation  |
| `6`      | Single uniform block of text |
| `7`      | Single text line             |
| `11`     | Sparse scattered text        |

The system tests:

```text
5 preprocessing modes × 4 PSM modes = 20 OCR configurations
```

The strongest result is selected automatically.

---

## Best-Result Selection Logic

The OCR configurations are ranked using:

1. Number of validated words
2. Average confidence score
3. Validated-word ratio

The system selects the configuration with the strongest combined result.

---

## Confidence Filtering

Each detected word receives a confidence score from Tesseract OCR.

The project applies an 80% minimum confidence threshold:

```python
MINIMUM_CONFIDENCE = 80.0
```

Words with confidence below 80%:

- remain visible in the confidence report
- are excluded from the validated text output
- do not receive bounding boxes in the annotated image

Words with confidence at or above 80%:

- appear in the validated text
- receive a visual bounding box
- contribute to the validated-word ratio

---

## Example Input

```text
It was the best of
times, it was the worst
of times, it was the age
of wisdom, it was the
age of foolishness...
```

---

## Actual Test Result

The pipeline automatically tested 20 OCR configurations and selected:

```text
Selected preprocessing mode: original_deskewed
Selected Tesseract PSM mode: 3
Detected deskew angle: -0.63 degrees
```

OCR performance:

```text
Total detected words: 24
Validated words with confidence >= 80%: 24
Validated ratio: 100.00%
Average detected-word confidence: 95.96%
```

Extracted text:

```text
It was the best of
times, it was the worst
of times, it was the age
of wisdom, it was the
age of foolishness...
```

Validated text:

```text
It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...
```

---

## Generated Files

### `01_original.png`

The original sample image.

### `02_grayscale.png`

The grayscale version of the input image.

### `03_blurred.png`

The image after Gaussian blur.

### `04_deskewed.png`

The image after automatic rotation correction.

### `05_otsu_threshold.png`

The image after Otsu thresholding.

### `06_adaptive_threshold.png`

The image after adaptive thresholding.

### `07_annotated_output.png`

The final visual output with bounding boxes and confidence labels around validated words.

### `extracted_text.txt`

The complete text extracted by the strongest OCR configuration.

### `validated_text.txt`

Only words that passed the 80% confidence threshold.

### `ocr_confidence_report.csv`

A word-level recognition report containing:

```text
word
confidence
validated
x
y
width
height
```

### `ocr_mode_comparison.csv`

A comparison report for all tested OCR configurations containing:

```text
preprocessing_mode
psm_mode
total_words
validated_word_count
validated_ratio
average_confidence
raw_text
```

### `ocr_summary.txt`

A readable report containing:

- Tesseract executable path
- detected deskew angle
- selected preprocessing mode
- selected PSM mode
- total detected words
- validated-word count
- validated ratio
- average confidence
- raw extracted text
- validated extracted text
- generated file paths

---

## Validation Checklist

| Requirement               | Implementation                           |
| ------------------------- | ---------------------------------------- |
| Library integration       | `pytesseract`, OpenCV, and NumPy         |
| Raw visual input          | Sample image loaded from `sample-input/` |
| Grayscale conversion      | Implemented                              |
| Gaussian blur             | Implemented                              |
| Deskewing                 | Implemented                              |
| Thresholding              | Otsu and adaptive thresholding           |
| OCR recognition           | Tesseract OCR                            |
| Confidence benchmarking   | Minimum 80% confidence gate              |
| Visual confirmation       | Annotated bounding boxes                 |
| OCR configuration testing | 20 configurations                        |
| Reporting                 | CSV and TXT reports                      |

---

## Concepts Demonstrated

This project demonstrates:

- Optical Character Recognition
- Computer vision
- Image preprocessing
- RGB image matrices
- Grayscale conversion
- Gaussian blur
- Deskewing
- Thresholding
- Otsu thresholding
- Adaptive thresholding
- Tesseract Page Segmentation Modes
- Confidence scores
- Confidence filtering
- Bounding boxes
- CSV reporting
- Automatic model evaluation
- Visual output generation

---

## Limitations

- Recognition quality depends on image quality.
- Blurry images may reduce OCR accuracy.
- Handwritten text may require specialized models.
- Decorative fonts may reduce recognition performance.
- High confidence does not always guarantee perfect recognition.
- The current version focuses on English printed text.
- The pipeline does not apply semantic spelling correction after OCR.

---

## Possible Future Improvements

- Add Arabic OCR support
- Add multilingual OCR
- Process multiple images in batch
- Add PDF page processing
- Generate searchable PDFs
- Add spelling correction
- Add document-type detection
- Build a graphical interface
- Add drag-and-drop input
- Add API endpoints
- Deploy as a web application
- Add object detection using MobileNet-SSD

---

## Project Status

Completed.

---

## Author

**Mahmoud Yassin**

Created as part of the DecodeLabs Artificial Intelligence Internship.
