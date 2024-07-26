import logging
from fastapi import FastAPI, Request, Response
from appSoap import conversor

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/soap/")
async def crear_planilla(number: dict):
    return conversor(number)

# @app.post("/soap/{number}")
# async def crear_planilla(number: str):
#     return conversor(number)

    
