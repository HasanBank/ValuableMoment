# import the necessary packages
from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import sys

video = sys.argv[1]
timeInterval = int(sys.argv[2])
fps = int(sys.argv[3])



# start the file video stream thread and allow the buffer to
# start to fill
print("[INFO] starting video file thread...")
fvs = FileVideoStream(video).start()
time.sleep(1.0)


# start the FPS timer
timer = FPS().start()

i = 1
frameCount = 0
while fvs.more():

	frame = fvs.read()
	frameCount += 1

	if frameCount == fps * timeInterval:

		frameCount = 0
        	#cv2.imshow('image',image)
        	cv2.imwrite('frames/frame%d.jpg'%i,frame)
        	i += 1
      

	timer.update()

# stop the timer and display FPS information
timer.stop()
print("[INFO] elasped time: {:.2f}".format(timer.elapsed()))

# do a bit of cleanup
cv2.destroyAllWindows()
fvs.stop()

