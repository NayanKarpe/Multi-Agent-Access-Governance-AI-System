from sentence_transformers import SentenceTransformer
import numpy as np

ST_MODEL_NAME = "all-MiniLM-L6-v2"

# Load once at startup
st_model = SentenceTransformer(
    ST_MODEL_NAME,
    local_files_only=True
)

def get_embedding(text):
    return st_model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True  # improves similarity search
    ).astype("float32")