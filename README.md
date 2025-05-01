FURIA Fan ChatBot

## Funcionalidades

- Chat em tempo real com respostas temáticas sobre a FURIA.
- Informações sobre lineup, campeonatos, transmissões e muito mais.
- Interface com identidade visual inspirada na FURIA.
- Layout ajustado com chatbot fixado no canto inferior direito e lore no canto superior.
- Backend desenvolvido com **FastAPI**.
- Frontend leve com HTML e CSS puro.

---

## Estrutura do Projeto

furia-chatbot/ 
├── main.py # Backend com FastAPI 
├── requirements.txt # Dependências do projeto 
├── templates/ 
│ └── index.html # Interface principal do chatbot 
├── static/ 
│ └── style.css # Estilos visuais da aplicação


---

## Exemplos de Interações

**Usuário**: campeonatos  
**Bot**: A FURIA está participando da IEM Katowice e outros torneios incríveis!

**Usuário**: time  
**Bot**: O lineup atual da FURIA é KSCERATO, yuurih, FalleN, molodoy, YEKINDAR e o treinador sidde.

**Usuário**: loja  
**Bot**: Confira os produtos oficiais na loja: https://loja.furia.gg/

---

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- HTML5 & CSS3

---

## Como Rodar Localmente
```bash
1. Clone este repositório:
git clone https://github.com/seuusuario/furia-chatbot.git
cd furia-chatbot

2. Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Instale as dependências: 
pip install -r requirements.txt

4. Inicie o servidor:
uvicorn main:app --reload

