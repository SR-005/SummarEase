import cv2
import easyocr
import matplotlib.pyplot as plt

imagepath="test.jpeg"       #specify image path here
image=cv2.imread(imagepath)     #read the image using imagepath
print("Image Read Successfull")

Reader=easyocr.Reader(['en'],gpu=True)  #create an instance for reader using easyocr, set gpu to TRUE for faster computation
readtext=Reader.readtext(image)     #using instance read text from image

#drawing boxes for text's found:
for i in readtext:   
    print(i)        #print original values
    box,text,score=i
    topleftbox=tuple(box[0])
    bottomrightbox=tuple(box[2])
    cv2.rectangle(image,topleftbox,bottomrightbox,(255,0,0),4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show() 