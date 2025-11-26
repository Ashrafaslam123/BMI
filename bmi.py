import streamlit as st

st.title("BMI CALCULATOR")
height = st.number_input("Please Enter Your Height in meter :- " )
weight = st.number_input("Please Enter Your Weight in Kg ")

# print("The BMi is :- ", weight/(height**2))
if st.button('Calculate'):
    st.write("The BMi is :- ", weight/(height**2))
else:
    pass