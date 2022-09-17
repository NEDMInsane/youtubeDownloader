import os
import sys
import subprocess
import requests as requests
from pytube import YouTube

# Need to set some 'Global' variables for users operating system specific paths
if os.name == "nt":
    video_filepath = f"{os.getenv('USERPROFILE')}\\Videos"
    audio_filepath = f"{os.getenv('USERPROFILE')}\\Music"
else:
    video_filepath = f"{os.getenv('HOME')}/Videos"
    audio_filepath = f"{os.getenv('HOME')}/Music"


def get_vid_name(video_url):
    yt = YouTube(video_url)
    print(yt.title)


def complete(stream, file_path):
    print("Download Complete " + file_path)


def is_valid_vid(video_url):
    # PyTube probably has a module for checking if this is a valid
    # video link or not. I hate reading documentation
    page_source = requests.get(video_url)
    if "Video unavailable" in page_source.text:
        return False
    else:
        return True


def user_url_input():
    # CLUI or what there is of one
    print("Enter the URL of the video you wanted downloaded: ")
    video_url = input()
    if is_valid_vid(video_url):
        return video_url
    else:
        print("Invalid YouTube Video URL please retry. Exiting program.")
        quit()


def arg_url_input(video_url):
    # if args are passed, this runs instead.
    if is_valid_vid(video_url):
        return video_url
    else:
        print("Invalid YouTube Video URL please retry. Exiting program.")
        quit()


def video_download(video_url):
    # Download video, obviously with audio, 720p works best,
    # anything higher uses 2 streams, 1 for audio 1 for video.
    yt = YouTube(video_url, on_complete_callback=complete)
    yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download(video_filepath)


def audio_only_download(video_url):
    # Downloads just highest quality audio
    yt = YouTube(video_url, on_complete_callback=convert_to_mp3)
    yt.streams.get_audio_only().download(audio_filepath)


def convert_to_mp3(stream, file_path):
    # this will run a ffmpeg command to create a mp3 from the webm/mp4 audio file
    # file_path[:-4] gets rid of the file extension (webm will give an extra period)
    # and if .contains statement would probably take care of that.
    subprocess.run('ffmpeg -i "' + file_path + '" "' + file_path[:-4] + '.mp3"', shell=True)
    # now we need to delete the webm/mp4 audio file, do we really need two audio files?
    os.remove(file_path)
    complete(stream, file_path)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Arg 1 - video, arg 2 - what to download, arg 3 - ???
        video_download(arg_url_input(sys.argv[1]))
    elif len(sys.argv) == 3:
        #print(str(sys.argv[2]))
        if str(sys.argv[2]) == "-a" or str(sys.argv[2]) == "audio":
            audio_only_download(arg_url_input(str(sys.argv[1])))
        elif str(sys.argv[2]) == "-v" or str(sys.argv[2]) == "video":
            video_download(arg_url_input(str(sys.argv[1])))
        elif str(sys.argv[2]) == "-t" or str(sys.argv[2]) == "title":
            get_vid_name(arg_url_input(str(sys.argv[1])))
    else:
        # I might use a java application to call this script later,
        # so making a CLUI would be useless, probably.
        video_download(user_url_input())
