import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag


example_string = "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin, but by the content of their character."

#sent_tokenize(example_string)
#word_tokenize(example_string)
word_token = word_tokenize(example_string)
print(word_token)

sentz = sent_tokenize(example_string)
print(sentz)

#creating filtered list using stopwords
stop_words = set(stopwords.words("English"))

filtered_list =[word for word in word_token if word.casefold() not in stop_words ]

print(filtered_list)

#stemming

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in word_token]

print(stemmed_words)

#POS tagging

tagged_list = pos_tag(word_token)

print(tagged_list)

#Lemmetization

lemmatizer = WordNetLemmatizer()

lemm_words = [lemmatizer.lemmatize(word) for word in word_token]
print('lemmatized words =',lemm_words)

#chunking

grammar = "NP: {<DT>?<JJ>*<NN>}"

chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(tagged_list)
""" tree.draw() """

#similarly chinking is used to EXCLUDE patterns using outward faced curly braces in grammar

#NER

tree2 = nltk.ne_chunk(tagged_list)
tree2.draw()

example_string 


