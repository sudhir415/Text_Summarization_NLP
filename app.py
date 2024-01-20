from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline 
import logging
from fastapi import Request


# text:str = "What is Text Summarization?" 

# app = FastAPI()

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")

# templates = Jinja2Templates(directory="templates")
# pipeline = PredictionPipeline()

# @app.post("/predict", tags=["authentication"])
# async def predict(text:str):
#     summary = pipeline.predict(text)
#     return templates.TemplateResponse("predict.html", {"request": Request, "summary": summary})


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)


# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")
    
text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    



@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)