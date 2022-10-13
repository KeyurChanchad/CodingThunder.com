# # importing libraries
# import cv2
# import numpy as np
# 
# # Create a VideoCapture object and read from input file
# cap = cv2.VideoCapture('Tom and Jerry 79 Episode Life with Tom 1953 - Mast.Video.mp4')
# 
# # Check if camera opened successfully
# if (cap.isOpened() == False):
#     print("Error opening video file")
# 
# # Read until video is completed
# while (cap.isOpened()):
# 
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if ret == True:
# 
#         # Display the resulting frame
#         cv.imshow('Frame', frame)
# 
#         # Press Q on keyboard to exit
#         if cv.waitKey(25) & 0xFF == ord('q'):
#             break
# 
#     # Break the loop
#     else:
#         break
# 
# # When everything done, release
# # the video capture object
# cap.release()
# 
# # Closes all the frames
# cv.destroyAllWindows()


# importing vlc module
# import vlc

# importing pafy module
# import pafy

# url of the video
# url = "https://www.youtube.com/watch?v = vG2PNdI8axo"

# creating pafy object of the video
# video = pafy.new(url)

# getting best stream
# best = video.getbest()

# creating vlc media player object
# media = .MediaPlayer(best.url)

# start playing video
# media.play()
