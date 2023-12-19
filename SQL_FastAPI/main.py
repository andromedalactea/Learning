from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Mi primera API"}

@app.get("/saludo")
def read_saludo():
    return {"message": "Hola, ¿cómo estás hoy?"}
