from flask import Flask,render_template,request
import pandas as pd

app=Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def index2():
    file=request.files['file']
    file=pd.read_excel(file)
    return render_template('excel.html',file=file.to_html())
if __name__ == "__main__":
    app.run(debug=True)