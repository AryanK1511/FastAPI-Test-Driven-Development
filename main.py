from fastapi import FastAPI

# Create an instance of the FastAPI class which is essentially our application
app = FastAPI()

# Defining a health-check route


@app.get("/")
def health_check() -> None:
    return {"msg": "FastAPI Server is ruuning"}


@app.get("/hello")
def hello():
    return {"hello": "how are you doing"}
