from ai.highlights.detector import detect_highlights


def format_time(seconds):
    """Convert seconds to MM:SS format."""

    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    return f"{minutes:02}:{seconds:02}"


def main():

    print("=" * 60)
    print("AI TIMESTAMP ENGINE TEST (v0.5.2)")
    print("=" * 60)

    results = detect_highlights(
        "processing/transcript/segments.json"
    )

    if not results:
        print("No highlights detected.")
        return

    for index, clip in enumerate(results, start=1):

        print()
        print("=" * 60)
        print(f"Candidate #{index}")
        print("=" * 60)

        print(f"Total Score      : {clip['score']}")
        print(f"Start            : {format_time(clip['start'])}")
        print(f"End              : {format_time(clip['end'])}")

        print()

        print("Feature Breakdown")
        print("------------------------------")

        print(
            f"Keyword Score    : {clip['features']['keyword']['score']}"
        )

        print(
            f"Structure Score  : {clip['features']['structure']['score']}"
        )

        print(
            f"Emotion Score    : {clip['features']['emotion']['score']}"
        )

        print()

        print("Detected Keywords")

        matches = clip["features"]["keyword"]["matches"]

        if matches:
            print(", ".join(matches))
        else:
            print("None")

        print()

        print("Transcript")
        print("------------------------------")

        print(clip["text"])


if __name__ == "__main__":
    main()