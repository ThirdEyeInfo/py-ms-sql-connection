import streamlit as st
import pyodbc as odbc
import pandas as pd

SERVER = '<DB-Server Name>' # Replace this value with your DB-Server Name e.g. SATYAPRAKASH\SQLEXPRESS
DATABASE = '<DB-Name>' # Replace this value with your DB-Name e.g master
USERNAME = '<DB-Username>' # Replace this value with your DB-Username e.g sa
PASSWORD = '<DB-Password>' # Replace this value with your DB-Password e.g root
DRIVER = '<DRIVER-Name>' # Replace this value with your DRIVER-Name e.g. {ODBC Driver 17 for SQL Server}

connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

with st.sidebar:
    st.header('My form')
    firstName = st.text_input('First Name')
    middleName = st.text_input('Middle Name')
    lastName = st.text_input('Last Name')

    flag = True

    if firstName:
        flag = False
    if middleName == '':
        middleName = None
    if lastName == '':
        lastName = None

    clicked = st.button('Submit', disabled=flag)

    def save(firstName, middleName, lastName):

        try:
            with odbc.connect(connectionString) as conn:
                cursor = conn.cursor()

                sql = "INSERT INTO PERSON VALUES (?, ?, ?)"
                values = (firstName, middleName, lastName)
                cursor.execute(sql, values)

                conn.commit()

            print('Details saved successfully!')
        except odbc.Error as ex:
            print("Database error:", ex)

    if clicked:
        save(firstName, middleName, lastName)

st.header('Fecth all records')
def display():
    try:
        with odbc.connect(connectionString) as conn:

            sql = "SELECT * FROM PERSON"
            df = pd.read_sql(sql, conn)
            st.table(df)

            conn.commit()
    except odbc.Error as ex:
        print("Database error:", ex)

display()