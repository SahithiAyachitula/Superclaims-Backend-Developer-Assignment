from fastapi import FastAPI, UploadFile, File
from typing import List
from agents.processors import process_claim

app = FastAPI(title="Claim Document Processor")

@app.post("/process-claim")
async def process_claim_endpoint(files: List[UploadFile] = File(...)):
    """Main API endpoint: processes multiple claim-related PDFs."""
    result = await process_claim(files)
    return result
