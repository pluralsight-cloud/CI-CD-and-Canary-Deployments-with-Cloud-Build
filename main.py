import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_hello_world():
    name = os.getenv("RESPONSE_MESSAGE", "Python")
    return {"message": f"Hello {name}!"}, 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)