import streamlit as st

st.title("Calculator ")

nummer_1 = st.text_input("Nummer 1")
pom = st.text_input("Plus, min, maal of deel")
nummer_2 = st.text_input("Nummer 2")

if nummer_1 and pom and nummer_2:
    if pom == 'plus':
        uitkomst = float(nummer_1) + float(nummer_2)
        st.text(uitkomst)
    elif pom == 'min':
        uitkomst = float(nummer_1) - float(nummer_2)
        st.text(uitkomst)
    elif pom == 'maal':
        uitkomst = float(nummer_1) * float(nummer_2)
        st.text(uitkomst)
    elif pom == 'deel':
        uitkomst = float(nummer_1) / float(nummer_2)
        st.text(uitkomst)
    else:
        st.text("Je kan alleen plus, min, maal of deel gebruiken.")

