import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib

import sys, os
sys.path.append(os.path.abspath('..'))

from data_utils import load_train, load_test, write_test
from report import *

if __name__ == '__main__':
    X, y = load_train('../data/train_2008.csv', False)
    
    param_grid = {
        'criterion':  ['gini', 'entropy'],
        'max_features': [None, 'auto', 'sqrt', 'log2'],
        'max_depth': [2, 5, 10, 20]
    }

    rfc = RandomForestClassifier()
    clf = GridSearchCV(estimator=rfc, scoring='accuracy', param_grid=param_grid, 
                       n_jobs=4, verbose=2)
    clf.fit(X, y)

    report(clf.cv_results_)
    
    print('Best Error: %f' %(clf.best_score_))
    print('Best Model: %s' %(clf.best_params_))
    
    
