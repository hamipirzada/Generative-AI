import streamlit as st  # type: ignore
import numpy as np 
import pandas as pd  # type: ignore

# Title for our streamlit application
st.title("Welcome to Streamlit")

#Input field
name = st.text_input("Enter your name: ")
if name:
    st.write(f"Welcome {name}")

#slider
age = st.slider("Select your age. ", 0,100,20)
st.write(f"Your age is {age}")

#dropdown
options = ["Python", "C++", "Java", "C language", "C#"]
choice = st.selectbox("Choose your favourite programming language ", options)
st.write(f"You selected {choice}")

#writing dataframe
data = {
    "Name" : ["James", "Doe", "Mark", "Sam", "Zack"],
    "Age" : [26, 23, 22, 20, 29],
    "City" : ["New York", "Colombo", "Washington", "New York", "India"]
}
df = pd.DataFrame(data)
st.write(df)

#save this csv
df.to_csv("Sample_csvfile.csv")

uploaded_file = st.file_uploader("Please upload any CSV file", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)