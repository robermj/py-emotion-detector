"""
File to define the function needed to detect the emotion of an input using Watson API
"""
import json
import requests
BASE_URL = "https://sn-watson-emotion.labs.skills.network"
API = "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
URL = BASE_URL + API
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """
    Make a request to Watson API to detect the emotion of text_to_analyze
    """
    text_input = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(URL, json = text_input, headers=HEADERS, timeout=5)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]['emotion']

        return {**emotions, "dominant_emotion": max(emotions, key=emotions.get)}
    elif response.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
            }
    elif response.status_code == 500:
        return None
