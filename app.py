from flask import Flask, request, render_template
import os
from pdfsummarizer import main as pdfsummarizer
from websitesummarizer import main as websitesummarizer
from imgtextsummarizer import main as imagesummarizer

app=Flask(__name__)
app.config["UPLOADFOLDER"]="uploads"
os.makedirs(app.config['UPLOADFOLDER'], exist_ok=True)#checks if the uploads folder exists or not

@app.route("/",methods=["GET", "POST"])
def index():
    summary=None
    if request.method == "POST":
        filetype = request.form.get("inputTypeSelector")

        if filetype=="document":
            docfile=request.files.get("documentFile") #extract the doc file from submitted forum
            if docfile.filename.endswith(".pdf"):   #verify's that it is a pdf or not
                filepath=os.path.join(app.config["UPLOADFOLDER"], docfile.filename) #links the 'uploads' folder path with the file
                docfile.save(filepath)  #save the file in that folder/path
                summaary=pdfsummarizer(filepath)
                print(summaary)

        elif filetype=="website":
            url=request.form.get("websiteURL")  #extract the url from submitted forum
            print("gotit")
            summary=websitesummarizer(url)
            print(summary)
            
        elif filetype=="image":
            imgfile=request.files.get("imageFile")  #extract the image file from submitted forum
            if imgfile:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], imgfile.filename)
                imgfile.save(filepath)
                summary=imagesummarizer(filepath)
                print(summary)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()