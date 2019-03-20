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


Polish language is recognized to be among the most difficult languages to learn. This implies challenges for both humans and NLP methods, who tries to understand this language. So what makes Polish language particularly difficult?


## Unsupervised Word Segmentation into Subword Units
ToDo description

## GloVe embeddings trained on our own corpus
ToDo description
