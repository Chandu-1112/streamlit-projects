import streamlit as st
import csv as c
import pandas as pd
st.set_page_config(page_title="College Dashboard")
st.title("Marks portal")
name=st.text_input("Enter student name:")
branch=st.text_input("Enter your branch:")
marks=st.number_input("Enter your marks:",value=None,placeholder="Enter marks")
if st.button("Submit"):
    with open("marks.csv","a",newline="") as f:
        writer=c.writer(f)
        writer.writerow([name,branch,marks])
    st.success("Marks submitted successfully!")
if st.button("Fetch marks"):
    df=pd.read_csv("marks.csv",names=["Name","Branch","Marks"])
    st.dataframe(df)
        