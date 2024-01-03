import pickle
from scipy.sparse import csr_matrix
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
from pandas import DataFrame
import pandas as pd
from typing import List


# Define a data model for the request body

class Input_raw(BaseModel):
    PULocationID: int
    DOLocationID: int
    passenger_count: float
    
    
    

def load_model() -> dict:
    model_uri = f"local_models/model.pkl"
    with open(model_uri, 'rb') as f:
        model = pickle.load(f)
    dv_uri = f"local_models/dv.pkl"
    with open(dv_uri, 'rb') as f:
        dv = pickle.load(f)
    
    return dv, model


def encode_categorical_cols(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ["PULocationID", "DOLocationID", "passenger_count"]
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype("int")
    df[categorical_cols] = df[categorical_cols].astype("str")
    return df


def extract_x_y(
    df: pd.DataFrame,
    categorical_cols: List[str] = None,
    dv: DictVectorizer = None,
    with_target: bool = True,
) -> dict:

    if categorical_cols is None:
        categorical_cols = ["PULocationID", "DOLocationID", "passenger_count"]
    dicts = df[categorical_cols].to_dict(orient="records")

    y = None
    if with_target:
        if dv is None:
            dv = DictVectorizer()
            dv.fit(dicts)
        y = df["duration"].values

    x = dv.transform(dicts)

    return x, y, dv


def loading_data(input_data: List[Input_raw], dv: DictVectorizer):
    # this was necessary:
    # +------
    input_data = [dict(tuples) for tuples in input_data]
    input_df = pd.DataFrame(input_data)
    # ------+
    input_df = encode_categorical_cols(input_df)
    X_pred, _, _ = extract_x_y(df=input_df, dv=dv, with_target=False)
    return X_pred


def predict_duration(input_data: csr_matrix, model: LinearRegression):
    return model.predict(input_data)


def process_predict(input_data: List[Input_raw]):
    # loading the necessary model and dictVectorizer
    dv, model = load_model()
    # Transforming the input data
    X_pred = loading_data(input_data, dv)
    # Running the prediction
    result = predict_duration(X_pred, model)
    return result
    



# if __name__=="__main__":
    # load_model()
    # it works and support the predict method