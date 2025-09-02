import spacy
import string

# Load the spacy model
# Note: The model needs to be downloaded first using:
# python -m spacy download en_core_web_sm
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Spacy model 'en_core_web_sm' not found. Please run 'python -m spacy download en_core_web_sm'")
    nlp = None

def preprocess_text(text):
    """
    Cleans, tokenizes, and lemmatizes text.

    Args:
        text: The input text as a string.

    Returns:
        A list of lemmatized tokens.
    """
    if nlp is None:
        return []

    # Remove punctuation from the text before processing with Spacy
    # This can sometimes help with more accurate tokenization
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Process the text with Spacy
    doc = nlp(text)

    # Lemmatize and remove stopwords and punctuation
    lemmatized_tokens = [
        token.lemma_.lower().strip()
        for token in doc
        if not token.is_stop and not token.is_punct and token.lemma_.strip()
    ]

    return lemmatized_tokens

def clean_text(text):
    """
    A more general text cleaning function.
    - Converts to lowercase
    - Removes punctuation
    - Removes special characters (non-alphanumeric)
    - Removes extra whitespace
    """
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove special characters (allow letters and spaces)
    text = "".join(filter(lambda x: x.isalpha() or x.isspace(), text))

    # Remove extra whitespace
    text = " ".join(text.split())

    return text
