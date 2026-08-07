import fitz

from langchain_core.documents import Document

from utils.clean_text import clean_text


def load_pdf(file_path: str):

    documents = []

    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf):

        text = page.get_text()

        text = clean_text(text)

        if text.strip():

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "page": page_number + 1
                    }
                )
            )

    pdf.close()

    return documents