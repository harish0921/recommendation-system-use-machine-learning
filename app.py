import streamlit as st
import pandas as pd
import pickle

df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommendation(title):
    idx = df[df['Title']==title].index[0]
    idx = df.index.get_loc(idx)
    distances= sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[1:20]

    recommended_jobs = []
    for i in distances:
        recommended_jobs.append(df.iloc[i[0]].Title)

    return recommended_jobs

# web app
st.title('Job Recommendation system')
title = st.selectbox('search job',df['Title'])

recommended_jobs = recommendation(title)

if recommended_jobs:
    st.write(recommended_jobs)
    