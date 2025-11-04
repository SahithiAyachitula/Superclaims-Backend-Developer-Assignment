import asyncio
from utils.pdf_parser import extract_text_from_pdf
from agents.classifier import classify_document
from agents.extractor import extract_fields
from agents.validator import validate_documents

async def process_single_document(file):
    """Handles one PDF document: extract → classify → extract structured data."""
    text = await extract_text_from_pdf(file)
    doc_type = await classify_document(text)
    data = await extract_fields(doc_type, text)
    return data

async def process_claim(files):
    """Processes all uploaded PDFs asynchronously."""
    tasks = [process_single_document(f) for f in files]
    documents = await asyncio.gather(*tasks)
    validation = await validate_documents(documents)
    decision = await make_claim_decision(validation)
    return {
        "documents": documents,
        "validation": validation,
        "claim_decision": decision
    }

async def make_claim_decision(validation: dict) -> dict:
    """Determines final claim decision."""
    if not validation["missing_documents"] and not validation["discrepancies"]:
        return {
            "status": "approved",
            "reason": "All required documents present and data is consistent"
        }
    else:
        return {
            "status": "rejected",
            "reason": f"Issues found: {validation}"
        }

