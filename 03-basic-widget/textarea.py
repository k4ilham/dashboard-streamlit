import streamlit as st
 
text = st.text_area('Feedback')
st.write('Feedback: ', text)