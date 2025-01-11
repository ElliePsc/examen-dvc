import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

def grid_search(input_dir, model_dir):
    # Charger les données d'entraînement
    X_train = pd.read_csv(f"{input_dir}/X_train_scaled.csv")
    y_train = pd.read_csv(f"{input_dir}/y_train.csv")

    # Identifier les colonnes numériques (et supprimer les dates si présentes)
    numeric_columns = X_train.select_dtypes(include=['float64', 'int64']).columns
    X_train = X_train[numeric_columns]

    # Définir le modèle et les hyperparamètres à tester
    model = GradientBoostingRegressor()
    param_grid = {
        'n_estimators': [100, 200],
        'learning_rate': [0.1, 0.01],
        'max_depth': [3, 5],
    }

    # Configurer la recherche par grille
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', verbose=2)
    grid_search.fit(X_train, y_train.values.ravel())

    # Sauvegarder les meilleurs paramètres
    best_params = grid_search.best_params_
    pd.to_pickle(best_params, f"{model_dir}/best_params.pkl")

if __name__ == "__main__":
    grid_search("data/processed_data", "models")

