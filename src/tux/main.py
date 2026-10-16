from flask import Flask, jsonify
from tux.api import consumir_api

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return jsonify(consumir_api())


def main():
    app.run(host="0.0.0.0", port=8080, debug=True)


#------------------------


if __name__ == "__main__":
    main()
