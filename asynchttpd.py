#!/usr/bin/env python3

#import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def path_root():
    return {"msg": "Hello, world!"}

#async def web_server():
#    uvicorn.run(app)

if __name__ == "__main__":
    #asyncio.run(web_server())
    uvicorn.run(app)