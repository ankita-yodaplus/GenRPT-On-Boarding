from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'John Doe', 'age': 30}}

@app.get('/about')
def about():
    return {'data': 'About Page'}