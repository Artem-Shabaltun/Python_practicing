from moviepy.video.io.VideoFileClip import VideoFileClip

input_file = "BES-ALTERA CODE - FIRST PRESENTATION.mp4"  # замін на назву свого файлу
output_file = "cutted.mp4"

with VideoFileClip(input_file) as video:
    cut = video.subclipped(16*60, 31*60 + 42)
    cut.write_videofile(output_file)