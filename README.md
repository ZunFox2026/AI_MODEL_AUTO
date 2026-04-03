
# AI_MODEL_AUTO

Tự động deploy một AI model (Hugging Face) với API endpoint công khai qua Cloudflare Tunnel, tích hợp Telegram bot.

## Cách sử dụng

1. Fork repository này.
2. Vào tab **Actions** → chọn workflow **Auto Deploy AI Model with Cloudflare Tunnel** → **Run workflow**.
3. Điền thông tin:
   - `model_name`: ID model trên Hugging Face (vd: `gpt2`, `google/flan-t5-base`, `bert-base-uncased`...)
   - `telegram_bot_token` và `telegram_chat_id` (tuỳ chọn, để nhận thông báo URL)
   - `use_gpu`: chọn true nếu runner có GPU (GitHub Actions không có GPU mặc định, nhưng bạn có thể tự host runner GPU riêng)
4. Sau khi chạy, file `API.txt` sẽ được tạo và lưu trong artifacts (có thể tải về). Nếu có Telegram, bạn sẽ nhận được URL.

## Lưu ý

- Model sẽ chạy trên CPU (vì GitHub Actions runner không có GPU). Để chạy GPU, bạn cần tự host runner với GPU.
- Tunnel hoạt động miễn là workflow chưa kết thúc. Bạn có thể tăng thời gian `sleep` trong workflow để giữ tunnel lâu hơn.
- Mỗi lần chạy sẽ tạo một URL mới.

## Tùy chỉnh

Sửa file `scripts/start_server.py` để thay đổi logic API (thêm endpoint, xử lý khác).
