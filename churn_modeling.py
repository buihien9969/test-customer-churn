import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Import basic data analysis libraries
# pandas: For data manipulation and analysis
# numpy: For numerical operations
# matplotlib and seaborn: For data visualization
# scipy.stats: For statistical tests and calculations

# Import machine learning libraries
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.inspection import permutation_importance

# Import libraries for:
# - Data splitting and cross-validation
# - Data preprocessing (scaling numerical features, encoding categorical features)
# - Model building (Pipeline, various classifiers)
# - Model evaluation (metrics, confusion matrix, classification report)
# - Feature importance analysis

# Load the training and testing datasets from CSV files
# The data is split 80/20 for training and testing
df_train = pd.read_csv('Copy of churn-bigml-80.csv')
df_test = pd.read_csv('Copy of churn-bigml-20.csv')

# Combine both datasets for comprehensive analysis
# axis=0 means we're stacking the dataframes vertically (row-wise)
df = pd.concat([df_train, df_test], axis=0)

# Convert the Churn column from boolean to numeric (0/1)
# This makes it easier to perform calculations and modeling
df['Churn'] = df['Churn'].map({False: 0, True: 1})

# Display basic information about the dataset
# This provides an overview of the data size and churn rate
print("Basic information about the dataset:")
print(f"Number of samples: {df.shape[0]}")  # Number of rows (samples)
print(f"Number of features: {df.shape[1]}")  # Number of columns (features)
print(f"Churn rate: {df['Churn'].mean() * 100:.2f}%")  # Percentage of churned customers

# Prepare data for modeling
# Separate features (X) and target variable (y)
X = df.drop('Churn', axis=1)  # All columns except Churn
y = df['Churn']  # Only the Churn column

# Identify categorical and numerical columns for appropriate preprocessing
categorical_cols = ['State', 'International plan', 'Voice mail plan']
numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()

# Create a preprocessing pipeline using ColumnTransformer
# This applies different transformations to different column types
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),  # Standardize numerical features (mean=0, std=1)
        ('cat', OneHotEncoder(drop='first'), categorical_cols)  # One-hot encode categorical features, dropping first category to avoid multicollinearity
    ])

# Split data into training and testing sets
# test_size=0.2: 80% training, 20% testing
# random_state=42: For reproducibility
# stratify=y: Maintain the same proportion of churned/non-churned customers in both sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Define a dictionary of models to evaluate
# Each model is initialized with default hyperparameters and a fixed random state
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),  # Linear model for classification
    'Decision Tree': DecisionTreeClassifier(random_state=42),  # Simple tree-based model
    'Random Forest': RandomForestClassifier(random_state=42),  # Ensemble of decision trees
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),  # Boosting ensemble method
    'XGBoost': XGBClassifier(random_state=42)  # Advanced implementation of gradient boosting
}

# Evaluate each model and store results
results = {}
for name, model in models.items():
    # Create a pipeline that combines preprocessing and the classifier
    # This ensures preprocessing is applied consistently to training and test data
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])

    # Train the model on the training data
    pipeline.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = pipeline.predict(X_test)

    # Calculate various evaluation metrics
    # Each metric provides different insights into model performance
    accuracy = accuracy_score(y_test, y_pred)  # Overall accuracy (correct predictions / total predictions)
    precision = precision_score(y_test, y_pred)  # Precision (true positives / predicted positives)
    recall = recall_score(y_test, y_pred)  # Recall or sensitivity (true positives / actual positives)
    f1 = f1_score(y_test, y_pred)  # F1 score (harmonic mean of precision and recall)
    roc_auc = roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])  # Area under ROC curve

    # Store all results in a dictionary for later comparison
    results[name] = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'roc_auc': roc_auc,
        'pipeline': pipeline  # Save the trained pipeline for later use
    }

    # Print evaluation metrics for the current model
    print(f"\nResults for {name} model:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")

    # Print detailed classification report
    # Shows precision, recall, f1-score for each class
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Print confusion matrix
    # Shows true positives, false positives, true negatives, false negatives
    cm = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:")
    print(cm)

# Select the best model based on F1 score
# F1 score balances precision and recall, good for imbalanced classes
best_model_name = max(results, key=lambda x: results[x]['f1'])
best_model = results[best_model_name]['pipeline']
print(f"\nBest model is {best_model_name} with F1 Score: {results[best_model_name]['f1']:.4f}")

# Analyze feature importance for the best model
# Different models provide feature importance in different ways
if best_model_name in ['Random Forest', 'Gradient Boosting', 'XGBoost', 'Decision Tree']:
    # For tree-based models, extract feature importance directly

    # Get the preprocessed feature names
    # This is necessary because preprocessing transforms the original features
    preprocessed_X_train = best_model.named_steps['preprocessor'].transform(X_train)

    # Handle different output types from the preprocessor
    if isinstance(preprocessed_X_train, np.ndarray):
        # Create feature names for the transformed dataset
        # For categorical features, create names for each one-hot encoded column
        feature_names = numerical_cols + [f"{col}_{cat}" for col in categorical_cols for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[categorical_cols.index(col)][1:]]
    else:  # Sparse matrix
        feature_names = numerical_cols + [f"{col}_{cat}" for i, col in enumerate(categorical_cols) for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[i][1:]]

    # Extract feature importance values based on the model type
    # All tree-based models have a feature_importances_ attribute
    if best_model_name == 'Random Forest':
        importances = best_model.named_steps['classifier'].feature_importances_
    elif best_model_name == 'Gradient Boosting':
        importances = best_model.named_steps['classifier'].feature_importances_
    elif best_model_name == 'XGBoost':
        importances = best_model.named_steps['classifier'].feature_importances_
    else:  # Decision Tree
        importances = best_model.named_steps['classifier'].feature_importances_

    # Create a DataFrame to display feature importance
    feature_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    })

    # Sort by importance in descending order
    feature_importance = feature_importance.sort_values('Importance', ascending=False)

    # Display the top 15 most important features
    print("\nFeature Importance:")
    print(feature_importance.head(15))
else:
    # For Logistic Regression, use coefficients as feature importance
    if best_model_name == 'Logistic Regression':
        # Get the preprocessed feature names (same as above)
        preprocessed_X_train = best_model.named_steps['preprocessor'].transform(X_train)

        if isinstance(preprocessed_X_train, np.ndarray):
            feature_names = numerical_cols + [f"{col}_{cat}" for col in categorical_cols for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[categorical_cols.index(col)][1:]]
        else:  # Sparse matrix
            feature_names = numerical_cols + [f"{col}_{cat}" for i, col in enumerate(categorical_cols) for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[i][1:]]

        # Extract coefficients from the logistic regression model
        # Higher absolute values indicate stronger influence on the prediction
        coefficients = best_model.named_steps['classifier'].coef_[0]

        # Create a DataFrame to display coefficients
        feature_importance = pd.DataFrame({
            'Feature': feature_names,
            'Coefficient': coefficients
        })

        # Sort by absolute coefficient value in descending order
        # This shows the most influential features regardless of direction
        feature_importance['Abs_Coefficient'] = feature_importance['Coefficient'].abs()
        feature_importance = feature_importance.sort_values('Abs_Coefficient', ascending=False)

        # Display the top 15 most important features
        print("\nFeature Coefficients (Logistic Regression):")
        print(feature_importance[['Feature', 'Coefficient']].head(15))
    else:
        # For other models, use permutation importance
        # This measures how model performance decreases when a feature is randomly shuffled
        result = permutation_importance(best_model, X_test, y_test, n_repeats=10, random_state=42)

        # Create a DataFrame to display permutation importance
        feature_importance = pd.DataFrame({
            'Feature': X.columns,
            'Importance': result.importances_mean
        })

        # Sort by importance in descending order
        feature_importance = feature_importance.sort_values('Importance', ascending=False)

        # Display the top 15 most important features
        print("\nFeature Importance (Permutation Importance):")
        print(feature_importance.head(15))

# Save results to a text file for future reference
with open('churn_modeling_results.txt', 'w') as f:
    f.write("CUSTOMER CHURN PREDICTION MODEL RESULTS\n\n")

    # Write overview section
    f.write("1. DATASET OVERVIEW\n")
    f.write(f"Number of samples: {df.shape[0]}\n")
    f.write(f"Number of features: {df.shape[1]}\n")
    f.write(f"Churn rate: {df['Churn'].mean() * 100:.2f}%\n\n")

    # Write model results section
    f.write("2. MODEL RESULTS\n")
    for name, result in results.items():
        f.write(f"\nModel: {name}\n")
        f.write(f"Accuracy: {result['accuracy']:.4f}\n")
        f.write(f"Precision: {result['precision']:.4f}\n")
        f.write(f"Recall: {result['recall']:.4f}\n")
        f.write(f"F1 Score: {result['f1']:.4f}\n")
        f.write(f"ROC AUC: {result['roc_auc']:.4f}\n")

    # Write best model section
    f.write(f"\n3. BEST MODEL\n")
    f.write(f"Best model is {best_model_name} with F1 Score: {results[best_model_name]['f1']:.4f}\n\n")

    # Write feature importance section
    f.write("4. IMPORTANT FEATURES\n")
    if 'feature_importance' in locals():
        for i, row in feature_importance.head(15).iterrows():
            if 'Coefficient' in feature_importance.columns:
                f.write(f"{row['Feature']}: {row['Coefficient']:.4f}\n")
            else:
                f.write(f"{row['Feature']}: {row['Importance']:.4f}\n")

# Confirm that the analysis results have been saved
print("\nAnalysis results saved to 'churn_modeling_results.txt'")
