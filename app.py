# Classic libraries
import os
import pandas as pd

# Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html

# Custom Function
import scripts.utils as f

# Association of server
app = dash.Dash(__name__)
server = app.server

# Load precomputed data
world = f.load_pickle('world_info.p')

# Layout
app.title = 'Diseases - World cases'
app.layout = html.Div( 
    children=[ 
     html.Div(
            children=[
                html.H1("Diseases - Monthly all over the world", className="header_text"),  
                html.Div('(Last update: {})'.format(world['last_date']), className="date_info"),            
            ],
        ), 
             
	dcc.Graph(id='world_map', figure=world['figure'], config={'scrollZoom': True})
],
)
# Start Server
if __name__ == '__main__':
    app.run_server(debug=True)
