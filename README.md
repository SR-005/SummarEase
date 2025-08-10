# SummarEase   

Ever opened a PDF and thought, *“Yeah… I’m not reading all that”*?  
Or clicked on an article, saw the scroll bar smaller than your will to live, and immediately closed the tab?  
**SummarEase** exists to save you from text overload. It reads through the boring stuff and delivers the good parts — short, clear, and human-friendly.  

---

## 🚀 What it Does
- Summarizes **PDF documents** into concise, easy-to-read text.  
- Summarizes **web articles** when given a URL.  
- **Reads text from images using OCR** and then summarizes it.  

---

## 🧠 How it Works
- **Summarization** – Powered by Hugging Face’s [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn).  
- **OCR** – Uses EasyOCR for reading text from images and scanned files.  
- **Flask** – Backend framework for serving the web application.  

---

## 🛠 Setup
Make sure you have Python 3.9+ installed.  

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶ Running the App
Run:
```bash
python app.py
```

Then visit:
```
http://127.0.0.1:5000
```

---

## ⚠ First Run Note
The first execution will download required AI models.  
This may take some time depending on your internet connection.  

---

## 📸 Screenshots  
*(Add your screenshots here to show SummarEase in action!)*  

Example:  
![Homepage Screenshot](screenshots/homepage.png)  
![PDF Summarization Example](screenshots/pdf_summary.png)  
![OCR Summarization Example](screenshots/ocr_summary.png)  

---

## 🗂 Project Structure
```
.
├── app.py                 # Main Flask app RUN THIS
├── pdfsummarizer.py       # PDF summarization logic
├── websitesummarizer.py   # Web article summarization logic
├── imgtextsumamrizer.py   # OCR text extraction logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
