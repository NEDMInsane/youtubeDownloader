# youtubeDownloader
a simple script to download youtube videos

This requires ffmpeg if you want to use the audio only functionality.

Also requires Requests and Pytube Python Packages (can be installed with PIP)

for now this will download full videos using commandline interface if ran with no args

if you want to run with args, the first arg is the youtube video url (full url),
second arg is if you want audio only (-a or audio), or video (-v or video)

if you do not have ffmpeg the audio file will be deleted after its downloaded,
because i didnt add a check for ffmpeg.

Arg Example:</br>
Audio Only</br>
.../youtubeDownloader/@- 'python3 main.py youtube.com/watch?v=cam0o3sg -a'

Video</br>
.../youtubeDownloader/@- 'python3 main.py youtube.com/watch?v=cam03sg -video'
