from pathlib import Path
from typing import List

file_path = "C:\\Users\\HP\\IdeaProjects\\KROC_mini\\.idea\\text_files\\sample_text.txt"

def read_text_file(path: str = file_path) -> str:
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"No file found at {path}")
    return p.read_text(encoding="utf-8")

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    if chunk_size <= overlap:
        raise ValueError("Chunk size must be greater than overlap")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks