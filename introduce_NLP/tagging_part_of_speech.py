import nltk
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
sagan_quote ='''
If you wish to make an apple pie from scratch , you must first invent the universe.
'''
words_in_sagan_quote = word_tokenize(sagan_quote)

print(words_in_sagan_quote)
### tagging part of speech 

tagged_pos_in_sagan_quote = nltk.pos_tag(words_in_sagan_quote)

print(tagged_pos_in_sagan_quote)