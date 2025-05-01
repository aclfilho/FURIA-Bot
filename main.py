from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# criando a aplicação
app = FastAPI() #instância de aplicação

# Servir arquivos estáticos (CSS, imagens, etc)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Definindo onde estão os templates (HTML)
templates = Jinja2Templates(directory="templates")

# Rota inicial (carrega o HTML)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota de resposta ao chat (agora só retorna JSON, não recarrega a página)
@app.post("/chat")
async def chat(message: str = Form(...)):
    resposta = processar_mensagem(message)
    return JSONResponse(content={"resposta": resposta})

# Função para gerar resposta automática usando dicionário e sinônimos
def processar_mensagem(mensagem):
    mensagem = mensagem.lower()  # Deixa tudo em minúsculo para facilitar a comparação

    # Dicionário com sinônimos como chave e respostas como valor
    respostas = {
        ("campeonato", "campeonatos", "torneio"): "A FURIA está participando da IEM Katowice e outros torneios incríveis!",
        ("time", "jogadores", "lineup"): "O lineup atual da FURIA é KSCERATO, yuurih, FalleN, molodoy, YEKINDAR, o treinador Sidde e o novo Assistant Coach Krizzen.",
        ("canal", "youtube", "vídeo"): "Segue o link do nosso canal oficial: https://www.youtube.com/@FURIAggCS/videos",
        ("live", "ao vivo", "twitch"): "Nossos jogos são transmitidos ao vivo na Twitch: https://www.twitch.tv/furiatv",
        ("loja", "camisa", "produtos", "shop"): "Confira os produtos oficiais na loja: https://loja.furia.gg/",
        ("lore", "história", "origem"): "Origem: Surgiu em 2017, mas explodiu em 2018 com um estilo hiperagressivo liderado por arT (Artista), virando a nova geração do CS:GO BR.",
        ("grito", "uhul", "força"): "Uhul FURIA!",
        ("rivalidade", "clássico", "imperial", "mibr"): "FURIA vs MIBR: Os véio vs os novo. FURIA aplicou 3x0 várias vezes. FURIA vs Imperial: FalleN vs arT, o clash de IGLs!",
        ("troll", "zueira", "eco round"): "A FURIA tava jogando no modo freestyle e, num eco round, todos foram de USP pra cima da Liquid e quase roubaram o round! KKK"
    }

    # Busca por palavra-chave dentro da mensagem
    for palavras_chave, resposta in respostas.items():
        if any(palavra in mensagem for palavra in palavras_chave):
            return resposta

    # Caso nenhuma palavra seja encontrada
    return "Desculpe, não entendi sua pergunta. Tente perguntar sobre campeonatos, time, loja ou live!"
