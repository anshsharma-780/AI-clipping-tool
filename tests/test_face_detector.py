import cv2

from ai.reframing.face_detector import FaceDetector


video = input("Video path:\n")

cap = cv2.VideoCapture(video)

success, frame = cap.read()

cap.release()

if not success:
    raise RuntimeError("Could not read video.")

detector = FaceDetector()

faces = detector.detect(frame)

print()

print("=" * 50)
print("MEDIAPIPE FACE DETECTOR")
print("=" * 50)

if not faces:

    print("\nNo faces detected.")

else:

    print(f"\nFaces Found: {len(faces)}\n")

    for face in faces:

        print(face)