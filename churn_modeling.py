import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Thư viện cho mô hình ML
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

# Đọc dữ liệu
df_train = pd.read_csv('Copy of churn-bigml-80.csv')
df_test = pd.read_csv('Copy of churn-bigml-20.csv')

# Kết hợp dữ liệu để phân tích
df = pd.concat([df_train, df_test], axis=0)

# Chuyển đổi cột Churn thành dạng số (0/1)
df['Churn'] = df['Churn'].map({False: 0, True: 1})

# Hiển thị thông tin cơ bản về dữ liệu
print("Thông tin cơ bản về dữ liệu:")
print(f"Số lượng mẫu: {df.shape[0]}")
print(f"Số lượng thuộc tính: {df.shape[1]}")
print(f"Tỷ lệ khách hàng rời bỏ: {df['Churn'].mean() * 100:.2f}%")

# Chuẩn bị dữ liệu cho mô hình
# Chia thành đặc trưng và nhãn
X = df.drop('Churn', axis=1)
y = df['Churn']

# Xác định các cột số và cột phân loại
categorical_cols = ['State', 'International plan', 'Voice mail plan']
numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()

# Tiền xử lý dữ liệu
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first'), categorical_cols)
    ])

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Danh sách các mô hình để thử nghiệm
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'XGBoost': XGBClassifier(random_state=42)
}

# Đánh giá các mô hình
results = {}
for name, model in models.items():
    # Tạo pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])
    
    # Huấn luyện mô hình
    pipeline.fit(X_train, y_train)
    
    # Dự đoán
    y_pred = pipeline.predict(X_test)
    
    # Tính các chỉ số đánh giá
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])
    
    # Lưu kết quả
    results[name] = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'roc_auc': roc_auc,
        'pipeline': pipeline
    }
    
    print(f"\nKết quả cho mô hình {name}:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")
    
    # In báo cáo phân loại
    print("\nBáo cáo phân loại:")
    print(classification_report(y_test, y_pred))
    
    # Ma trận nhầm lẫn
    cm = confusion_matrix(y_test, y_pred)
    print("\nMa trận nhầm lẫn:")
    print(cm)

# Chọn mô hình tốt nhất dựa trên F1 Score
best_model_name = max(results, key=lambda x: results[x]['f1'])
best_model = results[best_model_name]['pipeline']
print(f"\nMô hình tốt nhất là {best_model_name} với F1 Score: {results[best_model_name]['f1']:.4f}")

# Phân tích tầm quan trọng của đặc trưng cho mô hình tốt nhất
if best_model_name in ['Random Forest', 'Gradient Boosting', 'XGBoost', 'Decision Tree']:
    # Lấy tên các đặc trưng sau khi tiền xử lý
    preprocessed_X_train = best_model.named_steps['preprocessor'].transform(X_train)
    
    if isinstance(preprocessed_X_train, np.ndarray):
        feature_names = numerical_cols + [f"{col}_{cat}" for col in categorical_cols for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[categorical_cols.index(col)][1:]]
    else:  # Sparse matrix
        feature_names = numerical_cols + [f"{col}_{cat}" for i, col in enumerate(categorical_cols) for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[i][1:]]
    
    # Lấy tầm quan trọng của đặc trưng
    if best_model_name == 'Random Forest':
        importances = best_model.named_steps['classifier'].feature_importances_
    elif best_model_name == 'Gradient Boosting':
        importances = best_model.named_steps['classifier'].feature_importances_
    elif best_model_name == 'XGBoost':
        importances = best_model.named_steps['classifier'].feature_importances_
    else:  # Decision Tree
        importances = best_model.named_steps['classifier'].feature_importances_
    
    # Tạo DataFrame để hiển thị tầm quan trọng
    feature_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    })
    
    # Sắp xếp theo tầm quan trọng giảm dần
    feature_importance = feature_importance.sort_values('Importance', ascending=False)
    
    print("\nTầm quan trọng của các đặc trưng:")
    print(feature_importance.head(15))  # Hiển thị 15 đặc trưng quan trọng nhất
else:
    # Đối với Logistic Regression, sử dụng hệ số
    if best_model_name == 'Logistic Regression':
        preprocessed_X_train = best_model.named_steps['preprocessor'].transform(X_train)
        
        if isinstance(preprocessed_X_train, np.ndarray):
            feature_names = numerical_cols + [f"{col}_{cat}" for col in categorical_cols for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[categorical_cols.index(col)][1:]]
        else:  # Sparse matrix
            feature_names = numerical_cols + [f"{col}_{cat}" for i, col in enumerate(categorical_cols) for cat in best_model.named_steps['preprocessor'].transformers_[1][1].categories_[i][1:]]
        
        coefficients = best_model.named_steps['classifier'].coef_[0]
        
        # Tạo DataFrame để hiển thị hệ số
        feature_importance = pd.DataFrame({
            'Feature': feature_names,
            'Coefficient': coefficients
        })
        
        # Sắp xếp theo giá trị tuyệt đối của hệ số giảm dần
        feature_importance['Abs_Coefficient'] = feature_importance['Coefficient'].abs()
        feature_importance = feature_importance.sort_values('Abs_Coefficient', ascending=False)
        
        print("\nHệ số của các đặc trưng (Logistic Regression):")
        print(feature_importance[['Feature', 'Coefficient']].head(15))  # Hiển thị 15 đặc trưng quan trọng nhất
    else:
        # Sử dụng permutation importance cho các mô hình khác
        result = permutation_importance(best_model, X_test, y_test, n_repeats=10, random_state=42)
        
        # Tạo DataFrame để hiển thị tầm quan trọng
        feature_importance = pd.DataFrame({
            'Feature': X.columns,
            'Importance': result.importances_mean
        })
        
        # Sắp xếp theo tầm quan trọng giảm dần
        feature_importance = feature_importance.sort_values('Importance', ascending=False)
        
        print("\nTầm quan trọng của các đặc trưng (Permutation Importance):")
        print(feature_importance.head(15))  # Hiển thị 15 đặc trưng quan trọng nhất

# Lưu kết quả vào file
with open('churn_modeling_results.txt', 'w') as f:
    f.write("KẾT QUẢ MÔ HÌNH DỰ ĐOÁN KHÁCH HÀNG RỜI BỎ\n\n")
    
    f.write("1. TỔNG QUAN VỀ DỮ LIỆU\n")
    f.write(f"Số lượng mẫu: {df.shape[0]}\n")
    f.write(f"Số lượng thuộc tính: {df.shape[1]}\n")
    f.write(f"Tỷ lệ khách hàng rời bỏ: {df['Churn'].mean() * 100:.2f}%\n\n")
    
    f.write("2. KẾT QUẢ CÁC MÔ HÌNH\n")
    for name, result in results.items():
        f.write(f"\nMô hình: {name}\n")
        f.write(f"Accuracy: {result['accuracy']:.4f}\n")
        f.write(f"Precision: {result['precision']:.4f}\n")
        f.write(f"Recall: {result['recall']:.4f}\n")
        f.write(f"F1 Score: {result['f1']:.4f}\n")
        f.write(f"ROC AUC: {result['roc_auc']:.4f}\n")
    
    f.write(f"\n3. MÔ HÌNH TỐT NHẤT\n")
    f.write(f"Mô hình tốt nhất là {best_model_name} với F1 Score: {results[best_model_name]['f1']:.4f}\n\n")
    
    f.write("4. ĐẶC TRƯNG QUAN TRỌNG\n")
    if 'feature_importance' in locals():
        for i, row in feature_importance.head(15).iterrows():
            if 'Coefficient' in feature_importance.columns:
                f.write(f"{row['Feature']}: {row['Coefficient']:.4f}\n")
            else:
                f.write(f"{row['Feature']}: {row['Importance']:.4f}\n")

print("\nĐã lưu kết quả phân tích vào file 'churn_modeling_results.txt'")
