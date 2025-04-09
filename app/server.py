
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    if random.random() < 0.2:
        app.logger.error("Returning 500 error")
        return "Internal Server Error", 500
    return "Hello, World!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
