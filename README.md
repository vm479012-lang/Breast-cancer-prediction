# Breast Cancer Detection System Using Machine Learning

An educational machine learning project that classifies breast cancer tumors as **Malignant** or **Benign** using the Wisconsin Diagnostic Breast Cancer dataset.

## Project Overview

This project develops and evaluates machine learning models for breast cancer classification. It compares Logistic Regression, Random Forest, and Support Vector Machine (SVM), and selects a model based on classification performance, with particular attention to malignant-case recall.

## Objectives

- Collect and explore the Wisconsin Diagnostic Breast Cancer dataset.
- Perform data preprocessing and exploratory data analysis.
- Train and compare multiple machine learning algorithms.
- Apply hyperparameter tuning.
- Evaluate models using classification metrics.
- Provide an interactive prediction interface using Streamlit.

## Dataset

- **Dataset:** Wisconsin Diagnostic Breast Cancer (WDBC)
- **Samples:** 569
- **Features:** 30 numerical features
- **Benign cases:** 357
- **Malignant cases:** 212

The dataset contains measurements computed from digitized images of fine needle aspirate (FNA) samples of breast masses.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Joblib
- Streamlit
- SHAP (explainability, if included in the final implementation)

## Machine Learning Models

The following models were trained and compared:

1. Logistic Regression
2. Random Forest Classifier
3. Support Vector Machine (SVM)

Hyperparameter tuning was performed using GridSearchCV with stratified cross-validation and recall as the optimization metric.

## Model Evaluation

The models were evaluated on a held-out test set containing 114 samples.

| Metric | Logistic Regression |
|---|---:|
| Accuracy | 97.37% |
| Precision | 97.56% |
| Recall | 95.24% |
| F1-score | 96.39% |
| ROC-AUC | 99.54% |

### Confusion Matrix

| | Predicted Benign | Predicted Malignant |
|---|---:|---:|
| Actual Benign | 71 | 1 |
| Actual Malignant | 2 | 40 |

Logistic Regression was selected because it achieved the highest malignant-case recall among the three evaluated models and had the fewest false negatives on the held-out test set.

## Project Structure

```text
Code-A-Nova/
│
├── app/
│   └── app.py
│
├── data/
│   └── breast_cancer.csv
│
├── models/
│   └── best_breast_cancer_model.joblib
│
├── notebooks/
│   └── 01_Dataset_Collection.ipynb
│
├── outputs/
├── reports/
│
├── test_model.py
├── verify_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Code-A-Nova
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Streamlit Application

From the project root, run:

```bash
python -m streamlit run app/app.py
```

The application will open in your browser.

## Model Selection

Logistic Regression was selected as the final model based on its held-out test performance, especially its malignant-case recall. The trained model is saved as a Joblib file and used by the Streamlit application.

## Disclaimer

**This project is developed for educational and internship purposes only.** It is not a clinically validated diagnostic tool and must not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Author

Developed as part of the **CODE-A-NOVA ML Developer Internship**.

## Acknowledgements

- Wisconsin Diagnostic Breast Cancer dataset
- Scikit-learn documentation
- Python open-source community