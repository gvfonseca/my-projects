# Reproducing "Understanding Deep Learning Requires Rethinking Generalization" by Zhang et al., 2017

This report reproduces key experiments from the paper **"Understanding Deep Learning Requires Rethinking Generalization"** by Zhang et al. (2017). Zhang's paper explores fundamental aspects of generalization in deep learning and evaluates how implicit and explicit regularization techniques influence model performance.

I worked on this project while studying abroad at EPFL in EE411-"Fundamentals of inference and learning" with Jan Clevorn, Ryoga Matsuo, and Jerome Mayolet. My role was in the reproduction of Figure 2 of Zhang's paper, described in section 5 of the report.

The final report can be found [here](./Reproducibility_Challenge_Rethinking_Generalization_Report.pdf).

## Objectives

- **Validate Findings**: Reproduce experiments to confirm the conclusions about generalization in deep learning.
- **Analyze Regularization**: Investigate the impact of implicit (e.g., data augmentation) and explicit (e.g., weight decay, dropout) regularizers.
- **Compare Models**: Evaluate the generalization behavior of different architectures, including Small Inception, Small AlexNet, and MLP.

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

- Although we were able to reproduce the main conclusions of the paper, there were various aspects of the paper's hyperparameters and steps that were unclear.



