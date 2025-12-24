# 🚀 MLflow CI Pipeline – Automated Model Training

Repository ini berisi implementasi Workflow Continuous Integration (CI) untuk sistem Machine Learning menggunakan MLflow Project dan GitHub Actions.
Workflow ini memungkinkan proses re-training model berjalan otomatis setiap kali terjadi perubahan kode (push) pada branch utama.

📌 Tujuan Workflow

Workflow CI ini dibuat untuk memenuhi Kriteria 3 – Membangun Workflow CI, dengan tujuan:

Mengotomatiskan proses training model Machine Learning

Menjalankan MLflow Project secara konsisten dan reproducible

Memastikan model dapat dilatih ulang secara otomatis ketika trigger dipantik

Menyediakan fondasi untuk tahapan monitoring dan deployment selanjutnya

🗂️ Struktur Repository
Workflow-CI/
├── .github/
│   └── workflows/
│       └── ci.yml
├── MLProject/
│   ├── modelling.py
│   ├── conda.yaml
│   ├── MLProject
│   ├── diabetes_preprocessing/
│   │   └── diabetes_preprocessed.csv
│   └── README.md
└── README.md

⚙️ Teknologi yang Digunakan

Python 3.9

MLflow Project

Scikit-Learn

XGBoost

GitHub Actions

🔁 Alur Workflow CI

Workflow CI berjalan dengan alur sebagai berikut:

Trigger

Workflow aktif setiap kali terjadi push ke branch main

Dapat dijalankan secara manual melalui workflow_dispatch

Checkout Repository

Mengambil source code terbaru dari repository GitHub

Set Up Python Environment

Menggunakan Python versi 3.9

Install Dependencies

Menginstal library yang dibutuhkan seperti MLflow, pandas, scikit-learn, dan xgboost

Run MLflow Project

Menjalankan perintah mlflow run . pada folder MLProject

Training model dilakukan secara otomatis menggunakan dataset hasil preprocessing

Metric dan parameter dicatat melalui MLflow Tracking (local)

▶️ File Workflow CI

File workflow CI berada pada:

.github/workflows/ci.yml


Isi utama workflow:

name: MLflow CI Pipeline

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  train-mlflow:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          pip install mlflow pandas scikit-learn xgboost

      - name: Run MLflow Project (Training)
        env:
          MLFLOW_TRACKING_URI: file:./mlruns
          MLFLOW_ARTIFACT_URI: file:./mlruns
        run: |
          cd MLProject
          mkdir -p mlruns
          mlflow run . --env-manager=local

✅ Hasil Workflow

Workflow berhasil dijalankan tanpa error

Model berhasil dilatih secara otomatis

MLflow Project berjalan dengan baik di environment CI

Workflow siap digunakan sebagai dasar untuk Monitoring & Logging (Kriteria 4)

📸 Bukti Keberhasilan

Workflow CI berhasil dijalankan dengan status Success (✔) pada GitHub Actions, ditunjukkan melalui halaman Actions pada repository ini.

🏁 Kesimpulan

Dengan adanya workflow CI ini, proses training model Machine Learning menjadi:

Otomatis

Reproducible

Terintegrasi dengan version control

Siap dikembangkan ke tahap monitoring dan deployment