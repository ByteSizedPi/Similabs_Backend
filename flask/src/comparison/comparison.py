import Levenshtein
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def jaccard(text1: str, text2: str) -> float:
    words1 = set(text1.split())
    words2 = set(text2.split())
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    return round(intersection / union, 4)


def levenshtein(text1: str, text2: str) -> float:
    return round(Levenshtein.ratio(text1, text2), 4)


def cosine(text1: str, text2: str) -> float:
    tfidf = TfidfVectorizer().fit_transform([text1, text2])
    return round(cosine_similarity(tfidf[0], tfidf[1])[0][0], 4)
