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
