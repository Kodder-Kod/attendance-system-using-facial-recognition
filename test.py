import cv2
import face_recognition as fc


# add imagen to the app
Elon= fc.load_image_file("C:/Users/D35KT0P/PycharmProjects/face5/items/kok.png")
imgElon =cv2.cvtColor(Elon,cv2.COLOR_BGR2RGB)

image= fc.load_image_file("C:/Users/D35KT0P/PycharmProjects/face5/items/Eon test.png")
imgtest =cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

test= fc.load_image_file("C:/Users/D35KT0P/PycharmProjects/face5/items/pop.png")
test =cv2.cvtColor(test,cv2.COLOR_BGR2RGB)


# finding face locations
face=fc.face_locations(image)[0]
face2=fc.face_locations(test)[0]
face4=fc.face_locations(Elon)[0]

#encoding face
enface=fc.face_encodings(image)[0]
enface2=fc.face_encodings(test)[0]
enface4=fc.face_encodings(Elon)[0]
print(enface)

#comapre face

comp=fc.compare_faces([enface4],enface2)
dis=fc.face_distance([enface],enface2)

print(comp)

print(face)
print(face2)
print(face4)
cv2.rectangle(test,(face[1],face[1]),(face[1],face[1]),(100,100,0),2)

#cv2.imshow("the image",Elon)
#cv2.imshow("the image",image)
#cv2.imshow("the image",test)

cv2.waitKey(0)

