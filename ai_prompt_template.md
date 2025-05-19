# Prompt cho phân tích dữ liệu khách hàng rời bỏ (Churn Analysis)

## Bối cảnh
Tôi đang làm một bài kiểm tra đầu vào cho vị trí Thực tập sinh/Fresher Phân tích Dữ liệu. Bài kiểm tra yêu cầu phân tích dữ liệu khách hàng rời bỏ (churn) của công ty viễn thông MCI. Tôi có hai tập dữ liệu: `Copy of churn-bigml-80.csv` (tập huấn luyện) và `Copy of churn-bigml-20.csv` (tập kiểm tra).

## Mô tả dữ liệu
Dữ liệu bao gồm các thông tin sau:
- Thông tin cá nhân: State, Account length, Area code
- Thông tin gói cước: International plan, Voice mail plan
- Hành vi sử dụng: Total day minutes, Total day calls, Total eve minutes, v.v.
- Tương tác với dịch vụ khách hàng: Customer service calls
- Trạng thái rời bỏ: Churn (True/False)

## Yêu cầu
Tôi cần phân tích dữ liệu và trả lời các câu hỏi sau:

1. **Ý nghĩa của Churn Rate** (1 điểm)
   - Phân tích ý nghĩa của tỷ lệ rời bỏ đối với các bên liên quan (Khách hàng, MCI, v.v.)

2. **Đặc điểm khách hàng** (2.5 điểm)
   - Phân tích đặc điểm của mỗi loại khách hàng (Rời bỏ hoặc Không rời bỏ)
   - Sử dụng các phương pháp thống kê mô tả và trực quan hóa dữ liệu

3. **Mô hình Machine Learning** (4.5 điểm)
   - Đề xuất và triển khai mô hình dự đoán khách hàng rời bỏ
   - Phân tích các đặc trưng đầu vào và giải thích tầm quan trọng của chúng
   - Đánh giá hiệu suất của mô hình

4. **Đề xuất hành động** (2 điểm)
   - Đề xuất các hành động liên quan đến phân tích định tính và định lượng để nâng cao tỷ lệ giữ chân khách hàng

## Hướng dẫn cụ thể
- Mã nguồn phải rõ ràng, đơn giản, tối ưu và có giải thích
- Tiếng Anh là bắt buộc cho mã nguồn và báo cáo
- Ưu tiên làm rõ insights và thống kê mô tả
- Trình bày từng bước huấn luyện mô hình

## Yêu cầu đầu ra
Tôi cần bạn giúp tôi với [chọn một hoặc nhiều mục sau]:
- [ ] Phân tích ý nghĩa của Churn Rate (Câu hỏi 1)
- [ ] Phân tích đặc điểm khách hàng (Câu hỏi 2)
- [ ] Đề xuất và triển khai mô hình Machine Learning (Câu hỏi 3)
- [ ] Đề xuất hành động để nâng cao tỷ lệ giữ chân khách hàng (Câu hỏi 4)
- [ ] Viết mã Python để phân tích dữ liệu
- [ ] Viết mã Python để xây dựng mô hình dự đoán
- [ ] Giải thích kết quả và insights từ phân tích

## Dữ liệu mẫu
Dưới đây là 5 dòng đầu tiên của tập dữ liệu:
```
State,Account length,Area code,International plan,Voice mail plan,Number vmail messages,Total day minutes,Total day calls,Total day charge,Total eve minutes,Total eve calls,Total eve charge,Total night minutes,Total night calls,Total night charge,Total intl minutes,Total intl calls,Total intl charge,Customer service calls,Churn
LA,117,408,No,No,0,184.5,97,31.37,351.6,80,29.89,215.8,90,9.71,8.7,4,2.35,1,False
IN,65,415,No,No,0,129.1,137,21.95,228.5,83,19.42,208.8,111,9.4,12.7,6,3.43,4,True
NY,161,415,No,No,0,332.9,67,56.59,317.8,97,27.01,160.6,128,7.23,5.4,9,1.46,4,True
SC,111,415,No,No,0,110.4,103,18.77,137.3,102,11.67,189.6,105,8.53,7.7,6,2.08,2,False
```

## Thông tin bổ sung
- Tôi đã thực hiện một số phân tích ban đầu và phát hiện rằng tỷ lệ khách hàng rời bỏ là khoảng 14.49%.
- Các đặc trưng như "International plan", "Customer service calls" và "Total day minutes" có vẻ có tương quan cao với việc khách hàng rời bỏ.

## Yêu cầu cụ thể
[Thêm bất kỳ yêu cầu cụ thể nào bạn có, ví dụ: "Tôi muốn tập trung vào việc sử dụng XGBoost cho mô hình dự đoán" hoặc "Tôi cần giải thích chi tiết về tầm quan trọng của các đặc trưng"]
