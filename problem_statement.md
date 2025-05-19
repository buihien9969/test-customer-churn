# BÀI KIỂM TRA ĐẦU VÀO (Số 2)

**Vị trí:** Thực tập sinh/Fresher Phân tích Dữ liệu

## Mô tả vấn đề

Dự đoán khách hàng rời bỏ (customer churn) là một khía cạnh quan trọng trong quản lý kinh doanh, đặc biệt là đối với các ngành như viễn thông, nhà cung cấp dịch vụ internet, truyền hình trả tiền, công ty bảo hiểm và dịch vụ giám sát báo động. Nó liên quan đến việc hiểu và giải quyết tình trạng mất khách hàng, tức là việc mất đi khách hàng hoặc người dùng.

Đối với các doanh nghiệp trong những lĩnh vực này, đo lường tỷ lệ mất khách hàng là một chỉ số kinh doanh quan trọng. Điều này là do việc giữ chân một khách hàng hiện tại tiết kiệm chi phí hơn đáng kể so với việc thu hút một khách hàng mới. Do đó, các công ty này thường có các bộ phận dịch vụ khách hàng chuyên tái kết nối với những khách hàng đang cân nhắc việc rời đi. Điều này là vì giá trị dài hạn của những khách hàng được giữ lại vượt xa so với những khách hàng mới thu hút được.

Để giải quyết vấn đề khách hàng rời bỏ, phân tích dự đoán được áp dụng, các mô hình dự đoán khách hàng rời bỏ để đánh giá khả năng khách hàng sẽ rời đi. Những mô hình này ưu tiên một danh sách nhỏ các khách hàng có khả năng rời bỏ, cho phép doanh nghiệp tập trung nỗ lực giữ chân khách hàng vào những người có nguy cơ rời bỏ cao nhất.

## Câu hỏi chính

1. Tỷ lệ rời bỏ (Churn Rate) có ý nghĩa gì đối với các bên liên quan (Khách hàng, MCI, v.v.)? (1 điểm)

2. Đặc điểm của mỗi loại khách hàng (Rời bỏ hoặc Không rời bỏ) là gì? (2,5 điểm)

3. Mô hình Machine Learning nào có thể được triển khai và trình bày kết quả mô hình? bao gồm các đặc trưng đầu vào và giải thích tầm quan trọng của các đặc trưng. (4,5 điểm)

4. Những hành động liên quan đến phân tích định tính và định lượng nào có thể được triển khai để nâng cao tỷ lệ giữ chân khách hàng? (2 điểm)

Phân tích này nhằm tận dụng dữ liệu khách hàng toàn diện để cải thiện sự tương tác và hài lòng của khách hàng đối với các dịch vụ của MCI.

## Dữ liệu

Bạn được cung cấp hai tập dữ liệu:
1. `Copy of churn-bigml-80.csv`: Tập dữ liệu huấn luyện (80% dữ liệu)
2. `Copy of churn-bigml-20.csv`: Tập dữ liệu kiểm tra (20% dữ liệu)

Các tập dữ liệu này chứa thông tin về khách hàng của công ty viễn thông MCI, bao gồm:
- Thông tin cá nhân (State, Account length, Area code)
- Thông tin gói cước (International plan, Voice mail plan)
- Hành vi sử dụng (Total day minutes, Total day calls, Total eve minutes, v.v.)
- Tương tác với dịch vụ khách hàng (Customer service calls)
- Trạng thái rời bỏ (Churn: True/False)

## Yêu cầu

- Mã nguồn rõ ràng, đơn giản, tối ưu (nếu có thể) + giải thích mã. (OOP là một điểm cộng nhưng không bắt buộc)
- Slide rõ ràng, sâu sắc và hấp dẫn (không bắt buộc)
- Tiếng Anh là bắt buộc (Nếu slide và mã không được trình bày bằng tiếng Anh, kết quả của bạn sẽ bị loại)
- Vui lòng trình bày từng bước huấn luyện mô hình trong Phụ lục
- Ưu tiên làm rõ insights và thống kê mô tả. Bạn có thể tham khảo cách mô tả thống kê trong các bài viết sau:
  - Home Credit Complete EDA & Feature Importance
  - What Determines Price of a Laptop?
  - HR Analytics Prediction - Why do people resign?
