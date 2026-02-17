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

* However in modern deep learning models such as transformer-based architetures (e.g. , BERT, GPT) stopwords are usually not removed, because these models rely on full sentence context to understand meaning. Removing words like not could completely change the interpertation of a sentence.
* To remove the stopwords run the following code:
```
python filtering_stopwords.py
```
## Stemming in NLP
Stemming is a text processing technique using in NLP to redude words to their base or root form. It removes suffixes such as : -ing, ed, er, s, and -ly to group related words under common root.
* For example :
  * helping to help
  * helped to help
  * helper to help
  * studying - study
* The aim of the stemming is to reduce vocaburaly size and treat similar words as the same feature. which is espicially useful in traditional machine learning approaches like Bag-of_Words and TF-IDF
### Why use stemming
* To reduce dimensionality
* To improve model generalization
* Sppeds up computation
### Porter Stemmer
One commonly used stemming algorithm is the Porter Stemming Algorithm, which applies rule-based transformations to remove common suffixes.
* Limitations of this:
   * May produce non dictionary word
   * Does not consider grammar or context
### Stemming overestimation and understimation
* **Stemming underestimation** occurs when two related words that are expected to reduce to the same root form fail to do so. This is False negative
* **Stemming overestimation** happens when two unrelated words are reduced to the same root. This results in a false positive.,
* To to perform stemmization run the following code:   ` python learn_stemming.py`

## Tagging Part of Speech (POS)
Part of Speech is important in NLP because it helps a computer to understand the grammatical rolo of each word in a sentence: whether word is noun, pronoun, verb, adjective, adverb , etc.
Without POS tagging, text is just a sequence of words.  With POS tagging the system understand the structure and meaning better.
### What is POS Tagging?
POS tagging assigns a grammatical label to each word in a sentence
* Example: "she is reading a book."
   * she : Pronoun
   * is : verb
   * reading: verb
   * a : determinant
   * book : noun
* **Example of Part of Speech**
  |Part of Speech | Role |  Examples |
  |---------------|---------|-----------|
  | Noun        | person, place, thing | mountain, bagel, Poland|
  | Pronoun   | Replaces noun | you, she, we |
  | Adjective | Gives information about what a noun is like | efficient, windy, colorful |
  | Verb  | Is an action or state of being | learn , is, go |
  | Adverb | Gives an information about verb, adjective, or another adverb | efficiently, always, very|
  | Preporsition | Gives an information about how a noun  or pronoun is connected to another word | from, about, at |
  | Conjunction | Connects two other words or sentence | so, because, and |
  | Interjection | Is an exclamation | yay, wow, ow |

  * To exercise with tagging Part of Speech run the following code: `python tagging_part_of_speech.py`



