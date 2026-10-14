#!/usr/bin/env bash

echo "=== AI Infrastructure Environment Verification ==="
echo ""

echo "=== Python ==="
python --version || echo "❌ Python missing"
python -m pip check
echo ""

echo "=== Python Packages ==="
python -c "import torch; print('PyTorch:', torch.__version__)" || echo "❌ PyTorch missing"
python -c "import tensorflow as tf; print('TensorFlow:', tf.__version__)" || echo "❌ TensorFlow missing"
python -c "import fastapi; print('FastAPI:', fastapi.__version__)" || echo "❌ FastAPI missing"
echo ""

echo "=== Git ==="
git --version
echo ""

echo "=== Docker ==="
docker --version
docker compose version
docker ps >/dev/null 2>&1 && echo "✅ Docker running" || echo "❌ Docker not accessible"
echo ""

echo "=== Kubernetes ==="
kubectl version --client
minikube version || echo "❌ Minikube missing"
helm version --short || echo "⚠️ Helm not installed"
echo ""

echo "=== Cloud CLI ==="
az version || echo "⚠️ Azure CLI not installed"
echo ""

echo "=== Verification Complete ==="
