from pydantic import BaseModel
import re, string, unicodedata
from num2words import num2words
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.preprocessing import FunctionTransformer
import pandas as pd
import nltk
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import dump
class DataModel(BaseModel):
    review_es: str


def columns(self):
        return ["review_es"]


def use_pipeline(movie):
    filename = 'modelo.joblib'
    df_recent = pd.read_csv('./data/'+movie+'.csv', sep=',', encoding = 'utf-8') # Lectura de los datos recientes
    pipeline = dump.load(filename)
    y_predicted =  pipeline.predict(df_recent)
    return y_predicted



