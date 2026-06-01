from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq
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
    context: str
    question: str
@app.post("/ask")
def ask(data: QuestionRequest):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content":
                """
                Answer ONLY using the provided context.
                If the answer is not in the context,
                say:
                'I cannot find that information in the provided text.'
                """
            },
            {
                "role": "user",
                "content":
                f"""
                Context:
                {data.context}

                Question:
                {data.question}
                """
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer
    }

print("API KEY =", os.getenv("GROQ_API_KEY"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
##to create virtual environment
# python -m venv venv
##to activate virtual environment
#.\venv\Scripts\activate
##to install python packages
#pip install fastapi uvicorn groq python-dotenv jinja2
#to run the app
# uvicorn main:app --reload  