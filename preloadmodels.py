from transformers import pipeline
import easyocr

def download_transformer_model():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarizer("Hello world", max_length=5, min_length=1)

def download_easyocr_model():
    reader = easyocr.Reader(['en'])  

if __name__ == "__main__":
    print("Downloading transformer model...")
    download_transformer_model()
    print("Downloading EasyOCR model...")
    download_easyocr_model()
    print("Models downloaded and cached!")
