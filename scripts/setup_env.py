import os
import subprocess
import sys
import torch

def check_gpu():
    if torch.cuda.is_available():
        print("✅ GPU detected:", torch.cuda.get_device_name(0))
        return True
    else:
        print("⚠️ No GPU found, using CPU (will be slower)")
        return False

def install_model_deps(model_name):
    # Có thể mở rộng theo model
    print(f"Installing dependencies for {model_name}...")
    # Ví dụ: transformers đã có trong requirements
    # Tải model xuống cache (optional)
    from transformers import AutoModel, AutoTokenizer
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)
        print("✅ Model loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        sys.exit(1)

def main():
    model_name = os.environ.get("MODEL_NAME", "gpt2")
    use_gpu = os.environ.get("USE_GPU", "true").lower() == "true"
    
    if use_gpu and not check_gpu():
        print("GPU requested but not available, falling back to CPU")
    
    install_model_deps(model_name)
    
    # Lưu model name để start_server.py dùng
    with open("model_config.txt", "w") as f:
        f.write(model_name)
    
    print("Environment setup completed.")
    
if __name__ == "__main__":
    main()
