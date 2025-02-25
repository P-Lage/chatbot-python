import nltk
import string
from nltk.corpus import stopwords

# Certifique-se de ter baixado os recursos do NLTK:
# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_text(text):
    # Converter para minúsculas
    text = text.lower()
    # Tokenizar o texto
    tokens = nltk.word_tokenize(text)
    # Remover pontuações e stopwords
    tokens = [word for word in tokens if word not in string.punctuation]
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens
