from fastapi import FastAPI
from fastapi import HTTPException, Path
from fastapi.responses import JSONResponse
from validation.user_input import user_input
from model.prediction import predict

app = FastAPI()


@app.get("/")
def home():
    return {"message": "This is an API to predict crop yeild"}


@app.post("/predict")
def prediction(data: user_input):
    input_df = {
        "State_Name": data.State_Name,
        "Crop_Type": data.Crop_Type,
        "Crop": data.Crop,
        "N": data.N,
        "P": data.P,
        "K": data.K,
        # "npk_sum": data.npk_sum,
        # "n_to_k_ratio": data.n_to_k_ratio,
        # "p_to_k_ratio": data.p_to_k_ratio,
        # "n_to_p_ratio": data.n_to_p_ratio,
        # "rainfall_temp": data.rainfall_temp,
        # "water_stress": data.water_stress,
        # "ph_optimal": data.ph_optimal,
        # "ph_distance": data.ph_distance,
        # "ph_squared": data.ph_squared,
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
