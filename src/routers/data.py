from fastapi import FastAPI, APIRouter , Depends , UploadFile, File , status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings , Sittings
from controllers import DataController , ProjectController
import aiofiles
from models import ResponseSignal
import logging


logger = logging.getLogger(uvicorn.error)



data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.get("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile = File , app_sittings: Sittings = Depends(get_settings)):


    data_controller = DataController()
    is_valid , result_signal = data_controller.validate_file(file = file)



    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )   
    
    project_dir_path = ProjectController().get_Project_Path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(orig_filename = file.filename , project_id = project_id)


    try :

        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_sittings.File_Default_Chunk_Size):  # Read file in chunks
                await f.write(chunk)

    except Exception as e:

        logger.error(f"File upload failed: {e}")
        
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.File_Upload_Failed.value
            }
        ) 

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "signal": ResponseSignal.File_Upload_Success.value,
            "file_path": file_path
        }
    )
    


