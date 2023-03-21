import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')

def article_date(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.publish_date

def article_title(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.title

def article_authors(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.authors

def article_summary(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.summary

def article_sentiment(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    analysis = TextBlob(article.text)
    return analysis.polarity

def senti_analysisa(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    analysis = TextBlob(article.text)
    polarity =  analysis.polarity
    if polarity > 0:
        ans = "Positive"
    elif polarity < 0:
        ans = "Negative"
    else:
        ans = "Neutral"
    return ans