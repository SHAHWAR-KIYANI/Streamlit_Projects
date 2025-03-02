import streamlit as st

st.title("BMI Calculator")
st.write("------------------------------------")

height = st.slider("Enter Your Height (in cm):",100,250,170)
weight = st.slider("Enter Your Weight (in kg):",40,200,70)

bmi = weight / ((height/100)**2)
st.write(f"BMI: {bmi:.2f}")

st.write("------------------------------------")
st.title("BMI Categories")
st.write("------------------------------------")
st.write("Underweight = <18.5")
st.write("Normal weight = 18.5 – 24.9")
st.write("Overweight = 25 – 29.9")
st.write("Obesity = BMI of 30 or greater")
st.write("------------------------------------")
category = ""
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

st.write(f"Your BMI is: {bmi:.2f} and you are {category}.")
st.write("------------------------------------")
