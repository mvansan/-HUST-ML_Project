import json
import csv
from langdetect import detect, DetectorFactory

# Đặt ngẫu nhiên để thư viện `langdetect` luôn trả về kết quả nhất quán
DetectorFactory.seed = 0

# Đường dẫn tới file JSON
json_file_path = 'reviews3.json'  # Điều chỉnh path nếu file JSON nằm ở vị trí khác

# Load dữ liệu từ file JSON
with open(json_file_path, 'r', encoding='utf-8') as f:
    reviews_data = json.load(f)

# Hàm để chuyển đổi rating từ chuỗi sang số nguyên
def extract_rating(rating_text):
    try:
        return int(float(rating_text.split()[0]))  # Chuyển sang số nguyên
    except (ValueError, IndexError):
        return None

# Hàm để kiểm tra xem review có phải bằng tiếng Anh không
def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False  # Nếu không phát hiện được ngôn ngữ, loại bỏ review đó

# Lọc và xử lý dữ liệu
csv_data_from_json = []
for review in reviews_data:
    review_text = review.get('reviewText', '')
    raw_rating = review.get('reviewRating', '')
    rating = extract_rating(raw_rating)  # Chuyển đổi rating
    if rating in {1, 2, 3, 4, 5} and is_english(review_text):  # Kiểm tra rating và ngôn ngữ
        csv_data_from_json.append((review_text, rating))

# Đường dẫn tới file CSV đầu ra
csv_output_path = 'english_reviews.csv'

# Ghi dữ liệu vào file CSV
with open(csv_output_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review Text', 'Review Rating'])  # Tiêu đề các cột
    writer.writerows(csv_data_from_json)

print(f"File CSV đã được lưu tại: {csv_output_path}")
