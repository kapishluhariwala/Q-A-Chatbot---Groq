import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
# os.environ['LANGCHAIN_TRACING_V2'] = 'true'
# os.environ['LANGCHAIN_PROJECT'] = 'Q&A Chatbot with GROQ'

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.set_page_config(page_title="Q&A Chatbot", layout = 'wide')
st.title('Q&A Chatbot with GROQ')

st.sidebar.title('Settings')
api_key = st.sidebar.text_input('GROQ API Key', type='password')

llm_select = st.sidebar.selectbox('GROQ Language Model', ['mixtral-8x7b-32768', 'llama3-70b-8192', 'llama3-8b-8192'])

temperature = st.sidebar.slider('Temperature', 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider('Max Tokens', 50, 300, 150)

system_prompt = st.sidebar.text_area(label = 'System Prompt', value = 'You are a helpful assistant. Please response to the user queries', placeholder = 'Enter your system prompt')

prompt = ChatPromptTemplate(
    [
        ('system',system_prompt),
        ('user','Question:{question}')
    ]
)

if not api_key:
    st.warning('Input GROQ API Key...')

else:
    llm = ChatGroq(model=llm_select,api_key=api_key,temperature=temperature,max_tokens=max_tokens)
    output_parser = StrOutputParser()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message['content'])

    if user_prompt := st.chat_input('Say Something...'):
        with st.chat_message('user'):
            st.markdown(user_prompt)
        st.session_state.messages.append({'role':'user','content':user_prompt})
        chain = prompt|llm|output_parser
        answer = chain.invoke({'question':user_prompt})
        with st.chat_message('assistant'):
            st.markdown(answer)
        st.session_state.messages.append({'role':'assistant','content':answer})



