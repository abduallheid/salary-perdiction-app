import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from vedio_page import call_vedieo

page = st.sidebar.selectbox("Chose your Action ", ("Predict", "Explore","view"))

if page == "Predict":
     show_predict_page()
elif page == "Explore":
     show_explore_page()
elif page == "view":
     call_vedieo()


