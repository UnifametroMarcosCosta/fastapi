from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    column1: str
    column2: str

@app.post("/data")
def create_data(data: Data):
    # Salvar os dados em um arquivo de texto
    with open("dados.txt", "a") as file:
        file.write(f"{data.column1}, {data.column2}\n")
    
    return {"message": "Dados salvos com sucesso!"}