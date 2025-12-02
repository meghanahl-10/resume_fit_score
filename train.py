import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

def train_model(df):

    X = df[["skill_score", "exp_score"]]
    y = df["fit_score"] * 100    # convert to 0–100

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("Model Performance:")
    print("R2 Score:", r2_score(y_test, preds))
    print("MAE:", mean_absolute_error(y_test, preds))

    with open("model/fit_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved to model/fit_model.pkl")
