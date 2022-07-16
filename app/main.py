from fastapi import FastAPI
from routes.inference import routes_inference

app = FastAPI()
app.include_router(routes_inference, prefix="/inference")
