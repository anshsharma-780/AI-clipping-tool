import whisper

_model = None


def get_model(model_name="base"):
    """
    Load the Whisper model only once.
    """

    global _model

    if _model is None:
        print(f"Loading Whisper model ({model_name})...")
        _model = whisper.load_model(model_name)
        print("Whisper model loaded.")

    return _model