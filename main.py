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

# Função para gerar resposta automática
def processar_mensagem(mensagem):
    mensagem = mensagem.lower()
    if "campeonatos" in mensagem:
        return "A FURIA está participando da IEM Katowice e outros torneios incríveis!"
    elif "time" in mensagem:
        return "O lineup atual da FURIA é KSCERATO, yuurih, FalleN, molodoy, YEKINDAR e o treinador sidde"
    elif "canal" in mensagem:
            return "Segue o link do nosso canal oficial https://www.youtube.com/@FURIAggCS/videos"
    elif "live" in mensagem:
            return "Nossos jogos são transmitidos ao vivo na Twitch: https://www.twitch.tv/furiatv"
    elif "loja" in mensagem:
        return "Confira os produtos oficiais na loja: https://loja.furia.gg/"
    elif "lore" in mensagem:
        return "Origem: Surgiu em 2017, mas explodiu em 2018 com um estilo hiperagressivo liderado por arT (Artista), virando a nova geração do CS:GO BR."
    elif "grito" in mensagem:
        return "Uhul FURIA!"
    elif "rivalidade" in mensagem:
        return "FURIA vs MIBR: Os véio vs os novo. FURIA aplicou 3x0 várias vezes.  FURIA vs Imperial: FalleN vs arT, o clash de IGLs, tinha mais xilique que jogo do flamengo!"
    elif "troll" in mensagem:
        return "A FURIA tava jogando no modo freestyle e, num eco round (quando o time tá SEM GRANA), resolveram RUSHAR MID TODOS DE USP contra a Liquid. A cena: 5 BRs correndo igual zumbi no meio do mapa, só de USP e sem colete. Resultado: Furia matou 3 e quase roubou o round, os gringos ficaram loucos KKKKKK"
    else:
        return "Desculpe, não entendi sua pergunta. Tente perguntar sobre campeonatos, time ou loja!"
