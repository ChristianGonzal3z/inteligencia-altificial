import cv2
from moviepy.editor import VideoFileClip

detectordecaras=cv2.CascadeClassifier(cv2.data.haarcascades +'/haarcascade_frontalface_alt.xml')
detectordeojos=cv2.CascadeClassifier(cv2.data.haarcascades +'/haarcascade_eye.xml')
 
def process_frame(cuadro):
    cuadrogrises=cv2.cvtColor(cuadro,cv2.COLOR_BGR2GRAY)
    cuadrogrises=cv2.equalizeHist(cuadrogrises)
    caras=detectordecaras.detectMultiScale(cuadrogrises )
    for (x,y,w,h) in caras:
        cv2.rectangle(cuadro,(x,y),(x+w,y+h),(0,0,255),1)
        regioncara = cuadrogrises[y:y+h,x:x+w]
        ojos = detectordeojos.detectMultiScale(regioncara)
        for (x2,y2,w2,h2) in ojos:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            cuadro = cv2.circle(cuadro, eye_center, radius, (0, 0, 255 ), 4)
    return cuadro

 
clip = VideoFileClip("video.mp4")

 
processed_clip = clip.fl_image(process_frame)

 
processed_clip.preview()
 
clip.close()
processed_clip.close()