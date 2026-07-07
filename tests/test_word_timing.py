from ai.subtitles.word_timing import split_segment_into_words

segment = {
    "start": 0,
    "end": 3,
    "text": "THIS IS AMAZING"
}

words = split_segment_into_words(segment)

for word in words:
    print(word)