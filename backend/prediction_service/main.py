from fastapi import FastAPI

app = FastAPI(title="MFGuide Prediction Service")

@app.get("/")
def root():
    return {"message": "Prediction Service Running..."}


@app.get("/predict")
def predict(scheme_code: str):
    #placeholder
    return {
        "scheme_code": scheme_code,
        "expected_return": "12.5%",
        "risk_level": "Medium",
        "confidence_interval": "10% - 15%"
    }
