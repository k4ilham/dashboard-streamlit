import streamlit as st
 
st.title('Belajar Analisis Data')
 
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)