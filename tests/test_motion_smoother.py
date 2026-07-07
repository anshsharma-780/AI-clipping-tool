from ai.reframing.motion_smoother import MotionSmoother

values = [

    410,
    430,
    470,
    450,
    420,
    415,
    418,
    421,
]

smoother = MotionSmoother()

result = smoother.smooth(values)

print()

print("=" * 50)

print("ORIGINAL")

print(values)

print()

print("SMOOTHED")

print(result)