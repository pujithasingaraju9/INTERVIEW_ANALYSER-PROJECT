from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_answer(user_answer, ideal_answer):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user_answer, ideal_answer])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return score