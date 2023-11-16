 
import numpy as np
import cv2
from scipy import ndimage


cap=cv2.VideoCapture('trafico.mp4')
 
length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
video=[]
 
for i in range(0,length):
    ret,frame=cap.read()
    if ret:
        video.append(frame)

suma=np.zeros(video[0].shape)

for frameI in video:
    suma=suma+frameI

modeloFondo=np.uint8(suma/len(video))

for frameI in video:
    carros=0
    diferencia=cv2.absdiff(frameI,modeloFondo).astype('uint8')
    
    diferencia=cv2.GaussianBlur(diferencia,(11,11),0)
    
    diferencia=cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY)
    
    umbral,_=cv2.threshold(diferencia,0,255,cv2.THRESH_OTSU)
    
    bina=255*np.uint8(diferencia>umbral)
    
    bina=255*np.uint8(ndimage.binary_fill_holes(bina))
    
    contours=cv2.findContours(bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
      
    


    for i in contours:
        
        rect=cv2.boundingRect(i)
        x,y,w,h=rect
        
        if cv2.contourArea(i)>200:
            cv2.rectangle(frameI,(x,y),(x+w,y+h),(0,255,0),2)
            carros+=1
    cv2.putText(frameI, f"Contador: {carros}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)        
    cv2.imshow("",frameI)    
    if cv2.waitKey(1)== ord('s'):   
        break
    
     