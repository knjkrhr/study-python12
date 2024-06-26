import numpy as np
import pandas as pd

from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: int
    age: int

    @field_validator("age")
    def age_size(cls, v):
        if 0 <= v <= 100:
            return v
        else:
            raise ValueError("範囲外のageが入力されました。")


vector = np.array([7, 6, 5])
print(f"{vector=}")
df = pd.DataFrame([])
print(f"{df=}")
print(BaseModel)

try:
    user = User(id=123, age=999)
except ValueError as e:
    print(e.json())
    # [{"loc": ["age"],"msg": "範囲外のageが入力されました。","type": "value_error"}]
