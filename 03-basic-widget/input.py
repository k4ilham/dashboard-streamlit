import streamlit as st
 
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)