import cv2
img=cv2.imread("l4/ash.png")
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
org=(200,200)
fontscale=1
color=(0,0,0)
thickness=2

image=cv2.putText(img,"this is ash",org,font,fontscale,color,thickness)

cv2.imshow("texted",image)

cv2.waitKey(0)
cv2.destroyAllWindows()