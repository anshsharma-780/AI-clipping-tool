from ai.reframing.crop_calculator import CropCalculator

frame_width = 1920
frame_height = 1080

face = (
    900,
    250,
    250,
    250
)

calculator = CropCalculator()

crop = calculator.calculate(
    frame_width,
    frame_height,
    face
)

print()

print("=" * 50)
print("SMART CROP")
print("=" * 50)

print(crop)