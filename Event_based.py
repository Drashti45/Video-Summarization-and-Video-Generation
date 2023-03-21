import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import os

def event_based_video(video_path):
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    threshold = 20.

    if os.path.exists ('static\\shorten_video.mp4') :
        os.remove ('static\\shorten_video.mp4')

    writer = cv2.VideoWriter('static\\shorten_video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 25, (width, height))
    ret, frame1 = video.read()
    prev_frame = frame1

    a = 0
    b = 0
    c = 0

    try:
        while True:
            ret, frame = video.read()
            cv2.imshow("video",frame)
            if cv2.waitKey(20) & 0xFF==ord("d"):
                break
            if ret is True:
                if (((np.sum(np.absolute(frame-prev_frame))/np.size(frame)) > threshold)):
                    writer.write(frame)
                    prev_frame = frame
                    a += 1
                else:
                    prev_frame = frame
                    b += 1

                cv2.imshow('frame', frame)
                c += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(e)

    print("Total frames: ", c)
    print("Unique frames: ", a)
    print("Common frames: ", b)
    video.release()
    writer.release()
    cv2.destroyAllWindows()

# event_based_video("D:\\Final\\src\\input\\files\\1.mp4")