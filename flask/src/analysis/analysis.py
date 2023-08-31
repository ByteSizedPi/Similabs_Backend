from docx import Document
from werkzeug.utils import secure_filename


def get_metadata(file) -> dict[str, str]:
    document = Document(file)
    p = document.core_properties
    return {
        "filename": secure_filename(file.filename),
        "metadata": {
            "author": p.author,
            "category": p.category,
            "comments": p.comments,
            "content_status": p.content_status,
            "created": p.created.isoformat() if p.created else None,
            "identifier": p.identifier,
            "keywords": p.keywords,
            "language": p.language,
            "last_modified_by": p.last_modified_by,
            "last_printed": p.last_printed.isoformat() if p.last_printed else None,
            "modified": p.modified.isoformat() if p.modified else None,
            "revision": p.revision,
            "subject": p.subject,
            "title": p.title,
            "version": p.version,
        },
    }
