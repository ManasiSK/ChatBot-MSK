import streamlit as st
from streamlit_chat import message
from bardapi import Bard

token = 'YAhut6eJhpHMm09cNYHzasXceYcDudbI1FgZps5OuXfyee49Hb4B6Xc2k7uqtV2gkfuqNw.'

#function that returns an output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

#function to receive the text input
def get_text():
    input_text = st.text_input("Intelli BOT:", " ", key='input')
    return input_text

#Title of the chatbot
st.title('Intelli BOT')

#url='https://images.unsplash.com/photo-1534447677768-be436bb09401?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=894&q=80'
changes = '''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=872&q=80');
    background-size:cover;
    }
    html{
    background:transparent;
    }
    div.esravye2 > iframe
    {
    background-color:transparent;
    }
    
</style>
'''
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


#Function to accept the user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True)
        #is_user is for user to know which part of the conversation is of the user




