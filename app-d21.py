import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
    st.write('Yout can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(.05)
    my_bar.progress(percent_complete + 1)

st.balloons()