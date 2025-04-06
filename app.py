#load all environment variables
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#Function to retrive query from sql db
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#define prompt
prompt=[
    """
    You are an expert in converting simple english text to sql query.The SQL DB has the 
    name STUDENT and has fields NAME,CLASS,SECTION,MARKS. \n\n Example 1- how many enteries of records are present?,
    the SQL command will be like SELECT COUNT(*) FROM STUDENT;
    EX 2 - Tell me all students studying in Business Analytics?,
    for this SQL command will be SELECT * FROM STUDENT WHERE CLASS = "Business Analytics";
    also the sql code should not have ''' in beggining or end and 
    sql word in the output
"""
]


#stremlit app

st.set_page_config(page_title="I can retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL data")

question=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

#if submit is click
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is ")
    for row in data:
        print(row)
        st.header(row)
