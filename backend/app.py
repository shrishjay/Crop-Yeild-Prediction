from fastapi import FastAPI, Request
from fastapi import HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from validation.user_input import user_input
from model.prediction import predict
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow Streamlit
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def home():
    return {"message": "hello"}


@app.post("/predict")
def prediction(data: user_input):
    input_df = {
        "State_Name": data.State_Name,
        "Crop_Type": data.Crop_Type,
        "Crop": data.Crop,
        "N": data.N,
        "P": data.P,
        "K": data.K,
        "rainfall": data.rainfall,
        "temperature": data.temperature,
        "pH": data.pH,
    }
    try:
        prediction = predict(input_df)
        return JSONResponse(
            status_code=200, content={"predicted yeild per hectare": prediction}
        )
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
