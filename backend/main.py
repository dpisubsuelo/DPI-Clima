from fastapi import FastAPI
from appSoap import conversor
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/soap/")
async def crear_planilla(number: dict):
    return conversor(number)

@app.get("/soap/")
async def crear_planilla1(number: dict):
    return conversor(number)

@app.get("/soap/{number}")
async def crear_planilla2(number: int):
    print("numero enviado: ",number)
    return conversor(number)

print("probando github desktop desde casa")    
