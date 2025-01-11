import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle

def train_model(input_dir, output_dir):
    # Charger les fichiers
    X_train = pd.read_csv(f"{input_dir}/X_train_scaled.csv")
    y_train = pd.read_csv(f"{input_dir}/y_train.csv").values.ravel()
    
    # Charger les meilleurs paramètres
    with open(f"{output_dir}/best_params.pkl", "rb") as f:
        best_params = pickle.load(f)
    
    # Entraîner le modèle
    model = GradientBoostingRegressor(**best_params)
    model.fit(X_train, y_train)
    
    # Sauvegarder le modèle
    with open(f"{output_dir}/gbr_model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model("data/processed_data", "models")