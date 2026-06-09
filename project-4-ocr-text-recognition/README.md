# Project 4: OCR Text Recognition Pipeline

## Overview

This project is an advanced **Optical Character Recognition (OCR) pipeline** built using Python, OpenCV, and Tesseract OCR for the **DecodeLabs Artificial Intelligence Internship**.

The system reads an image containing printed text, applies image preprocessing techniques, extracts text using Tesseract OCR, calculates word-level confidence scores, filters low-confidence detections, draws bounding boxes around validated words, and saves detailed output reports.

The pipeline goes beyond basic OCR by automatically comparing multiple preprocessing strategies and Tesseract Page Segmentation Modes before selecting the strongest recognition result.

---

## Project Goal

The goal of this project is to build a functional recognition pipeline that can:

- Ingest raw visual data
- Improve image quality using preprocessing
- Extract machine-readable text
- Calculate OCR confidence scores
- Apply an 80% confidence threshold
- Draw bounding boxes around validated words
- Save readable text output
- Save machine-readable confidence reports
- Compare multiple OCR configurations
- Select the strongest result automatically

---

## Core Workflow

```text
Input Image
→ Image Loading
→ Deskewing
→ Grayscale Conversion
→ Gaussian Blur
→ Thresholding
→ OCR Recognition
→ Confidence Filtering
→ Bounding Boxes
→ Extracted Text
→ Reports
```

---

## Features

This project includes:

- Tesseract OCR integration
- OpenCV image processing
- Automatic Tesseract executable discovery
- Raw image loading
- Grayscale conversion
- Gaussian blur
- Automatic deskewing
- Otsu thresholding
- Adaptive thresholding
- Multiple preprocessing modes
- Multiple Tesseract PSM modes
- Automatic configuration comparison
- Automatic selection of the strongest OCR result
- Word-level OCR confidence scores
- 80% minimum confidence filtering
- Bounding boxes around validated words
- Annotated output image
- Extracted raw text
- Confidence-filtered validated text
- OCR confidence report
- OCR mode comparison report
- Summary report

---

## Technologies Used

- Python
- OpenCV
- Tesseract OCR
- pytesseract
- NumPy
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

## Input Image

Place the input image inside:

```text
sample-input/
```

Rename it:

```text
sample_document.png
```

A clear image containing printed English text is recommended for the first test.

---

## Installation

Install the Python dependencies:

```bash
pip install pytesseract opencv-python numpy
```

Tesseract OCR must also be installed separately on Windows.

The default installation location is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The Python script automatically checks this location.

---

## How to Run

From the repository root folder:

```bash
python project-4-ocr-text-recognition/ocr_pipeline.py
```

On Windows, if `python` does not work:

```bash
py project-4-ocr-text-recognition/ocr_pipeline.py
```

---

## Preprocessing Pipeline

The system generates several image versions.

### 1. Original Image

The raw input image is saved for reference.

### 2. Grayscale Conversion

Color channels are removed to simplify visual analysis.

```text
RGB Image
→ Grayscale Intensity Matrix
```

### 3. Gaussian Blur

Minor noise and visual artifacts are reduced.

```text
Grayscale Image
→ Smoothed Image
```

### 4. Deskewing

The script detects text rotation and corrects tilted images.

```text
Tilted Text
→ Horizontal Text Alignment
```

### 5. Otsu Thresholding

The system calculates a global threshold and converts pixels into black or white values.

```text
Grayscale Pixel
→ Black or White Pixel
```

### 6. Adaptive Thresholding

Different areas of the image receive local threshold values. This is useful for uneven lighting.

---

## OCR Configuration Testing

The pipeline tests five preprocessing modes:

```text
original_deskewed
grayscale
blurred
otsu_threshold
adaptive_threshold
```

It also tests four Tesseract Page Segmentation Modes:

| PSM Mode | Description                  |
| -------- | ---------------------------- |
| `3`      | Automatic page segmentation  |
| `6`      | Single uniform block of text |
| `7`      | Single text line             |
| `11`     | Sparse scattered text        |

The complete pipeline tests:

```text
5 preprocessing modes × 4 PSM modes = 20 configurations
```

The strongest configuration is selected automatically based on:

- number of validated words
- average confidence score
- validated-word ratio

---

## Confidence Filtering

Each detected word receives a confidence score.

The project uses an 80% minimum threshold:

```python
MINIMUM_CONFIDENCE = 80.0
```

Words below 80% confidence are recorded in the CSV report but excluded from the validated text output and annotated bounding boxes.

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

## Example Output

```text
DecodeLabs Advanced OCR Text Recognition Pipeline
======================================================================

Tesseract OCR configured successfully.
Input image loaded successfully.
Image preprocessing completed.
Applied: grayscale, blur, deskewing, Otsu thresholding, adaptive thresholding.

Testing multiple preprocessing modes and Tesseract PSM configurations...
Tested 20 OCR configurations.

----------------------------------------------------------------------

Best OCR Configuration
----------------------------------------------------------------------

Selected preprocessing mode: grayscale
Selected Tesseract PSM mode: 6
Detected deskew angle: 0.00 degrees

----------------------------------------------------------------------

OCR Results
----------------------------------------------------------------------

Total detected words: 24
Validated words with confidence >= 80%: 24
Validated ratio: 100.00%
Average detected-word confidence: 95.92%
```

Results may vary depending on the image.

---

## Generated Files

### `01_original.png`

The original input image.

### `02_grayscale.png`

The grayscale version of the image.

### `03_blurred.png`

The Gaussian-blurred image.

### `04_deskewed.png`

The rotation-corrected image.

### `05_otsu_threshold.png`

The image after Otsu thresholding.

### `06_adaptive_threshold.png`

The image after adaptive thresholding.

### `07_annotated_output.png`

The visual output containing bounding boxes and confidence labels around validated words.

### `extracted_text.txt`

The complete OCR text extracted by the strongest OCR configuration.

### `validated_text.txt`

Only words with confidence scores of at least 80%.

### `ocr_confidence_report.csv`

Word-level OCR details:

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

Performance comparison across all tested OCR configurations:

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

A readable summary of the selected OCR configuration, confidence scores, extracted text, and generated files.

---

## Validation Checklist

| Requirement             | Implementation                                                       |
| ----------------------- | -------------------------------------------------------------------- |
| Library integration     | `pytesseract` and OpenCV                                             |
| Image preprocessing     | Grayscale, blur, deskewing, Otsu thresholding, adaptive thresholding |
| Confidence benchmarking | 80% minimum confidence gate                                          |
| Visual confirmation     | Annotated image with bounding boxes                                  |
| Text extraction         | Raw and validated text files                                         |
| Comparison testing      | 20 OCR configurations                                                |
| Reporting               | CSV reports and summary file                                         |

---

## Concepts Used

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
- Page segmentation modes
- Confidence scores
- Confidence filtering
- Bounding boxes
- CSV reporting
- Automated model evaluation
- Visual output generation

---

## Limitations

- Recognition quality depends on image clarity.
- Handwritten text may require a more specialized model.
- Decorative fonts may reduce OCR accuracy.
- A high confidence score does not always guarantee perfect recognition.
- The current pipeline focuses on English printed text.
- The script does not perform semantic correction after OCR extraction.

---

## Possible Future Improvements

- Add Arabic OCR support
- Add multiple-language recognition
- Add PDF page processing
- Add batch image processing
- Add spelling correction
- Add a graphical user interface
- Add drag-and-drop file upload
- Add document-type detection
- Add searchable PDF generation
- Add API endpoints
- Deploy the pipeline as a web application
- Add object detection using MobileNet-SSD

---

## Project Status

Completed.

---

## Author

**Mahmoud Yassin**

Created as part of the DecodeLabs Artificial Intelligence Internship.
