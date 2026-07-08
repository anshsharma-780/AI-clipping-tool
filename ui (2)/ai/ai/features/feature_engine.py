from ai.features.keyword_features import keyword_score
from ai.features.structure_features import structure_score
from ai.features.emotion_features import emotion_score


def extract_features(text: str):
    """
    Run all feature extractors and combine the results.
    """

    keyword = keyword_score(text)
    structure = structure_score(text)
    emotion = emotion_score(text)

    total_score = (
        keyword["score"]
        + structure["score"]
        + emotion["score"]
    )

    return {
        "keyword": keyword,
        "structure": structure,
        "emotion": emotion,
        "total_score": total_score
    }