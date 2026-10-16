from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route("/")
def home() -> str:
    return jsonify(consumir_api())


def consumir_api():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response = requests.get(f"{url}", timeout=10)

    # Verificar se a requisição HTTP retornou um erro e gerar exceção automaticamente
    response.raise_for_status()
    dados = response.json()
    return dados


#-------- main -------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

