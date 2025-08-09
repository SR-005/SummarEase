from newspaper import Article
from transformers import pipeline
import textwrap

def main(websiteurl):
    websiteurl=websiteurl
    maxcharacter=1000

    urltext=Article(websiteurl)
    urltext.download()
    urltext.parse()
    fulltext=urltext.text.strip()

    if not fulltext:
        summary="No Text could be extracted"
    else:
        formattedtext=textwrap.wrap(fulltext,maxcharacter)
        summarease = pipeline("summarization", model="facebook/bart-large-cnn",device=1)

        appendsummary=[]
        for i in formattedtext:
            summary = summarease(i,  max_length=130, min_length=30, do_sample=False)[0]['summary_text']  #properties adjustments
            appendsummary.append(summary) 
        
        finalsummary="\n".join(appendsummary)
        return finalsummary