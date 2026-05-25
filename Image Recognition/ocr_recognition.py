import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
import sys
import datetime
# ── Windows: tell pytesseract where Tesseract is installed ──
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ─────────────────────────────────────────
#  OCR TEXT RECOGNITION
# ─────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════════════╗
║        🔍  OCR TEXT RECOGNITION TOOL        ║
║           ║
╚══════════════════════════════════════════════╝
"""

# ─────────────────────────────────────────
#  STEP 1 — Preprocess the image
# ─────────────────────────────────────────

def preprocess_image(image_path: str) -> Image.Image:
    """
    Load and preprocess an image for OCR.
    Steps: open → grayscale → enhance contrast → sharpen
    """
    img = Image.open(image_path)

    img = img.convert("L")

    # Boost contrast so text stands out from background
    img = ImageEnhance.Contrast(img).enhance(2.0)

    # Sharpen edges to make characters crisper
    img = img.filter(ImageFilter.SHARPEN)

    return img


# ─────────────────────────────────────────
#  STEP 2 — Run OCR on the image
# ─────────────────────────────────────────

def run_ocr(image_path: str) -> dict:
    """
    Run Tesseract OCR on an image file.
    Returns a dict with extracted text and metadata.
    """
    if not os.path.exists(image_path):
        return {"error": f"File not found: {image_path}"}

    # Load original image info
    original = Image.open(image_path)
    width, height = original.size
    mode = original.mode

    # Preprocess
    processed = preprocess_image(image_path)

    # ── Core OCR call ──────────────────────
    raw_text = pytesseract.image_to_string(
        processed,
        config="--oem 3 --psm 6"
    )

    # Also get per-word confidence scores
    data = pytesseract.image_to_data(
        processed,
        config="--oem 3 --psm 6",
        output_type=pytesseract.Output.DICT
    )

    # Filter confident words only 
    confidences = [
        int(c) for c in data["conf"] if str(c).lstrip("-").isdigit() and int(c) > 0
    ]
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0

    words = [
        w for w, c in zip(data["text"], data["conf"])
        if w.strip() and str(c).lstrip("-").isdigit() and int(c) > 60
    ]

    return {
        "file":           os.path.basename(image_path),
        "size":           f"{width} x {height} px",
        "mode":           mode,
        "raw_text":       raw_text.strip(),
        "word_count":     len(words),
        "avg_confidence": round(avg_confidence, 1),
        "words_detected": words,
    }


# ─────────────────────────────────────────
#  STEP 3 — Display results clearly
# ─────────────────────────────────────────

def display_result(result: dict, label: str = ""):
    """Print OCR results in a clean, readable format."""

    if "error" in result:
        print(f"  ❌ ERROR: {result['error']}\n")
        return

    conf = result["avg_confidence"]
    conf_bar = "█" * int(conf // 10) + "░" * (10 - int(conf // 10))
    conf_label = "Excellent" if conf >= 80 else "Good" if conf >= 60 else "Fair" if conf >= 40 else "Low"

    print(f"\n  {'─'*44}")
    if label:
        print(f"  📄 {label}")
    print(f"  {'─'*44}")
    print(f"  File       : {result['file']}")
    print(f"  Image size : {result['size']}  |  Mode: {result['mode']}")
    print(f"  Words found: {result['word_count']}")
    print(f"  Confidence : [{conf_bar}] {conf}%  ({conf_label})")
    print(f"\n  📝 Extracted Text:")
    print(f"  {'·'*44}")
    for line in result["raw_text"].splitlines():
        if line.strip():
            print(f"  {line}")
    print(f"  {'·'*44}")


# ─────────────────────────────────────────
#  STEP 4 — Save output to a text file
# ─────────────────────────────────────────

def save_output(results: list, output_file: str = "ocr_output.txt"):
    """Save all extracted text results to a .txt file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"OCR Results — Generated: {timestamp}\n")
        f.write("=" * 50 + "\n\n")
        for r in results:
            if "error" not in r:
                f.write(f"File: {r['file']}\n")
                f.write(f"Confidence: {r['avg_confidence']}%\n")
                f.write(f"Extracted Text:\n{r['raw_text']}\n")
                f.write("-" * 50 + "\n\n")
    print(f"\n  💾 Results saved to: {output_file}")


# ─────────────────────────────────────────
#  STEP 5 — Interactive mode
# ─────────────────────────────────────────

def interactive_mode():
    """Let the user provide their own image for OCR."""
    print("\n" + "═" * 48)
    print("  🖼️  Try Your Own Image")
    print("  Supported: PNG, JPG, JPEG, BMP, TIFF")
    print("═" * 48)
    path = input("\n  Enter image path (or press Enter to skip): ").strip()
    if not path:
        print("  Skipped.\n")
        return
    result = run_ocr(path)
    display_result(result, label="Your Image")


# ─────────────────────────────────────────
#  MAIN — Run all sample images
# ─────────────────────────────────────────

def main():
    print(BANNER)

    # ── Sample images to process ──────────
    sample_images = [
        ("img1.jpg",    "Img1"),
        ("img2.png",   "Img2"),
        ("img3.png", "Img3"),
    ]

    print("  📂 Processing sample images...\n")

    all_results = []

    for path, label in sample_images:
        print(f"  ⏳ Running OCR on: {path}")
        result = run_ocr(path)
        display_result(result, label=label)
        all_results.append(result)

    # ── Summary ───────────────────────────
    valid = [r for r in all_results if "error" not in r]
    if valid:
        avg = sum(r["avg_confidence"] for r in valid) / len(valid)
        total_words = sum(r["word_count"] for r in valid)
        print(f"\n{'═'*48}")
        print(f"  📊 SUMMARY")
        print(f"{'═'*48}")
        print(f"  Images processed : {len(valid)}")
        print(f"  Total words found: {total_words}")
        print(f"  Avg confidence   : {round(avg, 1)}%")
        print(f"{'═'*48}")

    # ── Save results ──────────────────────
    save_output(all_results)

    # ── Interactive mode ──────────────────
    interactive_mode()

    print("\n  ✅ OCR Recognition Complete! 🏁\n")


if __name__ == "__main__":
    main()