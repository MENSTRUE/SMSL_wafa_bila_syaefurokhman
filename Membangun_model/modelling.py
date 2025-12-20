import pandas as pd
import mlflow
import dagshub
from sklearn.ensemble import RandomForestClassifier
import os

# 1. Hubungkan ke DagsHub biar laporannya Online
OWNER = 'MENSTRUE'
REPO_NAME = 'Eksperimen_SML_wafa_bila_syaefurokhman'

dagshub.init(repo_owner=OWNER, repo_name=REPO_NAME, mlflow=True)
mlflow.set_tracking_uri(f"https://dagshub.com/{OWNER}/{REPO_NAME}.mlflow")

# 2. Path Data
X_path = '../preprocessing/nearest_earth_object_preprocessing/X_train.csv'
y_path = '../preprocessing/nearest_earth_object_preprocessing/y_train.csv'

X_train = pd.read_csv(X_path)
y_train = pd.read_csv(y_path)

# 3. Autolog
mlflow.autolog()

with mlflow.start_run(run_name="NASA_Asteroid_Basic"):
    # Pakai parameter default aja karena ini versi Basic
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train.values.ravel())

    print("Modelling Basic Selesai! Cek DagsHub gih.")