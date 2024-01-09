import streamlit as st
from eda import run_eda_app

def main():
    st.sidebar.title("EDA App")
    app_mode = st.sidebar.selectbox("Choose the app mode",
                                    ["Exploratory Data Analysis", "About"])
    if app_mode == "Exploratory Data Analysis":
        run_eda_app()
    elif app_mode == "About":
        st.sidebar.success('In this application, you can upload your own csv file and perform exploratory data analysis. The application provides a user-friendly interface to interactively explore the data.')
        st.sidebar.info('For any queries or suggestions, you can contact us at: info@edaapp.com')

if __name__ == "__main__":
    main()
