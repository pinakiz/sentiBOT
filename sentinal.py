from PIL import Image
import pytesseract as pt
import os
from LeXmo import LeXmo
import requests
import re
from pygoogletranslation import Translator

def senal(): 
    # path for the folder for getting the raw images 
    path ="./images"
   
    # path for the folder for getting the output 
    tempPath ="./textFiles"
  
    # iterating the images inside the folder 
    for imageName in os.listdir(path): 
        print ("-----------------------------")
              
        inputPath = os.path.join(path, imageName) 
        img = Image.open(inputPath) 
  
        # applying ocr using pytesseract for python 
        text = pt.image_to_string(img, lang ="hin+eng") 
        # text = re.sub(r'\n$', '', text) 
        # for removing the .jpg from the imagePath 
        # imageName = imageName[0:-4] 
        # print(text)
        translator = Translator()
        t = translator.translate(text)
        fullTempPath = os.path.join(tempPath, imageName+".txt") 
        print((t.text))
        emo=LeXmo.LeXmo(t.text)
        del emo['text']
        # print (translator)

        return (emo)
        
        # saving the  text for every image in a separate .txt file 
        # file1 = open(fullTempPath, "w", encoding='utf-8') 
        # file1.write(text) 
        # file1.close()  

if __name__ == '__main__':
    (senal())