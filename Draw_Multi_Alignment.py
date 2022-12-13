# Plot multi-sequence alignment
# Place the script in the same directory as the fasta file

import dash
import dash_bio as dashbio
from dash import html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)


data = open('Multi-alignment.fasta').read()

app.layout = html.Div([
    dashbio.AlignmentChart(
        id='my-default-alignment-viewer',
        data=data,
        height=900,
        tilewidth=30,
    ),
    html.Div(id='default-alignment-viewer-output')
])

@app.callback(
    Output('default-alignment-viewer-output', 'children'),
    Input('my-default-alignment-viewer', 'eventDatum')
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)

