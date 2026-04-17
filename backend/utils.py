import nltk
from nltk import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# # load vectorizer
tk = pickle.load(open("model/vectorizer.pkl", "rb"))


nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

def text_preprocessing(text):

    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text = re.sub(r'<.*?>', '', text)

    tokens = word_tokenize(text)
    stop_words = stopwords.words('english')

    tokens = [t for t in tokens if t not in stop_words]

    ps = PorterStemmer()
    tokens = [ps.stem(t) for t in tokens]

    text = ' '.join(tokens)
   
    X = tk.transform([text])

    return X