from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video(input_file, output_folder, duration=60):
    clip = VideoFileClip(input_file)

    # Get the duration of the video
    total_duration = clip.duration

    # Calculate the number of clips needed
    num_clips = int(total_duration / duration)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(num_clips):
        start_time = i * duration
        end_time = (i + 1) * duration #Duration

        # Make sure the last clip doesn't exceed the total duration
        if end_time > total_duration:
            end_time = total_duration

        # Extract the subclip
        subclip = clip.subclip(start_time, end_time)

        # Save the subclip to the output folder
        subclip_file = os.path.join(output_folder, f"part_{i+1}.mp4")
        subclip.write_videofile(subclip_file, codec="libx264", audio_codec="aac")

    # Close the original clip
    clip.close()

if __name__ == "__main__":
    input_video = r"D:\Documents\Vid" #Path to your vid
    output_folder = r"D:\Documents\Outputd #Output folder

    split_video(input_video, output_folder)
