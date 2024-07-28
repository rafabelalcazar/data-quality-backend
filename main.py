from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5174",
    # Añade otros orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
async def test():
    return {"message": "Hello World"}

@app.post("/upload-dataset/")
async def upload_dataset(file: UploadFile = File(...)):
    
    # Save the uploaded file to the datasets folder
    file_path = f"./datasets/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    print(file.filename)
    # Check if the uploaded file is a CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    # Read the CSV file into a pandas DataFrame
    try:
        contents = await file.read()
        
        
        # Check if the file is empty
        # if file.file.seek(0, 2) == 0:
        #     raise HTTPException(status_code=400, detail="Empty CSV file")

        # Reset the file pointer to the beginning
        # file.file.seek(0)

        # Read the CSV file into a pandas DataFrame
        try:
            path = './datasets/'+file.filename
            print('path: ',path)
            data = pd.read_csv(path, encoding='latin1')
            print(data.head())
            data = data.fillna(0)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing the file: {e}")
        # data = pd.read_csv(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the file: {e}")

    # Process the DataFrame (example: calculate descriptive statistics)
    try:
        stats = data.describe().to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the data: {e}")

    return JSONResponse(content=stats)

# To run the server, use the following command:
# uvicorn main:app --reload
