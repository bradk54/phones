import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def countVectorizorByCategory(dataframe,vector,category,tfidf=False):
    """
    this will return a mutliple count vectorizers
    by category specified in the dataframe


    """
    if tfidf:
        count_vectorizer = TfidfVectorizer(stop_words='english')
    else:
        count_vectorizer = CountVectorizer(stop_words='english')
    unique_cagetories = dataframe[category].unique()
    
    initial_df = pd.DataFrame(columns=['feature','category','count'])
    for cat in unique_cagetories:
        filtered_df = dataframe[dataframe[category]==cat]
        vectors = count_vectorizer.fit_transform(filtered_df[vector])
        feature_names = count_vectorizer.get_feature_names()
        vector_counts = vectors.sum(axis=0).T
        append_df =  pd.DataFrame(feature_names,columns=['feature'])
        append_df['category'] = cat
        append_df['count'] = vector_counts
        initial_df = initial_df.append(append_df,ignore_index=True)
    return initial_df
