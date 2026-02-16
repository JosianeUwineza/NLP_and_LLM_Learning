import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from  nltk.tokenize import word_tokenize

worf_quote = 'Sir, I protest. I am not a merry man'
words_in_quote = word_tokenize(worf_quote)

print('Before stopwords remove')
print (words_in_quote)
stop_words = set(stopwords.words('english'))
print('English stopwords ')
print(stop_words)
filtered_list = []

for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

print('------------------Filtered words')
print(filtered_list)