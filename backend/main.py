# -*- coding: utf-8 -*-

from pytube import YouTube
import urllib.request
import os
from os.path import expanduser
                     
#
#
# EVENTS
#
#

# Catch video by link
def catch_video(link):  
        video = YouTube(link)
        return video

# Function to catch the thumbnail
def catch_thumbnail(video):
        video_thumbnail = video.thumbnail_url
        urllib.request.urlretrieve(video_thumbnail, "thumbnail_last_video.png")

# Remove thumbnail image after it became useless
def remove_thumb():
        try:
                os.remove("thumbnail_last_video.png")
        except FileNotFoundError:
                pass

# Function to download the video
def download_video(video):
        video_highest_resolution = video.streams.get_highest_resolution()
        path = expanduser("~\\Downloads\\")
        video_highest_resolution.download(path)


# if __name__ == "__main__":
#         try:
#                 link = input("\nInsira o link do vídeo que deseja baixar: ")
#                 video = catch_video(link)
#         except Exception as error:
#                 error_msg = "\n Error in catching video link, please repeat it or contact the developer"
                
#         try:
#                 confirm_video(video)
#         except Exception as error:
#                 error_msg = "\n Error in confirming video, please repeat it or contact the developer"
                
#         try:
#                 download_video(video)
#         except (http.client.IncompleteRead):
#                 pass
#         except Exception as error:
#                 error_msg = "\n Error in downloading video, please repeat it or contact the developer"