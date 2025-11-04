# Superclaims-Backend-Developer-Assignment

Overview

The Claim Document Processor is an AI-powered FastAPI backend that automates insurance claim document handling.
It accepts multiple PDFs (e.g., bill, ID card, discharge summary), classifies them using a Google Gemini LLM, extracts structured information, validates data consistency, and returns a final claim decision (approve/reject) in JSON format.

Project Architecture
claim-processor/
│
├── main.py                          # FastAPI app with /process-claim endpoint
│
├── agents/
│   ├── classifier.py                # Classifies PDFs (bill, ID, discharge summary)
│   ├── extractor.py                 # Extracts structured data from text
│   ├── processors.py                # Handles logic per document type
│   └── validator.py                 # Validates data consistency and completeness
│
├── utils/
│   └── pdf_parser.py                # Extracts raw text from PDFs using PyPDF2
│
├── config.py                        # API keys and model configuration
├── requirements.txt                 # Dependencies
└── README.md                        # Documentation

Logic Flow
1️.Upload & Parsing
User uploads multiple PDF files via /process-claim endpoint.
Each PDF’s text is extracted using PyPDF2 in utils/pdf_parser.py.

2️.Classification (LLM Agent)
The Classifier Agent uses Google Gemini to determine document type.
It analyzes text context or filename to classify as bill, id_card, or discharge_summary.

3️.Extraction (LLM Agent)
Based on classification, the Extractor Agent uses Gemini to extract key fields.
Example: for bills → hospital name, date, amount; for discharge summaries → diagnosis, admission/discharge dates.

4️.Validation
The Validator Agent checks if all required document types exist and whether dates/fields are consistent.
Missing or mismatched data triggers a “rejected” decision.

5️.Response
Returns structured JSON

I have used ChatGPT as an AI tool the example prompts are:

1. Hey Please check this requirement and quicly summarize this for me (it gave me the quick summary)
2. Now could you please tell me  how do I proceed further using Fast API and Google Gemini LLM for this task? (it gave me a project structure)
