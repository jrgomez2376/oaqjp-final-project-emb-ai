import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        
        # Debugging: Print the full response to check the structure
        print(json.dumps(data, indent=2))
        
        # Extract emotions from the response
        emotions = data.get("document", {}).get("emotion", {})
        
        if not emotions:
            return {"error": "No emotion data found"}
        
        # Get individual emotion scores or default to 0.0 if not found
        anger_score = emotions.get("anger", 0.0)
        disgust_score = emotions.get("disgust", 0.0)
        fear_score = emotions.get("fear", 0.0)
        joy_score = emotions.get("joy", 0.0)
        sadness_score = emotions.get("sadness", 0.0)
        
        # Find the dominant emotion with the highest score
        dominant_emotion = max(emotions, key=emotions.get, default="unknown")
        
        # Return the results in the required format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
