from fastapi import FastAPI
app = FastAPI(title="TattooPH Booking")
@app.get("/")
def read_root():
    return {"message": "TattooPH API is Live! 🚀"}
@app.get("/health")
def health_check():
    return {"status": "healthy"}
