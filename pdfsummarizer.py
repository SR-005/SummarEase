import fitz
from transformers import pipeline
import textwrap 

def main(pdfpath):
    pdfpath=pdfpath
    maxcharacter=1000

    document=fitz.open(pdfpath)
    text=""
    for page in document:
        text=text+page.get_text()
    document.close()

    #spliting words according to max limit
    formattedtext=textwrap.wrap(text,maxcharacter)

    #Summarizer
    summarease = pipeline("summarization", model="facebook/bart-large-cnn",device=1)     #setting up summarizer model

    appendsummary=[]
    for i in formattedtext:
        summary = summarease(i,  max_length=130, min_length=30, do_sample=False)[0]['summary_text']  #properties adjustments
        appendsummary.append(summary)

    fullsummary="\n\n".join(appendsummary)
    return fullsummary
