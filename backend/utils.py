import re
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already
nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """
    Clean email text for model prediction:
    - Lowercase
    - Remove URLs
    - Remove numbers
    - Remove punctuation
    - Remove stopwords
    """
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)               # remove links
    text = re.sub(r"\d+", "", text)                   # remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    text = " ".join([w for w in text.split() if w not in STOPWORDS])
    return text
