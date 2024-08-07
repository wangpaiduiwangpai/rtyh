url = "https://mvwebfs.hw.kugou.com/202408070945/13c6725d866d4d6599ca933500be5583/KGTX/CLTX002/0b3350d8a718666060d33e25ade49a55.mp4"
import requests
res = requests.get(url)
with open("qwert.mp4", "wb") as f:
    f.write(res.content)
with open("qwert.mp3", "wb") as k:
    k.write(res.content)
    
    from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

# 读取视频和音频文件
video_clip = VideoFileClip("qwert.mp4")
audio_clip = AudioFileClip("qwert.mp4")

# 将音频添加到视频中
final_clip = video_clip.set_audio(audio_clip)

# 输出合并后的视频
final_clip.write_videofile("qwert_final.mp4")



