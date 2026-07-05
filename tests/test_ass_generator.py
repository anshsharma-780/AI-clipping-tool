from ai.subtitles.ass_generator import generate_ass

generate_ass(

    "processing/transcript/segments.json",

    "processing/transcript/subtitles.ass"

)

print()

print("Subtitle file created.")