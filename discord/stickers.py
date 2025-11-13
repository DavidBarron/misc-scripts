from moviepy import VideoFileClip

# Specify the path to your input video file
input_video_path = "/Users/davidbarron/Downloads/924D2FDD-D3F6-452A-B7A7-F270B1A09C37.mov"

# Specify the desired output GIF file name
output_gif_path = "/Users/davidbarron/github/scripts/linh_hearts.gif"

# Load the video clip
video_clip = VideoFileClip(input_video_path)

# Convert the video to a GIF
# You can adjust the 'fps' parameter for desired quality and file size
video_clip.resized(width=250, height=250).subclipped(0, 1.71).write_gif(output_gif_path, fps=7)

# .subclipped(0, 2)

print(f"Video '{input_video_path}' successfully converted to GIF '{output_gif_path}'.")