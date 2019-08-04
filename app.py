import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly_express as px

import pandas as pd

df = pd.read_csv('homicides.csv')

fig = px.line(
    df,
    x='Year',
    y='Homicides',
    color='Type',
    #facet_col='Type',
    #template='presentation',
    )
#fig.update_traces(mode='lines+markers')

app = dash.Dash(__name__)

app.layout = html.Div(
    [html.H1("Homicides in Australia"),
    dcc.Graph(figure=fig)
    ])

app.run_server(debug=True)
