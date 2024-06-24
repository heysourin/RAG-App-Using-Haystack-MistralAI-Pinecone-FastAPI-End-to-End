# fastapi
from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
from fastapi import FastAPI
import json
import os
from dotenv import load_dotenv
# from QASystem.retrievalandgenrator import get_result

# object of fastapi
app = FastAPI()

# reading html files from template directory
templates = Jinja2Templates(directory="templates")

# creating routes


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_answer")
async def get_answer(request: Request, question: str=Form(...)):
    pass