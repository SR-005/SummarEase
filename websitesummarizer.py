from newspaper import article
from transformers import pipeline
import textwrap

websiteurl="https://en.wikipedia.org/wiki/Indochinese_green_magpie"
maxcharacter=1000

urltext=article(websiteurl)
urltext.download()
urltext.parse()
fulltext=urltext.text.strip()

if not fulltext:
    summary="No Text could be extracted"
else:
    formattedtext=textwrap.wrap(fulltext,maxcharacter)
    summarease = pipeline("summarization", model="facebook/bart-large-cnn")

    appendsummary=[]
    for i in formattedtext:
        summary = summarease(i,  max_length=130, min_length=30, do_sample=False)[0]['summary_text']  #properties adjustments
        appendsummary.append(summary) 
    
    finalsummary="\n".join(appendsummary)

    print("-------SUMMARY--------\n"+finalsummary)