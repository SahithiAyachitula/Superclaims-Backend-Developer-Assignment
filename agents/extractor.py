import json
from config import client, GOOGLE_MODEL

async def extract_fields(doc_type: str, text: str) -> dict:
    """Extracts structured data from document text using Gemini."""
    prompt = f"""
    You are an AI extraction agent. Extract structured JSON for this {doc_type} document.

    Examples:
    - bill: {{"type": "bill", "hospital_name": "XYZ", "total_amount": 1234, "date_of_service": "YYYY-MM-DD"}}
    - discharge_summary: {{"type": "discharge_summary", "patient_name": "John", "diagnosis": "Fever", "admission_date": "YYYY-MM-DD", "discharge_date": "YYYY-MM-DD"}}

    Document:
    {text}
    """
    response = client.GenerativeModel(GOOGLE_MODEL).generate_content(prompt)
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {"type": doc_type, "raw_text": text[:200]}
