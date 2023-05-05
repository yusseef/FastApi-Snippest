from fastapi import FastAPI, Path

app = FastAPI()

students = ['yussef', 'raouf']
@app.get('/')
def index():
    return {'name': 'index',}

@app.get('/get_id/{id}')
def get_by_id(id:int = Path(..., description = "Students ID", ge = 0 ,lt = len(students))):
    print(len(students))
    return students[id]