# Unsupervised methods to NLP Polish language 
(description is still in progress)

#### Setup

If you wish to run code yourself, the easiest way is to use **Google Colab**. It provides ready to use enviroment with free GPU, python, keras and all packages already configured to run this code.

Here's how you can use it:

1. Open [https://colab.research.google.com](https://colab.research.google.com) click **Sign in** in the upper right corner, use your Google credentials to sign in.
2. Click **GITHUB** tab, paste https://github.com/ksulima/Unsupervised-method-to-NPL-Polish-language and press Enter
3. Choose the notebook you want to open, e.g. 01TextCleaning.ipynb
4. Click **File -> Save a copy in Drive...** to save your progress in Google Drive
5. If you need a GPU, click **Runtime -> Change runtime type** and select **GPU** in Hardware accelerator box
6. Download dataset from my [google drive](https://drive.google.com/drive/folders/1F41MZVPitnya9xE4goWDpw_wVHqqNxLG) or original source (described in paragraph Dataset) and upload it to your google drive. Files should be in directory according to **01TextCleaning.ipynb.**




## Introduction

This project is dedicated to unsupervised methods of text data transformation. The representation of text in such transformed form is inherent part of Natural Language Processing (NLP) and allows to consume unstructured data by various deep learning algorithms.

If NLP is a new term for you and sounds a bit mysterious, Yoav Goldberg in his [book](https://www.amazon.com/Language-Processing-Synthesis-Lectures-Technologies/dp/1627052984) describes it as:

>_Natural language processing (NLP) is a collective term referring to automatic computational processing of human languages. This includes both algorithms that take human-produced text as input, and algorithms that produce natural looking text as outputs._

NLP embraces wide range of tasks e.g. named entity recognition, sentiment analysis, automatic summarization, natural language generation and many more. Each one is a subject for separate project and could be thoroughly studied. 


Two tested methods in this project are **Unsupervised Word Segmentation into Subword Units** and **GloVe embeddings trained on our own corpus**.

I intentionally choose Polish language text to be analyzed, what I elaborate below, but be aware that the methods used are applicable to any language and text data.


## Dataset
Dataset comes from [PolEval competition](http://poleval.pl/tasks/task6). It contains tweets collected from openly available Twitter discussions. Original goal is to distinguish between normal/non-harmful tweets and tweets that contain any kind of harmful information. This includes cyberbullying, hate speech, personal threats, accumulation of vulgarities, profane language and related phenomena. 


**Example of tweets with normal content:**<br>
_"Czerwone Gitary, Historia jednej znajomości... i parawany które istniały zawsze…"_

**Example of tweets with harmful content:**<br>
_"Ja mam dla ciebie lepszą propozycję : powieś się gdzieś pod lasem UB-ecka gnido._"<br>
_"macie jej numer zdissujcie ją"_

## Why is NLP for Polish language difficult?

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

One of the possible solution to deal with complex polish morphology is to transform our corpus to be represented with subwords. The idea originally comes from neural machine translation and helps to resolve the problem of rare words.<br>
If you wish to dive into details, here is the original paper: https://arxiv.org/abs/1508.07909 and source code: https://github.com/rsennrich/subword-nmt <br>

The method involves generating subwords from our corpus in an unsupervised learning and use them to replace words in a text. This allows to represent various alternations of the same word with one subword therefore decrease number of unique words in a corpus while keeping the adequate meaning. 

Depending on how many subwords is generated to transform orginal text, the created subwords are more or less atomic. We control number of subwords with hyperparameter _symbols_.  

The example of results for diffrent number of _symbols_:

**original:** pewnie macie same pytania nie potraficie wymyslic nowych    
symbols = 10000
**transformed:** pewnie macie same pytania nie potrafi@@ cie wymysli@@ c nowych 

symbols = 5000
**transformed:** pewnie macie same pytania nie potrafi@@ cie wymysli@@ c now@@ ych

symbols = 1000
**transformed:** pewnie macie sa@@ me pyta@@ nia nie po@@ trafi@@ cie wy@@ mysli@@ c now@@ ych

symbols = 500
**transformed:** pewnie ma@@ cie sa@@ m@@ e pyta@@ nia nie po@@ tra@@ fi@@ cie wy@@ mys@@ li@@ c now@@ ych




## GloVe embeddings trained on our own corpus
ToDo description
