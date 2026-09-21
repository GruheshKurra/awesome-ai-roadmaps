# MLOps

Goal: Make ML training reproducible, track and test models, deploy predictions, and plan monitoring and retraining.

Prereqs: [Python for ML](../python-for-ml/) and [ML Basics](../ml-basics/), plus basic Git and command-line use. Be able to train and evaluate a scikit-learn model.

Status: done

Use DVC's local-storage option and a local MLflow server for the hands-on steps. Follow the numbered order from training data to a deployed model and its maintenance.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Baselines, metrics, and training-serving skew | | [Google — Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) |
| 2 | Version data alongside code | | [DVC — Track, store, and restore dataset versions](https://doc.dvc.org/start) |
| 3 | Reproducible training pipelines | | [DVC — Define stages, dependencies, and reruns](https://doc.dvc.org/start/data-pipelines/data-pipelines) |
| 4 | Track experiments and model artifacts | | [MLflow — Tracking Quickstart](https://mlflow.org/docs/latest/ml/tracking/quickstart/) |
| 5 | Test data, models, and infrastructure | | [Breck et al. 2017 — The ML Test Score](https://research.google.com/pubs/archive/aad9f93b86b7addfea4c419b9100c6cdd26cacea.pdf) |
| 6 | Register model versions and promotion aliases | | [MLflow — Model Registry Workflows](https://mlflow.org/docs/latest/ml/model-registry/workflow/) |
| 7 | Serve predictions and check endpoint health | | [MLflow — Deploy a Model as a Local Inference Server](https://mlflow.org/docs/latest/ml/deployment/deploy-model-locally/) |
| 8 | Monitor drift and decide when to retrain | **[FSDL 2022 — Continual Learning](https://www.youtube.com/watch?v=nra0Tt3a-Oc)** | [Evidently — Detecting and handling data drift](https://www.evidentlyai.com/ml-in-production/data-drift) |
