import dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
from model.energy_predictor import EnergyPredictor
from utils.kpi_utils import calculate_kpis
import numpy as np
import joblib

# Load pre-trained model
model = EnergyPredictor()
model.load_model('model/best_model.pkl')
scaler = joblib.load('model/scaler.pkl')

def register_callbacks(app):
    
    @ app.callback(
        [Output("total-predicted-kwh", "children"),  
        Output("total-actual-kwh", "children")],     
        Output("total-savings-kwh", "children"),
        Output("savings-percent", "children"),
        Output("total-savings-thb", "children"),
        Output("energy-comparison-graph", "figure"),
        Output("temp-graph", "figure"),
        Output("humidity-graph", "figure"),
        Output("wind-uv-graph", "figure"),
        Output("r2-metric", "children"),
        Output("rmse-metric", "children"),   
        Output("CVRMSE-metric", "children"),
        Output("NMBE-metric", "children"),   
        [Input("interval-component", "n_intervals")]
        )


    def update_dashboard(n_intervals):
        # Load data
        df = pd.read_csv('data/energy_weather_df.csv')
        df['date'] = pd.to_datetime(df['date'])

        df['month'] = df['date'].dt.month
        df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
        df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)


        # Filter only the rows between '2024-07-29' and '2025-03-03' for prediction
        predict_start = pd.to_datetime('2024-07-29')
        predict_end = pd.to_datetime('2025-03-03')
        prediction_df = df[(df['date'] >= predict_start) & (df['date'] <= predict_end)].copy()

        numerical_cols = ['tempmin', 'humidity', 'feelslike', 'windspeed', 'uvindex']
        prediction_df[numerical_cols] = scaler.transform(prediction_df[numerical_cols])
        # Make prediction (handle missing values just in case)
        features = ['tempmin', 'humidity', 'feelslike', 'windspeed', 'uvindex', 'month_sin', 'month_cos']
        # prediction_df = prediction_df.dropna(subset=features)  # Ensure no NaNs
        prediction_df['predicted_plant_energy_before(kwh)'] = model.predict(prediction_df[features])

        # KPI Calculation
        kpis = calculate_kpis(df, prediction_df)

        actual_start = pd.to_datetime('2024-09-02')
        actual_end = pd.to_datetime('2025-03-03')
        df_actual = df[df['plant_energy_after(kwh)'].notna()]
        prediction_df1 = prediction_df[(prediction_df['date'] >= actual_start) & (prediction_df['date'] <= actual_end)].copy()


        comparison_df = pd.merge(df_actual[['date', 'plant_energy_after(kwh)']],
                prediction_df1[['date', 'predicted_plant_energy_before(kwh)']],
                on='date',
                how='left')
        
        comparison_df['savings_kwh'] = (
        comparison_df['predicted_plant_energy_before(kwh)'] -
        comparison_df['plant_energy_after(kwh)']
        )

        # Calculate percentage savings
        comparison_df['savings_percent'] = (
        comparison_df['savings_kwh'] /
        comparison_df['predicted_plant_energy_before(kwh)']
        ) * 100

        # Calculate savings
        total_baseline_kwh = comparison_df['predicted_plant_energy_before(kwh)'].sum()
        total_actual_kwh = comparison_df['plant_energy_after(kwh)'].sum()
        total_savings_kwh = comparison_df['savings_kwh'].sum()
        average_savings_percent = comparison_df['savings_percent'].mean()

        cost_per_kwh = 3.72
        estimated_cost_savings = total_savings_kwh * cost_per_kwh
        estimated_cost_savings_per_month = estimated_cost_savings/7

        # Filter by date
        before_ai = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2024-07-28')]
        predicted = prediction_df[(prediction_df['date'] >= '2024-07-29') & (prediction_df['date'] <= '2025-03-03')]
        after_ai = df[(df['date'] >= '2024-09-02') & (df['date'] <= '2025-03-03')]

        # Energy Comparison Graph
        energy_comparison_figure = go.Figure()
        if not before_ai.empty:
            energy_comparison_figure.add_trace(go.Scatter(
                x=before_ai['date'], y=before_ai['plant_energy_before(kwh)'],
                mode='lines', name="Before AI", line=dict(color='blue')))
        if not predicted.empty:
            energy_comparison_figure.add_trace(go.Scatter(
                x=predicted['date'], y=predicted['predicted_plant_energy_before(kwh)'],
                mode='lines', name="Predicted Before AI", line=dict(color='red', dash='dash')))
        if not after_ai.empty:
            energy_comparison_figure.add_trace(go.Scatter(
                x=after_ai['date'], y=after_ai['plant_energy_after(kwh)'],
                mode='lines', name="After AI", line=dict(color='green')))

        energy_comparison_figure.update_layout(
            title="Energy Usage Before, Predicted, and After AI",
            xaxis_title="Date", yaxis_title="Energy (kWh)")


        # Temperature Graph
        temp_figure = go.Figure([
            go.Scatter(x=df['date'], y=df['tempmin'], mode='lines', name="Min Temperature", line=dict(color='orange')),
            go.Scatter(x=df['date'], y=df['feelslike'], mode='lines', name="Feels Like", line=dict(color='green')),
        ])
        temp_figure.update_layout(title="Temperature Trends", xaxis_title="Date", yaxis_title="Temperature (°C)")

        # Humidity Graph
        humidity_figure = go.Figure([
            go.Scatter(x=df['date'], y=df['humidity'], mode='lines', name="Humidity", line=dict(color='blue')),
        ])
        humidity_figure.update_layout(title="Humidity Trend", xaxis_title="Date", yaxis_title="Humidity (%)")

        # Wind + UV Graph
        wind_uv_figure = go.Figure([
            go.Scatter(x=df['date'], y=df['windspeed'], mode='lines', name="Wind Speed", line=dict(color='purple')),
            go.Scatter(x=df['date'], y=df['uvindex'], mode='lines', name="UV Index", line=dict(color='red')),
        ])
        wind_uv_figure.update_layout(title="Wind Speed & UV Index", xaxis_title="Date", yaxis_title="Value")


        return (
                f"{total_baseline_kwh:.2f} kWh",  
                f"{total_actual_kwh:.2f} kWh",     
                f"{total_savings_kwh:.2f} kWh",
                f"{average_savings_percent:.2f}%",
                f"{estimated_cost_savings:.2f} THB",
                energy_comparison_figure,
                temp_figure,
                humidity_figure,
                wind_uv_figure,
                f"R²: 0.8866",
                f"RMSE: 2742.68",
                f"CVRMSE: 0.0503",
                f"NMBE: -0.0028")


