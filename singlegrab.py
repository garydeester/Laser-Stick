#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy')
import numpy as np
import cv2
import time
import scipy.misc
from scipy import misc


frame_list=list()
cap = cv2.VideoCapture(0)
for i in range (1,5):
    ret, frame = cap.read()
    frame_list.append(frame)
     
summed_frames=sum(frame_list)                                  #Add a few frames together
resized_image=cv2.resize(summed_frames, (0,0), fx=0.5, fy=0.5) #Resize the image by half
resized_image_array=np.array(resized_image)                    #Convert it to an array so that pyplot can plot it.
grey_image=resized_image_array[:,:,:]                          #I put this in so I could selectively analyse one of the R,G,B channels                 
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
print grey_image.shape                                         #Show the size of the array
print np.amax(grey_image)
imgplot = plt.imshow(gray)                               #This will plot the file for you
imgplot.set_cmap('gist_gray')                                        #Set the colour map.
plt.colorbar()
imgplot.set_clim(0, 255)
plt.show()

cap.release()
cv2.destroyAllWindows()


#Messing around with averging over several frames. Could not get scipy.misc.imresize to
#to work. It seems like the method imresize is not installed correctly.
#Other scipy methods seem to work fine. Not sure what to make of this.

#cv2.imshow('frame',summed_matrix)
#time.sleep(10)
#(arr, size, interp='bilinear', mode=None)[source]
#cv2.resize(frame, resized_image,resized_image.size,0,0)
#cv2.destroyAllWindows()

#cv2.imshow('frame',summed_matrix)
#time.sleep(10)


#frame_list=list()
#matrix_list=list()
#frames_to_cap=5
#for i in range (1,frames_to_cap):
    #ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame_list.append(frame)
    #matrix_list.append(np.matrix(gray))

#small = scipy.misc.imresize(summed_frame,(6,5))
#summed_frame=sum(frame_list)
#summed_matrix=sum(matrix_list)