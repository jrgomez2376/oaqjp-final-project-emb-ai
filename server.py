from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page for the emotion detection application.
    
    Returns:
        str: HTML template for the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyzes the provided text for emotional content and returns the emotion analysis results.
    
    Args:
        textToAnalyze (str): The text to be analyzed for emotions.
    
    Returns:
        str: The emotion analysis result or an error message.
        int: HTTP status code, indicating the success or failure of the request.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        
        if "error" in result:
            return f"Error: {result['error']}", 400
        
        # Check if the dominant emotion is None
        if result.get('dominant_emotion') is None:
            return "Invalid text! Please try again!", 400
        
        # Format the response as requested
        return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    else:
        return "No text provided to analyze", 400

if __name__ == "__main__":
    """
    Starts the Flask web application.
    
    The application will be accessible on port 5004.
    """
    app.run(debug=True, host='0.0.0.0', port=5004)
