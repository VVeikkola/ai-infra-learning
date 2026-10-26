# Module 101 – ML Frameworks Fundamentals

## Self-Check Questions

### 1. What's the difference between PyTorch and TensorFlow's computation graphs?

**My answer:**

PyTorch uses dynamic computation graphs, which makes it flexible for developing and testing models. TensorFlow also supports dynamic execution but can use optimized computation graphs for production.

I would choose PyTorch when developing new models or experimenting with machine learning.

### 2. Why must you call `model.eval()` before inference?

**My answer:**

It puts the model into evaluation mode and changes how some layers work, such as dropout.

I would also use `torch.no_grad()` to disable gradient calculations because they are not needed during inference. This helps reduce memory usage.

### 3. What are the two ways to save PyTorch models and when should you use each?

**My answer:**

You can save the entire model or just its `state_dict`.

The `state_dict` contains the model's weights, biases and other stored state. It does not include the model architecture, so you need to recreate it when loading the weights.

I would prefer `state_dict` because it is more flexible.

### 4. What is TorchScript and how does it improve inference?

**My answer:**

TorchScript converts a PyTorch model into a graph representation that can be executed without the original Python model code. It can improve inference performance and make deployment easier.

TorchScript is now deprecated, and torch.export is the recommended alternative. It captures the model's calculations as a graph that can be saved and used for optimization or deployment. Exporting alone does not make the model faster.

### 5. What is ONNX and why is it useful for infrastructure?

**My answer:**

ONNX is an open model format that allows models to be moved between different frameworks and runtime environments.

For example, I could develop a model using PyTorch, export it to ONNX and run it using ONNX Runtime in production.

### 6. How do you warm up a model and why is it necessary?

**My answer:**

Warm-up means running the model a few times before the actual inference or benchmark.

It is similar to a cold start in a car. The first runs can be slower because the system needs to initialize resources and allocate memory.

Warm-up helps make performance measurements more reliable.

### 7. What's the difference between batch inference and single inference?

**My answer:**

Single inference processes one sample at a time, while batch inference processes multiple samples together.

Batch inference can improve throughput because the CPU or GPU can process multiple samples more efficiently.

However, larger batches can increase memory usage and waiting time.

---

## Practical Exercise – CPU Inference Benchmark

I created two neural networks using PyTorch and tested their inference performance on my AMD Ryzen 7 8700G CPU.

The small model had 601 parameters and the larger model had over 4 million parameters.

I tested batch sizes of 1, 8, 16 and 32.

### Results

| Model | Batch Size | Latency (ms) | Throughput (samples/sec) |
|---|---:|---:|---:|
| Small | 1 | 0.0079 | 125,982 |
| Small | 32 | 0.0133 | 2,413,740 |
| Large | 1 | 0.4276 | 2,339 |
| Large | 32 | 1.0307 | 31,047 |

### Observations

The larger model was much slower because it required more computation.

Increasing the batch size improved throughput significantly. I also noticed that latency increased much less than the number of samples.

I learned that the largest batch size is not always the best choice because it can increase memory usage and customer waiting time.

I also encountered a tensor shape mismatch error when changing the model architecture. I fixed it by changing the input tensor dimensions to match the model.

The benchmarks were performed using CPU only. I will compare the results with my RTX 3060 later.

---

## What I Learned

In this lesson, I learned the basics of PyTorch and TensorFlow and how neural networks are used for inference. I learned how to calculate model parameters, understand tensor dimensions and use evaluation mode. I also tested how model size and batch size affect latency and throughput. The practical exercise helped me understand why performance testing and resource management are important in AI infrastructure.