filter_none
edit
play_arrow

brightness_4

from pytube import YouTube 
  
 
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
try: 
 
    yt = YouTube(link) 
except: 
    print("Connection Error") 
  
mp4files = yt.filter('mp4') 
  
yt.set_filename('GeeksforGeeks Video') 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!')