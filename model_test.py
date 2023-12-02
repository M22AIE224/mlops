import joblib
import pytest
from sklearn.linear_model import LogisticRegression




@pytest.mark.parametrize("solver", ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'])
def test_model(solver):
    model_name = "./models/m22aie224_ls_"+ solver + ".joblib"
    lr_model = joblib.load('/models/m22aie224_ls_lbfgs.joblib')
    assert isinstance(lr_model, LogisticRegression), f"Model {lr_model} is not a Logistic Regression model."


    assert solver == lr_model.get_params()['solver'], f"Solver mismatch for model {model_name}. Expected: {solver}, Actual: {lr_model.get_params()['solver']}"