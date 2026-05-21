from fastembed import TextEmbedding
import numpy as np

model = TextEmbedding()

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def semantic_chunk(sentences, threshold=0.75):
    chunks = []
    current = [sentences[0]]

    emb_prev = next(model.embed([sentences[0]]))

    for s in sentences[1:]:
        emb = next(model.embed([s]))

        if cosine(emb_prev, emb) > threshold:
            current.append(s)
        else:
            chunks.append(" ".join(current))
            current = [s]

        emb_prev = emb

    chunks.append(" ".join(current))
    return chunks