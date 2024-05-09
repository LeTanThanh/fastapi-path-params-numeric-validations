from fastapi import FastAPI
from fastapi import Path
from fastapi import Query

from typing import Annotated

app = FastAPI()

# Import Path
"""
@app.get("/items/{id}")
async def read_item(
  id: Annotated[int, Path(description = "The ID of the item to get")],
  q: Annotated[str | None, Query(alias = "item-query")] = None
):
  response = {"id": id}

  if q:
    response.update({"q": q})

  return response
"""

# Number validations: greater than or equal
"""
@app.get("/items/{id}")
async def read_item(
  id: Annotated[int, Path(
    ge = 1,
    description = "The ID of the item to get"
  )],
  q: Annotated[str, Query()]
):
  response = {"id": id}

  if q:
    response.update({"q": q})

  return response
"""
