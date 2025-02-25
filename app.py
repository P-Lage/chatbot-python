from flask import Flask, render_template, request, jsonify
from chatbot.chatbot import load_intents, generate_response

app = Flask(__name__)
intents = load_intents('data/intents.json')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = generate_response(user_input, intents)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
