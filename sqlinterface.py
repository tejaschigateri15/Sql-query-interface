import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent


st.title("SQL Chat Interface")


db_path = st.text_input("Enter the path to the SQLite database file")

if db_path:
    try:
   
        db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

       
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0,api_key = "api_key")

 
        agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

        user_input = st.text_area("Ask a question about the database")

        if st.button("Submit"):
           
            response = agent_executor.invoke({"input": user_input})
            output = response["output"]
            formatted_output = f"<pre>{output}</pre>"
            
          
            st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")