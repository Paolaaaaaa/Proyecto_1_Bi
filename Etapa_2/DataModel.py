from pydantic import BaseModel
from sklearn.pipeline import Pipeline
from sklearn.pipeline import Pipeline
from joblib import dump
class DataModel(BaseModel):
    review_es: str


def columns(self):
        return ["review_es"]


 def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    return [x.lower() for x in words]

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', ' ', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = num2words(word, lang = 'es_CO')
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    stopword_es = nltk.corpus.stopwords.words('spanish')
    new_words = []

    for word  in words:
        if word not in stopword_es:
            new_words.append(word)
    return new_words
    
def preprocessing(words):
    words = to_lowercase(words)
    words = replace_numbers(words)
    words = remove_punctuation(words)
    words = remove_non_ascii(words)
    words = remove_stopwords(words)
    return words



def generate_pipeLine():

    pipeline = Pipeline(
        [
            ('preprocessing',FunctionTransformer(preprocessing))
            ('scaler', CountVectorizer()),
            ('model', LogisticRegression())
        ]
    )
    pipeline.fit(x_train_m2, y_train_m2)
    dump(pipeline, 'modelo.joblib')



def use_pipeline(movie):
    filename = 'modelo.joblib'
    df_recent = pd.read_csv('./data/'+movie+'.csv', sep=',', encoding = 'utf-8') # Lectura de los datos recientes
    pipeline = joblib.load(filename)
    y_predicted =  pipeline.predict(df_recent)
    return y_predicted

