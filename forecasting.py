import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def load_forecaster():
    # Dummy: no persistent model for forecasting, stateless
    return None

def forecast_expense_amounts(df, forecaster=None):
    # Requires 'date' and 'amount' columns
    if "date" not in df.columns or "amount" not in df.columns:
        return pd.DataFrame({"error": ["Missing 'date' or 'amount' column!"]})
    df["date"] = pd.to_datetime(df["date"])
    df.sort_values("date", inplace=True)
    df_grouped = df.groupby("date")["amount"].sum()
    try:
        model = ExponentialSmoothing(df_grouped, seasonal=None, trend="add").fit()
        forecast = model.forecast(steps=5)
    except Exception:
        forecast = pd.Series([df_grouped.mean()] * 5, 
                             index=pd.date_range(df_grouped.index[-1], periods=5, freq='D'))
    return forecast