import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

def load_expense_categorizer(model_path="categorizer.pkl", vectorizer_path="tfidf.pkl"):
    # Load model and vectorizer, or create dummy if not found
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        with open(vectorizer_path, "rb") as f:
            vectorizer = pickle.load(f)
    except FileNotFoundError:
        model = LogisticRegression()
        vectorizer = TfidfVectorizer()
    return {"model": model, "vectorizer": vectorizer}

def categorize_expenses(df, categorizer):
    # Requires 'description' column
    if "description" not in df.columns:
        return pd.DataFrame({"error": ["Missing 'description' column!"]})
    X = categorizer["vectorizer"].fit_transform(df["description"].astype(str))
    # Dummy prediction if model not fitted
    try:
        preds = categorizer["model"].predict(X)
    except Exception:
        preds = ["Other"] * len(df)
    df["predicted_category"] = preds
    return df