# -*- coding: utf-8 -*-

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

all_teams_df = pd.read_csv('srcdata/shot_dist_compiled_data_2019_20.csv')


# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
import plotly.express as px

fig = px.scatter(all_teams_df[all_teams_df.group == 'NOP'], x='min_mid', y='player', size='shots_freq', color='pl_pps')

team_names = all_teams_df.group.unique()
team_names.sort()


app = dash.Dash(__name__#,external_stylesheets=[dbc.themes.DARKLY]#
	)

server = app.server

app.layout =html.Header([
                html.H1('Hello Dash', draggable='yes', n_clicks=0),

                html.H3(children='''
        Dash: A web application framework for Python.
    '''),

        #         dcc.Graph(
        # id='example-graph',
        # figure=fig),

    html.Section([
    html.Div([dcc.Dropdown(id='group-select', options=[{'label': i, 'value': i} for i in team_names],
                           value='TOR', style={'width': '140px'})]),
    html.Div(
    	[
    	    dcc.Graph(id='shot-dist-graph', config={'displayModeBar': False}
    	    	),

    	], className='col-6',)
    ]),

    html.Section([
                html.H1('Hello Dash', draggable='yes', n_clicks=0),

                html.H3(children='''
        Dash: A web application framework for Python.
    ''')
                ]
                , className='col-6'),

    html.Div([dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            },


        }
        
    )            

            ] ,className='col-6')
    ])


@app.callback(
    Output('shot-dist-graph', 'figure'),
    [Input('group-select', 'value')]
)
def update_graph(grpname):
    import plotly.express as px
    return px.scatter(all_teams_df[all_teams_df.group == grpname], x='min_mid', y='player', size='shots_freq', color='pl_pps')

   
if __name__ == '__main__':
    app.run_server(debug=True)