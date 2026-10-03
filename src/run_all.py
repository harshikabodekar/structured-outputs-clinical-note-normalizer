import json
import time
from normalize import normalize
from notes import NOTES

results = []
valid = 0

for kind, note in NOTES:
    try:
        result = normalize(note)
        results.append({"type": kind, "note": note, "output": result.model_dump()})
        valid += 1
    except Exception as e:
        results.append({"type": kind, "note": note, "error": str(e)})
    time.sleep(1)

with open("data/results_v1.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"{valid}/{len(NOTES)} notes converted to valid JSON")