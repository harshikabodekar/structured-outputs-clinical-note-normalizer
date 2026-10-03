from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI


class NoteV1(BaseModel):
    symptoms: str
    symptoms_confidence: float
    bp_reading: str
    bp_confidence: float
    medication: str
    medication_confidence: float
    clarifications_needed: list[str]


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
structured_llm = llm.with_structured_output(NoteV1)


def normalize(note):
    prompt = f"""Turn this caregiver note into structured data.
Never guess. If something is missing, write "unknown", give a low confidence (0 to 1),
and add a question to clarifications_needed.

Note: {note}"""
    return structured_llm.invoke(prompt)