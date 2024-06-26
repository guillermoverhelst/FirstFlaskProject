
import cv2

camera = cv2.VideoCapture(0)

def cctv_live():
    while True:
        success,frame = camera.read()
        if not success:
            break
        else:
            ret,buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n'+ frame +b'\r\n')
        