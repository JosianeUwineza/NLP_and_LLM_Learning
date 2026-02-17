import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer  = WordNetLemmatizer()

lemmatized_w = lemmatizer.lemmatize("scarves")

print(lemmatized_w)

string_lem = ' The friends of Desoto love scarves'
string_lem_words = word_tokenize(string_lem)
lemmatized_string = [lemmatizer.lemmatize(word) for word in string_lem_words]

print (lemmatized_string)