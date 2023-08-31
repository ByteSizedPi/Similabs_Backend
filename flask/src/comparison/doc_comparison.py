import base64
import io
from difflib import SequenceMatcher

import numpy as np
from docx import Document
from PIL import Image


def docx_to_html(docx):
    fullText = []
    for para in Document(docx).paragraphs:
        fullText.append(para.text)
    return "\n".join(fullText)


def sim(docx1, docx2):
    tokens1 = docx_to_html(docx1).split()
    tokens2 = docx_to_html(docx2).split()
    matrix = np.zeros((len(tokens1), len(tokens2)))
    for i, token1 in enumerate(tokens1):
        for j, token2 in enumerate(tokens2):
            matrix[i][j] = SequenceMatcher(None, token1, token2).ratio()
    # img = Image.fromarray(matrix * 255).convert("RGB")
    # buffered = io.BytesIO()
    # img.save(buffered, format="PNG")

    # # Convert BytesIO to Base64 string
    # img_str = base64.b64encode(buffered.getvalue()).decode()
    return matrix.tolist()
