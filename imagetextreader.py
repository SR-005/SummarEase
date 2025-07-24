import cv2
import easyocr
import matplotlib as plt

imagepath="test.jpeg"       #specify image path here
image=cv2.imread(imagepath)     #read the image using imagepath
print("Image Read Successfull")

Reader=easyocr.Reader(['en'],gpu=True)  #create an instance for reader using easyocr, set gpu to TRUE for faster computation
text=Reader.readtext(image)     #using instance read text from image

for i in text:   
    print(i)