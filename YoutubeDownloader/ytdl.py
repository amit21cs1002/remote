from pytube import YouTube
link=input("Enter the link of YouTube video you want to download: ")
yt=YouTube(link)
videos=yt.streams.all()
video= list(enumerate(videos))
for i in video:
                    print(i)

qual=int(input("Enter the quality of video you want to download: "))
videos[qual].download()

# dn_option=int(input("Enter here: "))
# dn_video=videos[dn_option]
# dn_video.download()
print("Downloaded successfully")

