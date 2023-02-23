import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import yake
import pdf_to_text

def compute_cosine_similarity(text1,text2):
    list_text = [text1,text2]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectorizer.fit_transform(list_text)
    tfidf_text1, tfidf_text2 = vectorizer.transform([list_text[0]]), vectorizer.transform([list_text[1]])

    cs_score = cosine_similarity(tfidf_text1, tfidf_text2)

    return np.round(cs_score[0][0],2)

def fetch_keywords(context,max_ngram_size = 1,deduplication_threshold = 0.1,
                   numOfKeywords = 5,language = "en"):
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(context)
    print(keywords)
    keywords = ",".join([key for key, score in keywords])
    return keywords