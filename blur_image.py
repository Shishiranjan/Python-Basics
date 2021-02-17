# Importing cv2 module 
import cv2  
  
# bat.jpg is the batman image. 
img = cv2.imread('bat.jpg')  
  
# make sure that you have saved it in the same folder 
# You can change the kernel size as you want 
blurImg = cv2.blur(img,(10,10))  
cv2.imshow('blurred image',blurImg) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 
