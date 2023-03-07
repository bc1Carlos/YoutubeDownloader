from pytube import YouTube

link = input("Enter a youtube video's URL:\n>> ") # i.e. https://youtu.be/dQw4w9WgXcQ

yt = YouTube(link)
title = yt.title

video = yt.streams.filter(file_extension='mp4').first()
audio = yt.streams.filter(only_audio=True).first()

video.download(filename=f'{title}.mp4')
audio.download(filename=f'{title}.mp3')

print(f'downloaded {title} from {link}')
