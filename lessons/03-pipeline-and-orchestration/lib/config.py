from pathlib import Path

CATEGORICAL_COLS = ["PULocationID", "DOLocationID", "passenger_count"]

# [2] means go up 2 levels from the current file -> from ./lessons/03/solution/config.py to ./
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
MODELS_DIRPATH = str(PROJECT_ROOT / "models")

train_path = f"{DATA_DIRPATH}/yellow_tripdata_2021-01.parquet"
test_path = f"{DATA_DIRPATH}/yellow_tripdata_2021-02.parquet"
predict_path = f"{DATA_DIRPATH}/yellow_tripdata_2021-03.parquet"
