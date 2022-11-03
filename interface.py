from flask import Flask,jsonify
from flask import request,render_template
from projectapp.utils import Boston

app=Flask(__name__)

@app.route("/")
def home():
    return "Boston Price Predictions"


@app.route("/price")
def price():
    CRIM=0.00564
    ZN=0
    INDUS=3.1
    CHAS=0.0
    NOX=0.358
    RM=6.78
    AGE=45
    DIS=3.900
    RAD=3.1
    TAX=321.0
    PTRATIO=15.4
    B=239.45
    LSTAT=4.33   
    # data=request.form
    # print("data is",data)
    # CRIM=eval(data["CRIM"])
    # ZN=eval(data["ZN"])
    # INDUS=eval(data["INDUS"])
    # CHAS=eval(data["CHAS"])
    # NOX=eval(data["NOX"])
    # RM=eval(data["RM"])
    # AGE=eval(data["AGE"])
    # DIS=eval(data["DIS"])
    # RAD=eval(data["RAD"])
    # TAX=eval(data["TAX"])
    # PTRATIO=eval(data["PTRATIO"])
    # B=eval(data["B"])
    # LSTAT=eval(data["LSTAT"])

    bs=Boston(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)  
    result=bs.get_price()
    return jsonify({"price":f"your preducted price is {result}"})




    
if (__name__)=="__main__":
    app.run()