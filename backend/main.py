import logging
from fastapi import FastAPI, Request, Response
from lxml import etree
from appSoap import conversor

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/soap/{number}")
async def crear_planilla(number: str):
    return conversor(number)

    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)