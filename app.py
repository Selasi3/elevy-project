from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from func import elevy_fee

from model import ModelInput, ModelOutput



app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.post("/predict")
async def predict(data: ModelInput):
    data_input = data.dict()
    value = float(data_input["value"])
    total_value = elevy_fee(value)

    return ModelOutput(elevy_fee=total_value)