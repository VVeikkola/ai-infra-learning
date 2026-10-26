# Exercise 04 – ML Frameworks Benchmark

## Objective

The goal of this exercise was to understand how neural network size and batch size affect inference performance.

I used PyTorch to create two different neural networks and tested their performance using CPU.

## Environment

- OS: Ubuntu
- CPU: AMD Ryzen 7 8700G
- Python: 3.12.3
- PyTorch: 2.11.0+cu128
- GPU: Not yet installed

## Models

I created two neural networks with different architectures.

**Small model:**
- Linear(10, 50)
- ReLU
- Linear(50, 1)
- Parameters: 601

**Large model:**
- Linear(1024, 2048)
- ReLU
- Linear(2048, 1024)
- ReLU
- Linear(1024, 10)
- Parameters: 4,209,674

Both models used randomly initialized weights.

## CPU Benchmark Results

### Small Model

| Batch Size | Latency (ms) | Throughput (samples/sec) |
|---|---:|---:|
| 1 | 0.0079 | 125,982 |
| 8 | 0.0128 | 624,989 |
| 16 | 0.0129 | 1,236,834 |
| 32 | 0.0133 | 2,413,740 |

### Large Model

| Batch Size | Latency (ms) | Throughput (samples/sec) |
|---|---:|---:|
| 1 | 0.4276 | 2,339 |
| 8 | 0.7983 | 10,021 |
| 16 | 0.9267 | 17,266 |
| 32 | 1.0307 | 31,047 |

## Observations

I noticed that increasing the model size made inference much slower because the larger model required more computation.

Increasing the batch size improved throughput significantly. This is because the CPU was able to process multiple samples more efficiently.

I also learned that increasing batch size is not always the best solution because it can increase memory usage and customer waiting time.

## What I Learned

- How to build a simple neural network using PyTorch.
- How to calculate neural network parameters.
- How tensor dimensions work.
- The difference between latency and throughput.
- How batch inference improves performance.
- Why model size affects inference performance.
- Why warm-up is useful before benchmarking.
- How to troubleshoot tensor shape mismatch errors.
