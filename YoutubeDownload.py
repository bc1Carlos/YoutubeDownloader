from pytube import YouTube

link = input("Enter a youtube video's URL") # i.e. https://youtu.be/dQw4w9WgXcQ

yt = YouTube(link)
yt.streams.filter(file_extension='mp4').first().download()

print("downloaded", link)
