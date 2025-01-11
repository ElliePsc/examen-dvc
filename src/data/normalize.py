import pandas as pd
from sklearn.preprocessing import StandardScaler

def normalize_data(input_dir, output_dir):
    # Charger les fichiers d'entraînement et de test
    X_train = pd.read_csv(f"{input_dir}/X_train.csv")
    X_test = pd.read_csv(f"{input_dir}/X_test.csv")

    # Identifier les colonnes numériques (exclure les dates)
    numeric_columns = X_train.select_dtypes(include=['float64', 'int64']).columns
    non_numeric_columns = X_train.select_dtypes(exclude=['float64', 'int64']).columns

    # Extraire uniquement les colonnes numériques pour la normalisation
    X_train_numeric = X_train[numeric_columns]
    X_test_numeric = X_test[numeric_columns]

    # Appliquer une normalisation standard
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_numeric)
    X_test_scaled = scaler.transform(X_test_numeric)

    # Créer de nouveaux DataFrames avec les colonnes normalisées
    X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=numeric_columns)
    X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=numeric_columns)

    # Ajouter les colonnes non numériques (comme les dates) aux DataFrames
    X_train_final = pd.concat([X_train_scaled_df, X_train[non_numeric_columns]], axis=1)
    X_test_final = pd.concat([X_test_scaled_df, X_test[non_numeric_columns]], axis=1)

    # Sauvegarder les fichiers finalisés
    X_train_final.to_csv(f"{output_dir}/X_train_scaled.csv", index=False)
    X_test_final.to_csv(f"{output_dir}/X_test_scaled.csv", index=False)

if __name__ == "__main__":
    normalize_data("data/processed_data", "data/processed_data")
