import torch
import tensorflow as tf

print("PyTorch:", torch.__version__)
print("TensorFlow:", tf.__version__)

x = torch.tensor([1, 2, 3])
print("PyTorch tensor:", x)