import os
from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm

# ==========================
# CONFIG
# ==========================
PDF_PATH = "original/EL_LIBRO_de_THOTH_COMPLETO.pdf"
OUTPUT_FILE = "imagenes_85_160.md"
START_PAGE = 85
END_PAGE = 160
LANGUAGE = "spa"  # Spanish OCR

# ==========================
# OCR PROCESS
# ==========================

print("Converting PDF pages to images...")
pages = convert_from_path(
    PDF_PATH,
    dpi=300,
    first_page=START_PAGE,
    last_page=END_PAGE
)

print("Running OCR...")
full_text = ""

for i, page in enumerate(tqdm(pages)):
    text = pytesseract.image_to_string(page, lang=LANGUAGE)
    full_text += f"\n\n# Página {START_PAGE + i}\n\n"
    full_text += text

print("Saving output...")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(full_text)

print("Done")