from fastapi import FastAPI
from appSoap import conversor
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
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

# @app.post("/soap/{number}")
# async def crear_planilla(number: str):
#     return conversor(number)

    
