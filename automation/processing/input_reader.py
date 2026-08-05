from pathlib import Path
from typing import Dict

from pypdf import PdfReader


def read_pdf(path: Path) -> Dict[str, object]:
    reader = PdfReader(str(path))
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        pages.append({"page": page_number, "text": page.extract_text() or ""})
    return {"filename": path.name, "pages": pages}


def read_text_files(directory: Path) -> Dict[str, str]:
    return {
        path.name: path.read_text(encoding="utf-8")
        for path in sorted(directory.glob("*.md"))
    }
