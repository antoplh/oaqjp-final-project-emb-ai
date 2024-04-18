import requests
import json

def emotion_detector(text_to_analyze):
    """ function that uses Watson NLP 
    to detect emotions from text_to_analyze"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    request = requests.post(url, json = myobj, headers = header)
    # Error Handling
    if request.status_code == 400:
        request_dic =  {
        'anger':None,
        'disgust':None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    elif request.status_code == 200:
        formatted_request = json.loads(request.text)
        # Extract emotion scores
        anger_score = formatted_request['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_request['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_request['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_request['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_request['emotionPredictions'][0]['emotion']['sadness']

        request_dic = {
            'anger':anger_score,
            'disgust':disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        # Get dominant emotion
        dominant_emotion = [i for i,j in request_dic.items() if j==max(request_dic.values())][0]
        # Append dominant emotion to request_dic
        request_dic['dominant_emotion'] = dominant_emotion

    return request_dic

