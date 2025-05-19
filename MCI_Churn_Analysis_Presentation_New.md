# Telecom Customer Churn Analysis
## Understanding and Reducing Customer Attrition at MCI

[Your Name]
[Date]

---

## Introduction

- **Problem Statement:** Analyzing customer churn patterns at MCI Telecommunications
- **Dataset Overview:** 3,333 customer records with 20 attributes
- **Churn Rate:** 14.49% of customers have churned
- **Key Questions:**
  1. What is the significance of churn rate?
  2. What are the characteristics of each customer segment?
  3. Which machine learning models best predict churn?
  4. What actions can reduce customer attrition?

*[Visualization: Pie chart showing 14.49% churn vs. 85.51% retained customers]*

---

## Significance of Churn Rate

- **Financial Impact:**
  - Acquiring new customers costs 5x more than retaining existing ones
  - 14.49% churn rate represents significant revenue loss
  - Reducing churn by just 5% can increase profits by 25-95%

- **Stakeholder Impact:**
  - **For MCI:** Revenue stability, market position, operational efficiency
  - **For Customers:** Service disruption, switching costs, potential for better offers
  - **For Investors:** Indicator of business health, predictor of future performance

*[Visualization: Line graph showing relationship between churn rate reduction and projected profit increase]*

---

## Customer Usage Patterns

- **Key Differences in Usage:**
  - Churned customers use 18.12% more daytime minutes (206.91 vs. 175.18)
  - 6.72% more evening minutes (212.41 vs. 199.04)
  - 5.33% more international minutes (10.70 vs. 10.16)

- **Charges:**
  - Day charges: $35.18 vs. $29.78 (+18.12%)
  - Evening charges: $18.05 vs. $16.92 (+6.71%)
  - International charges: $2.89 vs. $2.74 (+5.33%)

*[Visualization: Grouped bar chart comparing usage patterns between churned and retained customers]*

---

## Service Plans & Customer Support

- **International Plan:**
  - 42.41% churn rate for customers with international plan vs. 11.50% without
  - 3.7x higher churn risk with international plan

- **Voice Mail Plan:**
  - 8.68% churn rate with voice mail plan vs. 16.72% without
  - Voice mail users have 48% lower churn risk

- **Customer Service:**
  - Churned customers make 53.8% more service calls (2.23 vs. 1.45)
  - Strong correlation between service calls and churn (r = 0.209)

*[Visualization: Bar charts showing churn rates by plan type]*

---

## Geographic Distribution

- **States with Highest Churn:**
  - New Jersey (26.47%)
  - California (26.47%)
  - Texas (25.00%)
  - Maryland (24.29%)
  - South Carolina (23.33%)

- **States with Lowest Churn:**
  - Alaska (5.77%)
  - Hawaii (5.66%)
  - Virginia (6.49%)
  - Iowa (6.82%)
  - Arizona (6.25%)

*[Visualization: US map heat map showing churn rates by state]*

---

## Customer Segmentation Analysis

- **High-Risk Segment:**
  - Has international plan
  - Makes frequent customer service calls (3+ calls)
  - High daytime usage (200+ minutes)
  - Low voicemail usage

- **Low-Risk Segment:**
  - Has voicemail plan
  - Few customer service calls (0-1 calls)
  - Moderate usage across all time periods
  - Long account tenure

*[Visualization: Scatter plot showing customer segments by risk factors]*

---

## Model Comparison

- **Models Evaluated:**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost

| Model | Accuracy | Precision | Recall | F1-Score | ROC AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 86.06% | 54.35% | 25.77% | 34.97% | 82.19% |
| Decision Tree | 91.45% | 70.41% | 71.13% | 70.77% | 83.02% |
| Random Forest | 93.85% | 98.28% | 58.76% | 73.55% | 92.40% |
| Gradient Boosting | 95.05% | 92.11% | 72.16% | 80.92% | 93.08% |
| XGBoost | 95.50% | 94.67% | 73.20% | 82.56% | 94.63% |

**Best Overall Model:** XGBoost (F1-Score: 0.8256, Accuracy: 95.50%)

---

## XGBoost Performance

- **Key Metrics:**
  - Accuracy: 95.50%
  - Precision: 94.67%
  - Recall: 73.20%
  - F1-Score: 82.56%
  - ROC AUC: 94.63%

- **Confusion Matrix:**
  - True Negatives: 566
  - False Positives: 4
  - False Negatives: 26
  - True Positives: 71

*[Visualization: Confusion matrix heatmap and ROC curve]*

---

## Feature Importance

- **Top Predictors of Churn:**
  1. International Plan (17.37%)
  2. Customer Service Calls (9.40%)
  3. Total International Calls (7.94%)
  4. Number of Voicemail Messages (7.59%)
  5. Total Day Minutes (7.47%)

- **Insight:** Service plan features and customer service interactions are stronger predictors than demographic factors

*[Visualization: Horizontal bar chart of feature importance]*

---

## Quantitative Recommendations

- **International Plan Optimization:**
  - Review pricing structure (42.41% churn rate)
  - Create tiered international plans based on usage patterns
  - Implement usage alerts to prevent bill shock

- **Customer Service Enhancement:**
  - Proactive outreach after 2+ service calls
  - Implement service quality metrics and training
  - Create dedicated team for high-value customers

*[Visualization: Impact vs. implementation difficulty matrix]*

---

## Targeted Retention Strategies

- **High Usage Customers:**
  - Create unlimited plans for high daytime users
  - Implement loyalty discounts based on usage
  - Develop bundled packages for multi-service users

- **Geographic Focus:**
  - Targeted campaigns in high-churn states (NJ, CA, TX)
  - Competitive analysis in these markets
  - Region-specific retention offers

*[Visualization: Customer segmentation matrix with targeted strategies]*

---

## Implementation Roadmap

- **Short-term Actions (0-3 months):**
  - Implement customer service improvement program
  - Launch international plan review and redesign
  - Deploy predictive churn model in production

- **Medium-term Actions (3-6 months):**
  - Roll out new plan structures and pricing
  - Implement automated early warning system
  - Launch targeted retention campaigns by segment

*[Visualization: Timeline with key milestones]*

---

## Conclusion & Next Steps

- **Key Findings:**
  - 14.49% overall churn rate with significant variation by segment
  - International plan, customer service calls, and usage patterns are key predictors
  - XGBoost model achieves 95.50% accuracy in predicting churn

- **Expected Impact:**
  - 5% reduction in churn rate within 6 months
  - Improved customer satisfaction scores
  - Increased customer lifetime value

---

## Appendix: Model Training Steps

1. **Data Preparation:**
   - Feature engineering and selection
   - Handling categorical variables with one-hot encoding
   - Standardizing numerical features
   - Train-test split (80/20)

2. **Model Training Process:**
   - Hyperparameter tuning with cross-validation
   - Model evaluation using multiple metrics
   - Feature importance analysis
   - Final model selection based on F1-Score

*[Visualization: Model training workflow diagram]*

---

# Thank You

**Contact Information:**
[Your Name]
[Your Email]
[Your Phone Number]
