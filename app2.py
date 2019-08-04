import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly_express as px

import pandas as pd

df = pd.read_csv('homicides.csv')

app = dash.Dash(__name__)

opts = [ dict(label=t, value=t)
         for t in df['Type'].unique() ]

app.layout = html.Div(
    [dcc.Markdown("""
# Homicides in Australia

Select homicide types from the dropdown menu.
    """),
     dcc.Dropdown(id='select-type',
                  options=opts,
                  multi=True,
                  value='Total'),
     dcc.Graph(id='graph')
    ])


@app.callback(Output('graph', 'figure'),
              [Input('select-type', 'value')])
def make_figure(select_type):
    select_type = select_type
                  if isinstance(select_type, list)
                  else [select_type]
    fig = px.line(
        df.loc[df['Type'].isin(select_type)],
        x='Year',
        y='Homicides',
        color='Type',
        line_dash='Type',
        template='presentation',
        category_orders={'Type': ['Total']},
        )
    return fig.update_traces(mode='lines+markers')

if __name__ == '__main__':
    app.run_server(debug=True)
