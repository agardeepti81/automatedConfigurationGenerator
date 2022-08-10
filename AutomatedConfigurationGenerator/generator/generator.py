from PIL import Image, ImageDraw, ImageFont
from os.path import exists
import os
import pandas as pd

class Generator:
    def __init(self):    
        pass
    
    def Convert(self):
        outputFiles =[]
        df = pd.ExcelFile(self.inFile)
        sheet_names = df.sheet_names
        count = len(sheet_names)
        i=0
        while(i<count):
            data = pd.read_excel(self.inFile, sheet_name=i)
            os.chdir('C:\Deepti\AutomatedConfigurationGenerator\AutomatedConfigurationGenerator\media')
            FName = sheet_names[i]+'.json'
            f = open(FName, "wt")
            json_str = data.to_json(orient = 'records')
            f.write(json_str)
            f.close()
            i = i+1
            outputFiles.append(FName)
        return outputFiles
    
    def setInputFile(self, inFile):
        self.inFile = inFile
        
