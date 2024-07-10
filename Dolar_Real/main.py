import requests

def get_dollar_quote(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        quote_usd_brl = data['conversion_rates']['BRL']
        return quote_usd_brl
    else:
        raise Exception(data.get("error-type", "unknown error"))

def main():
    api_key = "7c5597414ff248032d3c89e5"
    try:
        quote = get_dollar_quote(api_key)
        print(f"The current exchange rate of the dollar in relation to the Brazilian real is: R$ {quote:.2f}")
    except Exception as e:
        print("It was not possible to get the dollar quote.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
