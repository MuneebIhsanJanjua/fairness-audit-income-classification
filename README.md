# Investigating Gender Bias in Machine Learning

A Fairness Audit of Income Classification

## Overview

This project investigates gender bias in a Random Forest classifier trained on the UCI Adult Census Income dataset. The model predicts whether an individual earns above or below $50,000 per year, using sex as the protected characteristic under the Equality Act 2010. Three fairness criteria (Equal Accuracy, Demographic Parity, and Equal Opportunity) are applied to assess whether the model treats male and female groups equitably.

## Author

**Muneeb Ihsan Janjua**


## Dataset

The UCI Adult Census Income dataset, originally extracted from the 1994 United States Census Bureau database.

| Property | Value |
|----------|-------|
| Records | 32,537 |
| Features | 15 |
| Numerical Columns | 6 (age, fnlwgt, education num, capital gain, capital loss, hours per week) |
| Categorical Columns | 8 (workclass, education, marital status, occupation, relationship, race, sex, native country) |
| Target Variable | income (binary: <=50K or >50K) |

## Project Structure

```
project/
│
├── data/
│   └── processed_dataset/
│       └── adult_cleaned.csv
│   └── Raw_dataset/
│       └── adult.data
│       └── adult.names
│       └── adult.test
│       └── index
│       └── old.adult.names
│
├──Notebooks/
│       └──01_EDA_and_DataPreprocessing.ipynb
|
|
├──report/
│       └──E4542052-JANJUA-MUNEEBIHSAN.docx
|
|
├──scr/
|   └──00_preprocessing.py
|
├── requirements.txt
|
└── README.md
```

## Model Details

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Classifier |
| Estimators | 100 |
| Class Weight | Balanced |
| Scaler | MinMaxScaler (numerical features) |
| Encoder | OneHotEncoder (categorical features) |
| Train/Test Split | 80/20 |

## Results

### Overall Performance

| Metric | Value |
|--------|-------|
| Accuracy | 0.84 |
| ROC AUC | 0.8813 |

### Fairness Audit (5% Threshold OR FOURTH-FIFTH) 

| Criterion | Male | Female | Gap | Bias Detected |
|-----------|------|--------|-----|---------------|
| Equal Accuracy | 79.26% | 91.11% | 11.85% | Yes |
| Demographic Parity | 28.37% | 7.78% | 20.58% | Yes |
| Equal Opportunity | 63.70% | 49.38% | 14.32% | Yes |

All EQUAL ACCURACY fairness criteria exceeded the 5% threshold AND DEMOGRAPHIC PARTY not between 0.80 to .125, confirming systematic gender bias in the model.

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/gender-bias-ml-audit.git
cd gender-bias-ml-audit
```

2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook

```bash
jupyter notebook
```

5. Open `01_EDA_and_DataPreprocessing.ipynb` and run all cells

## Key Findings

1. The dataset contains a pronounced sex imbalance with approximately two thirds male and one third female records
2. The model achieves higher accuracy for women (91.11%) than men (79.26%), but this is misleading due to severe class imbalance in the female group where only 12% earn above 50K
3. Demographic Parity shows the largest gap (20.58%), meaning the model predicts high income for men at a significantly higher rate than for women
4. Equal Opportunity reveals the model is less likely to correctly identify high earning women (recall 49.38%) compared to high earning men (recall 63.70%)
5. The fairness impossibility theorem means all three criteria cannot be satisfied simultaneously when base rates differ between groups

## Technologies Used

| Library | Purpose |
|---------|---------|
| pandas | Data manipulation and analysis |
| numpy | Numerical computing |
| scikit learn | Machine learning pipeline, model training, evaluation |
| matplotlib | Data visualisation |
| seaborn | Statistical visualisation |
| scipy | Statistical tests (Spearman correlation, Q Q plots) |

## Disclaimer

**DO NOT DEPLOY IN ANY REAL WORLD APPLICATION**

This model card is for academic use only.
