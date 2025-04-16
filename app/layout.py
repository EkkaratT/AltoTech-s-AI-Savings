# import dash_html_components as html
# import dash_core_components as dcc
from dash import dcc, html
import plotly.graph_objects as go

def create_layout():
    layout = html.Div([
        html.H1("AltoTech Energy Savings Dashboard"),
        html.Div([
            html.H3("Key Performance Indicators (KPIs)"),
            html.Div([
                html.Div([
                    html.P("Total Predicted (Baseline)"),
                    html.H4(id="total-predicted-kwh", children="0 kWh")
                ], className="kpi"),
                html.Div([
                    html.P("Total Actual Usage"),
                    html.H4(id="total-actual-kwh", children="0 kWh")
                ], className="kpi"),
                html.Div([
                    html.P("Verified Energy Savings (kWh)"),
                    html.H4(id="total-savings-kwh", children="0 kWh")
                ], className="kpi"),
                html.Div([
                    html.P("Energy Savings (%)"),
                    html.H4(id="savings-percent", children="0%")
                ], className="kpi"),
                html.Div([
                    html.P("Estimated Savings (THB)"),
                    html.H4(id="total-savings-thb", children="0 THB")
                ], className="kpi")
            ], className="kpi-container"),
        ], className="kpi-section"),

        html.Div([
            html.H3("Key weather trends alongside Energy"),
            # dcc.Graph(id="energy-comparison-graph"),
            # dcc.Graph(id="weather-trends-graph")
            dcc.Graph(id="energy-comparison-graph"),
            dcc.Graph(id="temp-graph"),
            dcc.Graph(id="humidity-graph"),
            dcc.Graph(id="wind-uv-graph"),

        ], className="graph-container"),

        html.Div([
        html.H3("Model Performance Metrics", style={'textAlign': 'center'}),
        html.Div([
            html.Div(id="r2-metric", children="R²: 0.00", className="kpi-card"),
            html.Div(id="rmse-metric", children="RMSE: 0.00", className="kpi-card"),
            html.Div(id="CVRMSE-metric", children="CVRMSE: 0.00", className="kpi-card"),
            html.Div(id="NMBE-metric", children="NMBE: 0.00", className="kpi-card"),
        ], className="metric-row")
        ], className="metrics-section"),


        dcc.Interval(id='interval-component', interval=1000 * 60 * 5, n_intervals=0)  # Update every 5 minutes
    ])
    return layout
