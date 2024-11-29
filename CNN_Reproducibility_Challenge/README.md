# Reproducibility Challenge: Rethinking Generalization in Deep Learning

This project reproduces key experiments from the paper **"Understanding Deep Learning Requires Rethinking Generalization"** by Zhang et al. (2017). The study explores fundamental aspects of generalization in deep learning and evaluates how implicit and explicit regularization techniques influence model performance.

## Objectives

- **Validate Findings**: Reproduce experiments to confirm the conclusions about generalization in deep learning.
- **Analyze Regularization**: Investigate the impact of implicit (e.g., data augmentation) and explicit (e.g., weight decay, dropout) regularizers.
- **Compare Models**: Evaluate the generalization behavior of different architectures, including Small Inception, Small AlexNet, and MLP.

## Key Experiments

### 1. Learning Curves
Reproduced learning curves under various data modifications:
- **True labels**: Original dataset.
- **Random labels**: Labels replaced uniformly at random.
- **Shuffled pixels**: Identical random pixel shuffling for all images.
- **Random pixels**: Independent random shuffling for each image.
- **Gaussian noise**: Pixel values redrawn from a Gaussian distribution.

### 2. Convergence Slowdown
Measured the impact of label corruption on the time required for models to overfit. A target accuracy threshold was used due to computational constraints.

### 3. Generalization Error Growth
Analyzed the test error growth of models trained on datasets with varying levels of label corruption.

### 4. Role of Regularization
Examined implicit and explicit regularizers:
- **Implicit regularizers**: Data augmentation, weight decay, and dropout.
- **Batch normalization**: Assessed its impact on learning and convergence.

## Models Used

- **Small Inception**: Simplified Inception architecture with convolutional and pooling layers.
- **Small AlexNet**: Compact AlexNet with feature extraction and classifier blocks.
- **MLP 1x512**: Multi-layer perceptron with a single hidden layer of 512 neurons.

## Pipeline

1. **Preprocessing**:
   - Dataset: CIFAR-10 (50,000 training and 10,000 validation images).
   - Center cropping to 28×28 pixels.
   - Custom standardization using PyTorch to normalize images by mean and standard deviation.
2. **Training**:
   - Stochastic Gradient Descent (SGD) with momentum (0.9) and learning rate scheduling.
   - Loss function: Cross-entropy.
3. **Evaluation**:
   - Metrics: Training loss, test accuracy, and generalization error.

## Challenges

- **Lack of Hyperparameter Details**: Many training parameters were not specified in the original paper and were estimated based on available results.
- **Computational Constraints**: Limited resources restricted full convergence for some experiments.

## Key Findings

- **Generalization Behavior**:
  - Rapid convergence for true and random labels but slower convergence for shuffled and noisy datasets.
  - Models demonstrate similar trends in generalization error growth under corruption.
- **Regularization Impact**:
  - Adding regularizers improved training stability but did not significantly enhance generalization.
  - Batch normalization slightly improved test accuracy but required careful implementation.

## Tools and Frameworks

- **Programming Language**: Python
- **Framework**: PyTorch
- **Dataset**: CIFAR-10
- **Techniques**: Data augmentation, convolutional neural networks (CNNs), regularization, and optimization.

## Conclusion

The reproduction validates key findings of the original paper, emphasizing that generalization in deep learning is influenced by more than just regularization. Computational and methodological constraints highlight the challenges of reproducibility in machine learning research.

## References

1. Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O. (2017). "Understanding Deep Learning Requires Rethinking Generalization."
2. Lobacheva, E., Kodryan, M., Chirkova, N., Malinin, A., & Vetrov, D. (2022). "On the periodic behavior of neural network training with batch normalization and weight decay."
