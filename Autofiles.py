import os,shutil
import time
path=r'C:/Users/SAI/Downloads/'
files=['images','pdfs','excels','dppts','words']
for i in range(0,5) :
    if not os.path.exists(path+files[i]):
        os.makedirs(path+files[i])
file=os.listdir(path)
for f in file :
    try:
        if ".jpeg" in f and not os.path.exists(path+ "images/"+f):
            shutil.move(path+f,path+"images/"+f)
        elif ".pptx"in f and not os.path.exists(path +"dppts/"+f):
            shutil.move(path+f,path+"dppts/"+f)
        elif ".pdf" in f and not os.path.exists(path+"pdfs/"+f):
            shutil.move(path+f,path+"pdfs/"+f)
        elif ".xlsx" in f and not os.path.exists(path+"excels/"+f):
            shutil.move(path+f,path+"excels/+f")
        elif ".csv" in f and not os.path.exists(path+"excels/"+f):
            shutil.move(path+f,path+"excels/+f")
        elif ".docx" in f and not os.path.exists(path+"words/"+f):
            shutil.move(path+f,path+"words/"+f)
        elif ".png" in f and not os.path.exists(path+"images/"+f):
            shutil.move(path+f,path+"images/"+f)
        elif ".jpg" in f and not os.path.exists(path+"images/"+f):
            shutil.move(path+f,path+"images/"+f)
        
    except FileNotFoundError :
        print("file is not present")

        
recycle="Recycle Bin"
pptsPath=os.listdir(path+"dppts/")
pdfsPath=os.listdir(path+"pdfs/")
new=os.listdir(path+"newdup/")
for ppt in pptsPath:
    if "(1).pptx" in ppt and not os.path.exists(path+"newdup/"+ppt):
        shutil.move(path+"dppts/"+ppt,path+"newdup/"+ppt)
    elif "(2).pptx" in ppt and not os.path.exists(path+"newdup/"+ppt):
        shutil.move(path+"dppts/"+ppt,path+"newdup/"+ppt)
for pdf in pdfsPath:
    if "(1).pdf" in pdf and not os.path.exists(path+"newdup/"+pdf):
        shutil.move(path+"pdfs/"+pdf,path+"newdup/"+pdf)
    elif "(1) - Copy.pdf" in pdf and not os.path.exists(path+"newdup/"+pdf):
        shutil.move(path+"pdfs/"+pdf,path+"newdup/"+pdf)
    elif "(2).pdf" in pdf and not os.path.exists(path+"newdup/"+pdf):
        shutil.move(path+"pdfs/"+pdf,path+"newdup/"+pdf)
print("done")
time.sleep(10)
