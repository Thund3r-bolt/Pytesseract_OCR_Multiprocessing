from PIL import Image
from multiprocessing import Pool
import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
files = os.listdir("Images")

def ocr_function(imgname):
    name=imgname.split(".",2)
    file = open("Text/"+name[0]+".txt","w")
    file.write("________________________________"+imgname+"________________________________")
    img_cv = cv2.imread("Images/"+imgname,0 )
    problem =str(pytesseract.image_to_string(img_cv))
    file.write(problem)
    file.write("________________________________"+imgname+"________________________________")
    print(imgname)
    file.close()
if __name__ == '__main__':
    p=Pool(4)
    p.map(ocr_function,files)
    


