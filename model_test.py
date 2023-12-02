from utils import get_hyperparameter_combinations, train_test_dev_split,read_digits, tune_hparams, preprocess_data
import joblib

model_folder = '/models'

def test_model():
    model = joblib.load('/models/m22aie224_ls_.joblib')