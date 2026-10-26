import torch
import torch.nn as nn
import time


class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(1024, 2048)
        self.layer2 = nn.Linear(2048, 1024)
        self.layer3 = nn.Linear(1024, 10)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.layer3(x)
        return x


# Create model
model = SimpleModel()
model.eval()

# Different batch sizes
batch_sizes = [1, 8, 16, 32]

# Number of benchmark runs
num_runs = 1000

for batch_size in batch_sizes:

    # Create test data
    input_data = torch.randn(batch_size, 1024)

    # Warm-up
    with torch.no_grad():
        for _ in range(100):
            model(input_data)

    # Benchmark
    start = time.perf_counter()

    with torch.no_grad():
        for _ in range(num_runs):
            output = model(input_data)

    end = time.perf_counter()

    # Calculate performance
    avg_latency = (end - start) / num_runs
    throughput = batch_size / avg_latency

    print(f"Batch size: {batch_size}")
    print(f"Average latency: {avg_latency * 1000:.4f} ms")
    print(f"Throughput: {throughput:.2f} samples/sec")
    print("-" * 40)