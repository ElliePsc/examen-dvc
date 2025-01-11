import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle

def train_model(input_dir, model_dir):
    # Charger les données d'entraînement
    X_train = pd.read_csv(f"{input_dir}/X_train_scaled.csv")
    y_train = pd.read_csv(f"{input_dir}/y_train.csv")

    # Identifier et sélectionner uniquement les colonnes numériques
    numeric_columns = X_train.select_dtypes(include=['float64', 'int64']).columns
    X_train = X_train[numeric_columns]

    # Charger les meilleurs paramètres
    best_params = pd.read_pickle(f"{model_dir}/best_params.pkl")

    # Initialiser et entraîner le modèle
    model = GradientBoostingRegressor(**best_params)
    model.fit(X_train, y_train.values.ravel())

    # Sauvegarder le modèle
    with open(f"{model_dir}/gbr_model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model("data/processed_data", "models")
