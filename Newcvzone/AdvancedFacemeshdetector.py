"""
Advanced Face mesh detection module
By: Georgge Naishel

"""

import cv2
import mediapipe as mp
import time

class FaceMeshDetector():
    def init(self,staticMode=False,MaxFaces=2,MinDetectionCn=0.6,MinTrackCn=0.7):
        self.staticMode = staticMode
        self.MaxFaces = MaxFaces
        self.MinDetectionCon = MinDetectionCn
        self.MinTrackCon = MinTrackCn
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,
                                                 self.minDetectionCn, self.minTrackCn)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=2, circle_radius=3)

    def findFaceMesh(self, img, draw=True):

        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS,
                                               self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
                faces.append(face)
        return img, faces

    def mainfile():
        cap = cv2.VideoCapture(0)
        detector = FaceMeshDetector(maxFaces=2)
        while True:
            success, img = cap.read()
            img, faces = detector.findFaceMesh(img)
            if faces:
                print(faces[0])
            cv2.imshow("Your Image", img)
            cv2.waitKey(1)

    if __name__ == "__mainfile__":
        mainfile()


