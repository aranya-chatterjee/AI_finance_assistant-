import streamlit as st
import pandas as pd

from categorization import load_expense_categorizer, categorize_expenses
from forecasting import load_forecaster, forecast_expense_amounts
from budget import load_budget_predictor, predict_budget

# Load models
expense_categorizer = load_expense_categorizer()
forecaster = load_forecaster()
budget_predictor = load_budget_predictor()

st.set_page_config(page_title="AI Finance Assistant", layout="wide")
st.title("AI Finance Assistant")
st.markdown("""
Welcome to your AI-powered finance assistant!  
Upload your transactions, view automated categorizations, generate forecasts, and get personalized budget suggestions.
""")

section = st.sidebar.radio(
    "Go to:",
    [
        "Upload Transactions",
        "Expense Categorization",
        "Expense Forecasting",
        "Budget Prediction"
    ]
)

if "transactions" not in st.session_state:
    st.session_state["transactions"] = None

if section == "Upload Transactions":
    st.header("Upload Transactions")
    st.info("Upload a CSV file with your transactions (date, amount, description, category, etc.)")
    uploaded = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.session_state["transactions"] = df
        st.success("Transactions uploaded successfully!")
        st.write(df.head())

elif section == "Expense Categorization":
    st.header("Expense Categorization")
    df = st.session_state.get("transactions")
    if df is not None:
        st.subheader("Categorized Expenses")
        categorized = categorize_expenses(df, expense_categorizer)
        st.write(categorized)
    else:
        st.warning("Please upload your transactions first.")

elif section == "Expense Forecasting":
    st.header("Expense Forecasting")
    df = st.session_state.get("transactions")
    if df is not None:
        st.subheader("Expense Forecast")
        forecast = forecast_expense_amounts(df, forecaster)
        st.line_chart(forecast)
    else:
        st.warning("Please upload your transactions first.")

elif section == "Budget Prediction":
    st.header("Budget Prediction & Suggestions")
    df = st.session_state.get("transactions")
    if df is not None:
        st.subheader("Budget Suggestions")
        income = st.number_input("Enter your monthly income", min_value=0.0, step=100.0)
        savings = st.number_input("Enter your current savings", min_value=0.0, step=100.0)
        if income > 0 and savings > 0:
            budget = predict_budget(income, savings, budget_predictor)
            st.success(f"Recommended budget for this month: ${budget:.2f}")
        else:
            st.info("Please enter your income and savings.")
    else:
        st.warning("Please upload your transactions first.")

st.sidebar.markdown("---")
st.sidebar.info("AI Finance Assistant by [aranya-chatterjee](https://github.com/aranya-chatterjee)")