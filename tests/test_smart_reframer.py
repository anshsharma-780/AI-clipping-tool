from ai.reframing.smart_reframer import SmartReframer

video = input("Video path:\n")

reframer = SmartReframer()

crop = reframer.analyze(video)

print()

print("=" * 50)

print("SMART REFRAMER")

print("=" * 50)

print()

print(crop)