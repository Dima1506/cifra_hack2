from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# once the middleware is applied, any route can then access the database session
# from the global ``db``

@app.get("/all")
def get_all():
    f = open("all.json", "r")
    sentence_json = eval(f.read())
    f.close()
    return sentence_json

@app.get("/npo")
def get_npo():
    f = open("npo.json", "r")
    sentence_json = eval(f.read())
    f.close()
    return sentence_json

@app.get("/ndfl")
def get_ndfl():
    f = open("ndfl.json", "r")
    sentence_json = eval(f.read())
    f.close()
    return sentence_json
