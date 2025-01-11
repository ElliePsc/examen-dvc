# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposé pour mettre en place la solution de l'examen. 

```bash       
├── examen_dvc          
│   ├── data       
│   │   ├── processed      
│   │   └── raw       
│   ├── metrics       
│   ├── models      
│   │   ├── data      
│   │   └── models        
│   ├── src       
│   └── README.md.py       
```
N'hésitez pas à rajouter les dossiers ou les fichiers qui vous semblent pertinents.

Vous devez dans un premier temps *Fork* le repo et puis le cloner pour travailler dessus. Le rendu de cet examen sera le lien vers votre dépôt sur DagsHub. Faites attention à bien mettre https://dagshub.com/licence.pedago en tant que colaborateur avec des droits de lecture seulement pour que ce soit corrigé.

Vous pouvez télécharger les données à travers le lien suivant : https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv.


Mise à jour:

1/

├── examen_dvc          
│   ├── data       
│   │   ├── processed_data      # Données transformées (e.g., X_train.csv, y_test.csv)
│   │   └── raw_data            # Données brutes (e.g., raw.csv)
│   ├── metrics                 # Contient les fichiers .json avec les métriques du modèle
│   ├── models                  # Contient les modèles sauvegardés (.pkl ou autres)
│   ├── src                     # Contient tous les scripts Python
│   │   ├── data                # Scripts liés aux données
│   │   │   ├── data_split.py       # Split des données
│   │   │   ├── normalize.py        # Normalisation
│   │   ├── models              # Scripts liés aux modèles
│   │   │   ├── grid_search.py      # Recherche des hyperparamètres
│   │   │   ├── training.py         # Entraînement du modèle
│   │   │   ├── evaluate.py         # Évaluation du modèle
│   └── README.md               # Documentation du projet

à la fin:
.
├── data/
│   ├── raw_data/
│   │   └── raw.csv
│   ├── processed_data/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
├── metrics/
│   └── scores.json
├── models/
│   ├── gbr_model.pld
│   └── best_params.pkl
├── src/
│   ├── data/
│       ├── data_split.py
│       └── normalize.py
│   ├── models/
│       ├── grid_search.py
│       ├── training.py
│       └── evaluate.py
├── dvc.yaml
├── dvc.lock
├── params.yaml
└── README.md