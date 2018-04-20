import pickle
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer

def chistka(input_string):
	vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
	cls = pickle.load(open("cls.pickle", "rb"))
	s = str(input_string)
	sample = vectorizer.transform([s])
	prediction = cls.predict_proba(sample)
	print(prediction) 
	return prediction

