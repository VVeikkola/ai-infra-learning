# Module 101 – ML Lifecycle

## Practical Exercise – Spam Detection

### 1. List data requirements – What data is needed? Where does it come from?

I need existing emails and labels that tell whether an email is SPAM or NOT_SPAM. I would also check for incorrect labels, missing data, and duplicates before training.

### 2. Identify compute needs – What resources for training? For serving?

For training, I need CPU or GPU resources, enough memory, and storage. For serving, I would use FastAPI and Docker. Kubernetes could help scale the application, and a load balancer could distribute traffic between Pods.

### 3. Define success metrics – How do you measure if the model works?

I would use a confusion matrix, accuracy, precision, recall, and F1 score. I would prioritize high precision because I don't want important emails to be marked as spam.

### 4. Plan monitoring – What would you track in production?

I would use Prometheus and Grafana to monitor the system. I would track system metrics like latency, CPU usage, and memory usage, and model metrics like prediction distribution, recall, and data drift.

### 5. Consider failure modes – What could go wrong at each stage?

- **Data:** Incorrect data or labels could affect model training.
- **Training:** Not enough computing resources could slow down or interrupt training.
- **Evaluation:** High accuracy could be misleading if the dataset is imbalanced.
- **Deployment:** A new model version could fail, so I would use Blue-Green Deployment and rollback.
- **Monitoring:** The model could start making bad predictions without being noticed.
- **Retraining:** I would collect new data, retrain the model, and test it before deploying.

---

## Self-Check Questions

### 1. What are the six stages of the ML lifecycle?

The six stages are Data Collection and Preparation, Training, Evaluation, Deployment, Monitoring, and Retraining. After retraining, the lifecycle continues again.

### 2. Why is model versioning important?

ML models have multiple versions because training is a continuous process. Versioning helps track changes, reproduce results, and roll back to an older model if something goes wrong.

### 3. What's the difference between system metrics and model metrics?

System metrics measure how the infrastructure works, such as CPU usage, memory usage, and API latency. Model metrics measure how the model behaves, such as prediction distribution and data drift.

### 4. What are three deployment strategies for ML models?

- **Canary:** Start with a small percentage of traffic and gradually increase it.
- **Blue-Green:** Switch between two production environments and roll back if something goes wrong.
- **Shadow:** Send requests to both models but only return predictions from the old model.

### 5. Why is monitoring critical for production ML systems?

The model could start making wrong predictions, and without monitoring, we might not know when or why it happened.

### 6. What infrastructure is needed for the training stage?

We need CPU or GPU resources, resource scheduling, experiment tracking with MLflow or TensorBoard, and storage for models, artifacts, and metadata.

### 7. What is data drift and why does it matter?

Data drift happens when the distribution of input data changes compared to the original training data. This can affect predictions because future data might not look like the data the model was trained on.

---

## What I Learned

I learned how the ML lifecycle works from data collection to retraining. I also learned why model versioning, deployment strategies, and monitoring are important. The biggest thing I learned is that a model can work technically but still make bad predictions, so we need to monitor both the infrastructure and the model itself.

## Source

[AI Infrastructure Engineer Curriculum](https://github.com/ai-infra-curriculum/ai-infra-engineer-learning)