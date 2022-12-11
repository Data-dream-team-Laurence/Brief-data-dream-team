import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, median_absolute_error
import numpy
from .db import get_freight_data



y1, features1 = get_freight_data()


def create_dash_application(flask_app):
    assets_path = os.getcwd()+r"/interface/app/dash_application/assets/"
    dash_app = Dash(server=flask_app, name="Dashboard", url_base_pathname="/predictions/", assets_folder=assets_path)
    dash_app.title = "Predictions"

    #=============== MAIN LAYOUT ================================

    dash_app.layout = html.Div(className= 'main-container', children=[
        html.Div(className = 'choice', children=[
            html.P("Type d'algorithme :"),
            html.Div(children = [
                dcc.Dropdown(options =[
                {'label': 'Régressions', 'value': 'REG'},      
                {'label': 'Classifications', 'value': 'CLA'},
                ],value = 'REG', id='choice1')
            ])
        ]),
        html.Div(className = 'choice', children=[
            html.P("Choix de l'algorithme :"),
            html.Div(id='choice2')           
        ]),
        html.Div(className = 'choice', children=[
            html.P("Valeur à prédire"),
            html.Div(children = [
                dcc.Dropdown(options =[
                {'label': 'Frais de port', 'value': 'FRA'},      
                {'label': 'Temps de livraison', 'value': 'LIV'},
                ],value = 'FRA', id='choice3'),
            ])
        ]),        
        html.Div(className = 'features_checkboxes', children=[
            html.P("Choix des features"),
            html.Div(id='features')
        ]),
        html.Button('Prédire', id='submit-val', n_clicks=0),
        html.H4("Résultat de la prédiction",className='subtitle'),
        html.Div(id='results')
    ])

    #================== CALLBACKS ====================

    #returns a list of models according to model type choice
    @dash_app.callback(
        Output('choice2', 'children'),
        Input('choice1','value')
    )
    def get_models(type):
        if (type == 'REG') :
            return dcc.Dropdown(options =[
                {'label': 'Regression lineaire', 'value': 'Régression Linéaire'},      
                {'label': 'Ridge', 'value': 'Ridge'},
                {'label': 'Lasso', 'value' : 'Lasso'},
                {'label': 'ElasticNet', 'value' : 'ElasticNet'}
            ],value = 'Régression Linéaire', id='algo') 
        if (type == 'CLA') :
            return dcc.Dropdown(options =[
            ],value = 'en construction...') 

    #returns a list of features according to target choice
    @dash_app.callback(
        Output('features', 'children'),
        Input('choice3','value')
    )
    def get_features(target):
        if (target == 'FRA') :
            return (dcc.Checklist(options = {
                'price' : 'prix',
                'product_weight_g' : 'poids',
                'product_length_cm' : 'longueur',
                'product_height_cm' : 'hauteur (cm)',
                'product_width_cm' : 'largeur (cm)'
                }, 
            value=['price', 'product_weight_g'],
            inline=True,
            id="features_checklist" ),
            html.P("Prix de l'objet"), 
            dcc.Input(id="input1", type="number"),
            html.Br(),
            html.P("Poids (g)"),
            dcc.Input(id="input2", type="number"),
            html.Br(),
            html.P("Longueur (cm)"),
            dcc.Input(id="input3", type="number"),
            html.Br(),
            html.P("Hauteur (cm)"),
            dcc.Input(id="input4", type="number"),
            html.Br(),
            html.P("Largeur (cm)"),
            dcc.Input(id="input5", type="number"))       
        elif (target == 'LIV') :
            return dcc.Checklist(
                ['New York City', 'Montréal', 'San Francisco'],
                ['New York City', 'Montréal'],
                inline=True)

    @dash_app.callback(
        Output('results', 'children'),
        Input('submit-val', 'n_clicks'),
        State('choice3','value'),
        State('algo','value'),
        State('input1','value'),
        State('input2','value'),        
        State('input3','value'),        
        State('input4','value'),        
        State('input5','value'),
        State('features_checklist','value')        
    )
    def predict(click,target, model, f1, f2, f3, f4, f5, checklist):
        if target == 'FRA' :
            df= pd.DataFrame(features1, columns=['price','product_weight_g','product_length_cm','product_height_cm','product_width_cm'])
            X = df[checklist]
            y = pd.DataFrame(y1)

            form = {'price' : f1, 'product_weight_g' : f2, 'product_length_cm' : f3, 'product_height_cm' : f4, 'product_width_cm' : f5 }
            X_to_predict = pd.DataFrame([form])
            X_to_predict = X_to_predict[checklist]
            
        elif target == 'LIV' :
            df= pd.DataFrame()
        
        X.fillna(0, inplace=True) # a modifier plus tard

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)
        lm = LinearRegression().fit(X_train, y_train)
        y_predict = lm.predict(X_test)
        
        prediction = lm.predict(X_to_predict)
        mse = mean_squared_error(y_test, y_predict)
        rmse = numpy.sqrt(mse)
        mae = median_absolute_error(y_test, y_predict)
        r2 = r2_score(y_test, y_predict)

        print(prediction)
        return html.Div(children=[
            html.P(f"Prix estimé : {prediction[0][0]}"),            
            html.P(f"MAE : {mae:.2f}"),
            html.P(f"MSE : {mse:.2f}"),
            html.P(f"RMSE : {rmse:.2f}"),
            html.P(f"R2 score : {r2:.2f}")
        ])

    return dash_app



    
    

    
