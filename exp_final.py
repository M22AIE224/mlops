from sklearn.datasets import load_digits
import joblib
from joblib import dump, load
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import GridSearchCV


#Define a Logistic Regression Model
lr = LogisticRegression()

#Define the hyperparamters fo LR

h_param_lr={}
h_param_lr['solver'] = ['newton-cg', 'liblinear', 'sag', 'saga']



# Perform GridSearchCV with 5-fold cross-validation
grid_search = GridSearchCV(lr, h_param_lr, cv=5, scoring='accuracy', n_jobs=-1)

#Load the data 
digits = load_digits()
data = digits.data
target = digits.target

#Search fit
grid_search.fit(data, target)

# Report mean and std across 5 CV for each solver
means_dt = grid_search.cv_results_['mean_test_score']

params = grid_search.cv_results_['params']
stds = grid_search.cv_results_['std_test_score']



for mean, std, solver_params in zip(means_dt, stds, params):
    solver = solver_params['solver']
    
    lr.set_params(**solver_params)
    
    lr.fit(data, target)
    
    # Save the model
    model_name = "./models/m22aie224_ls_"+ solver + ".joblib"
    joblib.dump(lr, model_name)

    

best_params = grid_search.best_params_
best_accuracy = grid_search.best_score_
print(f'Best Accuracy: {best_accuracy:.4f}')
print(f'Best Hyperparams: {best_params}')
