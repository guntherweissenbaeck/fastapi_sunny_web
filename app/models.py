from pydantic import BaseModel


class SunnyWebData(BaseModel):
    power: float
    daily_yield: float
    total_yield: float
