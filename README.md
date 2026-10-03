# Clinical Note Normalizer

Turn messy nurse/caregiver notes into **clean, structured JSON** — without guessing missing information.

## Overview

Clinical notes written by nurses or caregivers can be short, informal, incomplete, or ambiguous. This project uses an LLM with **structured outputs and validation** to convert these notes into a consistent JSON format.

Instead of inventing missing information, the system identifies uncertainty and adds clarification questions to `clarifications_needed`.

### Example

**Input**

```text
pt had dizzy spell after lunch, bp maybe high?? took meds, not sure which
```

**Output**

```json
{
  "symptoms": "dizzy spell after lunch",
  "symptoms_confidence": 0.9,
  "bp_reading": "maybe high",
  "bp_confidence": 0.3,
  "medication": "unknown",
  "medication_confidence": 0.1,
  "clarifications_needed": [
    "What was the exact blood pressure reading?",
    "Which medication was taken?"
  ]
}
```

The system keeps uncertain information uncertain instead of making up values.

---

## How It Works

```text
Messy Clinical Note
        ↓
Prompt + Pydantic Schema
        ↓
       LLM
        ↓
Structured Output
        ↓
    Validation
        ↓
 ┌───────────────┐
 │               │
Valid         Missing/Unclear
 │               │
 ↓               ↓
Confidence     Clarification
Scoring        Questions
 │               │
 └───────┬───────┘
         ↓
      JSON Output
```

---

## Key Features

### Structured Outputs

Uses a **Pydantic schema** with LangChain's `with_structured_output()` to ensure the LLM returns data in the expected structure.

### Validation

The extracted information is validated against the defined schema so malformed or unexpected output does not pass through as valid data.

### Confidence Scores

Each important field includes a confidence score representing how certain the extraction is.

For example:

```json
{
  "symptoms": "dizziness and headache",
  "symptoms_confidence": 0.95,
  "bp_reading": "unknown",
  "bp_confidence": 0.1
}
```

### Clarification Detection

When information is missing or unclear, the system generates questions instead of guessing.

```json
"clarifications_needed": [
  "What is the exact blood pressure reading?",
  "Which medication was taken?"
]
```

### Schema Versioning

The project is designed to support schema evolution:

```text
Schema v1
   ↓
Schema v2
   ↓
Future versions
```

This makes it possible to add or modify fields without losing track of which schema version produced an output.

---

## Tech Stack

* **Python**
* **LangChain**
* **Google Gemini**
* **Pydantic**
* **Structured Outputs**
* **Git / GitHub**

---

## Project Structure

```text
structured-outputs-clinical-note-normalizer/
│
├── README.md
│
└── src/
    ├── normalize.py
    └── requirements.txt
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd structured-outputs-clinical-note-normalizer
```

### 2. Install dependencies

```bash
pip install -r src/requirements.txt
```

### 3. Configure your API key

Set your Google Gemini API key in your environment.

For example:

```text
GOOGLE_API_KEY=your_api_key_here
```

**Do not commit API keys or `.env` files to GitHub.**

### 4. Run the normalizer

```bash
python src/normalize.py
```

---

## Testing

The system is tested using synthetic noisy clinical notes covering different levels of completeness and uncertainty.

Example test cases include:

### Complete information

```text
Patient reports a headache since this morning. Blood pressure is 128/82 mmHg. Patient took paracetamol 500 mg at 10 AM.
```

### Missing information

```text
Patient felt dizzy after breakfast. Blood pressure was high. Patient took something for the dizziness but cannot remember the name.
```

### Conflicting information

```text
Patient reports dizziness and headache after lunch. Blood pressure was either 130/85 or 160/100 according to different readings. Patient thinks they took amlodipine but is not certain.
```

### Very vague information

```text
Dizzy after lunch. BP high. Took medicine.
```

These cases test whether the system can distinguish between **known, unknown, and uncertain information**.

---

## Project Goals

The project is considered complete when it can:

* [x] Convert messy notes into structured JSON
* [x] Use a Pydantic schema for structured output
* [x] Generate field-level confidence scores
* [x] Identify missing or ambiguous information
* [x] Generate clarification questions
* [ ] Convert 20+ synthetic noisy notes into valid JSON
* [ ] Add a dedicated validation layer
* [ ] Evaluate whether confidence scores reflect extraction quality
* [ ] Implement schema versioning
* [ ] Document Schema v1 → Schema v2
* [ ] Implement a clarification loop

---

## Development Stages

### Stage 1 — Schema + Basic Extraction

Define the Pydantic schema and successfully normalize the first clinical note.

### Stage 2 — Synthetic Dataset

Create 20+ synthetic noisy clinical notes representing different levels of completeness and ambiguity.

### Stage 3 — Validation + Confidence

Add validation and field-level confidence scoring to make the output more reliable and measurable.

### Stage 4 — Clarification Loop + Schema v2

Add a clarification workflow for incomplete notes and introduce a versioned schema for future changes.

---

## Why This Project?

The project combines two practical areas:

**Clinical information normalization**

Real-world caregiver and nursing notes are often informal and inconsistent. Converting them into structured information can make downstream processing easier.

**LLM structured outputs**

The project applies LangChain, Pydantic, and structured outputs to a practical problem rather than using an LLM only for free-form text generation.

---

## Important Note

This project is intended as an **educational and experimental prototype** using synthetic clinical notes.

It is **not a medical diagnostic system** and should not be used to make clinical decisions or replace professional medical judgment.

---

## Future Improvements

Potential extensions include:

* Persistent storage of normalized notes
* Better confidence calibration
* Automated evaluation against ground-truth annotations
* More robust handling of conflicting information
* Schema version migration
* Interactive clarification conversations
* Batch processing of clinical notes
* Audit logging for extracted information
* Support for additional clinical fields

---

## Status

**Current stage:** Stage 1 — Structured clinical note extraction

The core pipeline is working:

```text
Messy Note
    ↓
Gemini + Structured Output
    ↓
Pydantic Schema
    ↓
Confidence + Clarifications
    ↓
Structured JSON
```
