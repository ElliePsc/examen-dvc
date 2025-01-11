import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
import pickle

def grid_search(input_dir, output_dir):
    # Charger les fichiers
    X_train = pd.read_csv(f"{input_dir}/X_train_scaled.csv")
    y_train = pd.read_csv(f"{input_dir}/y_train.csv").values.ravel()
    
    # Modèle et grille de paramètres
    model = GradientBoostingRegressor()
    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [3, 5],
        "learning_rate": [0.01, 0.1]
    }
    
    # Recherche des meilleurs paramètres
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring="r2")
    grid_search.fit(X_train, y_train)
    
    # Sauvegarder les meilleurs paramètres
    with open(f"{output_dir}/best_params.pkl", "wb") as f:
        pickle.dump(grid_search.best_params_, f)

if __name__ == "__main__":
    grid_search("data/processed_data", "models")
