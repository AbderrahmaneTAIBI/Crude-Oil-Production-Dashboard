import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
load_figure_template('FLATLY')

# load preprocessed dataset
df_ts = pd.read_csv("/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/Crude Oil Production by Country/Crude Oil Production by Country Pre-processed.csv", parse_dates=['index'])

# load bubble map data
df_map = pd.read_csv('/Users/macbookpro/Desktop/LinkedIn Work/LinkedIn Posts/Crude Oil Production by Country/TopProducersPerYear.csv')

# create a Dash app
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.FLATLY])

# define country options for dropdown menu
country_options = [{'label': c, 'value': c} for c in df_ts.columns]

# define layout of the app
app.layout = html.Div(children=[
    html.H1(children='Crude Oil Production Dashboard', style={"text-align": "center"}),
    html.Div(children=[
        dcc.Graph(id='world-map'),
        dcc.Slider(
            id='year-slider',
            min=df_map['Year'].min(),
            max=df_map['Year'].max(),
            value=df_map['Year'].min(),
            marks={str(year): str(year) for year in df_map['Year'].unique()},
            step=None,
            tooltip={'always_visible': True, 'placement': 'bottom'}
        )
    ], style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'}),
    html.Div(children=[
        dcc.Dropdown(
            id='country-dropdown',
            options=country_options,
            value=['United States'],  # default selected country
            multi=True  # allow selecting multiple countries
        ),
        dcc.Graph(id='oil-production-plot')
    ], style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'})
])


# define callback function for the dropdown menu and time series plot
@app.callback(
    [dash.dependencies.Output('oil-production-plot', 'figure'), 
     dash.dependencies.Output('world-map', 'figure')],
    [dash.dependencies.Input('country-dropdown', 'value'),
     dash.dependencies.Input('year-slider', 'value')]
)
def update_figures(selected_countries, selected_year):
    # filter time series data by selected countries
    filtered_df_ts = df_ts[selected_countries]
    # melt the dataframe to long format
    melted_df_ts = pd.melt(filtered_df_ts.reset_index(), id_vars=['index'], var_name='Country', value_name='Production')
    # create line chart using Plotly Express
    fig_ts = px.line(melted_df_ts, x='index', y='Production', color='Country')
    fig_ts.update_layout(title=f'Crude Oil Production by Country')

    # filter bubble map data by selected year and top 20 producers
    filtered_df_map = df_map[df_map['Year'] == selected_year].nlargest(20, 'Production')
    # create the world map using Plotly Express
    fig_map = px.scatter_geo(filtered_df_map, locations='Country', locationmode='country names',
                             hover_name='Country', size='Production', projection='natural earth')

    # set the title of the map
    fig_map.update_layout(title=f'Top 20 Crude Oil Producers in {selected_year}')
    
    return fig_ts, fig_map

if __name__ == '__main__':
    app.run_server(debug=True)
