import streamlit as st
import pandas

st.set_page_config("wide")

st.title("Natacha Halflants")

intro = """
Hi, I am Natacha ! I am a python programmer. I love to learn and build apps. I am a driven Senior Functional Analyst 
with an overall 9 years of IT experience in varied technologies and domains. I have a rich experience in analyzing 
requirements, designing technical solution, creating specifications and ensuring development and implementation of web 
and mobile solutions. Enriched exposure to third party services integration, api development and delivering financial 
services interfaces. 
"""
st.write(intro)

apps_intro = """
Below you can find some of the apps I have built in Python. Feel free to contact me
"""
st.info(apps_intro)

df = pandas.read_csv("data.csv", sep=";")

project_col1, project_col2 = st.columns(2)

with project_col1:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with project_col2:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
