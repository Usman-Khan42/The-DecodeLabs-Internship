🔍 OCR Text Recognition — Python Project
---

##  📌 What This Project Does

This program takes image files (PNG, JPG, etc.) and **reads the text inside them** using a pre-trained OCR (Optical Character Recognition) model.

---

##  Expected output

```
╔══════════════════════════════════════════════╗
║        🔍  OCR TEXT RECOGNITION TOOL        ║
║     Powered by Tesseract + pytesseract       ║
╚══════════════════════════════════════════════╝

  ⏳ Running OCR on: sample1_simple.png

  ────────────────────────────────────────────
  📄 Sample 1 — Simple Text
  ────────────────────────────────────────────
  File       : sample1_simple.png
  Image size : 520 x 158 px  |  Mode: RGB
  Words found: 6
  Confidence : [█████████░] 94.3%  (Excellent)

  📝 Extracted Text:
  ············································
  Hello, World!
  This is OCR recognition.
  ············································

  📊 SUMMARY
  Images processed : 3
  Total words found: 24
  Avg confidence   : 94.4%
```

---

## 🔑 Key Functions

| Function | What it does |
|----------|-------------|
| `preprocess_image(path)` | Loads and cleans the image for better OCR |
| `run_ocr(path)` | Runs Tesseract and returns text + confidence data |
| `display_result(result)` | Prints results in a clean, readable format |
| `save_output(results)` | Writes all extracted text to `ocr_output.txt` |
| `interactive_mode()` | Lets the user test their own image at runtime |

---

## 🧪 OCR Engine Settings Explained

```python
pytesseract.image_to_string(img, config="--oem 3 --psm 6")
```

| Flag | Value | Meaning |
|------|-------|---------|
| `--oem` | `3` | Engine mode: use the best available (LSTM neural net) |
| `--psm` | `6` | Page segmentation: treat as a single block of text |

Other useful `--psm` values:
- `psm 11` → sparse text, no assumed layout
- `psm 7` → single line of text
- `psm 4` → single column of text

---

## 📦 Libraries Used

| Library | Purpose |
|---------|---------|
| `pytesseract` | Python wrapper for the Tesseract OCR engine |
| `Pillow (PIL)` | Image loading, preprocessing (grayscale, contrast, sharpen) |
| `os` | File path handling |
| `datetime` | Timestamp for saved output file |

### Pre-trained model used
**Tesseract OCR** — open-source engine developed by Google, trained on millions of text samples. The `--oem 3` flag uses its built-in **LSTM (Long Short-Term Memory) neural network**, which is the most accurate mode.