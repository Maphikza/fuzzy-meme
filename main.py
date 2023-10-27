import os
from pytube import YouTube
from moviepy.editor import *


def download_video(url, path='.'):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(path)
    return os.path.join(path, stream.default_filename)


def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    audio.close()
    video.close()


if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    output_audio_path = input("Enter the output audio path (e.g. output.mp3): ")

    video_path = download_video(video_url)
    extract_audio(video_path, output_audio_path)

    # Optional: remove the downloaded video after extraction
    os.remove(video_path)

    print(f"Audio saved at: {output_audio_path}")
