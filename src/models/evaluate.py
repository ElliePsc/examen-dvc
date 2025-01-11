import pandas as pd
import json
from sklearn.metrics import mean_squared_error, r2_score
from joblib import load
import os

def evaluate_model(X_test_path, y_test_path, model_path, prediction_path, scores_path):
    # Charger les données de test et le modèle
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path).iloc[:, 0]  # Suppose que la colonne cible est la première colonne

    # Supprimer les colonnes inutiles comme 'date' si elles existent
    if 'date' in X_test.columns:
        X_test = X_test.drop(columns=['date'])

    model = load(model_path)

    # Faire des prédictions
    predictions = model.predict(X_test)

    # Vérifier si le fichier prediction.csv existe et ajouter les nouvelles données
    if os.path.exists(prediction_path):
        existing_predictions = pd.read_csv(prediction_path)
        new_predictions = pd.DataFrame(predictions, columns=["prediction"])
        updated_predictions = pd.concat([existing_predictions, new_predictions], ignore_index=True)
        updated_predictions.to_csv(prediction_path, index=False)
    else:
        pd.DataFrame(predictions, columns=["prediction"]).to_csv(prediction_path, index=False)

    # Calculer les métriques
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    # Vérifier si le fichier scores.json existe et ajouter les nouvelles données
    scores = {"mse": mse, "r2": r2}
    if os.path.exists(scores_path):
        with open(scores_path, "r") as f:
            existing_scores = json.load(f)
        if isinstance(existing_scores, list):
            existing_scores.append(scores)
        else:
            existing_scores = [existing_scores, scores]
        with open(scores_path, "w") as f:
            json.dump(existing_scores, f, indent=4)
    else:
        with open(scores_path, "w") as f:
            json.dump(scores, f, indent=4)

if __name__ == "__main__":
    evaluate_model(
        "data/processed_data/X_test_scaled.csv",
        "data/processed_data/y_test.csv",
        "models/gbr_model.pkl",
        "data/prediction.csv",
        "metrics/scores.json"
    )


