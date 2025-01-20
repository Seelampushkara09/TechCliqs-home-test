import assemblyai as aai
aai.settings.api_key="d5224319a6c648939ca81e64d182be48"
transcript=aai.Transcriber().transcribe("C:/Users/Seelam Pushkara/Downloads/audio.m4a")
subtitles= transcript.export_subtitles_srt()
f=open("subtitles.srt","a")
f.write(subtitles)
f.close()