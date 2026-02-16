from nltk.stem import SnowballStemmer #PorterStemmer
from nltk.tokenize import word_tokenize

# stemmer = PorterStemmer()
stemmer = SnowballStemmer("english")
String_for_stemming = """
The crew of USS Discovery discovered many discoveries
Discovering is what explorers do.
"""
words = word_tokenize(String_for_stemming)

print(words)

Stemmed_words = [stemmer.stem(word) for word in words]

print (Stemmed_words)