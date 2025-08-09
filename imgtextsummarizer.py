import cv2
import easyocr
import matplotlib.pyplot as plt
from transformers import pipeline
from preloadmodels import reader as Reader

def main(imagepath):
    imagepath=imagepath     #specify image path here
    image=cv2.imread(imagepath)     #read the image using imagepath
    print("Image Read Successfull")

    '''Reader=easyocr.Reader(['en'],gpu=True)'''  #create an instance for reader using easyocr, set gpu to TRUE for faster computation
    readtext=Reader.readtext(image)     #using instance read text from image

    textlist=[]     #declare a list to store the texts
    threshold=0.25  #decides how much in depth you want to read the text
    #drawing boxes for text's found:
    for i in readtext:   
        '''print(i)'''        #print original values
        box,text,score=i    #seperate the raw values

        if score>threshold:
            '''topleftbox=tuple(box[0])    #get the coordinates of the topleft point of bounding box, we use tuple cause it's in format [x,y]
            bottomrightbox=tuple(box[2])    #get the coordinates of the bottomright point of bounding box
            cv2.rectangle(image,topleftbox,bottomrightbox,(255,0,0),4)  #draw the rectange using extracted coordinates'''
            textlist.append(text)

    #print the fulltext:
    fulltext=" ".join(textlist)
    print(fulltext)

    '''plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  #convert the BGRcoloured image to RGBcoloured
    plt.show() '''


    #Summarizer
    summarease = pipeline("summarization", model="facebook/bart-large-cnn",device=1)     #setting up summarizer model

    #dynamic min and max length
    inputlength = len(fulltext.split())
    max_len = min(130, int(0.8 * inputlength))  # max 80% of input
    min_len = min(30, max_len - 1)               # min less than max

    summary = summarease(fulltext,  max_length=max_len, min_length=min_len, do_sample=False)  #properties adjustments
    return summary[0]['summary_text']