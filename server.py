from typing import Union
from flask_app import calculate
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse 


app = FastAPI(debug=True)
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],      
    )

class CalculateData(BaseModel):
    skill_damage_increase: float
    base_skill_multiplier: float
    attack_power: float
    attack_power_by_hp: float
    attacker_hp: float
    defense_ratio: float
    team1_ability_power: float
    team2_ability_power: float
    compatibility_damage: float
    strike_judgement: float
    extra_stat: float
    max_damage_limit: float


@app.get("/")
def read_root():
    return FileResponse('src/html/index.html')

@app.get("/css/{file_name}")
def read_css(file_name: str):
    return FileResponse(f'src/css/{file_name}')

@app.get("/js/{file_name}")
def read_js(file_name: str):
    return FileResponse(f'src/js/{file_name}')

@app.post("/api/calculate")
def calculate_(data: CalculateData):
    return {"result":calculate(dict(data))}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)