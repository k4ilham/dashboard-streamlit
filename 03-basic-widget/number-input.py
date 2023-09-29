import streamlit as st
 
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')