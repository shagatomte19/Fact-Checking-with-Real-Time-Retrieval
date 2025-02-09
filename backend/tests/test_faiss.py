import faiss
import numpy as np

def test_faiss_store_and_retrieve():
    d = 128  # Feature vector size
    index = faiss.IndexFlatL2(d)  # FAISS L2 index
    assert index.is_trained

    # Add fake data
    vectors = np.random.rand(10, d).astype("float32")
    index.add(vectors)

    # Search a random query
    query = np.random.rand(1, d).astype("float32")
    distances, indices = index.search(query, k=5)

    assert len(indices[0]) == 5
    assert isinstance(indices[0][0], int)
