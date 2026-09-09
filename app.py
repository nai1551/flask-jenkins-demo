from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Jenkins Flask CI/CD!"


@app.route("/health")
def health():
    return "Application is healthy"


@app.route("/info")
def info():
    return "Flask application deployed by Jenkins"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
