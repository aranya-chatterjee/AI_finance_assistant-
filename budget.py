import numpy as np

class DummyBudgetModel:
    def predict(self, X):
        # Simple rule-based prediction
        income, savings = X[0]
        return income * 0.6 + savings * 0.2

def load_budget_predictor(model_path="budget_model.pkl"):
    # Load model or create dummy
    try:
        import pickle
        with open(model_path, "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        model = DummyBudgetModel()
    return model

def predict_budget(income, savings, model):
    X = np.array([[income, savings]])
    try:
        budget = model.predict(X)
    except Exception:
        budget = income * 0.5
    return budget