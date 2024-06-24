import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_sales_data.csv')

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Dash app
app = dash.Dash(__name__)

#the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Sales Data Visualiser'),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            df.sort_values('date'), 
            x='date', 
            y='sales', 
            title='Sales Over Time',
            labels={'date': 'Date', 'sales': 'Sales'}
        )
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

