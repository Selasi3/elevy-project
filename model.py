from pydantic import BaseModel


class ModelInput(BaseModel):
    value : float

class ModelOutput(BaseModel):
   
    elevy_fee: float
