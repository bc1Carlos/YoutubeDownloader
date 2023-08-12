import yt_dlp as youtube_dl

link = input("Enter a youtube video's URL:\n>> ")

# Define the post-processing options to extract audio in MP3 format.
postprocessors = [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}]

ydl_opts_video = {
    'outtmpl': '%(title)s.%(ext)s',  # This makes sure the filename is the title of the video.
    'format': 'bestvideo[ext=mp4]',  # Download best quality video in mp4 format.
}

ydl_opts_audio = {
    'outtmpl': '%(title)s.%(ext)s',  # This makes sure the filename is the title of the video.
    'format': 'bestaudio[ext=mp3]',  # Download best quality audio in mp3 format.
    'postprocessors': postprocessors
}

with youtube_dl.YoutubeDL(ydl_opts_video) as ydl:
    ydl.download([link])

with youtube_dl.YoutubeDL(ydl_opts_audio) as ydl:
    ydl.download([link])
