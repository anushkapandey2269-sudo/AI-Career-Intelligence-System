from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode(text)


def semantic_match(resume_text, job_text):
    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(job_text)

    score = cosine_similarity([emb1], [emb2])[0][0]
    return round(score * 100, 2)