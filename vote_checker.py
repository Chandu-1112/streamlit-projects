import streamlit as st
st.title("Vote eligibility checker.")
st.subheader("Check the results:")
name=st.text_input("Enter your name:")
age=st.text_input("Enter your age:")
if st.button("Check"):
    if int(age)>=18:
        st.success(f"{name} you are eligible to vote.")
    else:
        st.error(f"{name} you are not eligible to vote.")