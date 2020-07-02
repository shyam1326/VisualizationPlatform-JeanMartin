import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_auth
#import pandas_profiling



markdown_text = '''
    ![Image](data:image/png;base64,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)
    '''

# markdown_text_1 = '''
#     ![Image](https://media0.giphy.com/media/3oKIPEqDGUULpEU0aQ/giphy.gif)
#     '''


df = pd.read_csv('dataset/sample_data1.csv', encoding='ISO-8859-1')
features = df.columns

for i in df.columns:
    if df[i].dtypes=='int64':
        df[i] = df[i].astype('float64')

#df7 = pandas_profiling.ProfileReport(df)
#df7.to_file('Report.html')


app = dash.Dash()

Username_Password_Pairs = {'jeanmartin' : 'welcome2jeanmartin'}

auth = dash_auth.BasicAuth(app, Username_Password_Pairs)
server = app.server

app.layout = html.Div(children=[
    dcc.Markdown(children=markdown_text, style={'textAlign': 'center'}),
    html.H1('Visualization Platform', style={'textAlign': 'center'}),
    #dcc.Markdown(children=markdown_text_1, style={'textAlign': 'center'}),


    html.Div([
        html.H3('X_Axis', style= {'fontSize' : 24}),
        dcc.Dropdown(id='x_axis',
                     options=[{'label': str(i), 'value': i} for i in features],
                     value='Industry',
                     placeholder='Select the X_axis',
                     style= {'border': '2px gold solid'})
    ], style={'width': '32%', 'display': 'inline-block'}),


    html.Div([
        html.H3('Y_Axis', style= {'fontSize' : 24}),
        dcc.Dropdown(id='y_axis',
                     options=[{'label': str(i), 'value': i} for i in features],
                     value='FTE',
                     placeholder='Select the Y_axis',
                     style= {'border': '2px gold solid'})
    ], style={'width': '32%', 'display': 'inline-block'}),

    html.Div([
            html.H3('Z_Axis', style= {'fontSize' : 24}),
            dcc.Dropdown(id='z_axis',
                         options=[{'label': str(i), 'value': i} for i in features],
                         value='',
                         multi= True,
                         placeholder='Select the Z_axis',
                         style= {'border': '2px gold solid'})
        ], style={'width': '32%', 'display': 'inline-block'}),

    html.Div([
    html.Button(id='submit',
                n_clicks=0,
                children='submit Here',
                style= {'fontSize': 24})
    ]),

    dcc.Graph(id='graph',style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='graph1', style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id = 'graph2'),
    dcc.Graph(id='graph3'),

])

@app.callback(Output('graph', 'figure'),
              [Input('submit', 'n_clicks')],
              [State('x_axis', 'value'),
              State('y_axis', 'value')],
              )
def update_figure(n_clicks,x_axis, y_axis):
    if (df[x_axis].dtypes == 'float64'):
        return {
            'data': [go.Histogram(
                x=df[x_axis]
            )],
            'layout': go.Layout(title= 'Histogram of ' + x_axis,
                                xaxis={'title': x_axis},
                                hovermode='closest'
                                )
        }
    elif (df[x_axis].dtypes == 'object'):
        df1 = df[x_axis].value_counts().reset_index()
        df1.columns = ['column', 'counts']
        return {
            'data': [go.Pie(
                labels = df1['column'],
                values= df1['counts']
            )],
            'layout': go.Layout(title= x_axis,
                                #xaxis={'title': x_axis},
                                hovermode='closest'
                                )
        }
@app.callback(Output('graph1', 'figure'),
              [Input('submit', 'n_clicks')],
              [State('x_axis', 'value'),
              State('y_axis', 'value')],
              )
def update_figure(n_clicks, x_axis, y_axis):
    if (df[y_axis].dtypes == 'float64'):
        return {
            'data': [go.Histogram(
                x=df[y_axis]
            )],
            'layout': go.Layout(title='Histogram of ' + x_axis,
                                xaxis={'title': y_axis},
                                hovermode='closest'
                                )
        }
    elif (df[y_axis].dtypes == 'object'):
        df2 = df[y_axis].value_counts().reset_index()
        df2.columns = ['column', 'counts']
        return {
            'data': [go.Pie(
                labels = df2['column'],
                values= df2['counts']
            )],
            'layout': go.Layout(title= y_axis,
                                #xaxis={'title': x_axis},
                                hovermode='closest'
                                )
        }
@app.callback(Output('graph2', 'figure'),
              [Input('submit', 'n_clicks')],
              [State('x_axis', 'value'),
              State('y_axis', 'value')],
              )
def update_figure(n_clicks,x_axis, y_axis):
    if (df[x_axis].dtypes == 'float64') & (df[y_axis].dtypes == 'float64'):
        return {
        'data': [go.Scatter(
            x = df[x_axis],
            y = df[y_axis],
            mode = 'markers',
            marker= {'color': 'red'}
        )],
            'layout': go.Layout(title= x_axis + ' vs ' + y_axis,
                                xaxis={'title': x_axis},
                                yaxis={'title': y_axis},
                                hovermode='closest'
                                )
        }
    elif (df[x_axis].dtypes == 'object') & (df[y_axis].dtypes == 'float64'):
        df3 = df.groupby([x_axis])[[y_axis]].sum().reset_index()
        return {
            'data': [go.Bar(
                    x = df3[x_axis],
                    y = df3[y_axis],
                    marker= {'color': 'tan'}
        )],
            'layout': go.Layout(title= x_axis + ' vs Sum of ' + y_axis ,
                                xaxis={'title': x_axis},
                                yaxis={'title': 'sum of ' + y_axis},
                                hovermode='closest'
                                )
        }
    elif (df[x_axis].dtypes == 'float64') & (df[y_axis].dtypes == 'object'):
        df4 = df.groupby([y_axis])[[x_axis]].count().reset_index()
        return {
            'data': [go.Bar(
                x=df4[x_axis],
                y=df4[y_axis],
                orientation= 'h',
                marker={'color': 'orange'}
            )],
            'layout': go.Layout(title= x_axis + ' vs Count of ' + y_axis ,
                                #xaxis={'title': x_axis},
                                yaxis={'title': y_axis},
                                hovermode='closest'
                                )
        }
    elif (df[x_axis].dtypes == 'object') & (df[y_axis].dtypes == 'object'):
        df5 = df.groupby([x_axis, y_axis]).count().reset_index()
        return {
            'data': [go.Bar(
                x=df5[x_axis],
                y=df5[y_axis],
                name = i) for i in df5[y_axis].unique()
                #marker={'color': 'violet'}
            ],
            'layout': go.Layout(title= x_axis + ' vs ' + y_axis,
                                xaxis={'title': x_axis},
                                yaxis={'title': y_axis},
                                barmode='stack',
                                hovermode='closest'
                                )
        }
    else:
        return {
            'data': [],
            'layout': go.Layout()
        }


@app.callback(Output('graph3', 'figure'),
              [Input('submit', 'n_clicks')],
              [State('x_axis', 'value'),
              State('y_axis', 'value'),
              State('z_axis', 'value')],
              )
def update_figure(n_clicks,x_axis, y_axis, z_axis):
    traces = []
    traces.append(
        {'x': df.groupby([x_axis]).mean().reset_index()[x_axis], 'y': df.groupby([x_axis]).mean().reset_index()[y_axis],'type': 'line', 'name': y_axis}),

    for col in z_axis:
        traces.append({'x': df.groupby([x_axis]).mean().reset_index()[x_axis], 'y': df.groupby([x_axis]).mean().reset_index()[col], 'type': 'line', 'name': col}),

    fig = {
        'data': traces,
        'layout': {'title': x_axis + ' vs Mean of ' + y_axis ,
                   'xaxis' : {'title': x_axis},
                   'hovermode': 'closest'}
    }
    return fig



if __name__ == '__main__':
    app.run_server()

