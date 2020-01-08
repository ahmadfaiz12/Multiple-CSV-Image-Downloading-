import pandas
import requests
import os
import shutil
import threading as Thread
from urllib import request
import glob
from threading import Thread
import time
#Path to the csv files
files=glob.glob("labelled_segmentations/*.csv")
#Function Defination
def fetch(i,id):
    #spliting the csv path to get base for different folder creation for each csv 
    name=i.split('/')[1]
    name=name.split('.')[0]
    #Check if folder already exist
    if os.path.exists(name):
        print('exists')
    #Make Directory
    else:
        direc=os.mkdir(name)
    #Reading CSV
    df = pandas.read_csv("labelled_segmentations/"+name+".csv")
    urls=df['Labeled Data']
    names=df['ID']
    datalist=[]
    namelist=[]
    for d in range(len(urls)):
        datalist.append(urls[d])
        namelist.append(names[d])
    missing=[]
    #Downloading Images
    for img in range(len(datalist)):
        try:
            if os.path.exists(name+"/"+namelist[img]+'.jpg'):
                print('exits')
            else:
                f = open(name+"/"+namelist[img]+'.jpg', 'wb')
                f.write(request.urlopen(datalist[img]).read())
                f.close()
        except:
            print("Exception at ",img)
            missing.append(names[img])
        pass
#Array for threads
jobs = []
for j in range (len(files)):
    i=files[j]
    thread = Thread(target=fetch,args=(i,j))
    jobs.append(thread)
    # Start the threads
for j in jobs:
    j.start()

    # Ensure all of the threads have finished
for j in jobs:
    j.join()
print('yes;;;')
