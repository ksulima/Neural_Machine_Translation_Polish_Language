# Unsupervised methods to NLP Polish language

## Introduction


This project is dedicated to unsupervised methods of text data transformation. The representation of text in such transformed form is inherent part of Natural Language Processing (NLP) and allows to consume unstructured data by various deep learning algorithms.

If NLP is a new term for you and sounds a bit mysterious, Yoav Goldberg in his [book](https://www.amazon.com/Language-Processing-Synthesis-Lectures-Technologies/dp/1627052984) describes it as:

>_Natural language processing (NLP) is a collective term referring to automatic computational processing of human languages. This includes both algorithms that take human-produced text as input, and algorithms that produce natural looking text as outputs._

NLP embraces wide range of tasks e.g. named entity recognition, sentiment analysis, automatic summarization, natural language generation and many more. Each one is a subject for separate project and could be thoroughly studied. 


Two tested methods in this project are **Unsupervised Word Segmentation into Subword Units** and **GloVe embeddings trained on our own corpus**.

I intentionally choose Polish language text to be analyzed, what I elaborate below, but be aware that the methods used are applicable to any language and text data.


## Dataset
Dataset comes from [PolEval competition](http://poleval.pl/tasks/task6). It contains tweets collected from openly available Twitter discussions. Original goal is to distinguish between normal/non-harmful tweets and tweets that contain any kind of harmful information. This includes cyberbullying, hate speech, personal threats, accumulation of vulgarities, profane language and related phenomena. 


Example of tweets with normal content:<br>
"Czerwone Gitary, Historia jednej znajomości... i parawany które istniały zawsze…"

Example of tweets with harmful content:<br>
"Ja mam dla ciebie lepszą propozycję : powieś się gdzieś pod lasem UB-ecka gnido ."<br>
"macie jej numer zdissujcie ją"

#### Why is NLP for Polish language difficult?

The grammar of the Polish language is characterized by a high degree of inflection, and has relatively free word order. There are no articles, and there is frequent dropping of subject pronouns. Distinctive features include the different treatment of masculine personal nouns in the plural, and the complex grammar of numerals and quantifiers.

The morphology of the Polish language is highly complex. Alternations affects nouns, adjectives, verbs, and other parts of speech. 

To give you an example let's list all possibilities of some word in two languages:<br>

**in English:**<br>
_two, second_<br>

**in Polish:**<br>
_drugiej, drudzy, dwiema, drugimi, dwojgiem, dwaj, drugie, drugiemu, dwojga, dwa, drugiego, dwójką, drugim, druga, dwoma, dwóch, dwojgu, dwójko, drugi, drugą, dwom, dwójce, dwoje, dwójki, drugich, dwójkę, dwie, dwójka_

Syntax is also not trivial. Polish is a synthetic language, it is possible to move words around in the sentence, which often leads to different interpretations of the meaning.

Polish verbs have the grammatical category of aspect. Each verb is either imperfective, meaning that it denotes continuous or habitual events, or perfective, meaning that it denotes single completed events.

Adjectives agree with the noun, they modify in terms of gender, number and case. 

There are various types of sentence in Polish that do not have subjects e.g. sentences formed from certain verbs that can appear without a subject, corresponding to an English impersonal "it", as in _padało_ ("it was raining/snowing").


## Unsupervised Word Segmentation into Subword Units
ToDo description

## GloVe embeddings trained on our own corpus
ToDo description
