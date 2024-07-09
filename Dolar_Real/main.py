import requests

def obter_cotacao_dolar(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    dados = response.json()
    if response.status_code == 200:
        cotacao_usd_brl = dados['conversion_rates']['BRL']
        return cotacao_usd_brl
    else:
        raise Exception(dados.get("error-type", "Erro desconhecido"))

def main():
    api_key = "7c5597414ff248032d3c89e5"
    try:
        cotacao = obter_cotacao_dolar(api_key)
        print(f"A cotação atual do dólar em relação ao real é: R$ {cotacao:.2f}")
    except Exception as e:
        print("Não foi possível obter a cotação do dólar.")
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
