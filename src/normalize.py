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


# the model
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
structured_llm = llm.with_structured_output(NoteV1)

# a messy note
note = "Patient reports dizziness and headache after lunch. Blood pressure was either 130/85 or 160/100 according to different readings. Patient thinks they took amlodipine but is not certain.."
# note = "Patient had a dizzy spell in the afternoon. BP was checked but the reading is not available. Medication history is unclear. Patient denies knowing whether they took their morning medication."
# the instructions
prompt = f"""Turn this caregiver note into structured data.
Never guess. If something is missing, write "unknown", give a low confidence (0 to 1),
and add a question to clarifications_needed.

Note: {note}"""

result = structured_llm.invoke(prompt)
print(result.model_dump_json(indent=2))