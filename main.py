import moviepy.editor as mp

clip = mp.VideoFileClip(a.mp4")

# make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized = clip.resize(height=720)

clip_resized.write_videofile("movie_resized.mp4")


""" ANOTHER WAY
from moviepy.video.io.VideoFileClip import VideoFileClip

clip = VideoFileClip("a.mp4")

clip_resized = clip.resized(height=720)

clip_resized.write_videofile("movie_resized.mp4")
"""
