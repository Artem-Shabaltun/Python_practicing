from moviepy.video.io.VideoFileClip import VideoFileClip

input_file = "BES-ALTERA CODE - FIRST PRESENTATION.mp4"  # замін на назву свого файлу
output_file = "compressed.mp4"

with VideoFileClip(input_file) as video:
    video.write_videofile(
        output_file,
        codec="libx264",
        audio_codec="aac",
        bitrate="500k"
    )