

import time
import cv2


class FPS:


    def __init__(self):
        self.pTime = time.time()

    def update(self, img=None, pos=(20, 50), color=(255, 0, 0), scale=3, thickness=3):

        cTime = time.time()
        try:
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            if img is None:
                return fps
            else:
                cv2.putText(img, f'FPS: {int(fps)}', pos, cv2.FONT_HERSHEY_PLAIN,
                            scale, color, thickness)
                return fps, img
        except:
            return 0


def main():

    fpsReader = FPS()
    while True:
        time.sleep(0.025)
        fps = fpsReader.update()
        print(fps)


def mainWebcam():
    """
    With Webcam
    """
    fpsReader = FPS()
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        fps, img = fpsReader.update(img)
        cv2.imshow("Images", img)
        cv2.waitKey(1)


if __name__ == "__main__":

    mainWebcam()