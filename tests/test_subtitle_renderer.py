from ai.subtitles.subtitle_renderer import burn_subtitles

video = input("Video path:\n")

burn_subtitles(
    video,
    "processing/transcript/subtitles.ass",
    "processing/clips/subtitled_clip.mp4"
)

print()
print("Subtitle rendering complete.")