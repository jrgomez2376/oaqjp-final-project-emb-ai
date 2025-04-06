from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

# Define the endpoint for the emotion detection
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Get the text from the POST request
    text = request.form['text']
    
    # Call the emotion detection function
    result = emotion_detector(text)
    
    # Check if there was an error in the result
    if "error" in result:
        return jsonify({"error": result["error"]})
    
    # Extract the individual emotions and the dominant emotion
    emotions = result.get("emotion", {})
    dominant_emotion = result.get("dominant_emotion", "unknown")
    
    # Format the response text
    response_text = f"For the given statement, the system response is 'anger': {emotions.get('anger', 0)}, " \
                    f"'disgust': {emotions.get('disgust', 0)}, 'fear': {emotions.get('fear', 0)}, " \
                    f"'joy': {emotions.get('joy', 0)}, 'sadness': {emotions.get('sadness', 0)}. " \
                    f"The dominant emotion is {dominant_emotion}."
    
    return jsonify({"response": response_text})


@app.route('/')
def index():
    # Render the index.html page located in the templates folder
    return render_template('index.html')


if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(debug=True, host='0.0.0.0', port=5000)
