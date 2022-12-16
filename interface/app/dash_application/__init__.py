import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import os
from .db import get_freight_data
from .models import get_results_by_model



y1, features1 = get_freight_data()


def create_dash_application(flask_app):
    assets_path = os.getcwd()+r"/interface/app/dash_application/assets/"
    dash_app = Dash(server=flask_app, name="Dashboard", url_base_pathname="/predictions/", assets_folder=assets_path)
    dash_app.title = "Predictions"
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
            html.P("Valeur à prédire :"),
            html.Div(children = [
                dcc.Dropdown(options =[
                {'label': 'Frais de port', 'value': 'FRA'},      
                {'label': 'Temps de livraison', 'value': 'LIV'},
                ],value = 'FRA', id='choice3'),
            ])
        ]),        
        html.Div(className = 'choice', children=[
            html.P("Choix des features :"),
            html.Div(id='features')
        ]),
        html.Div( className = 'input-fields', children=[
            html.Div(id='input-fields')
        ]),
        html.Button('Prédire', id='submit-val', n_clicks=0),
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
                {'label': 'ElasticNet', 'value' : 'ElasticNet'},
                {'label': 'DummyRegressor', 'value': 'DummyRegressor'}
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
            id="features_checklist" ))
        elif (target == 'LIV') :
            return dcc.Checklist(
                ['feature1', 'feature2', 'feature3'],
                ['feature1'],
                inline=True)

    #return inputs fields according selected features
    @dash_app.callback(
        Output('input-fields','children'),
        Input('features_checklist','value')
    )
    def get_input_fields(features):
        return(
            html.P("Prix de l'objet"), 
            dcc.Input(id="input1", type="number", disabled='price' not in features),
            html.Br(),
            html.P("Poids (g)"),
            dcc.Input(id="input2", type="number", disabled='product_weight_g' not in features),
            html.Br(),
            html.P("Longueur (cm)"),
            dcc.Input(id="input3", type="number", disabled='product_length_cm' not in features),
            html.Br(),
            html.P("Hauteur (cm)"),
            dcc.Input(id="input4", type="number", disabled='product_height_cm' not in features),
            html.Br(),
            html.P("Largeur (cm)"),
            dcc.Input(id="input5", type="number", disabled='product_width_cm' not in features)
        )       

    # return a prediction and metrics with user inputs
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
            #TO DO
            df= pd.DataFrame()    

        X.fillna(0, inplace=True) # a modifier plus tard
        prediction, mae, mse, rmse, r2 = get_results_by_model(model, X, y, X_to_predict)

        print(prediction)
        print(mae)
        print(mse)
        print(rmse)
        print(r2)

        return html.Div(children=[
            html.P(f"Prix estimé : {prediction[0]:.2f}"),            
            html.P(f"MAE : {mae:.2f}"),
            html.P(f"MSE : {mse:.2f}"),
            html.P(f"RMSE : {rmse:.2f}"),
            html.P(f"R2 score : {r2:.2f}")
        ])

    return dash_app



    
    

    
