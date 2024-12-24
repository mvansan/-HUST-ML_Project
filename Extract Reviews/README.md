# Công cụ Trích xuất Đánh giá

## Yêu cầu
- Python 3.x
- Các thư viện bên ngoài:
  - `langdetect`: Dùng để phát hiện ngôn ngữ của nội dung đánh giá.
  - `json`: Đọc dữ liệu từ file JSON.
  - `csv`: Ghi dữ liệu đã lọc vào file CSV.

## Cài đặt
1. Clone repository hoặc tải script Python về máy.
2. Đảm bảo đã cài đặt Python 3.x trên hệ thống của bạn.
3. Cài đặt các thư viện cần thiết bằng cách chạy lệnh sau:

```bash
pip install langdetect
```
4. Đặt file JSON chứa các đánh giá (ví dụ: reviews3.json) trong cùng thư mục với script Python.
5. Mở script Python và kiểm tra đường dẫn tới file JSON. Nếu file JSON không nằm trong cùng thư mục với script, hãy điều chỉnh đường dẫn trong dòng:
```bash
json_file_path = 'reviews3.json'
```
6. Trong terminal hoặc command prompt, điều hướng tới thư mục chứa script Python và chạy lệnh sau để thực thi script:
```bash
python jsontocsv.py
```
7. Sau khi chạy script, file CSV chứa các đánh giá đã được lọc sẽ được tạo trong cùng thư mục. Mở file CSV để kiểm tra kết quả.