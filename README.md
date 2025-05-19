# Customer Churn Analysis and Prediction

A project analyzing customer churn rate in the telecommunications industry.

## Project Description

This project analyzes customer data from MCI Telecommunications to identify factors influencing customer churn and proposes solutions to reduce the churn rate. Customer churn refers to when customers stop using a company's services.

## Key Components

- Analysis of Churn Rate significance
- Customer characteristics and usage pattern analysis
- Comparison of Machine Learning models for churn prediction
- Recommendations for reducing churn rate

## Project Structure

- `analyze_churn.py`: Script for analyzing churn data
- `churn_modeling.py`: Script for building and evaluating ML models
- `requirements.txt`: List of required Python packages

## Installation and Setup

1. Clone the repository:
```
git clone https://github.com/yourusername/test-customer-churn.git
cd test-customer-churn
```

2. Install required packages:
```
pip install -r requirements.txt
```

3. Run the analysis script:
```
python analyze_churn.py
```

4. Run the modeling script:
```
python churn_modeling.py
```

## Key Results

- Overall churn rate: 14.49%
- Top churn predictors: International plan, customer service calls, total international calls
- Best model: XGBoost (Accuracy: 95.50%, F1-Score: 82.56%)
- Recommendations: Optimize international plans, improve customer service, implement segment-based retention strategies

## Data

The project uses the Telco Customer Churn dataset, which includes information about:
- Customer demographics
- Account information
- Services used
- Call details

## Models Evaluated

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

## License

This project is licensed under the MIT License - see the LICENSE file for details.
