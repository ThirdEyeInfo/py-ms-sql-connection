## Step to run py-ms-sql-connection
POC on establishing ODBC connection between python and mssql server
- Clone run py-ms-sql-connection in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to py-ms-sql-connection (in step 1) from conda prompt and follow below commands
    * cd <basepath>/run py-ms-sql-connection
    * conda create -n practice-python-3.11 python=3.11 -y
    * conda activate practice-python-3.11
    * pip install -r requirements.txt
- Download ODBC Driver and install it on your windows machine https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#download-for-windows
- Make sure to note down the Driver version before installing as same we have to configure in Driver properties
- Open app.py file and configure it with below properties
    * SERVER = '<DB-Server Name>' # Replace this value with your DB-Server Name e.g. SATYAPRAKASH\SQLEXPRESS
    * DATABASE = '<DB-Name>' # Replace this value with your DB-Name e.g master
    * USERNAME = '<DB-Username>' # Replace this value with your DB-Username e.g sa
    * PASSWORD = '<DB-Password>' # Replace this value with your DB-Password e.g root
    * DRIVER = '<DRIVER-Name>' # Replace this value with your DRIVER-Name e.g. {ODBC Driver 17 for SQL Server}
- Use below SQL script to create MS SQL database along with table
    * CREATE DATABASE myapp
    * USE myapp
    * CREATE TABLE PERSON(id int primary key identity(1,1), first_name varchar(50) not null, middle_name varchar(50), last_name varchar(50))
- Run py-ms-sql-connection application with below command
    * streamlit run app.py
- Open http://localhost:8501/ on your favorite browser and supply Person details to save changes