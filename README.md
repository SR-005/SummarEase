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

<img width="1851" height="980" alt="Screenshot 2025-08-10 153320" src="https://github.com/user-attachments/assets/46c5155a-9ac0-4dfd-b0be-1bb7effe1c6f" />

<img width="1517" height="932" alt="Screenshot 2025-08-10 153534" src="https://github.com/user-attachments/assets/901394ee-bd32-4d3c-90fd-3a6165588488" />

---

## 📸 Video  
https://drive.google.com/file/d/1KkX9YhS08QXKx3BgZpYuucXtw_hB_-dL/view?usp=sharing

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
