from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq
from scraper import scrape_website
from db import add_documents
from rag import ask_rag
load_dotenv()
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
class QuestionRequest(BaseModel):
    question: str
class URLRequest(BaseModel):
    url: str
# 
@app.post("/index")
def index_website(data: URLRequest):

    print("URL RECEIVED:", data.url)

    website_text = scrape_website(
        data.url
    )

    chunk_count = add_documents(
        website_text
    )

    return {
        "message":
        f"Website indexed successfully. {chunk_count} chunks stored."
    }
# 
@app.post("/ask")
def ask(data: QuestionRequest):

    answer = ask_rag(
        data.question
    )

    return {
        "answer": answer
    }
# 
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
##to create virtual environment
# python -m venv venv
##to activate virtual environment
#.\venv\Scripts\activate
##to install python packages
#pip install fastapi uvicorn groq python-dotenv jinja2 chromadb sentence-transformers beautifulsoup4 requests
#to run the app
# uvicorn main:app --reload  