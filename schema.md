graph TD
    A[raw.csv] --> B[data_split.py]
    B --> C[X_train.csv]
    B --> D[X_test.csv]
    B --> E[y_train.csv]
    B --> F[y_test.csv]

    C --> G[normalize.py]
    D --> G
    G --> H[X_train_scaled.csv]
    G --> I[X_test_scaled.csv]

    E --> J[grid_search.py]
    J --> K[best_params.pkl]

    H --> L[training.py]
    E --> L
    K --> L
    L --> M[gbr_model.pld]

    M --> N[evaluate.py]
    I --> N
    F --> N
    N --> O[prediction.csv]
    N --> P[scores.json]