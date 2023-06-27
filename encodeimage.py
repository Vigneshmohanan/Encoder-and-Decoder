import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow

gdict={} #global dictionary which stores image details.(acts as a suppliment for database in initial version)

#encoder function
def main(f):
  global gdict
  x=cv2.imread(f)
  original=x.shape
  flag=0
  if (x.shape[0]*x.shape[1])%2==0:
    resize=int(x.size/(2*2*2))
    flag=1
  else:
    resize=int(x.size/(3*3*3))
  if flag==1:
    y=np.random.randint(255,size=(2,2))
  else:
    y=np.random.randint(255,size=(3,3))
  if flag==1:
    x=x.reshape(resize, 2, 2, 2)
  else:
    x=x.reshape(resize, 3, 3, 3)
  x_=np.linalg.pinv(x)
  z=x_*y
  z=z.reshape(original)
  with open("o.txt","w") as f:
    for j in z:
      np.savetxt(f,j)
  cv2.imwrite("fig.jpg",z)
  gdict["y"]=y
  gdict["OD"]=original
  return ("fig.jpg","o.txt")

#encoder gradio call
def gmain(file1):
  img,fl=main(file1.name)
  return img, fl

import gradio as gr
demo=gr.Interface(gmain,inputs="file",outputs=["image","file"],capture_session=True)
demo.launch(debug=True)

#decoder function
def dmain(file1):
  global gdict
  t=np.loadtxt(file1,dtype=np.double)
  nt=np.array(t)
  flag=0
  if (nt.shape[0]*nt.shape[1])%2==0:
    resize=int(nt.size/(2*2*2))
    flag=1
  else:
    resize=int(nt.size/(3*3*3))
  original=gdict['OD']
  if flag==1:
    nt=nt.reshape(resize, 2, 2, 2)
  else:
    nt=nt.reshape(resize, 3, 3, 3)
  nz0=nt/gdict['y']
  nz0=np.linalg.pinv(nz0)
  nz0=nz0.reshape(original)
  cv2.imwrite("out.jpg",nz0)
  return "out.jpg"

#decoder gradio call
def gmain1(file1):
  im=dmain(file1.name)
  return im

demo1=gr.Interface(gmain1,inputs="file",outputs="image",capture_session=True)
demo1.launch(debug=True)
