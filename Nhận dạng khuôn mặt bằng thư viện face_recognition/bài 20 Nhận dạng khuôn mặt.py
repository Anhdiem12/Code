import cv2
import face_recognition as f

imginput = cv2.imread("anh/elonmusk.jpg")
#imginput = cv2.cvtColor(imginput,cv2.COLOR_BGR2RGB)
ma_hoa_input = f.face_encodings(imginput)[0]
vi_tri_face_input = f.face_locations(imginput)[0]
cv2.rectangle(imginput, (vi_tri_face_input[3], vi_tri_face_input[0]), (vi_tri_face_input[1], vi_tri_face_input[2]), [233,23,122], 2)

check = cv2.imread("anh/eloncheck.jpg")
#check = cv2.cvtColor(check,cv2.COLOR_BGR2RGB)
ma_hoa_check = f.face_encodings(check)[0]
vi_tri_face_check = f.face_locations(check)[0]
cv2.rectangle(check, (vi_tri_face_check[3], vi_tri_face_check[0]), (vi_tri_face_input[1], vi_tri_face_check[2]), [233,23,122], 2)

result = f.compare_faces([ma_hoa_input],ma_hoa_check)
lost = f.face_distance([ma_hoa_input],ma_hoa_check)

print(result)
print(lost)

cv2.putText(check,f"{result}{round(lost[0],2)}",(12,31),cv2.FONT_HERSHEY_SIMPLEX,1,[122,12,122],1)
cv2.imshow(" input ", imginput)
cv2.imshow(" check ", check)
cv2.waitKey(0)





