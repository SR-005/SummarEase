from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == ['POST']:
        filetype=request.form("inputTypeSelector")

        if filetype=="document":
            docfile=request.files.get("documentFile") #extract the doc file from submitted forum

        elif filetype=="website":
            url=request.form.get("websiteURL")  #extract the url from submitted forum

        elif filetype=="image":
            imgfile=request.files.get("imageFile")  #extract the image file from submitted forum

    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)