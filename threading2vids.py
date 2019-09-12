import motion_detector
import threading
import argparse

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def start(self):
        print("Starting " + self.previewName)
        camstart(self.previewName, self.camID)

def camstart(previewName, camID):
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", help="path to the video file")
    ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
    args = vars(ap.parse_args())
    motion_detector.camtrack(camID, args)
# def camPreview(previewName, camID):
#     cv2.namedWindow(previewName)
#     cam = cv2.VideoCapture(camID)
#     if cam.isOpened():  # try to get the first frame
#         rval, frame = cam.read()
#     else:
#         rval = False
#
#     while rval:
#         cv2.imshow(previewName, frame)
#         rval, frame = cam.read()
#         key = cv2.waitKey(20)
#         if key == 27:  # exit on ESC
#             break
#     cv2.destroyWindow(previewName)

# Create two threads as follows
thread1 = camThread("Camera 1", 3) #change the camID to camID of pseye1
thread2 = camThread("Camera 2", 2) #change the camID to camID of pseye2
thread1.start()
thread2.start()
