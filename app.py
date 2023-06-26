# BASE CODE: THIS WORKS!

from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")
    
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






# ## TRIAL 1:

# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from textSummarizer.pipeline.prediction import PredictionPipeline

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# pipeline = PredictionPipeline()

# @app.get("/", tags=["authentication"])
# async def index(request: Request):
#     return RedirectResponse(url="/docs")

# @app.post("/predict")
# async def predict_route(request: Request, text: str = Form(...)):
#     try:
#         obj = PredictionPipeline()
#         output = obj.predict(text)
#         return templates.TemplateResponse("result.html", {"request": request, "summary": output})
#     except Exception as e:
#         raise e

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)
