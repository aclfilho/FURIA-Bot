import requests

url_chat = "http://127.0.0.1:8000/chat"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

while True:
    mensagem_usuario = input("Você: ")
    if mensagem_usuario.lower() == "sair":
        break

    dados = {"message": mensagem_usuario}

    try:
        resposta = requests.post(url_chat, data=dados, headers=headers)
        resposta.raise_for_status()
        conteudo_da_resposta = resposta.json()
        print(f"FURIA Bot: {conteudo_da_resposta['resposta']}")

    except requests.exceptions.RequestException as e:
        print(f"Erro na comunicação com o servidor: {e}")
        if resposta is not None:
            print(f"Código de status da resposta: {resposta.status_code}")
            print(f"Texto da resposta: {resposta.text}")

print("Chat encerrado.")