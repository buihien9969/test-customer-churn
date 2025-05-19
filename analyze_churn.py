import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Đọc dữ liệu
df_train = pd.read_csv('Copy of churn-bigml-80.csv')
df_test = pd.read_csv('Copy of churn-bigml-20.csv')

# Kết hợp dữ liệu để phân tích
df = pd.concat([df_train, df_test], axis=0)

# Kiểm tra giá trị trong cột Churn
print("Các giá trị duy nhất trong cột Churn:")
print(df['Churn'].unique())

# Chuyển đổi cột Churn thành dạng số (0/1)
df['Churn'] = df['Churn'].map({False: 0, True: 1})

# Hiển thị thông tin cơ bản về dữ liệu
print("Thông tin cơ bản về dữ liệu:")
print(f"Số lượng mẫu: {df.shape[0]}")
print(f"Số lượng thuộc tính: {df.shape[1]}")
print("\nCác cột trong dữ liệu:")
print(df.columns.tolist())

# Kiểm tra giá trị null
print("\nKiểm tra giá trị null:")
print(df.isnull().sum())

# Thống kê mô tả
print("\nThống kê mô tả:")
print(df.describe())

# Phân tích tỷ lệ churn
churn_count = df['Churn'].value_counts()
churn_percentage = df['Churn'].value_counts(normalize=True) * 100
print("\nPhân bố khách hàng rời bỏ:")
print(f"Không rời bỏ (0): {churn_count[0]} ({churn_percentage[0]:.2f}%)")
print(f"Rời bỏ (1): {churn_count[1]} ({churn_percentage[1]:.2f}%)")

# Phân tích đặc điểm của từng nhóm khách hàng
print("\nĐặc điểm của khách hàng không rời bỏ (Churn = 0):")
print(df[df['Churn'] == 0].describe())

print("\nĐặc điểm của khách hàng rời bỏ (Churn = 1):")
print(df[df['Churn'] == 1].describe())

# So sánh các đặc điểm giữa hai nhóm
print("\nSo sánh các đặc điểm giữa hai nhóm:")
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numerical_cols.remove('Churn')  # Loại bỏ cột Churn khỏi danh sách

for col in numerical_cols:
    mean_non_churn = df[df['Churn'] == 0][col].mean()
    mean_churn = df[df['Churn'] == 1][col].mean()
    diff_percentage = ((mean_churn - mean_non_churn) / mean_non_churn * 100) if mean_non_churn != 0 else 0

    # Kiểm tra ý nghĩa thống kê
    t_stat, p_value = stats.ttest_ind(df[df['Churn'] == 0][col], df[df['Churn'] == 1][col], equal_var=False)

    print(f"{col}:")
    print(f"  - Trung bình (Không rời bỏ): {mean_non_churn:.2f}")
    print(f"  - Trung bình (Rời bỏ): {mean_churn:.2f}")
    print(f"  - Chênh lệch: {diff_percentage:.2f}%")
    print(f"  - p-value: {p_value:.4f} {'(Có ý nghĩa thống kê)' if p_value < 0.05 else '(Không có ý nghĩa thống kê)'}")

# Phân tích các biến phân loại
categorical_cols = ['State', 'International plan', 'Voice mail plan']
print("\nPhân tích các biến phân loại:")

for col in categorical_cols:
    print(f"\n{col}:")
    # Tính tỷ lệ churn cho mỗi giá trị của biến phân loại
    churn_by_category = df.groupby(col)['Churn'].mean() * 100
    count_by_category = df.groupby(col).size()

    for category, churn_rate in churn_by_category.items():
        count = count_by_category[category]
        print(f"  - {category}: {count} khách hàng, tỷ lệ rời bỏ {churn_rate:.2f}%")

# Phân tích tương quan
print("\nPhân tích tương quan với Churn:")
correlations = df[numerical_cols + ['Churn']].corr()['Churn'].sort_values(ascending=False)
print(correlations)

# Lưu kết quả phân tích vào file
with open('churn_analysis_results.txt', 'w') as f:
    f.write("PHÂN TÍCH ĐẶC ĐIỂM KHÁCH HÀNG RỜI BỎ VÀ KHÔNG RỜI BỎ\n\n")

    f.write("1. TỔNG QUAN VỀ DỮ LIỆU\n")
    f.write(f"Số lượng mẫu: {df.shape[0]}\n")
    f.write(f"Số lượng thuộc tính: {df.shape[1]}\n")
    f.write(f"Tỷ lệ khách hàng rời bỏ: {churn_percentage[1]:.2f}%\n\n")

    f.write("2. ĐẶC ĐIỂM KHÁCH HÀNG RỜI BỎ\n")
    # Liệt kê các đặc điểm nổi bật của khách hàng rời bỏ

    f.write("3. ĐẶC ĐIỂM KHÁCH HÀNG KHÔNG RỜI BỎ\n")
    # Liệt kê các đặc điểm nổi bật của khách hàng không rời bỏ

    f.write("4. SO SÁNH GIỮA HAI NHÓM\n")
    # Liệt kê các khác biệt quan trọng giữa hai nhóm

print("\nĐã lưu kết quả phân tích vào file 'churn_analysis_results.txt'")
