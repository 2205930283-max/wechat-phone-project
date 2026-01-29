from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>自助制作网站</h1>
    <p>欢迎访问</p>
    <p>注册功能开发中...</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
