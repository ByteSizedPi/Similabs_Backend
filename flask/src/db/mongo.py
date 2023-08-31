from analysis.analysis import get_metadata
from pymongo import MongoClient


def get_all_documents():
    corpus = MongoClient("mongodb://localhost:27017/")["Similabs"]["corpus"]
    return corpus.find({})


def push_corpus(file):
    corpus = MongoClient("mongodb://localhost:27017/")["Similabs"]["corpus"]
    try:
        doc = get_metadata(file)
        result = corpus.insert_one(doc)
        file_name = str(result.inserted_id) + ".docx"
        return file_name
    except Exception as e:
        print(e)
        return False
