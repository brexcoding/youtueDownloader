import pytube 
from pytube import YouTube

print('dowtube v 1.0')
'''[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="8fps" vcodec="mp4v.20
.3" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="18" mime_type="video/mp4" res="360p" fp
s="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type
="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, 
<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video"
>, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">, 
<Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">
, <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">
 , <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">
 , <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type=
 "video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="v
 ideo">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False"
  type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False"
   type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive
   ="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="
   False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False"
    type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False"
     type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" 
     type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False"
      type="audio">, 

<Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]'''
res_144 = 160
res_240 = 242
res_360 = 18
res_480 = 135
res_720 = 136
res_1080 = 137

audio = {
    'abr_128kbps': 140 ,
    'abr_70kbps ': 250 , 

} 



def download():
    print('================================')
    print('enter your the video url')
    url = input()
    yt = YouTube(url)
    print('select video resoulution')
    video_resolution = [160 , 242 ,18 , 135 , 136 , 137 ]
    print('press 1 for 144p \n 2 for 240p \n 3 for 300p \n 4 for 480p \n 5 for 720p \n 6 for1080p')
    number = int(input("Enter a number: "))
    if number == 1:
        print('downloading the video with 144p resolution')
        resolution = video_resolution[0]
    if number == 2:
        resolution = video_resolution[1]
        print('downloading the video with 240p resolution')
    if number == 3:
        resolution = video_resolution[2]
        print('downloading the video with 360 resolution')
    if number == 4:
        resolution = video_resolution[3]
        print('downloading the video with 480p resolution')
    if number == 5:
        resolution = video_resolution[4]
        print('downloading the video with 720p resolution')
    if number == 6:
        resolution = video_resolution[5]
        print('downloading the video with 1080 resolution')

    stream = yt.streams.get_by_itag(resolution)
    print('-------------------->>> Downloading')
    stream.download()
    print('Downloading finished')

    

download()


