from pathlib import Path
from sentence_transformers import SentenceTransformer

model_name = "all-MiniLM-L6-v2"

PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / model_name

model = SentenceTransformer(model_name)

model.save(str(MODEL_PATH))