from docx import Document

def replace_iterating_paragraphs(doc: Document, replace_map: dict[str, str]) -> Document:
    for para in doc.paragraphs:
        for run in para.runs:
            for k, v in replace_map.items():
                if k in run.text:
                    run.text = run.text.replace_iterating_paragraphs(k, v)
    return doc