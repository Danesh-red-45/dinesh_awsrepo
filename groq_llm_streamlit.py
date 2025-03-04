# # Import necessary libraries
# import os  # For environment  variables
# import streamlit as st  # For creating the web app interface
# from langchain_groq import ChatGroq  # For interacting with the Groq model

# # Set up the Groq API key
# from dinesh_apikey import groq_api_key  # Import the API key from a separate file
# os.environ['groq_api_key'] = groq_api_key  # Set the API key in the environment

# # Initialize the Groq model
# # Use the 'llama3-8b-8192' model with a temperature of 0.6 for creativity
# llm_groq_obj = ChatGroq(model_name='llama3-8b-8192', temperature=0.6)

# # Streamlit app setup
# st.title("Groq Chatbot with Llama3")  # Set the title of the web app

# # Create a text input box for the user to enter their question
# user_input = st.text_input("Enter your question:")

# # Check if the user has entered a question
# if user_input:
#     # Show a loading spinner while the model generates a response
#     with st.spinner("Generating response..."):
#         # Invoke the Groq model with the user's input
#         response = llm_groq_obj.invoke(user_input).content
        
#         # Display the response to the user
#         st.write("Response:")
#         st.write(response)  # Show the model's response in the app
# Import necessary libraries
import os  # For environment variables
import streamlit as st  # For creating the web app interface
from langchain_groq import ChatGroq  # For interacting with the Groq model
from langchain.memory import ConversationBufferMemory  # For storing conversation history

# Set up the Groq API key
from dinesh_apikey import groq_api_key  # Import the API key from a separate file
os.environ['groq_api_key'] = groq_api_key  # Set the API key in the environment

# Initialize the Groq model
# Use the 'llama3-8b-8192' model with a temperature of 0.6 for creativity
llm_groq_obj = ChatGroq(model_name='llama3-8b-8192', temperature=0.6)

# Initialize conversation buffer memory to store chat history
# This will help the chatbot remember the context of the conversation
memory = ConversationBufferMemory()

# Streamlit app setup
st.title("Restaurant Chatbot with Llama3")  # Set the title of the web app

# Create a text input box for the user to enter their question
user_input = st.text_input("Enter your question or request:")

# Check if the user has entered a question
if user_input:
    # Save the user's input to the conversation memory
    memory.save_context({"input": user_input}, {"output": ""})
    
    # Retrieve the conversation history from memory
    chat_history = memory.load_memory_variables({})["history"]
    
    # Combine the user's input with the chat history for context
    full_prompt = f"Chat History:\n{chat_history}\n\nUser: {user_input}\nBot:"
    
    # Show a loading spinner while the model generates a response
    with st.spinner("Generating response..."):
        # Invoke the Groq model with the user's input and chat history
        response = llm_groq_obj.invoke(full_prompt).content
        
        # Save the bot's response to the conversation memory
        memory.save_context({"input": user_input}, {"output": response})
        
        # Display the response to the user
        st.write("Response:")
        st.write(response)  # Show the model's response in the app

# Display the conversation history (optional)
st.subheader("Conversation History")
st.write(memory.load_memory_variables({})["history"])  # Show the full chat history