from nltk.tokenize import word_tokenize

lotr_quote = " It's dangerous business, Fordo, going out your door."

words_in_lotr_quote = word_tokenize(lotr_quote)

import nltk
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()

grammar = """
Chunk: {<.*>+}   # include everything
       }<JJ>{    # exclude adjectives
"""

chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()