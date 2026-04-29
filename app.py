from src.extractor import extract_text_from_pdf
from src.qa_system import DocumentQA

# Load PDF
pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(pdf_path)

# Initialize QA system
qa = DocumentQA(text)

print("📄 Document QA System (type 'exit' to quit)")

while True:
    query = input("\nAsk a question: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    answer = qa.get_answer(query)
    print("Answer:", answer)