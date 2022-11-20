import cv2
import os
import numpy as np
import face_recognition as fc
from datetime import datetime


class recon():

    def __init__(self,path,image,classname,mylist):
        self.path=path
        self.image=image
        self.classname=classname
        self.mylist=mylist

    def findEnc(self,images):
        enclist=[]
        for i in images:
            img = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
            enface = fc.face_encodings(img)[0]
            enclist.append(enface)
        return enclist

    def markatt(self,name):
            f=open('file.csv', 'r+')
            myDateList = f.readlines()
            nameList = []
            for line in myDateList:
                entry = line.split(',')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{dtString}')

def face():
    path = 'C:/Users/D35KT0P/PycharmProjects/face5/items'
    images = []
    classname = []
    mylist = os.listdir(path)
    print(mylist)

    for i in mylist:
        img = cv2.imread(f'{path}/{i}')
        images.append(img)
        classname.append(os.path.splitext(i)[0])

        print(classname)
        print(len(images))

    daro=recon(path,images,classname,mylist)

    daro.markatt('elon')

    enclistknown = daro.findEnc(images)
    print(len(enclistknown))
    print('Encoding Complte')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

        try:
            faceframe = fc.face_locations(imgs)
            encode = fc.face_encodings(imgs, faceframe)

            for encodeface, faceloc in zip(encode, faceframe):
                matches = fc.compare_faces(enclistknown, encodeface)
                facedis = fc.face_distance(enclistknown, encodeface)
                print(matches)
                print(facedis)
                matchindex = np.argmin(facedis)

                if matches[matchindex]:
                    name = classname[matchindex].upper()
                    print(name)

                    daro.markatt(name)

                cv2.imshow('image', img);

        except:
            print('[]')

if __name__=='__main__':
    face()





