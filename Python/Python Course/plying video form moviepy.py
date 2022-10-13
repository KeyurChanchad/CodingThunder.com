
# Below is the implementation

# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
class VideoFileClip:
    def subclip(self, param, param1):
        pass


clip = VideoFileClip("dsa_geek.webm")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# looping video 3 times
clip.ipython_display(loop = 3)


# This video will get played 3 times in continuous loop
# Another example

# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# looping video 3 times
clip.ipython_display(loop = 3)



