import streamlit as st
from bardapi import Bard
from streamlit_chat import message

#title of the streamlit app
st.title('Viraj Personal Tutoring Bot ')

token = 'YAiv-auUY6qYvw1a0GH8HOE19GoNWgpY25TfsUcCqZdktsJ6-ByL6S8XMzmP3xYjV4GFXA.'



#function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

#function to recieve users queries
def get_text():
    input_text=st.text_input("CN BOT : ", "", key='input')
    return input_text

# CSS code to change the background image
changes = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1682687982204-f1a77dcc3067?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80");
    background-size: cover;
}
</style>
'''
#commiting that change
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

#accepting user input
user_input= get_text()
if user_input:
    print(user_input)
    output=generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_" +str(i),is_user=True)





#url=https://images.unsplash.com/photo-1505506874110-6a7a69069a08?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80

#data-testid ="stAppViewContainer"





