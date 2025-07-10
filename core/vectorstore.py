import faiss
import numpy as np

class FaissVectorStore:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity search
        self.texts = []

    def add(self, embeddings, texts):
        # Ensure embeddings are float32
        embeddings = np.array(embeddings).astype('float32')
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=5):
        # Ensure query_embedding is float32 and 2D
        query_embedding = np.array(query_embedding).astype('float32')
        if query_embedding.ndim == 1:
            query_embedding = np.expand_dims(query_embedding, axis=0)

        # Ensure query_embedding matches the index dimension
        if query_embedding.shape[1] != self.dimension:
            raise ValueError(f"Query embedding dimension {query_embedding.shape[1]} does not match index dimension {self.dimension}")

        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for i, idx_list in enumerate(indices):
            for j, idx in enumerate(idx_list):
                if idx != -1:  # Check if a valid index was returned
                    results.append({"text": self.texts[idx], "distance": distances[i][j]})
        return results