from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API Running OK"

@app.route("/wechat-phone", methods=["POST"])
def wechat_phone():
    data = request.json
    return jsonify({
        "status": "success",
        "received_data": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
