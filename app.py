from youtube_transcript_api import YouTubeTranscriptApi
import requests

def get_transcript(video_id):
    srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    def array_fi(array):
        newArray = []
        for item in array:
            newArray.append(item["text"])
        return newArray
    return array_fi(srt)

def get_sentences(text, num_of_sentences=5):
    length = len(text)
    length_of_each_part = length // num_of_sentences
    new_array = []
    for i in range(0, 5):
        new_array.append(text[i*length_of_each_part:(i+1)*length_of_each_part])
    return new_array
