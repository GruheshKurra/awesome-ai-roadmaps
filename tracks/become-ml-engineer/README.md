# ML Engineering Project

Goal: Build, evaluate, document, and serve a tabular classification model locally, from a defined prediction task to a reproducible handoff.

Prereqs: [Python for ML](../python-for-ml/) and [ML Basics](../ml-basics/), plus basic Git and command-line use. Be able to fit and evaluate a scikit-learn classifier.

Status: done

Apply the lessons to one small classification dataset. Produce a baseline comparison, a saved preprocessing/model pipeline, a local prediction endpoint, and a model card. Use validation data for diagnosis and threshold selection; keep a separate test set untouched until those choices are fixed. Use local MLflow storage and serving. Continue with [MLOps](../mlops/) for data versioning, registries, and monitoring.

| Step | Concept | **YouTube** | Read |
| ---: | --- | --- | --- |
| 1 | Define the prediction target and success criteria | | [Google — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing) |
| 2 | Split data before preprocessing and prevent leakage | | [scikit-learn — Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) |
| 3 | Build a baseline pipeline for numeric and categorical features | | [scikit-learn — Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html) |
| 4 | Log parameters, metrics, and the fitted pipeline | | [MLflow — Tracking Quickstart](https://mlflow.org/docs/latest/ml/tracking/quickstart/) |
| 5 | Diagnose overfitting and misleading feature importance | | [scikit-learn — Permutation Importance vs Random Forest Feature Importance](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html) |
| 6 | Tune decision thresholds against the costs of errors | | [scikit-learn — Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html) |
| 7 | Choose a persistence format and record the training environment | | [scikit-learn — Model persistence](https://scikit-learn.org/stable/model_persistence.html) |
| 8 | Serve the final logged model and test predictions and health checks | | [MLflow — Deploy a Model as a Local Inference Server](https://mlflow.org/docs/latest/ml/deployment/deploy-model-locally/) |
| 9 | Document intended use, evaluation results, and limitations | | [Hugging Face — Model Cards](https://huggingface.co/docs/hub/en/model-cards) |
