import streamlit as st
import numpy as np
import pandas as pd

header=st.beta_container()
dataset=st.beta_container()
features=st.beta_container()
modelTraining=st.beta_container()



with header:
    st.title('welcome to my Fist Data Science Project!!')



with dataset:
    st.header('NBA DataSet')
    nba=pd.read_csv(r'https://raw.githubusercontent.com/sairamsnv/stream/main/myds.csv')
    data=pd.DataFrame(nba['Team'].value_counts()).head(20)
    st.bar_chart(data)



