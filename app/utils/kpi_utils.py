from sklearn.metrics import r2_score, root_mean_squared_error
import numpy as np
import pandas as pd

def calculate_kpis(df, prediction_df):
    # Align on datetime or index
    merged = df[['date', 'plant_energy_before(kwh)']].merge(
        prediction_df[['date', 'predicted_plant_energy_before(kwh)']],
        on='date',
        how='inner'
    )

    y_true = merged['plant_energy_before(kwh)']
    y_pred = merged['predicted_plant_energy_before(kwh)']

    # Drop rows with NaNs just to be safe
    valid = (~y_true.isna()) & (~y_pred.isna())
    y_true = y_true[valid]
    y_pred = y_pred[valid]

    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)

    return {
        "r2": round(r2, 4),
        "rmse": round(rmse, 2)
    }


