from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Configurações
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rota principal - Landing Page
@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

# Rota para a página do chatbot
@app.get("/chatbot", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota para processar as mensagens do chat
@app.post("/api/chat")
async def chat(message: str = Form(...)):
    resposta = processar_mensagem(message)
    return JSONResponse(content={"resposta": resposta})

# Função de processamento de mensagens
def processar_mensagem(mensagem):
    mensagem = mensagem.lower()

    respostas = {
        ("campeonato", "campeonatos", "torneio"): "A FURIA está participando da IEM Katowice e outros torneios incríveis!",
        ("time", "jogadores", "lineup"): "O lineup atual da FURIA é KSCERATO, yuurih, FalleN, molodoy, YEKINDAR, o treinador Sidde e o novo Assistant Coach Krizzen.",
        ("canal", "youtube", "vídeo"): "Segue o link do nosso canal oficial: https://www.youtube.com/@FURIAggCS/videos",
        ("live", "ao vivo", "twitch"): "Nossos jogos são transmitidos ao vivo na Twitch: https://www.twitch.tv/furiatv",
        ("loja", "camisa", "produtos", "shop"): "Confira os produtos oficiais na loja: https://loja.furia.gg/",
        ("lore", "história", "origem"): "Origem: Surgiu em 2017, mas explodiu em 2018 com um estilo hiperagressivo liderado por arT (Artista), virando a nova geração do CS:GO BR.",
        ("grito", "uhul", "força"): "Uhul FURIA!",
        ("rivalidade", "clássico", "imperial", "mibr"): "FURIA vs MIBR: Os véio vs os novo. FURIA aplicou 3x0 várias vezes. FURIA vs Imperial: FalleN vs arT, o clash de IGLs!",
        ("troll", "zueira", "eco round"): "A FURIA tava jogando no modo freestyle e, num eco round, todos foram de USP pra cima da Liquid e quase roubaram o round! KKK",
        ("próximo jogo", "proximo jogo", "agenda", "calendário", "quando joga"): "Você pode acompanhar o calendário de partidas em https://www.hltv.org/team/8297/furia"
    }

    for palavras_chave, resposta in respostas.items():
        if any(palavra in mensagem for palavra in palavras_chave):
            return resposta

    return "Desculpe, não entendi sua pergunta. Tente perguntar sobre campeonatos, time, loja ou live!"