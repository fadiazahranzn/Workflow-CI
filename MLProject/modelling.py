import argparse
import mlflow
import mlflow.xgboost
import pandas as pd
import os

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score


def main(data_path):
    # =========================
    # FORCE MLflow local paths (CI SAFE)
    # =========================
    mlflow.set_tracking_uri("file:./mlruns")
    os.environ["MLFLOW_ARTIFACT_URI"] = "file:./mlruns"

    # Load dataset
    data = pd.read_csv(data_path)


    TARGET_COL = "diabetes"

    X = data.drop(TARGET_COL, axis=1)
    y = data[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    with mlflow.start_run():
        model = XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            random_state=42,
            eval_metric="logloss"
        )

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        # mlflow.xgboost.log_model(model, "model")

        print(f"Model trained with Accuracy: {acc:.4f}, F1 Score: {f1:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        type=str,
        default="diabetes_preprocessing/diabetes_preprocessed.csv"
    )
    args = parser.parse_args()

    main(args.data_path)
