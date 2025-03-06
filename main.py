import streamlit as st
from numerical import numerical_main
from counting import counting_main

type_q = st.selectbox(
    "Pilih Tentang...",
    ["Numerik Deret"],
    index=None,
)

if type_q == "Numerik Deret":
    numerical_main()
if type_q == "Numerik Berhitung":
    counting_main()