from fastapi import FastAPI
import uvicorn
<<<<<<< HEAD
from src.routes import contacts, auth
=======
from src.routes import contacts
>>>>>>> 0f6ac3d411da53a6f22c60888b0f4e17ab578fdf

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
<<<<<<< HEAD
=======

>>>>>>> 0f6ac3d411da53a6f22c60888b0f4e17ab578fdf
