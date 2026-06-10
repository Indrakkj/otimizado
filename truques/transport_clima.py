

import requests
def climatizacao():
    cidade = input("Digite a cidade: ")

    url = f"https://wttr.in/{cidade}?format=j1"

    resposta = requests.get(url)

    dados = resposta.json()

    temperatura = dados["current_condition"][0]["temp_C"]

    print("Temperatura:", temperatura, "°C")

    temperatura = int(temperatura)
    return temperatura