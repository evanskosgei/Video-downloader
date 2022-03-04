# from pytube import YouTube

# #ask for the link from user
# link = input("https://youtu.be/7BXJIjfJCsA?t=257")
# yt = YouTube(link)

# #highest Resolution
# ys = yt.streams.get_highest_resolution()

# #download
# ys.download()


from pytube import YouTube

#save path
SAVE_PATH = "C:/Users/kiongoss/Desktop/Video downloader/"
FILE_NAME = "Rock Blaster Scrach video.mp4"

#video link for downloading
LINK = "https:/youtu.be/4eYSyucr_uU?list=RD4eYSyucr_uU"

try:
    yt = YouTube(LINK)
    yt.streams.filter(res = "720p", progressive= True, file_extension= "mp4").first().download(output_path = SAVE_PATH, filename = FILE_NAME)
except:
    print("connection error")

print("download complete")