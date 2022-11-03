
import numpy as np
import pickle
import json
import config

class Boston():
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM=CRIM
        self.ZN=ZN
        self.INDUS=INDUS
        self.CHAS=CHAS
        self.NOX=NOX
        self.RM=RM
        self.AGE=AGE
        self.DIS=DIS
        self.RAD=RAD
        self.TAX=TAX
        self.PTRATIO=PTRATIO
        self.B=B
        self.LSTAT=LSTAT

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb")as f:
            self.model=pickle.load(f)
        with open (config.JSON_FILE_PATH,"r")as f:
            self.json_data=json.load(f)

    def get_price(self):
        self.load_model()
        test_array=np.zeros(len(self.json_data["columns"]))

        test_array[0]=self.CRIM
        test_array[1]=self.ZN
        test_array[2]=self.INDUS
        test_array[3]=self.CHAS
        test_array[4]=self.NOX
        test_array[5]=self.RM
        test_array[6]=self.AGE
        test_array[7]=self.DIS
        test_array[8]=self.RAD
        test_array[9]=self.TAX
        test_array[10]=self.PTRATIO
        test_array[11]=self.B
        test_array[12]=self.LSTAT

        get_price=np.around(self.model.predict([test_array])[0],2)
        return get_price

if __name__=="__main__":
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

    bs=Boston(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)  
    bs.get_price()   



    