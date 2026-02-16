## What is NLP
Natural Language Processing (NLP) is a broad field of Artificial Intelligence that aims to enable computers to understand, interpret, and generate human language.

Most of the data analyzed today is unstructured data. This type of data often contains human-readable text such as documents, emails, reports, or social media posts. Before it can be analyzed by a computer, it must go through several important steps:
* Start with unstructured text data
* Preprocess and clean the data
* Analyze it programmatically using algorithms and NLP techniques

NLP tools such as NLTK (Natural Language Toolkit) help perform these tasks efficiently by providing methods for text preprocessing, tokenization, stemming, lemmatization, and more
## What Is Tokenization and Why It Matters
Tokenization is a convenient way to split text into smaller units, such as words or sentences. This allows us to work with smaller pieces of text that are still coherent and meaningful.

### Types of Tokenization

**Word Tokenization**: This splits the text into individual words (a word being a basic unit of natural language). It helps you identify which words appear multiple times in the text and analyze word frequency.

**Sentence Tokenization**: This splits the text into sentences. It helps analyze how words are related to one another and provides more context for understanding the meaning of the text.

* To perform tokenization using NLTK you can run the following code:
```
python learn_nltk_tokenization_nlp.py
```
## Stopwords in NLP
Stopwords are common words in a language( such as the, is, and, in , of ) that usually carry a little meaningfull information in many NLP tasks.
* In traditional NLP approaches like Bag-of-words and TF-IDF , stops words are often removed to
    * Reduce noise
    * Decrease dimensionality and
    * Improve model performance.
  * For example: " The patient is in the hospital for a liver examination" after removing stopwords it becomes: "patient hospital liver examination"

*
