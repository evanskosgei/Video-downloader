# from pytube import YouTube

# #ask for the link from user
# link = input("https://youtu.be/7BXJIjfJCsA?t=257")
# yt = YouTube(link)

# #highest Resolution
# ys = yt.streams.get_highest_resolution()

# #download
# ys.download()


from pytube import YouTube
from pathlib import Path

#save path
SAVE_PATH = str(Path.home() / "Downloads/YouTube Videos")
FILE_NAME = "Rock Blaster Scrach video.mp4"

#video link for downloading
LINK = "https://youtu.be/sPPsOmQh76A"

try:
    yt = YouTube(LINK)
    yt.streams.filter(res = "720p", progressive= True, file_extension= "mp4").first().download(output_path = SAVE_PATH, filename = FILE_NAME)
except:
    print("connection error")

print("download complete")

# import os
# from pathlib import Path


# directory = "YouTube Videos"
# parent_dir = str(Path.home() / "Downloads")

# path = os.path.join(parent_dir, directory)

# try:
#     os.makedirs(path, exist_ok=True)
#     print("Directory '% s' created" % directory)
# except OSError as error:
#     print("Directory '%s' can not be created" % directory)