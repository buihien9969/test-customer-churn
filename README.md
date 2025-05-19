# test-customer-churn

Dự án phân tích churn rate của khách hàng trong lĩnh vực viễn thông.

## Mô tả dự án

Dự án này phân tích dữ liệu khách hàng của MCI Telecommunications để xác định các yếu tố ảnh hưởng đến việc khách hàng rời bỏ dịch vụ (churn) và đề xuất các giải pháp để giảm tỷ lệ churn.

## Nội dung chính

- Phân tích ý nghĩa của Churn Rate
- Phân tích đặc điểm khách hàng và mẫu sử dụng
- So sánh các mô hình Machine Learning để dự đoán churn
- Đề xuất các giải pháp để giảm tỷ lệ churn

## Cấu trúc dự án

- `analyze_churn.py`: Script phân tích dữ liệu churn
- `churn_modeling.py`: Script xây dựng và đánh giá các mô hình ML
- `create_all_slides.py`: Script tạo bài thuyết trình PowerPoint
- `MCI_Churn_Analysis_Presentation_Final.pptx`: Bài thuyết trình PowerPoint
- `MCI_Churn_Analysis_Presentation_New.md`: Nội dung bài thuyết trình dạng Markdown

## Kết quả chính

- Tỷ lệ churn tổng thể: 14.49%
- Các yếu tố dự đoán churn hàng đầu: Gói quốc tế, số cuộc gọi dịch vụ khách hàng, tổng số cuộc gọi quốc tế
- Mô hình tốt nhất: XGBoost (Độ chính xác: 95.50%, F1-Score: 82.56%)
- Đề xuất: Tối ưu hóa gói quốc tế, cải thiện dịch vụ khách hàng, chiến lược giữ chân khách hàng theo phân khúc
