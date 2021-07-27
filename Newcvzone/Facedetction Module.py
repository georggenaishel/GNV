"""
Face detection module
By: Georgge Naishel

"""


import cv2
import mediapipe as mp


class FaceDetector:


    def __init__(self, minDetectionCon=0.5):


        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        fboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                fboxs = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                fboxs = int(fboxs.xmin * iw), int(fboxs.ymin * ih), \
                       int(fboxs.width * iw), int(fboxs.height * ih)
                cx, cy = fboxs[0] + (fboxs[2] // 2), \
                         fboxs[1] + (fboxs[3] // 2)
                fboxsInfo = {"id": id, "bbox": fboxs, "score": detection.score, "center": (cx, cy)}
                fboxs.append(fboxsInfo)
                if draw:
                    img = cv2.rectangle(img, fboxs, (255, 0, 255), 2)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                                (fboxs[0], fboxs[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                                2, (255, 0, 255), 2)
        return img, fboxs


def core():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, fboxs = detector.findFaces(img)

        if fboxs:
            # bboxInfo - "id","bbox","score","center"
            center = fboxs[0]["center"]
            cv2.circle(img, center, 5, (0, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__core__":
    core()