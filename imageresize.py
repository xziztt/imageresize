import cv2
import numpy
import glob
images=glob.glob("*.jpg")
print(images)
print("what size do u wanna resize to ? Enter the resolutio.")
height=int(input())
width=int(input())
for image in images:
    temp=cv2.imread(image)
    resized_image=cv2.resize(temp,(height,width))
    cv2.imshow("resized_image",resized_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,resized_image)

    