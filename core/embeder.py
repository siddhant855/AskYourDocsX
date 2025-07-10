from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    return model.encode(
        chunks,
        show_progress_bar=True,
        # convert_to_tensor=True
    )
