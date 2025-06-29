from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import tool

@tool("read_blood_report")
def read_blood_report(path: str = "data/sample.pdf") -> str:
    """Reads and summarizes a blood test report PDF from the given path."""
    try:
        docs = PyPDFLoader(file_path=path).load()
        return "\n".join(doc.page_content.replace("\n\n", "\n") for doc in docs)
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
