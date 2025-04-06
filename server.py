from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        if "error" in result:
            return f"Error: {result['error']}", 400
        # Format the response as requested
        return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    else:
        return "No text provided to analyze", 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
