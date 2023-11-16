import cv2
 
 
 
"""
haarcascade_fullbody.xml
haarcascade_lefteye_2splits.xml
haarcascade_lowerbody.xml
haarcascade_eye_tree_eyeglasses.xml
haarcascade_smile.xml
haarcascade_frontalcatface.xml
haarcascade_profileface.xml
haarcascade_eye.xml
haarcascade_frontalface_default.xml
haarcascade_frontalface_alt_tree.xml
haarcascade_license_plate_rus_16stages.xml
haarcascade_frontalcatface_extended.xml
haarcascade_righteye_2splits.xml
haarcascade_russian_plate_number.xml
haarcascade_upperbody.xml
haarcascade_frontalface_alt.xml
haarcascade_frontalface_alt2.xml

""" 
 
detector=cv2.CascadeClassifier(cv2.data.haarcascades +'/haarcascade_fullbody.xml')

#camara= cv2.VideoCapture(0,cv2.CAP_DSHOW)#descomentar esta linea y comentar  la siguiente para usar camara
camara=cv2.VideoCapture("video4.mp4") 

while True:
    ret,cuadro=camara.read()
    if True: 
         
        cuadrogrises=cv2.cvtColor(cuadro,cv2.COLOR_BGR2GRAY)
        cuadrogrises=cv2.equalizeHist(cuadrogrises)
        cuerpo=detector.detectMultiScale(cuadrogrises )
        
        for (x,y,w,h) in cuerpo:
            cv2.rectangle(cuadro,(x,y),(x+w,y+h),(0,0,255),1) 
     
    cv2.imshow("camara", cuadro )
    if cv2.waitKey(1)== ord('s'):   
        break

camara.release()
cv2.destroyAllWindows()     