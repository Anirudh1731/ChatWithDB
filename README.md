# ChatWithDB

##Langchain Chat with DB App

#Overview
The Langchain Chat with DB App is a Streamlit-based application that allows users to interact with a database using natural language queries. Powered by Langchain and Groq's API, this app enables users to chat with either a local SQLite database or a remote MySQL database. The app leverages a conversational AI model to interpret user queries and fetch relevant data from the database.

##Features
1) Database Options:
-Connect to a local SQLite database (student.db).
-Connect to a remote MySQL database by providing connection details.
2) Natural Language Queries:
-Ask questions in plain English, and the app will translate them into SQL queries.
3)Conversational Interface:
-Chat-based interface for seamless interaction with the database.
4)Session Management:
-Clear chat history with a single button click.
5)Streamlit Integration:
-Easy-to-use UI with Streamlit components for input and output.

##Prerequisites
-Before running the app, ensure you have the following:
-Python 3.7+ installed.
-Required Python libraries installed (see Installation).
-A Groq API Key for using the Groq LLM model.
-(Optional) MySQL database credentials if you plan to connect to a remote MySQL database.

##Installation
-Clone the repository:
--git clone https://github.com/your-repo/langchain-chat-with-db.git
--cd langchain-chat-with-db
-Install the required dependencies:
--pip install -r requirements.txt
-Alternatively, install the dependencies manually:
--pip install streamlit langchain sqlalchemy mysql-connector-python langchain-groq

Place your SQLite database file (student.db) in the project directory (if using a local database).

## Usage
Run the Streamlit app:
streamlit run app.py
Open the app in your browser (usually at http://localhost:8501).

##Sidebar Options:
-Choose between using a local SQLite database or connecting to a MySQL database.
-Provide the necessary database credentials (if using MySQL).
-Enter your Groq API key.

##Chat Interface:
-Type your query in the chat input box (e.g., "How many students are enrolled?").
-The app will process your query and display the response.

##Clear Chat History:
-Use the "Clear message history" button in the sidebar to reset the chat.

##Code Structure
-app.py: The main Streamlit application script.
--Handles user input, database configuration, and chat interactions.
--Uses Langchain's SQL agent and Groq's LLM for query processing.
-student.db: (Optional) A local SQLite database file for testing.

##Configuration
Database Options

##Local SQLite Database:
--Place your SQLite database file (student.db) in the project directory.
--The app will automatically detect and use it.

##Remote MySQL Database:
--Provide the following details in the sidebar:

---MySQL Host
---MySQL User
---MySQL Password
---MySQL Database Name

##Groq API Key
-Obtain a Groq API key from Groq's website.
-Enter the API key in the sidebar to enable the LLM.

#Example Queries
Here are some example queries you can try:
For a student database:
-"How many students are there?"
-"List all students with a GPA greater than 3.5."
-"What is the average age of students?"

#For a custom MySQL database:
-"How many orders were placed last month?"
-"List all customers from New York."
-"What is the total revenue for Q1 2023?"

##Troubleshooting
###Database Connection Issues:
-Ensure the database file (student.db) is in the correct location.
-Double-check MySQL credentials (host, user, password, database name).

###Groq API Key Issues:
-Ensure the API key is valid and entered correctly.
-Check your internet connection.

###Streamlit Errors:
-Restart the Streamlit app if it becomes unresponsive.
-Clear the cache using st.cache_resource.clear() if needed.

