"""
File that contains the main logic to start the server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect the emotion data from user input
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response and response["dominant_emotion"]:
        return f"""
                For the given statement, the system response is 
                'anger': {response["anger"]},
                'disgust': {response["disgust"]},
                'fear': {response["fear"]},
                'joy': {response["joy"]} and
                'sadness': {response["sadness"]}.
                The dominant emotion is {response["dominant_emotion"]}.
                """
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"Internal server error detecting the emotions for {text_to_analyze}"

@app.route("/")
def render_index_page():
    """
    Render the index template for the index route
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
