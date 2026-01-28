from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_ocr_text = ""

@app.route("/")
def home():
    return "Screen AI Helper Backend Running"

@app.route("/ocr", methods=["POST"])
def receive_ocr():
    global latest_ocr_text
    latest_ocr_text = request.json.get("text", "")
    print("OCR received")
    return jsonify({"status": "received"})

@app.route("/get-ocr", methods=["GET"])
def get_ocr():
    return jsonify({"ocr_text": latest_ocr_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
