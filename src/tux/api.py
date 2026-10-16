import requests

def consumir_api():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response = requests.get(f"{url}", timeout=10)

    # Verificar se a requisição HTTP retornou um erro e gerar exceção automaticamente
    response.raise_for_status()
    dados = response.json()
    return dados