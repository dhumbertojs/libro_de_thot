import pdfplumber
import os

def extract_pdf_text(pdf_path, output_md="output.md"):
    all_pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            width = page.width
            # Split into left and right halves
            left_bbox = (0, 0, width/2, page.height)
            right_bbox = (width/2, 0, width, page.height)

            left_text = page.crop(left_bbox).extract_text() or ""
            right_text = page.crop(right_bbox).extract_text() or ""

            # Join columns: left before right
            page_text = (left_text + "\n" + right_text).strip()
            all_pages.append(page_text)

    # Save as Markdown
    with open(output_md, "w", encoding="utf-8") as f:
        for i, page in enumerate(all_pages, start=1):
            f.write(f"# Página {i}\n\n")
            f.write(page)
            f.write("\n\n---\n\n")  # page separator

    print(f"Texto extraído a {output_md}")
    return all_pages

extract_pdf_text("original/EL_LIBRO_de_THOTH_COMPLETO.pdf")