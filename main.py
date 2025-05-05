# Backend principal para la versión web con FastAPI

from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    return {"message": "GlitchX API activa"}