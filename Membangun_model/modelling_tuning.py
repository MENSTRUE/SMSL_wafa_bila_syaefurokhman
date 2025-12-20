import pandas as pd
import mlflow
import dagshub
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import os

# 1. Masukkan Nama Owner dan Repo DagsHub Anda yang sebenarnya
OWNER = 'MENSTRUE' # Ganti jika berbeda
REPO_NAME = 'Eksperimen_SML_wafa_bila_syaefurokhman' # Ganti jika berbeda

# Inisialisasi DagsHub
dagshub.init(repo_owner=OWNER, repo_name=REPO_NAME, mlflow=True)

# Set Tracking URI
mlflow.set_tracking_uri(f"https://dagshub.com/{OWNER}/{REPO_NAME}.mlflow")

# 2. Path Data
X_path = '../preprocessing/nearest_earth_object_preprocessing/X_train.csv'
y_path = '../preprocessing/nearest_earth_object_preprocessing/y_train.csv'

X_train = pd.read_csv(X_path)
y_train = pd.read_csv(y_path)

# Memulai Run MLflow
with mlflow.start_run(run_name="NASA_Asteroid_Tuning_Advance"):
    # Parameter tuning
    n_estimators = 150
    max_depth = 10

    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train.values.ravel())

    # Manual Logging
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)

    y_pred = model.predict(X_train)
    acc = accuracy_score(y_train, y_pred)
    mlflow.log_metric("train_accuracy", acc)

    # Artefak Tambahan
    # Artefak 1: Plot Confusion Matrix
    cm = confusion_matrix(y_train, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(f"Confusion Matrix - {REPO_NAME}")
    plt.savefig("confusion_matrix.png")
    mlflow.log_artifact("confusion_matrix.png")

    # Artefak 2: Requirements file
    # Pastikan file requirements.txt sudah Anda buat di folder yang sama
    mlflow.log_artifact("Membangun_model/requirements.txt")

    # Simpan Model
    mlflow.sklearn.log_model(model, "model_asteroid_nasa")

    print(f"Berhasil! Data terkirim ke DagsHub {OWNER}/{REPO_NAME}")
    print(f"Akurasi: {acc}")