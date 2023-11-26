import streamlit as st
import pandas as pd

###### LLM and Q&A Chatbot functions ######

from get_reco import create_recommendation



###### Streamlit App ######

st.set_page_config(page_title="Machine Learning and Data Science Books Recommender Chatbot", page_icon=":books", layout="wide", initial_sidebar_state="expanded")

st.header(":green[Machine Learning] and :blue[Data Science] Books recommender 🤖 :red[Chatbot]", divider="rainbow")

st.caption("🚀 A streamlit chatbot recommending ML and DS books from Amazon dataset on Kaggle [LINK](https://www.kaggle.com/datasets/jiteshkumarsahoo/ml-and-ds-books-on-amazon14-countries)")

st.markdown("This is a chatbot that recommends books about Machine Learning and Data Science from Amazon dataset.")
st.markdown("The chatbot uses the [OpenAI API](https://beta.openai.com/) and langchain library to answer questions and recommend books.")

# load the dataset and show the first 5 rows on streamlit

df = pd.read_csv("amazon_ml_ds_books_cleaned.csv")

# round to 2 decimal place the values in the "Price" column

df["Price"] = df["Price"].round(2)

# show the 5 rows by Stars

df = df.sort_values(by="Stars", ascending=False).reset_index(drop=True)

st.success("Amazon ML and DS Books: Top 5 Books by Stars")


st.dataframe(df.head(5), hide_index=True, use_container_width=True,column_order=["Title","Stars","Number of Reviews","Price","Authors","Country"])


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"



# create the chatbot interface

with st.form("my_form"):
    input_text = st.text_area("Enter text:", "Suggest a book about Pandas?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if not openai_api_key:
            st.warning("Please enter your OpenAI API key in the sidebar")
        else:
            create_recommendation(openai_api_key,input_text)
    
    
    


    






