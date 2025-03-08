import streamlit as st
import pandas as pd

st.title("Data DashBoard")
uploaded_file = st.file_uploader("Choose a CSV File", type="CSV")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = list(df.columns)
    selected_column = st.selectbox("Select Column to Filter By:", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Value:", unique_values)
    filtered_data = df[df[selected_column] == selected_value]
    st.write(filtered_data)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-Axis Column:", columns)
    y_column = st.selectbox("Select Y-Axis Column:", columns)
    if st.button("Generate Plot"):
        st.line_chart(filtered_data.set_index(x_column)[y_column])

else:
    st.write("Waiting for File Upload...")
    
