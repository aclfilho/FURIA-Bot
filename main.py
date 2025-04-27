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
        return "O lineup atual da FURIA é KSCERATO, yuurih, chelo, FalleN e arT."
    elif "loja" in mensagem:
        return "Confira os produtos oficiais na loja: https://loja.furia.gg/"
    else:
        return "Desculpe, não entendi sua pergunta. Tente perguntar sobre campeonatos, time ou loja!"
