import pandas as pd

def load_data(file):
    """
    Function to load a csv file and return a pandas dataframe
    """
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        print(f"Error: {e}")

def get_columns(df):
    """
    Function to get column names from a dataframe
    """
    return df.columns.tolist()

def get_unique_values(df, column):
    """
    Function to get unique values from a specific column in a dataframe
    """
    return df[column].unique().tolist()

def get_column_data(df, column):
    """
    Function to get data from a specific column in a dataframe
    """
    return df[column]

def get_summary(df):
    """
    Function to get summary statistics of a dataframe
    """
    return df.describe()

