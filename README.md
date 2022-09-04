# youtubeDownloader
a simple script to download youtube videos

This requires ffmpeg if you want to use the audio only functionality.

for now this will download full videos using commandline interface if ran with no args

if you want to run with args, the first arg is the youtube video url (full url),
second arg is if you want audio only (-a or audio), or video (-v or video)

if you do not have ffmpeg the audio file will be deleted after its downloaded,
because i didnt add a check for ffmpeg.
