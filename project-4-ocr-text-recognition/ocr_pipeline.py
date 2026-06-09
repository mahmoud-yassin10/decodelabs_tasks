# DecodeLabs Artificial Intelligence Internship
# Project 4: Image or Text Recognition
#
# Advanced OCR Text Recognition Pipeline
#
# Features:
# - Loads a raw input image
# - Configures Tesseract automatically
# - Applies grayscale conversion
# - Applies Gaussian blur
# - Applies deskewing
# - Creates Otsu and adaptive-threshold versions
# - Tests multiple preprocessing modes
# - Tests multiple Tesseract PSM modes
# - Automatically selects the strongest OCR result
# - Filters words below 80% confidence
# - Draws bounding boxes around validated words
# - Saves extracted text
# - Saves confidence reports
# - Saves a comparison report
# - Saves a full summary report

import csv
import shutil
from pathlib import Path

import cv2
import numpy as np
import pytesseract
from pytesseract import Output


# --------------------------------------------------
# 1. Define project paths
# --------------------------------------------------

PROJECT_FOLDER = Path(__file__).parent

INPUT_IMAGE = PROJECT_FOLDER / "sample-input" / "sample_document.png"

OUTPUT_FOLDER = PROJECT_FOLDER / "generated-output"
OUTPUT_FOLDER.mkdir(exist_ok=True)

ORIGINAL_IMAGE_FILE = OUTPUT_FOLDER / "01_original.png"
GRAYSCALE_IMAGE_FILE = OUTPUT_FOLDER / "02_grayscale.png"
BLURRED_IMAGE_FILE = OUTPUT_FOLDER / "03_blurred.png"
DESKEWED_IMAGE_FILE = OUTPUT_FOLDER / "04_deskewed.png"
OTSU_IMAGE_FILE = OUTPUT_FOLDER / "05_otsu_threshold.png"
ADAPTIVE_IMAGE_FILE = OUTPUT_FOLDER / "06_adaptive_threshold.png"
ANNOTATED_IMAGE_FILE = OUTPUT_FOLDER / "07_annotated_output.png"

EXTRACTED_TEXT_FILE = OUTPUT_FOLDER / "extracted_text.txt"
VALIDATED_TEXT_FILE = OUTPUT_FOLDER / "validated_text.txt"
CONFIDENCE_REPORT_FILE = OUTPUT_FOLDER / "ocr_confidence_report.csv"
MODE_COMPARISON_FILE = OUTPUT_FOLDER / "ocr_mode_comparison.csv"
SUMMARY_FILE = OUTPUT_FOLDER / "ocr_summary.txt"


# --------------------------------------------------
# 2. Configuration
# --------------------------------------------------

MINIMUM_CONFIDENCE = 80.0

# Tesseract Page Segmentation Modes:
# 3  = automatic page segmentation
# 6  = single uniform block of text
# 7  = single line of text
# 11 = sparse text
PSM_MODES = [3, 6, 7, 11]


# --------------------------------------------------
# 3. Configure Tesseract OCR
# --------------------------------------------------

def configure_tesseract():
    """
    Find the Tesseract OCR executable automatically.

    Priority:
    1. Search system PATH
    2. Search the default Windows installation folder
    """

    tesseract_in_path = shutil.which("tesseract")

    if tesseract_in_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_in_path
        return tesseract_in_path

    default_windows_path = Path(
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    if default_windows_path.exists():
        pytesseract.pytesseract.tesseract_cmd = str(
            default_windows_path
        )

        return str(default_windows_path)

    raise FileNotFoundError(
        "Tesseract OCR could not be found.\n"
        "Install Tesseract OCR or update the executable path."
    )


# --------------------------------------------------
# 4. Load input image
# --------------------------------------------------

def load_image(image_path):
    """
    Load the sample input image from disk.
    """

    if not image_path.exists():
        raise FileNotFoundError(
            f"Input image not found:\n{image_path}\n\n"
            "Add sample_document.png inside the sample-input folder."
        )

    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError(
            "The image exists, but OpenCV could not read it.\n"
            "Use a valid PNG or JPG file."
        )

    return image


# --------------------------------------------------
# 5. Deskew image
# --------------------------------------------------

def deskew_image(image):
    """
    Attempt to detect and correct image rotation.

    Returns:
    - deskewed image
    - detected rotation angle
    """

    grayscale = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    threshold = cv2.threshold(
        grayscale,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )[1]

    coordinates = np.column_stack(
        np.where(threshold > 0)
    )

    if len(coordinates) == 0:
        return image, 0.0

    angle = cv2.minAreaRect(
        coordinates
    )[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    height, width = image.shape[:2]

    center = (
        width // 2,
        height // 2
    )

    rotation_matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    deskewed = cv2.warpAffine(
        image,
        rotation_matrix,
        (width, height),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )

    return deskewed, angle


# --------------------------------------------------
# 6. Generate preprocessing versions
# --------------------------------------------------

def create_preprocessed_versions(image):
    """
    Create multiple versions of the input image.

    The OCR engine will test all versions and automatically
    choose the best result.
    """

    deskewed_image, detected_angle = deskew_image(
        image
    )

    grayscale = cv2.cvtColor(
        deskewed_image,
        cv2.COLOR_BGR2GRAY
    )

    blurred = cv2.GaussianBlur(
        grayscale,
        (5, 5),
        0
    )

    otsu_threshold = cv2.threshold(
        blurred,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    adaptive_threshold = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    cv2.imwrite(
        str(ORIGINAL_IMAGE_FILE),
        image
    )

    cv2.imwrite(
        str(GRAYSCALE_IMAGE_FILE),
        grayscale
    )

    cv2.imwrite(
        str(BLURRED_IMAGE_FILE),
        blurred
    )

    cv2.imwrite(
        str(DESKEWED_IMAGE_FILE),
        deskewed_image
    )

    cv2.imwrite(
        str(OTSU_IMAGE_FILE),
        otsu_threshold
    )

    cv2.imwrite(
        str(ADAPTIVE_IMAGE_FILE),
        adaptive_threshold
    )

    preprocessing_modes = {
        "original_deskewed": deskewed_image,
        "grayscale": grayscale,
        "blurred": blurred,
        "otsu_threshold": otsu_threshold,
        "adaptive_threshold": adaptive_threshold
    }

    return preprocessing_modes, deskewed_image, detected_angle


# --------------------------------------------------
# 7. Run OCR on one image version
# --------------------------------------------------

def run_ocr(image, preprocessing_mode, psm_mode):
    """
    Run Tesseract OCR on one image version using one PSM mode.

    Returns:
    - OCR detections
    - raw extracted text
    - validated words
    - performance statistics
    """

    config = f"--oem 3 --psm {psm_mode}"

    ocr_data = pytesseract.image_to_data(
        image,
        output_type=Output.DICT,
        config=config
    )

    raw_text = pytesseract.image_to_string(
        image,
        config=config
    ).strip()

    detections = []
    validated_words = []

    total_entries = len(
        ocr_data["text"]
    )

    for index in range(total_entries):
        word = ocr_data["text"][index].strip()

        if not word:
            continue

        try:
            confidence = float(
                ocr_data["conf"][index]
            )
        except ValueError:
            confidence = -1.0

        x = int(
            ocr_data["left"][index]
        )

        y = int(
            ocr_data["top"][index]
        )

        width = int(
            ocr_data["width"][index]
        )

        height = int(
            ocr_data["height"][index]
        )

        is_validated = (
            confidence >= MINIMUM_CONFIDENCE
        )

        detection = {
            "word": word,
            "confidence": round(confidence, 2),
            "validated": is_validated,
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }

        detections.append(
            detection
        )

        if is_validated:
            validated_words.append(
                word
            )

    valid_confidences = [
        detection["confidence"]
        for detection in detections
        if detection["confidence"] >= 0
    ]

    if valid_confidences:
        average_confidence = (
            sum(valid_confidences)
            / len(valid_confidences)
        )
    else:
        average_confidence = 0.0

    total_words = len(
        detections
    )

    validated_word_count = len(
        validated_words
    )

    if total_words > 0:
        validated_ratio = (
            validated_word_count
            / total_words
        )
    else:
        validated_ratio = 0.0

    result = {
        "preprocessing_mode": preprocessing_mode,
        "psm_mode": psm_mode,
        "detections": detections,
        "raw_text": raw_text,
        "validated_words": validated_words,
        "total_words": total_words,
        "validated_word_count": validated_word_count,
        "average_confidence": average_confidence,
        "validated_ratio": validated_ratio
    }

    return result


# --------------------------------------------------
# 8. Compare OCR configurations
# --------------------------------------------------

def compare_ocr_configurations(preprocessing_modes):
    """
    Run OCR using every preprocessing mode and every
    PSM mode.

    The strongest result is selected automatically.
    """

    results = []

    for preprocessing_mode, image in preprocessing_modes.items():
        for psm_mode in PSM_MODES:
            result = run_ocr(
                image,
                preprocessing_mode,
                psm_mode
            )

            results.append(
                result
            )

    results.sort(
        key=lambda result: (
            result["validated_word_count"],
            result["average_confidence"],
            result["validated_ratio"]
        ),
        reverse=True
    )

    best_result = results[0]

    return results, best_result


# --------------------------------------------------
# 9. Draw validated bounding boxes
# --------------------------------------------------

def create_annotated_image(
    base_image,
    best_result
):
    """
    Draw bounding boxes around validated OCR words.
    """

    annotated_image = base_image.copy()

    for detection in best_result["detections"]:
        if not detection["validated"]:
            continue

        x = detection["x"]
        y = detection["y"]
        width = detection["width"]
        height = detection["height"]

        word = detection["word"]
        confidence = detection["confidence"]

        cv2.rectangle(
            annotated_image,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

        label = (
            f"{word} ({confidence:.1f}%)"
        )

        cv2.putText(
            annotated_image,
            label,
            (x, max(y - 8, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 255, 0),
            1
        )

    cv2.imwrite(
        str(ANNOTATED_IMAGE_FILE),
        annotated_image
    )


# --------------------------------------------------
# 10. Save extracted text files
# --------------------------------------------------

def save_text_files(best_result):
    """
    Save full extracted text and confidence-filtered text.
    """

    raw_text = best_result["raw_text"]

    validated_text = " ".join(
        best_result["validated_words"]
    )

    with open(
        EXTRACTED_TEXT_FILE,
        mode="w",
        encoding="utf-8"
    ) as file:
        file.write(
            raw_text
        )

    with open(
        VALIDATED_TEXT_FILE,
        mode="w",
        encoding="utf-8"
    ) as file:
        file.write(
            validated_text
        )

    return raw_text, validated_text


# --------------------------------------------------
# 11. Save confidence report
# --------------------------------------------------

def save_confidence_report(best_result):
    """
    Save word-level OCR confidence details.
    """

    fieldnames = [
        "word",
        "confidence",
        "validated",
        "x",
        "y",
        "width",
        "height"
    ]

    with open(
        CONFIDENCE_REPORT_FILE,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            best_result["detections"]
        )


# --------------------------------------------------
# 12. Save mode comparison report
# --------------------------------------------------

def save_mode_comparison(results):
    """
    Save the performance of every preprocessing and PSM
    combination.
    """

    fieldnames = [
        "preprocessing_mode",
        "psm_mode",
        "total_words",
        "validated_word_count",
        "validated_ratio",
        "average_confidence",
        "raw_text"
    ]

    with open(
        MODE_COMPARISON_FILE,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for result in results:
            writer.writerow(
                {
                    "preprocessing_mode": (
                        result["preprocessing_mode"]
                    ),
                    "psm_mode": (
                        result["psm_mode"]
                    ),
                    "total_words": (
                        result["total_words"]
                    ),
                    "validated_word_count": (
                        result["validated_word_count"]
                    ),
                    "validated_ratio": (
                        f"{result['validated_ratio']:.4f}"
                    ),
                    "average_confidence": (
                        f"{result['average_confidence']:.2f}"
                    ),
                    "raw_text": (
                        result["raw_text"]
                    )
                }
            )


# --------------------------------------------------
# 13. Save summary report
# --------------------------------------------------

def save_summary_report(
    tesseract_path,
    detected_angle,
    best_result,
    raw_text,
    validated_text
):
    """
    Save a readable summary report for the selected OCR mode.
    """

    summary_lines = [
        "DecodeLabs OCR Text Recognition Pipeline",
        "=" * 70,
        "",
        f"Tesseract executable: {tesseract_path}",
        f"Detected deskew angle: {detected_angle:.2f} degrees",
        "",
        "Selected OCR Configuration",
        "-" * 70,
        (
            "Preprocessing mode: "
            f"{best_result['preprocessing_mode']}"
        ),
        (
            "Tesseract PSM mode: "
            f"{best_result['psm_mode']}"
        ),
        "",
        "Accuracy Summary",
        "-" * 70,
        (
            "Total detected words: "
            f"{best_result['total_words']}"
        ),
        (
            "Validated words with confidence >= "
            f"{MINIMUM_CONFIDENCE:.0f}%: "
            f"{best_result['validated_word_count']}"
        ),
        (
            "Validated ratio: "
            f"{best_result['validated_ratio'] * 100:.2f}%"
        ),
        (
            "Average detected-word confidence: "
            f"{best_result['average_confidence']:.2f}%"
        ),
        "",
        "Raw Extracted Text",
        "-" * 70,
        raw_text,
        "",
        "Validated Extracted Text",
        "-" * 70,
        validated_text,
        "",
        "Generated Files",
        "-" * 70,
        str(ORIGINAL_IMAGE_FILE),
        str(GRAYSCALE_IMAGE_FILE),
        str(BLURRED_IMAGE_FILE),
        str(DESKEWED_IMAGE_FILE),
        str(OTSU_IMAGE_FILE),
        str(ADAPTIVE_IMAGE_FILE),
        str(ANNOTATED_IMAGE_FILE),
        str(EXTRACTED_TEXT_FILE),
        str(VALIDATED_TEXT_FILE),
        str(CONFIDENCE_REPORT_FILE),
        str(MODE_COMPARISON_FILE),
        str(SUMMARY_FILE)
    ]

    with open(
        SUMMARY_FILE,
        mode="w",
        encoding="utf-8"
    ) as file:
        file.write(
            "\n".join(summary_lines)
        )


# --------------------------------------------------
# 14. Display results
# --------------------------------------------------

def display_results(
    detected_angle,
    best_result,
    raw_text,
    validated_text
):
    """
    Print the final OCR results clearly.
    """

    print("-" * 70)
    print("Best OCR Configuration")
    print("-" * 70)

    print(
        "Selected preprocessing mode: "
        f"{best_result['preprocessing_mode']}"
    )

    print(
        "Selected Tesseract PSM mode: "
        f"{best_result['psm_mode']}"
    )

    print(
        "Detected deskew angle: "
        f"{detected_angle:.2f} degrees"
    )

    print("-" * 70)
    print("OCR Results")
    print("-" * 70)

    print(
        "Total detected words: "
        f"{best_result['total_words']}"
    )

    print(
        "Validated words with confidence >= "
        f"{MINIMUM_CONFIDENCE:.0f}%: "
        f"{best_result['validated_word_count']}"
    )

    print(
        "Validated ratio: "
        f"{best_result['validated_ratio'] * 100:.2f}%"
    )

    print(
        "Average detected-word confidence: "
        f"{best_result['average_confidence']:.2f}%"
    )

    print("-" * 70)
    print("Raw Extracted Text")
    print("-" * 70)

    if raw_text:
        print(
            raw_text
        )
    else:
        print(
            "No text was detected."
        )

    print("-" * 70)
    print("Validated Extracted Text")
    print("-" * 70)

    if validated_text:
        print(
            validated_text
        )
    else:
        print(
            "No words passed the confidence threshold."
        )

    print("-" * 70)
    print("Generated Files")
    print("-" * 70)

    print(
        ORIGINAL_IMAGE_FILE
    )

    print(
        GRAYSCALE_IMAGE_FILE
    )

    print(
        BLURRED_IMAGE_FILE
    )

    print(
        DESKEWED_IMAGE_FILE
    )

    print(
        OTSU_IMAGE_FILE
    )

    print(
        ADAPTIVE_IMAGE_FILE
    )

    print(
        ANNOTATED_IMAGE_FILE
    )

    print(
        EXTRACTED_TEXT_FILE
    )

    print(
        VALIDATED_TEXT_FILE
    )

    print(
        CONFIDENCE_REPORT_FILE
    )

    print(
        MODE_COMPARISON_FILE
    )

    print(
        SUMMARY_FILE
    )


# --------------------------------------------------
# 15. Run the complete OCR pipeline
# --------------------------------------------------

def main():
    print(
        "DecodeLabs Advanced OCR Text Recognition Pipeline"
    )

    print(
        "=" * 70
    )

    tesseract_path = configure_tesseract()

    print(
        "Tesseract OCR configured successfully."
    )

    print(
        f"Executable: {tesseract_path}"
    )

    image = load_image(
        INPUT_IMAGE
    )

    print(
        "Input image loaded successfully."
    )

    preprocessing_modes, deskewed_image, detected_angle = (
        create_preprocessed_versions(
            image
        )
    )

    print(
        "Image preprocessing completed."
    )

    print(
        "Applied: grayscale, blur, deskewing, "
        "Otsu thresholding, adaptive thresholding."
    )

    print(
        "Testing multiple preprocessing modes "
        "and Tesseract PSM configurations..."
    )

    results, best_result = compare_ocr_configurations(
        preprocessing_modes
    )

    print(
        f"Tested {len(results)} OCR configurations."
    )

    create_annotated_image(
        deskewed_image,
        best_result
    )

    raw_text, validated_text = save_text_files(
        best_result
    )

    save_confidence_report(
        best_result
    )

    save_mode_comparison(
        results
    )

    save_summary_report(
        tesseract_path,
        detected_angle,
        best_result,
        raw_text,
        validated_text
    )

    display_results(
        detected_angle,
        best_result,
        raw_text,
        validated_text
    )

    print("-" * 70)

    print(
        "Advanced OCR pipeline completed successfully."
    )


if __name__ == "__main__":
    main()
