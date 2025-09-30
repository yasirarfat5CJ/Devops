from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Docker"

if __name__ == "__main__":
    print("Server starting... listening on port 5000")
    app.run(host="0.0.0.0", port=5000)
