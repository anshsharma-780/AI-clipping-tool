from ai.branding.logo_overlay import overlay_logo

video = input("Video path:\n")
logo = input("Logo path (PNG preferred):\n")

overlay_logo(
    input_video=video,
    logo_path=logo,
    output_video="processing/clips/logo_test.mp4",
)

print("Logo overlay complete.")