from moviepy.editor import VideoFileClip
import openai
import requests

# Replace with your actual OpenAI API key
openai.api_key = "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"

def video_to_text(video_path):
    """
    Extracts audio from the video and transcribes it using OpenAI Whisper.

    Args:
        video_path: Path to the video file.

    Returns:
        Tuple containing:
            - Transcribed text.
            - List of timestamps (start, end) for each sentence.
    """

    # Extract audio from the video
    audio_clip = VideoFileClip(video_path).audio

    # Save audio to a temporary file
    audio_clip.write_audiofile("temp_audio.wav")

    # Transcribe audio using OpenAI Whisper
    with open("temp_audio.wav", "rb") as audio_file:
        transcript = openai.Audio.transcribe("audio", audio_file)

    # Extract timestamps (if available)
    timestamps = []
    if "segments" in transcript:
        for segment in transcript["segments"]:
            start = segment["start"]
            end = segment["end"]
            timestamps.append((start, end))

    return transcript["text"], timestamps

def get_video_clips(video_path, timestamps):
    """
    Generates video clips based on the provided timestamps.

    Args:
        video_path: Path to the video file.
        timestamps: List of timestamps (start, end) for each sentence.

    Returns:
        List of video clips.
    """

    video_clip = VideoFileClip(video_path)
    clips = []
    for start, end in timestamps:
        clip = video_clip.subclip(start, end)
        clips.append(clip)
    return clips

# Example usage
video_path = "C:/Users/Seelam Pushkara/Downloads/videoplayback.mp4"
text, timestamps = video_to_text(video_path)

print("Transcribed Text:\n", text)

if timestamps:
    clips = get_video_clips(video_path, timestamps)

    # Option 1: Save clips to individual files
    for i, clip in enumerate(clips):
        clip.write_videofile(f"clip_{i}.mp4")

    # Option 2: Concatenate clips into a single video (optional)
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("concatenated_clips.mp4")