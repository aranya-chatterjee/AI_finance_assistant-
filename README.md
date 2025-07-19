# AI Finance Assistant

An intelligent personal finance assistant web application built with Python and Streamlit. This project helps users manage, analyze, and visualize their financial transactions, offering automated categorization, forecasting, and personalized budget suggestions powered by machine learning models.

## Features

- **Expense Categorization:** Automatically classifies transaction descriptions into categories using Logistic Regression and TF-IDF.
- **Expense Forecasting:** Predicts future expenses using Exponential Smoothing time series analysis.
- **Budget Prediction:** Suggests monthly budgets based on income and savings using Linear Regression.
- **Interactive Web App:** User-friendly interface for uploading transactions, viewing insights, and exploring visualizations.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aranya-chatterjee/AI_finance_assistant-.git
   cd AI_finance_assistant-
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

- Upload your transactions as a CSV file (see `transactions_sample.csv` for format).
- Navigate through the sidebar to:
  - View categorized transactions
  - Forecast upcoming expenses
  - Get personalized budget recommendations

## Example CSV Format

```csv
date,amount,description,category
2024-06-01,35.50,Uber ride,Transport
2024-06-02,12.00,Starbucks coffee,Food
...
```
See `transactions_sample.csv` for a full sample.

## Project Structure

- `streamlit_app.py`: Main app interface
- `categorization.py`: Expense categorization model
- `forecasting.py`: Expense forecasting model
- `budget.py`: Budget prediction model
- `requirements.txt`: Python dependencies
- `transactions_sample.csv`: Sample data

## Credits

This project was inspired by and adapted from [nirajdsouza/personal-finance-assistant-ai-agent](https://github.com/nirajdsouza/personal-finance-assistant-ai-agent/tree/main).  
Special thanks to Niraj Dsouza for providing foundational ideas and code structure.

## License

This project is licensed under the MIT License.

---

**Created by [aranya-chatterjee](https://github.com/aranya-chatterjee)**
