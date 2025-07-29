import fitz
from transformers import pipeline
import textwrap 

pdfpath=""
maxcharacter=1000

document=fitz.open(pdfpath)
text=""
for page in document:
    text=text+page.get_text()
document.close()

#spliting words according to max limit
formattedtext=textwrap.wrap(text,maxcharacter)