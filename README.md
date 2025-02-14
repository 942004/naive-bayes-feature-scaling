# naive-bayes-feature-scaling
# Naïve Bayes with Feature Scaling

## Overview
This project investigates the impact of **feature scaling (StandardScaler)** on the performance of a **Gaussian Naïve Bayes classifier** using the **Iris dataset**.

## Features
- Loads the **Iris dataset** from `sklearn.datasets`.
- Splits the dataset into **training (80%)** and **testing (20%)** sets.
- Trains a **Gaussian Naïve Bayes classifier** on unscaled features.
- Standardizes features using **StandardScaler**.
- Trains the classifier again using scaled features.
- Compares performance before and after scaling using:
  - **Accuracy**
  - **Confusion Matrix**
  - **Classification Report**
- Visualizes the accuracy difference using **bar charts**.

## Installation
### Prerequisites
Ensure you have Python installed along with the necessary dependencies:
```bash
pip install numpy pandas scikit-learn matplotlib
```

## Usage
### Running the Experiment
Clone this repository and execute the script:
```bash
git clone https://github.com/yourusername/naive-bayes-feature-scaling.git
cd naive-bayes-feature-scaling
python naive_bayes_scaling.py
```

### Expected Output
- **Accuracy Score** before and after scaling.
- **Confusion Matrix** for both unscaled and scaled models.
- **Classification Report** showing precision, recall, and F1-score.
- **Bar Chart** comparing accuracy.

## Example Output
```
Without Feature Scaling:
Accuracy: 95.67%
Confusion Matrix:
[[10  0  0]
 [ 0  9  1]
 [ 0  0 10]]
Classification Report:
               precision    recall  f1-score   support
    setosa       1.00      1.00      1.00        10
versicolor       0.90      0.90      0.90        10
 virginica       1.00      0.91      0.95        11

With Feature Scaling:
Accuracy: 96.67%
Confusion Matrix:
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]
Classification Report:
               precision    recall  f1-score   support
    setosa       1.00      1.00      1.00        10
versicolor       1.00      1.00      1.00        10
 virginica       1.00      1.00      1.00        10
```

## Visualization
A bar chart is generated to compare the accuracy of the classifier **before and after scaling**:

![Accuracy Comparison](accuracy_comparison.png)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Feel free to open issues and submit pull requests.

## Author
[D.Anu Kumari](https://github.com/942004)

