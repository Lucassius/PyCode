#get the library pytube <first>
# type: '!pip install pytube' or 'pip install pytube' in your terminal

from pytube import YouTube

def download_video(url):
    # Get the YouTube object
    yt = YouTube(url)

    # Get the first video stream available in mp4 format
    video_stream = yt.streams.filter(file_extension='mp4').first()

    # Download the video
    video_stream.download()
    
# Example usage
url = str(input("Type URL:"))
download_video(f"{url}")
