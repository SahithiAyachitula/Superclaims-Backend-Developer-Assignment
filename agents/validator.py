import json
from config import client, GOOGLE_MODEL

async def validate_documents(docs: list) -> dict:
    """Validates documents for missing or inconsistent data."""
    prompt = f"""
    Validate these claim documents for missing or inconsistent data.
    Return valid JSON like:
    {{
      "missing_documents": [],
      "discrepancies": []
    }}

    Documents:
    {json.dumps(docs, indent=2)}
    """
    response = client.GenerativeModel(GOOGLE_MODEL).generate_content(prompt)
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {"missing_documents": [], "discrepancies": ["Validation failed"]}
