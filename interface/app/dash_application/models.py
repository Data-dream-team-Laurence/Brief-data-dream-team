from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, r2_score, median_absolute_error
from sklearn import metrics
import numpy as np

#todo

def get_results_by_model(model, X, y, X_to_predict):

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)
    if ( model == 'Régression Linéaire' ) :
        lm = linear_model.LinearRegression().fit(X_train, y_train)
    elif ( model == 'Ridge' ) :
        lm = linear_model.Ridge().fit(X_train, y_train)
    elif ( model == 'Lasso' ) :
        lm = linear_model.Lasso(alpha=0.8).fit(X_train, y_train)
    elif ( model == 'ElasticNet' ):
        lm = linear_model.ElasticNet().fit(X_train, y_train)
    elif ( model == 'DummyRegressor') :
        lm = DummyRegressor(strategy = 'mean').fit(X_train, y_train)  

    y_predict = lm.predict(X_test)
    prediction = lm.predict(X_to_predict)
    if ( model == 'Régression Linéaire' ) | ( model == 'Ridge') :
        prediction = prediction[0]

    mse = mean_squared_error(y_test, y_predict)
    rmse = np.sqrt(mse)
    mae = median_absolute_error(y_test, y_predict)
    r2 = r2_score(y_test, y_predict)
    return prediction, mae, mse, rmse, r2