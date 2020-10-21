# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   html.Div(children='''Dash Framework: A web application framework for Python.'''),
	
   dcc.Graph(
      id='example-graph',
      figure={
         'data': [
            {'x': ['onion','capsicum','carrot'], 'y': [40, 19, 29], 'type': 'bar', 'name': 'Delhi'},
            {'x': ['onion','capsicum','carrot'], 'y': [25, 47, 50], 'type': 'bar', 'name': u'Mumbai'},
         ],
         'layout': {
            'title': 'Data Visualization for prices of vegies in Delhi and Mumbai'
         }
      }
   )
])

if __name__ == '__main__':
   app.run_server(debug=True)