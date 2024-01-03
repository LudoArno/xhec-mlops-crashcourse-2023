from prefect import flow, task

from modeling import *
from preprocessing import *



@flow
def train_model_workflow(
    train_filepath: str,
    test_filepath: str,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    
    # process
    x_train, y_train, dv = process_data(train_filepath, with_target=True)
    x_test, y_test, _ = process_data(test_filepath, dv, with_target=True)
    
    # train model
    model = train_model(x_train, y_train)
    
    # evaluation
    y_pred_test = predict(x_test, model)
    evaluation = evaluate_model(y_true=y_test, y_pred=y_pred_test)
    
    return {"model":model, "evalution":evaluation, "dv":dv}

@flow
def batch_predict_workflow(
    input_filepath: str,
    model: Optional[LinearRegression] = None,
    dv: Optional[DictVectorizer] = None,
    artifacts_filepath: Optional[str] = None,
) -> np.ndarray:
    
    # process
    x, _, _ = process_data(input_filepath, dv, with_target=False)
    y = predict(x, model)
    return {"y":y}