#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pickle
import math
import numpy as np

def maxMinNorm(array):
    maxrows=array.max(axis=1)
    minrows=array.min(axis=1)
    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t=np.empty((data_rows,data_cols))
    for i in range(data_rows):
        t[i,:]=(array[i,:]-minrows[i])/(maxrows[i]-minrows[i]+1e-20)
    return t

def visualization(text, textfull, textAtten, sentenceAtten, num):
    filepath="./run_result/visualization"+str(num)+".html"
    f = open(filepath, 'w')
    message="<html> \n<head></head> \n<body> \n"

    textAttenN=maxMinNorm(textAtten)
    sentenceAttenN=maxMinNorm(sentenceAtten)

    for i in range(len(text)):
        sentence=text[i]
        sentencefull=textfull[i]
        color="rgba(0,0,255,"+str(textAttenN[0][i])+")"
        line = "<p><span style=\"background-color: "+color+"\">&emsp;&emsp;</span><span style=\"background-color: rgba(0,0,0,0)\">&emsp;</span>"
        p=0
        for q in range(len(sentencefull)):
            if p<len(sentence) and sentencefull[q] != sentence[p]:
                line = line + "<span style=\"background-color: rgba(0,0,0,0)\">" + sentencefull[q] + "</span>"
            else:
                color="rgba(255,0,0,"+str(sentenceAttenN[i][p])+")"
                line=line+"<span style=\"background-color: "+color+"\">"+sentencefull[q]+"</span>"
                p=p+1
        line=line+"</p>"
        message=message+line+"\n"

    message=message+"</body>\n</html>"
    f.write(message)
    f.close()

if __name__ == "__main__":
    for i in range(1,53):
        i=28
        path='./visualization/attentoin'+str(i)+'.pkl'
        f=open(path, 'rb')
        text, textfull, textAtten, sentenceAtten = pickle.load(f)
        visualization(text, textfull, textAtten, sentenceAtten,i)
        f.close()