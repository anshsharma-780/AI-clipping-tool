from ui.thumbnail_generator import ThumbnailGenerator

video = input("Video:\n")

generator = ThumbnailGenerator()

image = generator.generate(
    video,
    "processing/thumbnails/thumb.jpg"
)

print()

print("="*50)

print(image)