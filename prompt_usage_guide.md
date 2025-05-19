# Hướng dẫn sử dụng prompt cho AI

## Giới thiệu
File `ai_prompt_template.md` chứa một mẫu prompt chi tiết để sử dụng với các công cụ AI như ChatGPT, Claude, Gemini hoặc các mô hình ngôn ngữ lớn khác khi làm việc với bài toán phân tích khách hàng rời bỏ (churn analysis). Dưới đây là hướng dẫn cách tùy chỉnh và sử dụng prompt này hiệu quả.

## Cách tùy chỉnh prompt

### 1. Xác định mục tiêu cụ thể
Trước khi sử dụng prompt, hãy xác định rõ bạn cần AI giúp gì:
- Phân tích dữ liệu
- Viết mã Python
- Giải thích khái niệm
- Đề xuất giải pháp
- Tất cả các mục trên

### 2. Điều chỉnh phần "Yêu cầu đầu ra"
- Đánh dấu vào các mục bạn cần AI giúp đỡ
- Nếu bạn chỉ cần giúp đỡ với một câu hỏi cụ thể, hãy chỉ chọn mục đó

### 3. Thêm thông tin bổ sung
- Nếu bạn đã thực hiện một số phân tích, hãy thêm kết quả vào phần "Thông tin bổ sung"
- Nếu bạn gặp khó khăn với một phần cụ thể, hãy mô tả chi tiết

### 4. Thêm yêu cầu cụ thể
- Điền vào phần "Yêu cầu cụ thể" với bất kỳ hướng dẫn đặc biệt nào
- Ví dụ: "Tôi muốn sử dụng Random Forest thay vì XGBoost" hoặc "Tôi cần giải thích chi tiết về cách tính F1 Score"

## Chiến lược sử dụng prompt hiệu quả

### 1. Chia nhỏ vấn đề
Thay vì gửi toàn bộ prompt cùng một lúc, hãy chia nhỏ thành các phần:
- **Phần 1**: Phân tích ý nghĩa của Churn Rate
- **Phần 2**: Phân tích đặc điểm khách hàng
- **Phần 3**: Mô hình Machine Learning
- **Phần 4**: Đề xuất hành động

### 2. Sử dụng phương pháp lặp
- Bắt đầu với một prompt đơn giản
- Dựa trên phản hồi, điều chỉnh prompt và hỏi thêm câu hỏi
- Tiếp tục quá trình này cho đến khi bạn có kết quả mong muốn

### 3. Cung cấp phản hồi cho AI
- Nếu phản hồi không đáp ứng yêu cầu, hãy giải thích tại sao
- Cung cấp ví dụ cụ thể về loại phản hồi bạn mong muốn

## Ví dụ prompt cụ thể

### Ví dụ 1: Phân tích ý nghĩa của Churn Rate
```
[Sao chép phần đầu của prompt template]

## Yêu cầu đầu ra
Tôi cần bạn giúp tôi với:
- [X] Phân tích ý nghĩa của Churn Rate (Câu hỏi 1)
- [ ] Các mục khác...

## Yêu cầu cụ thể
Tôi muốn phân tích sâu về ý nghĩa của Churn Rate đối với 3 bên liên quan: công ty viễn thông (MCI), khách hàng, và đối thủ cạnh tranh. Vui lòng cung cấp ví dụ cụ thể và số liệu thống kê nếu có thể.
```

### Ví dụ 2: Xây dựng mô hình Machine Learning
```
[Sao chép phần đầu của prompt template]

## Yêu cầu đầu ra
Tôi cần bạn giúp tôi với:
- [ ] Phân tích ý nghĩa của Churn Rate (Câu hỏi 1)
- [ ] Phân tích đặc điểm khách hàng (Câu hỏi 2)
- [X] Đề xuất và triển khai mô hình Machine Learning (Câu hỏi 3)
- [ ] Đề xuất hành động để nâng cao tỷ lệ giữ chân khách hàng (Câu hỏi 4)
- [X] Viết mã Python để xây dựng mô hình dự đoán
- [X] Giải thích kết quả và insights từ phân tích

## Thông tin bổ sung
Tôi đã thực hiện phân tích EDA và phát hiện rằng "International plan", "Customer service calls" và "Total day minutes" có tương quan cao với việc khách hàng rời bỏ.

## Yêu cầu cụ thể
Tôi muốn so sánh hiệu suất của 3 mô hình: Logistic Regression, Random Forest và XGBoost. Vui lòng cung cấp mã Python đầy đủ để xây dựng, huấn luyện và đánh giá các mô hình này. Đồng thời, giải thích chi tiết về tầm quan trọng của các đặc trưng trong mô hình tốt nhất.
```

## Lưu ý quan trọng
1. **Giới hạn token**: Các mô hình AI có giới hạn về số lượng token trong mỗi lần tương tác. Nếu prompt quá dài, hãy chia nhỏ thành nhiều phần.

2. **Cung cấp ngữ cảnh**: Luôn cung cấp đủ ngữ cảnh để AI hiểu vấn đề của bạn.

3. **Yêu cầu cụ thể**: Càng cụ thể trong yêu cầu, phản hồi càng có khả năng đáp ứng nhu cầu của bạn.

4. **Kiểm tra kết quả**: Luôn kiểm tra kết quả từ AI, đặc biệt là mã và phân tích thống kê.

5. **Lặp lại quá trình**: Đừng ngại yêu cầu AI điều chỉnh hoặc cải thiện phản hồi của nó.

## Kết luận
Prompt là công cụ giao tiếp giữa bạn và AI. Một prompt được thiết kế tốt sẽ giúp bạn nhận được phản hồi chất lượng cao và tiết kiệm thời gian. Hãy sử dụng template này như điểm khởi đầu và điều chỉnh theo nhu cầu cụ thể của bạn.
