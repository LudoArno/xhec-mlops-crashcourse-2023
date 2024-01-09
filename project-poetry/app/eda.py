import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_columns, get_unique_values, get_column_data, get_summary

def run_eda_app():

    st.sidebar.title("Exploratory Data Analysis")

    data_file = st.sidebar.file_uploader("Upload CSV", type=['csv'])
    if data_file is not None:
        df = load_data(data_file)
        columns = get_columns(df)

        st.header('Data')
        number_of_rows = st.slider("Number of Rows to View", min_value=0, max_value=200, value=50)
        st.dataframe(df.head(number_of_rows))

        st.header('Columns')
        st.write(columns)

        st.header('Summary')
        st.table(get_summary(df))

        st.header('Plot')
        column_to_plot = st.selectbox("Select 1 Column", columns)
        column_to_filter = st.selectbox("Select a Column to Filter by", columns)
        filter_value = st.text_input("Enter a Value to Filter by")
        if st.button("Generate Plot"):
            st.success(f"Generating Customizable Plot for {column_to_plot}")
            fig = plt.figure()
            plt.title(f"Distribution Plot for {column_to_plot}")
            filtered_df = df[df[column_to_filter] == filter_value]
            sns.lineplot(x=filtered_df.index, y=filtered_df[column_to_plot])
            st.pyplot(fig)

        st.header('Unique Values')
        column_to_show_unique_values = st.selectbox("Select a Column to Display Unique Values", columns)
        st.write(get_unique_values(df, column_to_show_unique_values))

if __name__ == "__main__":
    run_eda_app()
