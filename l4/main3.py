import cv2

img=cv2.imread("l4/PFP.jpg")
center=(200,200)
r=30
color=(255,0,0)
thickness=-1

image=cv2.circle(img,center,r,color,thickness)
cv2.imshow("circle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()