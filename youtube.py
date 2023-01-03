from pytube import YouTube
from sys import argv

if len(argv) < 2:
    print("Usage: python youtube.py URL(provide valid url)")
    exit()

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/users//Username//Downloads//your_video_dir')
