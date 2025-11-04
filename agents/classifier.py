from config import client, GOOGLE_MODEL

async def classify_document(text: str) -> str:
    """Classifies a document based on its content using Gemini."""
    prompt = f"Classify this document as bill, discharge_summary, or id_card:\n{text[:1000]}"
    response = client.GenerativeModel(GOOGLE_MODEL).generate_content(prompt)
    return response.text.strip().lower()
