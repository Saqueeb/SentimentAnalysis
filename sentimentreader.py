# -*- coding: utf-8 -*-
"""SentimentReader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXSS8BiqNn8Wqfo3CncgVJ2mjIGlL6N7
"""

from textblob import TextBlob
text= input("Enter your comment: ")
obj= TextBlob(text)
sentiment = obj.sentiment.polarity
if sentiment>=0:
 print("Your comment was Positive")
else:
  print("Your comment was Negative")