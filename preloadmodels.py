from transformers import pipeline
import easyocr

summarizer = pipeline("summarization", model="facebook/bart-large-cnn",device=1)
reader = easyocr.Reader(['en'])  

def download_transformer_model():
    summarizer("Hello world", max_length=5, min_length=1)


if __name__ == "__main__":
    print("Downloading transformer model...")
    download_transformer_model()
    print("Downloading EasyOCR model...")

